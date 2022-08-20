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

def getStory():
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
            time.sleep(0.5)



def mainLoop():
    if isWindowFocus(screenOpts):
        #clickGame(screenOpts, Clicks.windowBar)  # windowFocus
        print(1)




    #else:
        #playsound('res\\mario.mp3')

def main():
    updateWindow(screenOpts)
    clickGame(screenOpts,Clicks.windowBar) #windowFocus

    launchApp()
    gotoLibrary()
    getStory()

    while True:
        updateWindow(screenOpts)
        printCoords(screenOpts)
        time.sleep(1)

        #scrollUp()

        mainLoop()

if __name__ == '__main__':
    main()

