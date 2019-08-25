import os
import sys
from traceback import format_exc

from farmware_tools import device
from point_sort import PointSort
from input_store import InputStore
from water_dose import WaterDose
from plants import Plants
from control import Control

# import static logger and create shortcut function
from logger import Logger
log = Logger.log

# Farmware name, must be same as "package" attrib in manifest.json
FARMWARE_NAME = "water-doser-dev"

# The defaults, see InputStore class for more information.

INPUT_DEFAULTS = {
    'plant_search_radius': (40, 'int'),
    'water_ml_per_sec': (100, 'int'),
    'plant_adult_age_weeks': (15, 'int'),
    'to_ml_multiplier': (3, 'int'),
    'weather_lat': (47.25, 'float'),
    'weather_lon': (-122.45, 'float'),
    'debug': (2, 'int')
}

if __name__ == "__main__":
    # get farmware name from path
    try:
        FARMWARE_NAME = ((__file__.split(os.sep))[len(__file__.split(os.sep)) - 3]).replace('-master', '')
    except:
        pass

    Logger.FARMWARE_NAME = FARMWARE_NAME

    try:
        # create new instance of the InputStore. this will load the user input or defaults
        input_store = InputStore(FARMWARE_NAME, defaults=INPUT_DEFAULTS)
        # set logger level
        Logger.set_level(input_store.input['debug'])

        log('Started with python version {}'.format(sys.version_info), message_type='info', title="init")

        currpos = {'x': 680, 'y': 380} if device.get_current_position() is None \
            else device.get_current_position()

        # init instances
        water_dose = WaterDose(FARMWARE_NAME, input_store.input)
        control = Control(FARMWARE_NAME)

        # load the plants
        plant_search_radius = input_store.input['plant_search_radius']
        plants = Plants(FARMWARE_NAME,
                        config={
                            'filter_plant_stage': ['planted', 'sprouted'],
                            'filter_min_x': currpos['x'] - plant_search_radius,
                            'filter_max_x': currpos['x'] + plant_search_radius,
                            'filter_min_y': currpos['y'] - plant_search_radius,
                            'filter_max_y': currpos['y'] + plant_search_radius,
                        })
        points_plants = plants.load_points_with_filters()

        # get closest plant to currpos
        points_sorted = PointSort.sort_points_by_dist(points_plants, currpos)
        if len(points_sorted) > 0:
            plant_closest = points_sorted[0]
            log("closest_point is {}".format(plant_closest), title="main")

            # use spread and age from MLH to decide Xms to water.
            dose_ms = water_dose.calc_watering_params(plant_closest)
            control.execute_watering(dose_ms)
        else:
            log("No close points, moving on.", "info", title="main")

    except Exception as e:
        log("Exception thrown: {}, traceback: {}".format(e, format_exc()), message_type='error', title="main")
        raise Exception(e)

    log('End', message_type='success', title=FARMWARE_NAME)
