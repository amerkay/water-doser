from datetime import datetime as dt
from openfarm import Openfarm
from plants import Plants
from input_store import InputStore

# import static logger and create shortcut function
from logger import Logger
log = Logger.log


class WaterDose():
    # defaults
    config = {
        # my pump produces 100ml/sec
        'water_ml_per_sec': 100,
        # Assumption: 15 weeks, plant becomes an adult (i.e. takes the full height and spread)
        # TODO: Better source per plant
        'plant_adult_age_weeks': 15,
        # Magic mutiplier to convert plant size to ml needed for watering
        'to_ml_multiplier': 3
    }

    def __init__(self, farmwarename, config):
        """ Plants class constructor

        Arguments:
            farmwarename {str} -- Farmware name
            config {dict} -- for loading the configurations. Subset of defaults to override.
        """
        self.farmwarename = farmwarename
        self.config = InputStore.merge_config(self.config, config)

    # small_rain = 1  # 1mm is a small rain (cancells watering today)
    # medium_rain = 10  # 10mm is a medium rain (cancells watering today and tomorrow)
    # big_rain = 20  # 20mm is a big rain (cancells watering today, tomorrow and day after tomorrow)

    def calc_watering_params(self, plant):
        age = self._plant_age(plant)
        if age == 0:
            return False

        # get OpenFarm data
        log("Plant meta: {}".format(plant['meta']), "success", title="calc_watering_params")

        if 'height' not in plant['meta'] or 'spread' not in plant['meta']:
            try:
                res = Openfarm.get_openfarm_attribs(plant['openfarm_slug'])

                plant['meta']['spread'] = res['spread'] * 10
                plant['meta']['height'] = res['height'] * 10

                # save the spread, height data
                Plants.save_plant({
                    'id': plant['id'],
                    'meta': {
                        'spread': plant['meta']['spread'],
                        'height': plant['meta']['height']
                    }
                })
            except Exception as e:
                log("Openfarm did not return results for {}, consider updated OpenFarm entry. {}".format(
                    plant['openfarm_slug'], e),
                    title="calc_watering_params")
                plant['meta']['spread'] = 5 * 10
                plant['meta']['height'] = 5 * 10
        else:
            plant['meta']['spread'] = int(plant['meta']['spread'])
            plant['meta']['height'] = int(plant['meta']['height'])

        # calculating supposed watering for today
        supposed_watering = self._get_supposed_watering(plant['meta']['spread'], age)

        # how much to water in ml, minimum value for ms is 250ms
        ml = int(round(supposed_watering)) if supposed_watering > 0 else 0
        ms = min(int(ml / self.config["water_ml_per_sec"] * 1000), 250)

        log("Water {} {}ml; for {}ms".format(plant['openfarm_slug'], ml, ms),
            title="calc_watering_params")

        return ms

    def _plant_age(self, p):
        if p['pointer_type'].lower() != 'plant' or p['plant_stage'].lower() != 'planted' \
            or p['planted_at'] is None:
            return 0

        return (dt.utcnow() - dt.strptime(p['planted_at'], "%Y-%m-%dT%H:%M:%S.%fZ")).days + 1

    # return supposed watering for the plant with the given spread and age
    def _get_supposed_watering(self, max_spread, age):
        step = max_spread / float(self.config["plant_adult_age_weeks"] * 7)
        d = step * age

        return int(d * self.config["to_ml_multiplier"])
