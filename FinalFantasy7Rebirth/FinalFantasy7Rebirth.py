from libBot import *
from directInput import *
import inspect


def mainLoop():
    if isWindowFocus(screenOpts):
        pointer = findImgOnScreen(screenOpts, 'res\\challengeComplete.png')
        if pointer != 0:
            Key(0x52) #R
            Key(0x26) #UP Arrow
            Key(0x0D) #Enter
    else:
        print("switch focus to game window")

def main():
    #listWindows()    
    screenOpts.windowName='FINAL FANTASY VII REBIRTH'
    updateWindow(screenOpts)

    while True:
        updateWindow(screenOpts)
        printCoords(screenOpts)
        time.sleep(1)

        mainLoop()



if __name__ == '__main__':
    main()

