# [FARMWARE] Smart Water Doser for Farmbot

From current position, finds closest plant, and automatically calculates how much water to dose it in milliseconds.

Calculation is based on spread and height parameters from OpenFarm. Parameters can be modified from configuration, see [manifest](manifest.json).

Uses SimpleCache, based on built in Pickle to cache API calls.

> FARMBOT_OS 6. Tested only on 7.0.1 for now. Should work on 6. Please open an issue with problems for other versions.

> Smart Watering functions adapted from https://github.com/etcipnja/MLH, thank you @etcipnja!

> Future, check the weather for past rain and adapt dose