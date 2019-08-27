import requests

# from datetime import datetime as dt
from datetime import datetime as dt
from input_store import InputStore
from simple_cache import SimpleCache as cache

# import static logger and create shortcut function
from logger import Logger
log = Logger.log


class Weather():
    # defaults
    config = {
        # using my, @amerkay, api key. Obtain yours @ https://darksky.net/dev/account
        'darksky_api_key': '46c52f6d9ff98422a9a11414df7cb97e',
        'weather_lat': 0,
        'weather_lon': 0
    }

    def __init__(self, farmwarename, config):
        """ Plants class constructor

        Arguments:
            farmwarename {str} -- Farmware name
            config {dict} -- for loading the configurations. Subset of defaults to override.
        """
        self.farmwarename = farmwarename
        self.config = InputStore.merge_config(self.config, config)

    def get_darksky_api_cached(self, on_date=None):
        """ Get Dark Sky API result (historic or forecast, same endpoint)

        Longer cache lifetime if date not today and in past
        Keyword Arguments:
            date {datetime} -- Python datetime object. Will be cached to 1 day accuracy (default: {None})
                Example: twelve_hours_ago = (dt.now() - timedelta(hours=12))
                         yesterday = dt.now() - timedelta(days=1)
        Returns:
            dict -- See https://darksky.net/dev/docs#time-machine-request
        """
        time_str = f'{on_date:%Y-%m-%d}' if on_date is not None and isinstance(on_date, dt) else "now"
        cache_id = "darksky_{}_{}_{}".format(self.config['weather_lat'], self.config['weather_lon'], time_str)
        # cache for 48 hours if date in past, otherwise shorter period
        lifetime = 48 * 60 * 60 if on_date and on_date.day < dt.now().day else 1 * 60 * 60

        if cache.is_cached(cache_id):
            response = cache.get(cache_id)
            log("hit; returning Dark Sky API response (id {}, lt {}) from cache with {} keys".format(
                cache_id, lifetime, len(response)),
                title='get_darksky_api_cached')
            return response
        else:
            log("miss; contacting Dark Sky API for id {}".format(cache_id), title='get_darksky_api_cached')

            response = self.get_darksky_api(on_date)

            # filtered_response = Openfarm._extract_attr_set(response.json())
            if type(response) is dict and 'currently' in response:
                cache.save(cache_id, response, lifetime)
            else:
                log("expected dict, got {}, {}".format(type(cache_id), response),
                    title='get_darksky_api_cached')

            return response

    def get_darksky_api(self, on_date=None):
        """ Get Dark Sky API result (historic or forecast, same endpoint)

        Keyword Arguments:
            date {datetime} -- Python datetime object. Will be cached to 1 day accuracy (default: {None})
                Example: twelve_hours_ago = (dt.now() - timedelta(hours=12))
        Returns:
            dict -- See https://darksky.net/dev/docs#time-machine-request
        """
        key = self.config['darksky_api_key']
        lat = self.config['weather_lat']
        lon = self.config['weather_lon']

        # build URI, will return only 24 hours for day provided if using
        time_qry = f',{on_date:%Y-%m-%dT%H:%M:%S}' if on_date is not None else ""
        req_url = "https://api.darksky.net/forecast/{}/{},{}{}?units=si&exclude=minutely".format(
            key, lat, lon, time_qry)

        request_params = {'headers': {'Accept-Encoding': 'gzip'}}
        response = requests.get(req_url, **request_params)

        print("req_url is {}".format(req_url))

        # throw error if != 200
        response.raise_for_status()

        log("Dark Sky API returned dict with {} keys".format(len(response.json())), title='get_darksky_api')

        return response.json()