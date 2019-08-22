# import static logger and create shortcut function
from logger import Logger
log = Logger.log


class FakePlants():
    """ FakePlants JSON for use in local testing/debugging. """

    @staticmethod
    def get_fake_plants():
        log("Loading FAKE PLANTS.", "success", title="FakePlants::get_fake_plants")

        return [{
            'id': 157884,
            'created_at': '2019-07-29T10:41:01.765Z',
            'updated_at': '2019-08-12T00:00:10.826Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-12 00:00:09.818638'
            },
            'x': 220,
            'y': 240,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:16:03.233Z',
            'radius': 25.0
        }, {
            'id': 157886,
            'created_at': '2019-07-29T10:41:06.469Z',
            'updated_at': '2019-08-12T00:00:16.349Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-12 00:00:14.962869'
            },
            'x': 220,
            'y': 330,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:16:09.145Z',
            'radius': 25.0
        }, {
            'id': 157903,
            'created_at': '2019-07-29T10:43:39.831Z',
            'updated_at': '2019-08-12T00:00:21.302Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-12 00:00:20.766326'
            },
            'x': 220,
            'y': 440,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:16:14.988Z',
            'radius': 25.0
        }, {
            'id': 158387,
            'created_at': '2019-07-31T00:35:17.660Z',
            'updated_at': '2019-08-12T00:00:26.609Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-12 00:00:26.046715'
            },
            'x': 270,
            'y': 570,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:16:21.090Z',
            'radius': 25.0
        }, {
            'id': 157862,
            'created_at': '2019-07-29T10:15:58.553Z',
            'updated_at': '2019-08-12T00:00:32.290Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-12 00:00:31.718903'
            },
            'x': 270,
            'y': 730,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:16:28.732Z',
            'radius': 25.0
        }, {
            'id': 157910,
            'created_at': '2019-07-29T10:48:54.507Z',
            'updated_at': '2019-08-12T00:00:38.029Z',
            'device_id': 5520,
            'name': 'Arugula',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-12 00:00:37.487245'
            },
            'x': 270,
            'y': 900,
            'z': 0,
            'openfarm_slug': 'arugula',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:16:35.334Z',
            'radius': 25.0
        }, {
            'id': 157062,
            'created_at': '2019-07-26T03:32:48.654Z',
            'updated_at': '2019-08-12T00:00:51.742Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-12 00:00:51.155648'
            },
            'x': 280,
            'y': 110,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:16:49.989Z',
            'radius': 25.0
        }, {
            'id': 157891,
            'created_at': '2019-07-29T10:41:23.208Z',
            'updated_at': '2019-08-11T23:41:12.403Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:41:07.564078'
            },
            'x': 280,
            'y': 380,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:16:57.927Z',
            'radius': 25.0
        }, {
            'id': 157902,
            'created_at': '2019-07-29T10:43:38.353Z',
            'updated_at': '2019-08-11T23:19:32.630Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:19:31.708659'
            },
            'x': 340,
            'y': 440,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:17:03.735Z',
            'radius': 25.0
        }, {
            'id': 157927,
            'created_at': '2019-07-29T10:54:03.224Z',
            'updated_at': '2019-08-11T23:19:43.506Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:19:42.157493'
            },
            'x': 370,
            'y': 690,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:17:11.691Z',
            'radius': 25.0
        }, {
            'id': 157916,
            'created_at': '2019-07-29T10:50:03.648Z',
            'updated_at': '2019-08-11T23:19:50.840Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:19:49.457818'
            },
            'x': 370,
            'y': 790,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:17:17.991Z',
            'radius': 25.0
        }, {
            'id': 157877,
            'created_at': '2019-07-29T10:37:01.503Z',
            'updated_at': '2019-08-11T23:20:06.911Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:20:06.374074'
            },
            'x': 380,
            'y': 280,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:17:28.934Z',
            'radius': 25.0
        }, {
            'id': 157900,
            'created_at': '2019-07-29T10:43:34.235Z',
            'updated_at': '2019-08-11T23:20:14.975Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:20:14.308913'
            },
            'x': 420,
            'y': 440,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:17:36.580Z',
            'radius': 25.0
        }, {
            'id': 158386,
            'created_at': '2019-07-31T00:35:16.022Z',
            'updated_at': '2019-08-11T23:20:24.246Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:20:21.705610'
            },
            'x': 470,
            'y': 570,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:17:44.263Z',
            'radius': 25.0
        }, {
            'id': 157922,
            'created_at': '2019-07-29T10:51:14.621Z',
            'updated_at': '2019-08-11T23:20:32.442Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:20:31.605609'
            },
            'x': 470,
            'y': 730,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:17:51.476Z',
            'radius': 25.0
        }, {
            'id': 157911,
            'created_at': '2019-07-29T10:48:57.702Z',
            'updated_at': '2019-08-11T23:20:41.519Z',
            'device_id': 5520,
            'name': 'Arugula',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:20:40.099783'
            },
            'x': 470,
            'y': 900,
            'z': 0,
            'openfarm_slug': 'arugula',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:17:59.027Z',
            'radius': 25.0
        }, {
            'id': 157063,
            'created_at': '2019-07-26T03:32:48.663Z',
            'updated_at': '2019-08-11T23:21:04.183Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:21:03.566111'
            },
            'x': 480,
            'y': 110,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:18:13.685Z',
            'radius': 25.0
        }, {
            'id': 157887,
            'created_at': '2019-07-29T10:41:15.967Z',
            'updated_at': '2019-08-11T23:21:15.075Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:21:14.158671'
            },
            'x': 480,
            'y': 380,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:18:21.584Z',
            'radius': 25.0
        }, {
            'id': 157899,
            'created_at': '2019-07-29T10:43:32.981Z',
            'updated_at': '2019-08-11T23:21:22.615Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:21:21.797685'
            },
            'x': 540,
            'y': 440,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:18:27.708Z',
            'radius': 25.0
        }, {
            'id': 157928,
            'created_at': '2019-07-29T10:54:05.025Z',
            'updated_at': '2019-08-11T23:21:32.931Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:21:32.117416'
            },
            'x': 570,
            'y': 690,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:18:35.289Z',
            'radius': 25.0
        }, {
            'id': 157917,
            'created_at': '2019-07-29T10:50:11.635Z',
            'updated_at': '2019-08-11T23:21:39.668Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:21:38.851899'
            },
            'x': 570,
            'y': 790,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:18:41.080Z',
            'radius': 25.0
        }, {
            'id': 157878,
            'created_at': '2019-07-29T10:37:03.200Z',
            'updated_at': '2019-08-11T23:21:57.209Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:21:55.183215'
            },
            'x': 580,
            'y': 280,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:18:52.084Z',
            'radius': 25.0
        }, {
            'id': 157898,
            'created_at': '2019-07-29T10:43:31.611Z',
            'updated_at': '2019-08-11T23:22:07.271Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:22:04.669530'
            },
            'x': 620,
            'y': 440,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:19:00.207Z',
            'radius': 25.0
        }, {
            'id': 158385,
            'created_at': '2019-07-31T00:35:12.699Z',
            'updated_at': '2019-08-11T23:22:14.514Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:22:13.966250'
            },
            'x': 670,
            'y': 570,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:19:07.407Z',
            'radius': 25.0
        }, {
            'id': 157923,
            'created_at': '2019-07-29T10:51:16.578Z',
            'updated_at': '2019-08-11T23:22:22.654Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:22:21.929243'
            },
            'x': 670,
            'y': 730,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:19:13.979Z',
            'radius': 25.0
        }, {
            'id': 157912,
            'created_at': '2019-07-29T10:48:59.887Z',
            'updated_at': '2019-08-11T23:22:31.351Z',
            'device_id': 5520,
            'name': 'Arugula',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:22:30.301043'
            },
            'x': 670,
            'y': 900,
            'z': 0,
            'openfarm_slug': 'arugula',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:19:20.740Z',
            'radius': 25.0
        }, {
            'id': 157873,
            'created_at': '2019-07-29T10:36:51.917Z',
            'updated_at': '2019-08-11T23:22:55.576Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:22:53.395691'
            },
            'x': 680,
            'y': 110,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:19:35.103Z',
            'radius': 25.0
        }, {
            'id': 157888,
            'created_at': '2019-07-29T10:41:17.482Z',
            'updated_at': '2019-08-11T23:23:11.244Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:23:05.560596'
            },
            'x': 680,
            'y': 380,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:19:43.006Z',
            'radius': 25.0
        }, {
            'id': 157897,
            'created_at': '2019-07-29T10:43:29.483Z',
            'updated_at': '2019-08-11T23:23:16.661Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:23:15.937858'
            },
            'x': 740,
            'y': 440,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:19:48.907Z',
            'radius': 25.0
        }, {
            'id': 157929,
            'created_at': '2019-07-29T10:54:07.236Z',
            'updated_at': '2019-08-11T23:23:26.836Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:23:26.177171'
            },
            'x': 770,
            'y': 690,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:19:56.615Z',
            'radius': 25.0
        }, {
            'id': 157918,
            'created_at': '2019-07-29T10:50:13.478Z',
            'updated_at': '2019-08-11T23:23:34.054Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:23:32.794679'
            },
            'x': 770,
            'y': 790,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:20:02.352Z',
            'radius': 25.0
        }, {
            'id': 157879,
            'created_at': '2019-07-29T10:37:04.760Z',
            'updated_at': '2019-08-11T23:23:50.893Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:23:49.589157'
            },
            'x': 780,
            'y': 280,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:20:14.170Z',
            'radius': 25.0
        }, {
            'id': 158924,
            'created_at': '2019-08-04T09:59:14.300Z',
            'updated_at': '2019-08-11T23:24:03.064Z',
            'device_id': 5520,
            'name': 'Red Carrot',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:24:00.840587'
            },
            'x': 800,
            'y': 550,
            'z': 0,
            'openfarm_slug': 'red-carrot',
            'plant_stage': 'planned',
            'planted_at': None,
            'radius': 25.0
        }, {
            'id': 157896,
            'created_at': '2019-07-29T10:43:25.792Z',
            'updated_at': '2019-08-11T23:24:20.544Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:24:09.293269'
            },
            'x': 820,
            'y': 440,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:20:20.727Z',
            'radius': 25.0
        }, {
            'id': 158388,
            'created_at': '2019-07-31T00:46:28.963Z',
            'updated_at': '2019-08-11T23:41:40.968Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:41:29.377036'
            },
            'x': 850,
            'y': 620,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:20:27.891Z',
            'radius': 25.0
        }, {
            'id': 157924,
            'created_at': '2019-07-29T10:51:18.053Z',
            'updated_at': '2019-08-11T23:41:52.531Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:41:47.163603'
            },
            'x': 870,
            'y': 730,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:20:33.787Z',
            'radius': 25.0
        }, {
            'id': 157913,
            'created_at': '2019-07-29T10:49:01.406Z',
            'updated_at': '2019-08-11T23:42:01.570Z',
            'device_id': 5520,
            'name': 'Arugula',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:42:00.120073'
            },
            'x': 870,
            'y': 900,
            'z': 0,
            'openfarm_slug': 'arugula',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:20:41.413Z',
            'radius': 25.0
        }, {
            'id': 157874,
            'created_at': '2019-07-29T10:36:54.133Z',
            'updated_at': '2019-08-11T23:42:27.607Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:42:23.606761'
            },
            'x': 880,
            'y': 110,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:20:56.090Z',
            'radius': 25.0
        }, {
            'id': 157889,
            'created_at': '2019-07-29T10:41:19.169Z',
            'updated_at': '2019-08-11T23:42:55.385Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:42:37.453925'
            },
            'x': 880,
            'y': 380,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:21:04.128Z',
            'radius': 25.0
        }, {
            'id': 158389,
            'created_at': '2019-07-31T00:46:31.398Z',
            'updated_at': '2019-08-11T23:43:02.864Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:43:02.274462'
            },
            'x': 880,
            'y': 520,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:21:10.538Z',
            'radius': 25.0
        }, {
            'id': 157895,
            'created_at': '2019-07-29T10:43:19.777Z',
            'updated_at': '2019-08-11T23:43:10.522Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:43:08.175133'
            },
            'x': 940,
            'y': 440,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:21:18.161Z',
            'radius': 25.0
        }, {
            'id': 158302,
            'created_at': '2019-07-29T22:56:07.166Z',
            'updated_at': '2019-08-11T23:43:20.217Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:43:17.901248'
            },
            'x': 960,
            'y': 600,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:21:24.703Z',
            'radius': 25.0
        }, {
            'id': 157919,
            'created_at': '2019-07-29T10:50:15.091Z',
            'updated_at': '2019-08-11T23:43:30.935Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:43:28.270291'
            },
            'x': 970,
            'y': 790,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:21:31.688Z',
            'radius': 25.0
        }, {
            'id': 157880,
            'created_at': '2019-07-29T10:37:06.111Z',
            'updated_at': '2019-08-11T23:43:49.518Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:43:46.455966'
            },
            'x': 980,
            'y': 280,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:21:42.543Z',
            'radius': 25.0
        }, {
            'id': 158293,
            'created_at': '2019-07-29T22:55:05.668Z',
            'updated_at': '2019-08-11T23:43:59.326Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:43:58.533894'
            },
            'x': 980,
            'y': 510,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:21:50.319Z',
            'radius': 25.0
        }, {
            'id': 157930,
            'created_at': '2019-07-29T10:54:08.914Z',
            'updated_at': '2019-08-11T23:44:07.940Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:44:07.189389'
            },
            'x': 980,
            'y': 690,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:21:57.034Z',
            'radius': 25.0
        }, {
            'id': 157894,
            'created_at': '2019-07-29T10:43:14.369Z',
            'updated_at': '2019-08-11T23:44:18.161Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:44:17.472200'
            },
            'x': 1020,
            'y': 440,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:22:04.708Z',
            'radius': 25.0
        }, {
            'id': 158301,
            'created_at': '2019-07-29T22:56:02.069Z',
            'updated_at': '2019-08-11T23:44:25.365Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:44:24.854660'
            },
            'x': 1030,
            'y': 570,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:22:11.349Z',
            'radius': 25.0
        }, {
            'id': 157925,
            'created_at': '2019-07-29T10:51:19.509Z',
            'updated_at': '2019-08-11T23:44:37.385Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:44:32.785404'
            },
            'x': 1070,
            'y': 730,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:22:17.832Z',
            'radius': 25.0
        }, {
            'id': 157914,
            'created_at': '2019-07-29T10:49:03.187Z',
            'updated_at': '2019-08-11T23:44:50.821Z',
            'device_id': 5520,
            'name': 'Arugula',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:44:44.978458'
            },
            'x': 1070,
            'y': 900,
            'z': 0,
            'openfarm_slug': 'arugula',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:22:25.267Z',
            'radius': 25.0
        }, {
            'id': 157875,
            'created_at': '2019-07-29T10:36:55.847Z',
            'updated_at': '2019-08-11T23:45:15.049Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:45:14.360395'
            },
            'x': 1080,
            'y': 110,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:22:42.793Z',
            'radius': 25.0
        }, {
            'id': 157890,
            'created_at': '2019-07-29T10:41:20.941Z',
            'updated_at': '2019-08-11T23:45:25.570Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:45:24.932770'
            },
            'x': 1080,
            'y': 380,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:23:00.629Z',
            'radius': 25.0
        }, {
            'id': 158294,
            'created_at': '2019-07-29T22:55:10.332Z',
            'updated_at': '2019-08-11T23:45:33.500Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:45:32.223822'
            },
            'x': 1080,
            'y': 510,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:23:09.488Z',
            'radius': 25.0
        }, {
            'id': 158303,
            'created_at': '2019-07-29T22:56:13.059Z',
            'updated_at': '2019-08-11T23:45:41.838Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:45:40.936701'
            },
            'x': 1080,
            'y': 640,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:23:19.405Z',
            'radius': 25.0
        }, {
            'id': 158300,
            'created_at': '2019-07-29T22:56:00.571Z',
            'updated_at': '2019-08-11T23:45:47.503Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:45:46.838074'
            },
            'x': 1130,
            'y': 570,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:23:29.996Z',
            'radius': 25.0
        }, {
            'id': 157905,
            'created_at': '2019-07-29T10:47:18.363Z',
            'updated_at': '2019-08-11T23:45:54.866Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:45:54.176231'
            },
            'x': 1140,
            'y': 440,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:23:38.721Z',
            'radius': 25.0
        }, {
            'id': 157931,
            'created_at': '2019-07-29T10:54:10.383Z',
            'updated_at': '2019-08-11T23:46:04.889Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:46:04.320081'
            },
            'x': 1170,
            'y': 690,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:23:48.489Z',
            'radius': 25.0
        }, {
            'id': 157920,
            'created_at': '2019-07-29T10:50:16.487Z',
            'updated_at': '2019-08-11T23:46:11.323Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:46:10.764451'
            },
            'x': 1170,
            'y': 790,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:23:55.964Z',
            'radius': 25.0
        }, {
            'id': 157881,
            'created_at': '2019-07-29T10:37:07.845Z',
            'updated_at': '2019-08-11T23:46:27.370Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:46:26.789071'
            },
            'x': 1180,
            'y': 280,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:24:07.579Z',
            'radius': 25.0
        }, {
            'id': 158295,
            'created_at': '2019-07-29T22:55:12.866Z',
            'updated_at': '2019-08-11T23:46:37.193Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:46:36.391515'
            },
            'x': 1180,
            'y': 510,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:24:15.809Z',
            'radius': 25.0
        }, {
            'id': 157906,
            'created_at': '2019-07-29T10:47:19.292Z',
            'updated_at': '2019-08-11T23:46:43.327Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'planted_at': '31-07-2019',
                'last_watering_at': '2019-08-11 23:46:42.192686'
            },
            'x': 1220,
            'y': 440,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:24:27.984Z',
            'radius': 25.0
        }, {
            'id': 158299,
            'created_at': '2019-07-29T22:55:57.898Z',
            'updated_at': '2019-08-11T23:46:50.611Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:46:49.985861'
            },
            'x': 1230,
            'y': 570,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:27:10.319Z',
            'radius': 25.0
        }, {
            'id': 157926,
            'created_at': '2019-07-29T10:51:21.285Z',
            'updated_at': '2019-08-11T23:46:58.690Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:46:58.005311'
            },
            'x': 1270,
            'y': 730,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-07-31T00:37:18.229Z',
            'radius': 25.0
        }, {
            'id': 157915,
            'created_at': '2019-07-29T10:49:05.664Z',
            'updated_at': '2019-08-11T23:47:12.221Z',
            'device_id': 5520,
            'name': 'Arugula',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:47:06.242892'
            },
            'x': 1270,
            'y': 900,
            'z': 0,
            'openfarm_slug': 'arugula',
            'plant_stage': 'planted',
            'planted_at': '2019-07-31T03:00:54.335Z',
            'radius': 25.0
        }, {
            'id': 157876,
            'created_at': '2019-07-29T10:36:57.354Z',
            'updated_at': '2019-08-11T23:47:35.432Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:47:34.248559'
            },
            'x': 1280,
            'y': 110,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-07-30T23:36:18.712Z',
            'radius': 25.0
        }, {
            'id': 157904,
            'created_at': '2019-07-29T10:47:16.515Z',
            'updated_at': '2019-08-11T23:47:46.757Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:47:45.320576'
            },
            'x': 1280,
            'y': 380,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:27:04.208Z',
            'radius': 25.0
        }, {
            'id': 158296,
            'created_at': '2019-07-29T22:55:15.513Z',
            'updated_at': '2019-08-11T23:47:54.703Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:47:53.446105'
            },
            'x': 1280,
            'y': 510,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:26:58.244Z',
            'radius': 25.0
        }, {
            'id': 158304,
            'created_at': '2019-07-29T22:56:15.959Z',
            'updated_at': '2019-08-11T23:48:03.347Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:48:01.366383'
            },
            'x': 1280,
            'y': 640,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:27:27.556Z',
            'radius': 25.0
        }, {
            'id': 158298,
            'created_at': '2019-07-29T22:55:54.740Z',
            'updated_at': '2019-08-11T23:48:10.152Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:48:09.353194'
            },
            'x': 1330,
            'y': 570,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:26:51.498Z',
            'radius': 25.0
        }, {
            'id': 157908,
            'created_at': '2019-07-29T10:47:22.246Z',
            'updated_at': '2019-08-11T23:48:17.918Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:48:16.813059'
            },
            'x': 1340,
            'y': 440,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:26:45.844Z',
            'radius': 25.0
        }, {
            'id': 157932,
            'created_at': '2019-07-29T10:54:12.378Z',
            'updated_at': '2019-08-11T23:48:28.043Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:48:27.324033'
            },
            'x': 1370,
            'y': 690,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-07-31T00:37:16.821Z',
            'radius': 25.0
        }, {
            'id': 157921,
            'created_at': '2019-07-29T10:50:18.007Z',
            'updated_at': '2019-08-11T23:48:34.525Z',
            'device_id': 5520,
            'name': 'Beets',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:48:33.962492'
            },
            'x': 1370,
            'y': 790,
            'z': 0,
            'openfarm_slug': 'beets',
            'plant_stage': 'planted',
            'planted_at': '2019-07-31T00:37:15.981Z',
            'radius': 25.0
        }, {
            'id': 157882,
            'created_at': '2019-07-29T10:37:37.226Z',
            'updated_at': '2019-08-11T23:48:50.913Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:48:50.020104'
            },
            'x': 1380,
            'y': 280,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-07-30T23:59:02.845Z',
            'radius': 25.0
        }, {
            'id': 158297,
            'created_at': '2019-07-29T22:55:17.367Z',
            'updated_at': '2019-08-11T23:49:00.663Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:48:59.923415'
            },
            'x': 1380,
            'y': 510,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planned',
            'planted_at': None,
            'radius': 25.0
        }, {
            'id': 157909,
            'created_at': '2019-07-29T10:47:23.057Z',
            'updated_at': '2019-08-11T23:49:06.273Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:49:05.705351'
            },
            'x': 1420,
            'y': 440,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:26:27.053Z',
            'radius': 25.0
        }, {
            'id': 158305,
            'created_at': '2019-07-29T22:58:10.330Z',
            'updated_at': '2019-08-11T23:49:13.756Z',
            'device_id': 5520,
            'name': 'Cherry Belle Radish',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:49:12.925629'
            },
            'x': 1430,
            'y': 570,
            'z': 0,
            'openfarm_slug': 'cherry-belle-radish',
            'plant_stage': 'planted',
            'planted_at': '2019-08-01T20:26:20.036Z',
            'radius': 25.0
        }, {
            'id': 158306,
            'created_at': '2019-07-29T23:00:24.712Z',
            'updated_at': '2019-08-11T23:49:25.964Z',
            'device_id': 5520,
            'name': 'Arugula',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 23:49:25.090320'
            },
            'x': 1470,
            'y': 900,
            'z': 0,
            'openfarm_slug': 'arugula',
            'plant_stage': 'planted',
            'planted_at': '2019-07-31T03:00:55.008Z',
            'radius': 25.0
        }, {
            'id': 158307,
            'created_at': '2019-07-29T23:00:44.093Z',
            'updated_at': '2019-08-11T20:33:36.645Z',
            'device_id': 5520,
            'name': 'Spinach',
            'pointer_type': 'Plant',
            'meta': {
                'last_watering_at': '2019-08-11 20:33:36.044854'
            },
            'x': 1480,
            'y': 110,
            'z': 0,
            'openfarm_slug': 'spinach',
            'plant_stage': 'planted',
            'planted_at': '2019-07-30T23:59:01.902Z',
            'radius': 25.0
        }]
