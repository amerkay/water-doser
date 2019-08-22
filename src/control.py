from farmware_tools import device, app
from simple_cache import SimpleCache as cache
from input_store import InputStore

# import static logger and create shortcut function
from logger import Logger
log = Logger.log


class Control():
    # defaults
    config = {}

    def __init__(self, farmwarename, config={}):
        """ Plants class constructor

        Arguments:
            farmwarename {str} -- Farmware name
            config {dict} -- for loading the configurations. Subset of defaults to override.
        """
        self.farmwarename = farmwarename
        self.config = InputStore.merge_config(self.config, config)

    def execute_watering(self, duration_ms):
        pin = self.get_water_pin()

        if Logger.LOGGER_LEVEL < 2:
            log("Water ON, wait {}ms, OFF on PIN {}".format(duration_ms, pin), title='execute_watering')

            # water on, wait, water off
            device.write_pin(pin, pin_value=1, pin_mode=0)
            device.wait(duration_ms)
            device.write_pin(pin, pin_value=0, pin_mode=0)
        else:
            log("FAKE: Water ON, wait {}ms, OFF on PIN {}".format(duration_ms, pin), title='execute_watering')

    def get_water_pin(self):
        return self.get_peripheral_cached("water")["pin"]

    def get_peripheral_cached(self, peripheral_name):
        cache_id = "peripherals"
        lifetime = 60 * 60

        if cache.is_cached(cache_id):
            log("hit; using cached result: {}".format(cache.get(cache_id)), title='get_peripheral_cached')
            res = cache.get(cache_id)
        else:
            res = app.get('peripherals')
            log("miss; loading from API: {}".format(res), title='get_peripheral_cached')

            # if not the expected response, replace with stub for debugging locally
            if type(res) is list and len(res) > 0:
                cache.save(cache_id, res, lifetime)
            else: # for debugging
                res = [{"pin": 999, "label": "water"}]

        # find peripheral in results
        try:
            out = next(item for item in res if item["label"].lower() == peripheral_name.lower())
        except:
            raise Exception("Cannot find peripheral_name {} in results {}".format(peripheral_name, res))

        return out
