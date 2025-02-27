from libBot import *
from directInput import *
import inspect

Clicks = {
    'windowBar': (200,200),
    'bookmarks': (92,280),
    'loc1': (600,400),
    'loc2': (600,600),
}

screen = screenOpts()

def overwrite():
    print("overwrite screen values")
    screen.x_min=0
    screen.y_min=0
    screen.x_max=3840
    screen.y_max=2160
    screen.x_len=3840
    screen.y_len=2160
    screen.dim_sum=-1
    print(screen)

def docking():
    print("docking")
    Key(0x43) #C - throttle 100%
    time.sleep(10)
    Key(0x58) #X - throttle 0%
    Key(0x31) #1 - external panel
    while findImgOnScreen(screen, 'res\\contacts.png') == 0:
        Key(0x45) #e - interface right
    Key(0x20) #space - enter
    while not findImgOnScreen(screen, 'res\\dockinggranted.png', 0.8) and not findImgOnScreen(screen, 'res\\canceldocking.png', 0.8):
        Key(0x44) #d - interface right
        Key(0x20) #space - enter
    Key(0x08) #backspace - go back
    print("waiting for docking")
    while not findImgOnScreen(screen, 'res\\starportservices1.png', 0.8):
        time.sleep(1)
    print("docking complete")

def dock():
    #screen.debug=1
    if findImgOnScreen(screen, 'res\\supercruise.png') != 0:
        print("supercruise detected")
        while True:
            if findImgOnScreen(screen, 'res\\supercruise.png') != 0:
                print('.', end="", flush=True)
            elif findImgOnScreen(screen, 'res\\supercruise3.png') == 0:
                break
        if not isWindowFocus(screen):
            clickGame(screen, Clicks['windowBar'])  # windowFocus
        docking()
        #print("exiting")
        #exit(0)
    
    #else:
        #print("no supercruise detected")
        #playsound('res\\mario.mp3')
    #loopDelay(300,-1,'res\\ding.mp3')

def aimTarget():
    print("targeting")
    target=(1473,1646)
    while True:
        printCoords(screen)

        #screen.debug=1
        if findImgOnScreen(screen, 'res\\markerempty2.png', 0.8, 1600, screen.y_len-1850, 1380, screen.x_len-1580) or not findImgOnScreen(screen, 'res\\marker3.png', 0.8, 1600, screen.y_len-1850, 1380, screen.x_len-1580):
            if isWindowFocus(screen):
                Key(0x62, pressTime=0.5)
            else:
                print("no focus, NOP")
            time.sleep(2)
        pointer = findImgOnScreen(screen, 'res\\marker3.png', 0.8, 1600, screen.y_len-1850, 1380, screen.x_len-1580)
        if pointer != 0:
            dx=target[0]-pointer[0]
            dy=target[1]-pointer[1]
            print(f"diff: {dx}, {dy}")
            if abs(dx)<5 and abs(dy)<5 or findImgOnScreen(screen, 'res\\supercruise.png', 0.8) or findImgOnScreen(screen, 'res\\supercruise2.png', 0.8):
                print("targeting complete")
                return 0
            if isWindowFocus(screen):
                if dx > 1:
                    Key(0x41,pressTime=0.05*abs(dx))
                if dx < -1:
                    Key(0x44,pressTime=0.05*abs(dx))
                if dy > 1:
                    Key(0x68,pressTime=0.05*abs(dy))
                if dy < -1:
                    Key(0x62,pressTime=0.05*abs(dy))
            else:
                print("no focus, NOP")
            time.sleep(2)

def jump():
    print("commencing jump")
    if not findImgOnScreen(screen, 'res\\shipmarkers.png', 0.8):
        Key(0x57,pressTime=1)
    while True:
        #screen.debug=1
        if findImgOnScreen(screen, 'res\\shipmarkers.png', 0.6, Yoffset=1820, Xoffset=3200, YbottomOffset=screen.y_len-1950, XrightOffset=screen.x_len-3280):
            Key(0x4a) #J - jump
            Key(0x43) #C - throttle 100%
            print("waiting for charge",end='')
            while not findImgOnScreen(screen, 'res\\charging.png', 0.8):
                print(".",end='')
                time.sleep(1)
            print("waiting for jump",end='')
            while findImgOnScreen(screen, 'res\\charging.png', 0.8):
                print(".",end='')
                time.sleep(1)
            print("jump complete")
            return 0
        time.sleep(1)

def autolaunch():
    if findImgOnScreen(screen, 'res\\starportservices1.png', 0.8):
        Key(0x53) #S - menu down
    if findImgOnScreen(screen, 'res\\autolaunch1.png', 0.8):
        Key(0x20) #space - enter
    else:
        fail("autolaunch not found")

