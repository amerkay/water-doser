# [FARMWARE] Water Doser for Farmbot

From current position, finds closest plant, and automatically calculates how much water to dose it in milliseconds.

Calculation is based on spread and height parameters from OpenFarm along with plant age. Parameters can be modified from configuration, see [manifest](manifest.json).

Uses SimpleCache, based on built in Pickle to cache API calls.

> FARMBOT_OS 6. Tested only on 7.0.1 for now. Should work on 6. Please open an [issue](../../issues) with any problems.

> Smart Watering functions adapted from https://github.com/etcipnja/MLH, thank you @etcipnja!

> IN PROGRESS: Check the weather from Dark Sky API for past/expected rain and adapt dose within a window of time (last 12 hours, next 6 hours).

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

## PowerLoop's Input Variables Documentation

[See manifest.json](manifest.json), includes extra "help" key with more information.

## Example usage

[Water all Farmbot plants using 'PowerLoop' farmware](https://github.com/amerkay/powerloop/blob/master/examples/Smart%20Watering%20for%20Farmbot.md), automatically calculating how many seconds to water each plant individually based on it's age and maximum spread from OpenFarm data.
