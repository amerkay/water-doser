import math
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
        'plant_adult_age_weeks': 12,
        # Water plant in ml, for each 0.01m^2 of plant area, modulated for plant age
        'to_ml_multiplier': 75
    }

    def __init__(self, farmwarename, config):
        """ Plants class constructor

        Arguments:
            farmwarename {str} -- Farmware name
            config {dict} -- for loading the configurations. Subset of defaults to override.
        """
        self.farmwarename = farmwarename
        self.config = InputStore.merge_config(self.config, config)

    def calc_watering_ms(self, plant, precip=0.0):
        """ Gets plant data if not already stored in Plant's 'meta' data dict, and save it.

        Arguments:
            plant {dict} -- Single Plant dict

        Keyword Arguments:
            precip {float} -- Sum of precipIntensity within 18-hour window (12 historical rain, 6 forecasted).
            Uses SI unit: Millimeters (per sqm) per hour. (default: {0})

        Returns:
            bool -- [description]
        """
        age = self._plant_age(plant)
        if age == 0:
            return False

        self._chk_openfarm_meta(plant)

        # calculating supposed watering for today
        supposed_watering = self._get_supposed_watering(plant['meta']['spread'], plant['meta']['height'], age)

        # how much to water in ml, minimum value for ms is 250ms
        ml = int(round(supposed_watering)) if supposed_watering > 0 else 0

        # get area of plant on ground, converted to m^2
        area_plant = (math.pi * (plant['meta']['spread']/2000)**2)
        # * 1000 to convert from mm/m^2 to ml
        rain_ml = precip * 1000 * area_plant
        ml_corrected_to_precip = ml - rain_ml

        ms = 0
        if ml_corrected_to_precip > 0:
            ms = int(ml_corrected_to_precip / self.config["water_ml_per_sec"]) * 1000

        log("Water {} {}ml; for {}ms (precip {}, rain_ml {} on area {})".format(
            plant['openfarm_slug'], ml, ms, precip, rain_ml, area_plant),
            title="calc_watering_ms")

        return ms

    def _chk_openfarm_meta(self, plant):
        """ Get OpenFarm data. Adds ['meta']['spread'] and ['height'], saves for future use.

        Arguments:
            plant {dict} -- Plant dict
        """
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
                    title="calc_watering_ms")
                plant['meta']['spread'] = 5 * 10
                plant['meta']['height'] = 5 * 10
        else:
            plant['meta']['spread'] = int(plant['meta']['spread'])
            plant['meta']['height'] = int(plant['meta']['height'])

    def _plant_age(self, p):
        if p['pointer_type'].lower() != 'plant' or p['plant_stage'].lower() != 'planted' \
            or p['planted_at'] is None:
            return 0

        return (dt.utcnow() - dt.strptime(p['planted_at'], "%Y-%m-%dT%H:%M:%S.%fZ")).days + 1

    # return supposed watering for the plant with the given spread and age
    def _get_supposed_watering(self, spread_max, height_max, age):
        # area of adult plant in mm^2, converted to m^2 by dividing by 1000^2
        age_adult = self.config["plant_adult_age_weeks"] * 7
        area_adult = (spread_max * height_max) / 1000**2

        # for each 0.01m^2 of plant area, output user-set to_ml_multiplier in ml, modulated for age
        ml_water_max = (area_adult / 0.01) * self.config["to_ml_multiplier"]
        ml_water = (ml_water_max / age_adult) * age

        log("[Watering {}ml] area_adult {}, age_adult {}, age {}, ml_water_max {}".format(
            int(ml_water), area_adult, age_adult, age, int(ml_water_max)),
            title="_get_supposed_watering")

        return int(ml_water)
