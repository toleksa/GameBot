from libBot import *
from libDuo import *

# TODO: change class to dictionary
class Clicks:
    windowBar = (200,-20)
    appsMenu = (600, 1000)
    clearAll = (500, 70)

def launchApp():
    if clickImage(2, 'res\\appicon.png'):

        updateWindow(screenOpts)

        counter = 30
        while True:
            pointer = findImgOnScreen(screenOpts, 'res\\menubar.png', 1, 940)
            if pointer != 0:
                break
            counter-=1
            if counter <= 0:
                fail("app failed to start")
            time.sleep(1)

def gotoLibrary():
    if not clickImage(2, 'res\\bookicon2.png'):

        pointer = findImgOnScreen(screenOpts, 'res\\bookicon.png')
        if pointer != 0:
            pointer = (pointer[0] + 30, pointer[1] + 30)
            clickAbsolute(screenOpts, pointer, 0.5)
            time.sleep(1)

    pointer = findImgOnScreen(screenOpts, 'res\\bookicon2.png')
    if pointer == 0:
        fail("failed to go to library")

def getStory1():
    counter=200
    while True:
        pointer = findImgOnScreen(screenOpts, 'res\\story1icon.png', 0.9)
        if pointer != 0:
            pointer = (pointer[0] + 30, pointer[1] + 30)
            clickAbsolute(screenOpts, pointer, 0.5)
            time.sleep(3)
            return 0
        else:
            scrollUp()
            counter-=1
            if counter==0:
                fail("failed to scroll to story")
            time.sleep(1.5)

def reset():
    print("reset")
    clickGame(screenOpts,Clicks.appsMenu,1)
    clickGame(screenOpts, Clicks.clearAll,1)
    launchApp()
    gotoLibrary()
    getStory1()

def clickContinue(sleep=0.5):
    return clickImage(sleep, 'res\\continue.png', 0.9, 900)

def story1():
    print("story1")
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickImage(2,'res\\story1\\001-woIstMeinPass.png'): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickImage(2, 'res\\story1\\002-yesThatsRight.png'): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickImage(2, 'res\\story1\\003-lauft.png'): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickImage(2, 'res\\story1\\004-nicht.png'): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickContinue(4): return False
    if not clickImage(2, 'res\\story1\\005-inHisHand.png'): return False
    if not clickContinue(4): return False
    return True

def mainLoop():
    if isWindowFocus(screenOpts):

        return story1()

    #else:
        #playsound('res\\error.mp3')

def main():
    updateWindow(screenOpts)
    clickGame(screenOpts,Clicks.windowBar) #windowFocus

    # for testing individual functions
    #reset()
    #mainLoop()
    #quiz()
    #exit(1)

    while True:
        updateWindow(screenOpts)
        printCoords(screenOpts)

        # reset()
        getStory1()
        if not mainLoop():
            reset()
            continue
        quiz()
        if not clickImage(2, 'res\\continueBlue.png'):
            reset()
            continue

        time.sleep(1)

if __name__ == '__main__':
    main()

