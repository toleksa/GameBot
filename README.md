# GameBot 
### for Warhammer 40000 Lost Crusade [Google Play](https://play.google.com/store/apps/details?id=com.orcacorp.wargame)
Your personal assistant for repetitive tasks including:
* Resource collection
* Join Breach Assault (in game event)
* Help other alliance members
* Claim drops from Landing Pad
* Request army production
* Restart crashed game application

## Tech

Bot uses following libraries:
- [pypiwin32](https://pypi.org/project/pypiwin32/) - windows handling, mouse cursor move, clicks
- [playsound](https://pypi.org/project/playsound/) - sound notifications
- [numpy](https://pypi.org/project/numpy/) [image](https://pypi.org/project/image/) [opencv](https://pypi.org/project/opencv-python/) - image recognition

## Installation & Launch

```pip install pypiwin32 playsound Image numpy opencv-python```

```python LostCrusade.py```

## Configuration


```python
def mainLoop():
    ...
    #enabled routines:
    crashedApp()
    gatherResources()
    if findImgOnScreen(screenOpts, 'res\\armyList2.png') != 0:
        clickGame(screenOpts, clicks.events, 1)
    joinBreach()
    helpFlag()
    helpFlag()
    dropship()
    trainArmy()
    ...
```

mainLoop() contains tasks for GameBot to execute, they can be disabled by commenting out unneeded routines

## How it works

Most of the time for this game, modus operandi is to find on screen, using image recognition if there is particular button/symbol using image recognition, click it and check results - for example another button/symbol appeared on screen, then proceed with next step.

### Example for Gather Resources. 
* Click ARMY button (1)
![1](https://raw.githubusercontent.com/toleksa/GameBot/main/doc/1.png)

* Check if there is free army slot:
![vacant](https://raw.githubusercontent.com/toleksa/GameBot/main/res/vacant.png)
![2](https://raw.githubusercontent.com/toleksa/GameBot/main/doc/2.png)

* Found free slot, so next step is to look for resources (2)
![3](https://raw.githubusercontent.com/toleksa/GameBot/main/doc/3.png)

* Choose resource type (3) - by default it goes by round robin for all four types and can be adjusted in nextRSS()
![4](https://raw.githubusercontent.com/toleksa/GameBot/main/doc/4.png)

* Check if there is collect icon and click it (5)
![5](https://raw.githubusercontent.com/toleksa/GameBot/main/doc/5.png)

* Deploy army (6)
![6](https://raw.githubusercontent.com/toleksa/GameBot/main/doc/6.png)

* Army is traveling to resource deposit for gathering - success
![7](https://raw.githubusercontent.com/toleksa/GameBot/main/doc/7.png)

* Yes, I skipped step (4) ;)

### Example for Landing Pad:
* Locate dropship icon and click it
![9](https://raw.githubusercontent.com/toleksa/GameBot/main/doc/9.png)

* If there is CLAIM button, get reward
![10](https://raw.githubusercontent.com/toleksa/GameBot/main/doc/10.png)

* Otherwise CLOSE window and come back later - in this example CLOSE button is on same place as CLAIM, but sometimes it's X in corner, this situation is also handled by bot.
![11](https://raw.githubusercontent.com/toleksa/GameBot/main/doc/11.png)

### Example output on console
![8](https://raw.githubusercontent.com/toleksa/GameBot/main/doc/8.png)

## License

MIT

**Free Software, Hell Yeah!**
