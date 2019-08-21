import requests
from simple_cache import SimpleCache as cache

# import static logger and create shortcut function
from logger import Logger
log = Logger.log


class Openfarm():
    """ Contact Openfarm API, disk cache enabled

    Variables:
        ATTRIBUTE_FIELDS_ALLOWED {list} -- Allowed fields/keys to cache from

        cached_attributes {dict} -- Using SimpleCache. Example
        {
            "arugula": {
               "spread": 10,
               "height": 10,
               ...
            },
            ...
        }
    """
    ATTRIBUTE_FIELDS_ALLOWED = ["spread", "height", "slug"]

    @staticmethod
    def get_openfarm_attribs(plant_slug):
        """ Get Openfarm attributes using Openfarm API,
        cached and stripped to ATTRIBUTE_FIELDS_ALLOWED only.

        Arguments:
            plant_slug {str} -- The slug_name of the plant (plant['openfarm_slug']).

        Returns:
            set -- of attributes for plant_slug result, see ATTRIBUTE_FIELDS_ALLOWED
        """
        cache_id = "openfarm-attribs-{}".format(plant_slug)
        lifetime = 12*60*60

        if cache.is_cached(cache_id):
            res = cache.get(cache_id)
            log("hit; returning openfarm response from cache: {}".format(res), title='get_openfarm_attribs')
            return res
        else:
            log("miss; contacting openfarm API for {}".format(plant_slug), title='get_openfarm_attribs')

            response = requests.get('https://openfarm.cc/api/v1/crops?filter={}'.format(plant_slug))
            response.raise_for_status()

            filtered_response = Openfarm._extract_attr_set(response.json())

            if type(filtered_response) is dict and len(filtered_response) > 0:
                cache.save(cache_id, filtered_response, lifetime)

            return filtered_response

    @staticmethod
    def _extract_attr_set(openfarm_response):
        """ Extract attribute set matching ATTRIBUTE_FIELDS_ALLOWED

        Arguments:
            openfarm_response {dict} -- of attributes for plant_slug result, see ATTRIBUTE_FIELDS_ALLOWED
        """
        filtered_response = {}

        for key, val in openfarm_response['data'][0]['attributes'].items():
            if key in Openfarm.ATTRIBUTE_FIELDS_ALLOWED:
                filtered_response[key] = val

        return filtered_response