def setNav(loc):
    print(f"setting navigation to {loc}")
    Key(0x31) #1 - left panel
    while not findImgOnScreen(screen, 'res\\navigation.png', 0.8):
        Key(0x45) #E - menu tab right
    Key(0x41) #A - menu left
    while not findImgOnScreen(screen, 'res\\galaxymap1.png', 0.8):
        Key(0x53) #S - menu down
    Key(0x20) #space - enter
    time.sleep(2)
    if not findImgOnScreen(screen, 'res\\nav-currentsystem.png', 0.8):
        fail("not in galaxy map")
    clickGame(screen,Clicks['bookmarks'])
    clickGame(screen,Clicks[loc],pressTime=2)
    Key(0x08) #backspace - menu back
    Key(0x08) #backspace - menu back
    Key(0x08) #backspace - menu back
    Key(0x08) #backspace - menu back
    Key(0x08) #backspace - menu back
    Key(0x08) #backspace - menu back
    Key(0x08) #backspace - menu back
    Key(0x08) #backspace - menu back
    print("navigation set")

def waitForAutolaunch():
    while True:
        if findImgOnScreen(screen, 'res\\autolaunchcomplete-mini.png', 0.8) or findImgOnScreen(screen, 'res\\autolaunchcomplete-big.png', 0.8):
            return 0
        time.sleep(0.5)

def setTarget(target):
    print(f"setting target to: {target}")
    while not findImgOnScreen(screen, 'res\\galaxysymbol.png', 0.8) and not findImgOnScreen(screen, 'res\\systemsymbol.png', 0.8):
        if isWindowFocus(screen):
            Key(0x31) #1 - left panel
        else:
            print("no focus, NOP")
        time.sleep(0.1)
    while not findImgOnScreen(screen, target, 0.6):
        if isWindowFocus(screen):
            Key(0x53) #S - menu down
        else:
            print("no focus, NOP")
        time.sleep(0.1)
    Key(0x20) #space - enter
    Key(0x44) #D - menu right
    Key(0x20) #space - enter
    Key(0x08) #backspace - menu back
    print("target set")

def restock():
    print("restocking")
    Key(0x57) #W - menu up
    Key(0x20) #space - enter
    Key(0x44) #D - menu right
    Key(0x20) #space - enter
    Key(0x44) #D - menu right
    Key(0x20) #space - enter
    Key(0x53) #S - menu down
    print("restocking complete")

def trade(sell,buy,menu):
    Key(0x20) #space - enter
    time.sleep(3)
    Key(menu) #menu set commodities market
    Key(0x20) #space - enter
    time.sleep(5)
    Key(0x53) #S - menu down
    Key(0x20) #space - enter
    Key(0x44) #D - menu right
    while not findImgOnScreen(screen, sell, 0.8):
        if isWindowFocus(screen):
            Key(0x53) #S - menu down
        else:
            print("no focus, NOP")
        time.sleep(0.1)
    Key(0x20) #space - enter
    Key(0x53) #S - menu down
    Key(0x20) #space - enter -> sell
    Key(0x41) #A - menu right
    Key(0x57) #W - menu up
    Key(0x20) #space - enter
    Key(0x44) #D - menu right
    Key(0x53,pressTime=5) 
    while not findImgOnScreen(screen, 'res\\exit2.png', 0.6):
        if isWindowFocus(screen):
            Key(0x53) 
        else:
            print("no focus, NOP")
        time.sleep(0.05)
    while not findImgOnScreen(screen, buy, 0.8):
        if isWindowFocus(screen):
            Key(0x57) #W - menu down
        else:
            print("no focus, NOP")
        time.sleep(0.1)
    Key(0x20) #space - enter
    Key(0x57) #W - menu right
    Key(0x44,pressTime=5) #D - menu right
    Key(0x53) #S - menu down
    Key(0x20) #space - enter
    Key(0x08) #backspace - menu back
    Key(0x08) #backspace - menu back

def route(loc,target,sell,buy,menu):
    autolaunch()
    setNav(loc)
    waitForAutolaunch()
    aimTarget()
    jump()
    time.sleep(20)
    setTarget(target)
    aimTarget()
    dock()
    restock()
    trade(sell,buy,menu)
    

def main():
    #listWindows()
    screen.windowName='Elite - Dangerous (CLIENT)'
    updateWindow(screen)
    clickGame(screen,Clicks['windowBar']) #windowFocus
    overwrite()    

    #docking()
    #screen.debug=1
    #grabGameWindow(screen,Yoffset=0,YbottomOffset=0,Xoffset=0,XrightOffset=0)
    #grabFragment(screen,1425,1600,1540,1705)
    #target()
    #jump()
    #Key(0x43) #C - throttle 100%
    dock()
    #route('loc2','res\\target-serebrovcity2.png','res\\powergenerators.png','res\\silver.png',0x44)
    #route('loc1','res\\target-soloorbiter2.png','res\\silver.png','res\\powergenerators.png',0x53)
    #docking()
    #restock()
    #trade('res\\powergenerators.png','res\\silver.png',0x44)
    #trade('res\\silver.png','res\\powergenerators.png',0x53)


    while True:
        printCoords(screen)
        time.sleep(1)

        #dock()
        #exit(0)


if __name__ == '__main__':
    main()

