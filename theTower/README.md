# The Tower
### for The Tower - [Google Play](https://play.google.com/store/apps/details?id=com.TechTreeGames.TheTower)
Very simple bot to farm resources by playing again and again

## Tech

Bot uses following libraries:
- [pypiwin32](https://pypi.org/project/pypiwin32/) - windows handling, mouse cursor move, clicks
- [playsound](https://pypi.org/project/playsound/) - sound notifications
- [numpy](https://pypi.org/project/numpy/) [image](https://pypi.org/project/image/) [opencv](https://pypi.org/project/opencv-python/) - image recognition


## How it works

GameBot has two main parts. libBot.py is a toolkit handling all technical stuff like mouse control, window control or image recognition. On top of that, LostCrusade.py has the game logic with all steps required to perform in-game tasks like send army to gather resources or order production of new units.

On technical level, modus operandi is to check on screen, using image recognition, if there is particular button/symbol, click it and check results - for example another button/symbol appeared on screen, then proceed with next step.

## Installation

```pip install -r requirements.txt```

OR

```pip install pypiwin32 playsound==1.2.2 Image numpy opencv-python```

## Configuration

No configuration, just fire & forget

