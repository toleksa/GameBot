# Duolingo
### for Duolingo - [Google Play](https://play.google.com/store/apps/details?id=com.duolingo)
Bot which can solve Story in Duolingo

## Tech

Bot uses following libraries:
- [pypiwin32](https://pypi.org/project/pypiwin32/) - windows handling, mouse cursor move, clicks
- [playsound](https://pypi.org/project/playsound/) - sound notifications
- [numpy](https://pypi.org/project/numpy/) [image](https://pypi.org/project/image/) [opencv](https://pypi.org/project/opencv-python/) - image recognition
- [easyocr](https://pypi.org/project/easyocr/) - read/recognize text
- [googletrans](https://pypi.org/project/googletrans/) - translation


## How it works

GameBot has two main parts. libBot.py is a toolkit handling all technical stuff like mouse control, window control or image recognition. On top of that, Duolingo.py has the game logic with all steps required to perform in-app tasks to choose and solve story.

On technical level, modus operandi is to check on screen, using image recognition, if there is particular button/symbol, click it and check results - for example another button/symbol appeared on screen, then proceed with next step.

## Installation

```pip install -r requirements.txt```

OR

```pip install pypiwin32 playsound==1.2.2 Image numpy opencv-python easyocr googletrans>=3.1.0a0```

## Configuration

No configuration, just fire & forget

## Demo

![full.gif](https://raw.githubusercontent.com/toleksa/GameBot/main/duolingo/doc/full.gif)

## Details

### Find story

### Go through the story

### Quiz

![quiz.png](https://raw.githubusercontent.com/toleksa/GameBot/main/duolingo/doc/quiz.png)
