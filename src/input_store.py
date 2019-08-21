import os

# import static logger and create shortcut function
from logger import Logger
log = Logger.log


class InputStore():
    """ InputStore class to load user input settings or defaults.

    Variables:
        INPUT_DEFAULTS {dict} -- Set of inputs to load and format
            {'variable name': (default value, type), ...}
            Types supported are
                - 'str',
                - 'int' (support 'randint(i,j)'),
                - 'bool'
                - 'list' (.split(",") run on it)
                - 'float'

            More info in manifest.json and README
    """

    INPUT_DEFAULTS = {
        'plant_search_radius': (40, 'int'),
        'water_ml_per_sec': (110, 'int'),
        'weather_lat': (47.25, 'float'),
        'weather_lon': (-122.45, 'float'),
        'debug': (2, 'int')
    }

    def __init__(self, farmwarename):
        self.farmwarename = farmwarename
        self.input = {}
        self.get_input_env()

    def get_input_env(self):
        """ Get input variables values. """
        prefix = self.farmwarename.replace('-', '_')
        log('using prefix {}'.format(prefix), 'info', title='get_input_env')

        # get all inputs values
        for key, settings in InputStore.INPUT_DEFAULTS.items():
            self.input[key] = self.get_input_val(key, settings, prefix)

        for key, val in self.input.items():
            log('input {}: {}'.format(key, val), title='get_input_env')

    def get_input_val(self, key, settings=('None', 'str'), prefix='farmware'):
        """ Get input values and sanitize them. None values returned for easy checking with 'is None'.

        Arguments:
            key {str} -- the input variable key

        Keyword Arguments:
            settings {tuple} -- default value (None, 0, or input val) and
                type (str, int, bool, list) (default: {('None', 'str')})
            prefix {str} -- farmware name prefix (default: {'farmware'})

        Returns:
            mixed types -- based on settings {tuple}
        """

        # get the value set by user or default
        val = os.environ.get('{p}_{k}'.format(p=prefix, k=key), settings[0])

        # remove trailing spaces and convert the value to lower case
        val_clean_str = str(val).lower().strip()

        # set the expected value type for post-processing
        val_type = settings[1] if settings[1] in ['str', 'int', 'bool', 'list', 'float'] else 'str'

        if val_type == 'int':
            return int(val) if val_clean_str != 'none' else None
        elif val_type == 'float':
            return float(val) if val_clean_str != 'none' else None
        elif val_type == 'bool':
            return val_clean_str in ['true', '1', 'y', 'yes', 'on']
        elif val_type == 'list':
            return val_clean_str.replace(" , ", ",").replace(", ", ",")\
                .replace(" ,", ",").split(",") if val_clean_str != 'none' else []

        # default treat like str
        return str(val).strip() if val_clean_str != 'none' else None

    @staticmethod
    def merge_config(default_config, new_config):
        merged_config = default_config.copy()

        if isinstance(default_config, dict) and isinstance(new_config, dict):
            # merge the input config with self.config, only if key defined.
            for k, v in new_config.items():
                if k in default_config:
                    merged_config[k] = v

            log("configs merged: {}".format(merged_config), title='merge_config')
            return merged_config
        else:
            log("configs must be dicts, instead got {} and {}".format(type(default_config), type(new_config)),
                'error',
                title='merge_config')
            raise Exception('configs must be a dict in merge_config')
