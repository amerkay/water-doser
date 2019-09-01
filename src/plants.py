""" Plants class

Uses API call POST points/search to load all Plants.
Then apply_filters() uses the config settings to filter just the matching subset.

Uses farmware_tools to control device and contact app API.

See https://github.com/amerkay/powerloop/blob/master/manifest.json for more info about configuring.

Unmodified Source: https://github.com/rdegosse/Loop-Plants-With-Filters, thank you @rdegosse!

For this copy of the class: https://github.com/amerkay/powerloop

Variables:
    log {method} -- A reference function Logger().log()
"""

import re
from simple_cache import SimpleCache as cache

from datetime import datetime as dt
from farmware_tools import app
from input_store import InputStore
from fake_plants import FakePlants

# import static logger and create shortcut function
from logger import Logger

log = Logger.log


class Plants:
    # defaults
    # See https://github.com/amerkay/powerloop/blob/master/manifest.json for more info.
    config = {
        "filter_pointname": "*",
        "filter_openfarm_slug": "*",
        "filter_age_min_day": -1,
        "filter_age_max_day": 36500,
        "filter_meta_key": None,
        "filter_meta_op": None,
        "filter_meta_value": None,
        "filter_plant_stage": None,
        "filter_min_x": None,
        "filter_max_x": None,
        "filter_min_y": None,
        "filter_max_y": None,
        "save_meta_key": None,
        "save_meta_value": None,
        "save_plant_stage": None,
    }

    def __init__(self, farmwarename, config):
        """ Plants class constructor

        Arguments:
            farmwarename {str} -- Farmware name
            config {dict} -- for loading the configurations. Subset of defaults to override.
        """
        self.farmwarename = farmwarename
        self.config = InputStore.merge_config(self.config, config)

    def load_points_with_filters(self, use_cache=False):
        points = self._get_points_cached() if use_cache is True else self._get_points()

        log(
            "all points loaded, count {}".format(len(points)),
            title="load_points_with_filters",
        )

        points_out = self.apply_filters(
            points=points,
            point_name=self.config["filter_pointname"],
            filter_openfarm_slug=self.config["filter_openfarm_slug"],
            filter_age_min_day=self.config["filter_age_min_day"],
            filter_age_max_day=self.config["filter_age_max_day"],
            meta_key=self.config["filter_meta_key"],
            meta_value=self.config["filter_meta_value"],
            min_x=self.config["filter_min_x"],
            min_y=self.config["filter_min_y"],
            max_x=self.config["filter_max_x"],
            max_y=self.config["filter_max_y"],
            pointer_type="Plant",
            plant_stages=self.config["filter_plant_stage"],
        )

        log(
            "filters applied, resulting in {} points".format(len(points_out)),
            title="load_points_with_filters",
        )

        # log(self.points, title='load_points_with_filters')
        return points_out

    def _get_points_cached(self):
        cache_id = "plants-search"
        lifetime = 15 * 60

        if cache.is_cached(cache_id):
            points_from_cache = cache.get(cache_id)
            log(
                "hit; using cache with {} plants".format(len(points_from_cache)),
                title="Plants::_get_points",
            )
            return points_from_cache
        else:
            log("miss; loading from API", title="_get_points")
            points = self._get_points()

            if type(points) is list and len(points) > 0:
                cache.save(cache_id, points, lifetime)

            return points

    def _get_points(self):
        points = app.post("points/search", payload={"pointer_type": "Plant"})
        return points if type(points) is list else FakePlants.get_fake_plants()

    def apply_filters(
        self,
        points,
        point_name="",
        filter_openfarm_slug="",
        filter_age_min_day=0,
        filter_age_max_day=36500,
        meta_key=None,
        meta_value=None,
        min_x=None,
        max_x=None,
        min_y=None,
        max_y=None,
        pointer_type="Plant",
        plant_stages=None,
    ):

        filtered_points = []
        now = dt.utcnow()

        for p in points:
            if p["pointer_type"].lower() == pointer_type.lower():
                ref_date = p["planted_at"]
                if (
                    str(p["planted_at"]).lower() == "none"
                    or str(p["planted_at"]).lower() is None
                ):
                    ref_date = p["created_at"]

                age_day = (now - dt.strptime(ref_date, "%Y-%m-%dT%H:%M:%S.%fZ")).days

                b_meta = self._filter_meta(p, meta_key, meta_value)
                b_coordinate_x = self._filter_coordinates(int(p["x"]), min_x, max_x)
                b_coordinate_y = self._filter_coordinates(int(p["y"]), min_y, max_y)
                b_plantstage = self._filter_plant_stage(p["plant_stage"], plant_stages)

                if (
                    (
                        p["name"].lower().find(point_name.lower()) >= 0
                        or point_name == "*"
                    )
                    and (
                        p["openfarm_slug"].lower().find(filter_openfarm_slug.lower())
                        >= 0
                        or filter_openfarm_slug == "*"
                    )
                    and (filter_age_min_day <= age_day <= filter_age_max_day)
                    and b_meta is True
                    and b_coordinate_x
                    and b_coordinate_y
                    and b_plantstage
                ):
                    filtered_points.append(p.copy())

        return filtered_points

    def _filter_plant_stage(self, p_stage, plant_stages):
        if (
            None not in (p_stage, plant_stages)
            and type(plant_stages) is list
            and len(plant_stages) > 0
        ):
            for s in plant_stages:
                if p_stage.lower() == s.lower():
                    return True

            # otherwise
            return False

        # default is True if None or failed
        return True

    def _filter_coordinates(self, p_coord, min_coord, max_coord):
        """ Test point p against min and max coordinates

        Arguments:
            p_coord {int} -- point coordinate, example p['x']
            min_coord {int} -- min coordinate value allowed
            max_coord {int} -- max coordinate value allowed

        Returns:
            bool -- True if match or None, False if not a match
        """
        if None not in (min_coord, max_coord, p_coord):
            if int(min_coord) <= int(p_coord) <= int(max_coord):
                return True
        else:
            return True

        # if not a match, return False
        return False

    def _filter_meta(self, p, meta_key, meta_value):
        """ Test point p against meta_key, meta_value

        Uses value from self.config['filter_meta_op'] to choose the comparision method used.

        Arguments:
            p {dict} -- Celeryscript Point JSON object
            meta_key {str} -- Comparision key
            meta_value {str} -- Comparision value

        Returns:
            bool -- True if match or None, False if not a match
        """
        if None not in (p, meta_key, meta_value):
            if (
                "meta" in p
                and meta_key in p["meta"]
                and p["meta"][meta_key] is not None
            ):
                target_age_in_seconds = (
                    dt.utcnow()
                    - dt.strptime(p["meta"][meta_key], "%Y-%m-%d %H:%M:%S.%f")
                ).total_seconds()
            else:
                return False

            try:
                # log('==> p is None {}, key {}, value {}'.format(p is None, meta_key, meta_value), title='_filter_meta')
                if (
                    self.config["filter_meta_op"] is None
                    or self.config["filter_meta_op"] == "=="
                ):
                    return (p["meta"][meta_key]).lower() == meta_value.lower()
                elif self.config["filter_meta_op"] == ">=":
                    return (p["meta"][meta_key]) >= meta_value
                elif self.config["filter_meta_op"] == "<=":
                    return (p["meta"][meta_key]) <= meta_value
                elif self.config["filter_meta_op"] == "<":
                    return (p["meta"][meta_key]) < meta_value
                elif self.config["filter_meta_op"] == ">":
                    return (p["meta"][meta_key]) > meta_value
                elif self.config["filter_meta_op"] == "!=":
                    return (p["meta"][meta_key]).lower() != meta_value.lower()
                elif self.config["filter_meta_op"].lower() == "regex":
                    return bool(re.compile(meta_value).match(p["meta"][meta_key]))
                elif self.config["filter_meta_op"].lower() == "daysmax":
                    return bool(target_age_in_seconds / 86400 <= int(meta_value))
                elif self.config["filter_meta_op"].lower() == "minutesmax":
                    return bool(target_age_in_seconds / 60 <= int(meta_value))
                elif self.config["filter_meta_op"].lower() == "daysmin":
                    return bool(target_age_in_seconds / 86400 >= int(meta_value))
                elif self.config["filter_meta_op"].lower() == "minutesmin":
                    return bool(target_age_in_seconds / 60 >= int(meta_value))
                else:
                    return False
            except Exception as e:
                log("{}".format(e), "error", title="exception in filter_meta")
                return False

        return True

    def update_save_meta(self, point, save_point={}):
        """ Creates or appends 'save_meta' data and returns ammended save_point set

        Arguments:
            point {dict} -- Celeryscript Point JSON object

        Keyword Arguments:
            save_point {dict} -- [description] (default: {{}})

        Returns:
            {dict} -- Ammended save_point set with the updates to be posted via API call
        """
        if self.config["save_meta_key"] is not None:
            save_meta_key = str(self.config["save_meta_key"]).lower()
            save_meta_value = str(self.config["save_meta_value"]).lower()

            save_point = (
                {"id": point["id"], "meta": {}} if len(save_point) < 1 else save_point
            )

            save_point["meta"][save_meta_key] = (
                str(dt.utcnow()) if save_meta_value == "#now#" else save_meta_value
            )

        return save_point

    def update_save_plant_stage(self, point, save_point={}):
        """ Creates or appends 'save_plant_stage' data and returns ammended save_point set.

        Arguments:
            point {dict} -- Celeryscript Point JSON object

        Keyword Arguments:
            save_point {dict} -- Optional, use if you already have a save_point created
                                 you'd like to append to (default: {{}})

        Returns:
            {dict} -- Ammended save_point set with the updates to be posted via API call
        """
        if self.config["save_plant_stage"] is not None:
            save_plant_stage = str(self.config["save_plant_stage"]).lower()
            save_point = {"id": point["id"]} if len(save_point) < 1 else save_point

            if save_plant_stage in ("planned", "planted", "sprouted", "harvested"):
                save_point["plant_stage"] = save_plant_stage

                if save_plant_stage == "planted":
                    save_point["planted_at"] = str(dt.utcnow())
            else:
                log(
                    "Wrong save_plant_stage value: {}".format(save_plant_stage),
                    "error",
                    title="save_plant_stage",
                )

        return save_point

    @staticmethod
    def save_plant(save_point):
        """ Execute the PUT points/{id} API call.

        Arguments:
            point {dict} -- Celeryscript Point JSON object to update

        Raises:
            e -- exception
        """
        try:
            if len(save_point) < 2:
                log("Nothing to save: {}".format(save_point), title="save_plant")
                return

            if Logger.LOGGER_LEVEL < 3:
                if "meta" in save_point:
                    # to avoid replacing older point meta data, we load it and merge it
                    log(
                        "Loading plant data from API for ID: {}".format(
                            save_point["id"]
                        ),
                        title="save_plant",
                    )
                    plant_data_from_api = app.get("points/{}".format(save_point["id"]))

                    if "meta" in plant_data_from_api:
                        # see https://stackoverflow.com/a/26853961
                        save_point["meta"] = {
                            **plant_data_from_api["meta"],
                            **save_point["meta"],
                        }

                log("Saving Point: {}".format(save_point), title="save_plant")

                endpoint = "points/{}".format(save_point["id"])
                app.put(endpoint, payload=save_point)
            else:
                log(
                    "FAKE Saving Point (debug level = 3): {}".format(save_point),
                    title="save_plant",
                )

        except Exception as e:
            log("Exception thrown: {}".format(e), "error", title="save_plant")
            raise e
