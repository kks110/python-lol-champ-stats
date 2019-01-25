# python-lol-champ-stats
This is a python script which will talk to the Riot Static game data API.

It will pull all of the stats (eg, health, health regen, AD, ect..) for all of the champions in the game.

It will then save the data to a CSV file.

The static data is manually updated by the Riot team.

When a patch comes out, it wont always be up to date the same day.

Requests is required for this to run. Install with pip:
```
py -m pip install requests
```
