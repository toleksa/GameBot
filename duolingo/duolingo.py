from libBot import *
import inspect

# TODO: change class to dictionary
class Clicks:
    windowBar = (200,-20)

def fail(text):
    print("ERR: " + text)
    exit(1)

def launchApp():
    pointer = findImgOnScreen(screenOpts, 'res\\appicon.png')
    if pointer != 0:
        pointer = (pointer[0] + 30, pointer[1] + 30)
        clickAbsolute(screenOpts, pointer, 0.5)

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
    pointer = findImgOnScreen(screenOpts, 'res\\bookicon2.png')
    if pointer == 0:

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
        pointer = findImgOnScreen(screenOpts, 'res\\story1icon.png', 1)
        if pointer != 0:
            pointer = (pointer[0] + 30, pointer[1] + 30)
            clickAbsolute(screenOpts, pointer, 0.5)
            return 0
        else:
            scrollUp()
            counter-=1
            if counter==0:
                fail("failed to scroll to story")
            time.sleep(1.5)

def reset():
    print("reset")
    launchApp()
    gotoLibrary()
    getStory1()

def clickContinue(sleep=0.5):
    return clickImage(sleep, 'res\\continue.png', 0.9, 900)

def story1():
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
    if not clickImage(2, 'res\\story1\\005-inHisHang.png'): return False
    if not clickContinue(4): return False

def mainLoop():
    if isWindowFocus(screenOpts):
        #clickGame(screenOpts, Clicks.windowBar)  # windowFocus

        if not story1(): reset()

    #else:
        #playsound('res\\mario.mp3')

def main():
    updateWindow(screenOpts)
    clickGame(screenOpts,Clicks.windowBar) #windowFocus

    #reset()
    mainLoop()
    exit(1)

    while True:
        updateWindow(screenOpts)
        printCoords(screenOpts)

        #mainLoop()

        time.sleep(1)

if __name__ == '__main__':
    main()

