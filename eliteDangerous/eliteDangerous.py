from libBot import *
from directInput import *
import inspect

Clicks = {
    windowBar = (200,200),
}

def docking():
    print("docking")
    Key(0x43) #C - throttle 100%
    time.sleep(10)
    Key(0x58) #X - throttle 0%
    Key(0x31) #1 - external panel
    while findImgOnScreen(screenOpts, 'res\\contacts.png') == 0:
        Key(0x45) #e - interface right
    Key(0x20) #space - enter
    Key(0x44) #d - interface right
    Key(0x20) #space - enter
    Key(0x08) #backspace - go back
    print("docking complete")

def dock():
    #screenOpts.debug=1
    if findImgOnScreen(screenOpts, 'res\\supercruise.png') != 0:
        print("supercruise detected")
        while True:
            if findImgOnScreen(screenOpts, 'res\\supercruise.png') != 0:
                print('.', end="", flush=True)
            elif findImgOnScreen(screenOpts, 'res\\supercruise3.png') == 0:
                break
        if not isWindowFocus(screenOpts):
            clickGame(screenOpts, Clicks['windowBar'])  # windowFocus
        docking()
        #print("exiting")
        #exit(0)
    
    #else:
        #print("no supercruise detected")
        #playsound('res\\mario.mp3')
    #loopDelay(300,-1,'res\\ding.mp3')

def main():
    #listWindows()
    screenOpts.windowName='Elite - Dangerous (CLIENT)'
    updateWindow(screenOpts)
    clickGame(screenOpts,Clicks['windowBar']) #windowFocus
    
    #docking()

    while True:
        updateWindow(screenOpts)
        printCoords(screenOpts)
        time.sleep(1)

        dock()


if __name__ == '__main__':
    main()

