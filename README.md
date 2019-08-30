# [FARMWARE] Water Doser for Farmbot

From current Farmbot position, finds closest plant, and automatically calculates how much water to dose it in milliseconds. Takes into consideration past 12 hours and next 6 hours of forecasted rain obtained from Dark Sky API.

Calculation is based on spread and height parameters from OpenFarm along with plant age. Parameters can be modified from configuration, see [manifest](manifest.json).

Uses SimpleCache, based on built in Pickle to cache API calls.

> FARMBOT_OS 6. Tested only on 7.0.1 for now. Should work on 6. Please open an [issue](../../issues) with any problems.

> I need help coming up with a better function for water plants with the data available, including weather information. If you have better ideas than the current implementation, please open an issue or message me. Current method in [water_dose.py](https://github.com/amerkay/water-doser/blob/master/src/water_dose.py) `\_get_supposed_watering()` function, adapted from https://github.com/etcipnja/MLH, thank you @etcipnja!

## Installation

Go to [My Farmbot -> Farmware](https://my.farm.bot/app/farmware/), then paste the manifest.json path to install:
```
https://raw.githubusercontent.com/amerkay/water-doser/master/manifest.json
```

## Developers

I tried to add as much comments and documentation within the files, as well as clear variable and method naming. If you want to use one of the files in your own project, I made sure they are as self-contained and documented as possible. Please use freely. Pull requests appreciated - even if it takes me time to get to it.

## Features

Smart Water Doser Farmware:

- From current Farmbot position, guesses which plant within area set and loads the point.
- Then uses spread and height from OpenFarm and age to decide how many ml/ms to water the plant.
- Caching OpenFarm and other expensive (slow) API calls using SimpleCache file caching.
- Write digital watering PIN ON, then wait for calculated period, then OFF.
- Get historical/forecasted rain and weather from Dark Sky API, then uses the hourly data to sum up rain stats (precipIntensity * precipProbability). Water dose adapted within window of time, hardcoded to past 12 hours historical data, next 6 hours of forecast.

## PowerLoop's Input Variables Documentation

[See manifest.json](manifest.json), includes extra "help" key with more information.

## Example usage

[Water all Farmbot plants using 'PowerLoop' farmware](https://github.com/amerkay/powerloop/blob/master/examples/Smart%20Watering%20for%20Farmbot.md), automatically calculating how many seconds to water each plant individually based on it's age and maximum spread from OpenFarm data.
