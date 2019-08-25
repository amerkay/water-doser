# [FARMWARE] Water Doser for Farmbot

From current position, finds closest plant, and automatically calculates how much water to dose it in milliseconds.

Calculation is based on spread and height parameters from OpenFarm. Parameters can be modified from configuration, see [manifest](manifest.json).

Uses SimpleCache, based on built in Pickle to cache API calls.

> FARMBOT_OS 6. Tested only on 7.0.1 for now. Should work on 6. Please open an [issue](../../issues) with any problems.

> Smart Watering functions adapted from https://github.com/etcipnja/MLH, thank you @etcipnja!

> TODO: check the weather for past/expected rain and adapt dose

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
- Then uses spread and age from to decide how many ml/ms to water the plant.
- Caching OpenFarm and other expensive (slow) API calls using SimpleCache file cachine.
- Write digital watering PIN ON, then wait for calculated period, then OFF.

## PowerLoop's Input Variables Documentation

[See manifest.json](manifest.json), includes extra "help" key with more information.