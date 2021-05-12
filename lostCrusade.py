from libBot import *

class clicks:
    windowBar = (200,-20)
    noxApps = (1790,980)
    starMap = (135,875)
    armies = (70,370)
    mapSearch = (1537,781)
    #without assault breach
    #mapMetal = (720,690)
    #mapFuel = (880,690)
    #mapAda = (1040,690)
    #mapPlasma = (1200, 690)
    #with assault breach icon
    mapMetal = (680,690)
    mapFuel = (820,690)
    mapAda = (960,690)
    mapPlasma = (1100, 690)
    mapCrystal = (1240, 690)
    mapRss = [mapMetal,mapFuel,mapAda,mapPlasma,mapCrystal]
    mapExplore = (1324,900)
    mapCollect = (1070,460)
    mapDeploy = (1590,890)
    events = (1680, 140)
    joinBreach = (1580,660)
    eventsClose = (1705, 85)
    trainButton = (1600, 900)
    back = (60, 30)

class gameState:
    lastRss = 0

def nextRss():
    print("getRSS: [",int(gameState.lastRss)," % 4] => ", gameState.lastRss % 4, sep='')
    click = (clicks.mapRss[gameState.lastRss % 4])
    gameState.lastRss+=1
    return click

def crashedApp():
    print("Starting " + sys._getframe().f_code.co_name)
    pointer = findImgOnScreen(screenOpts, 'res\\appIcon3.png')
    if pointer != 0:
        clickGame(screenOpts, clicks.noxApps, 1)
        while True:
            pointer2 = findImgOnScreen(screenOpts, 'res\\noxX.png')
            if pointer2 != 0:
                pointer2 = (pointer2[0] + 20, pointer2[1] + 20)
                clickGame(screenOpts, pointer2, 0.5)
            else:
                break
        pointer2 = findImgOnScreen(screenOpts, 'res\\noRecentItems.png')
        if pointer2 != 0:
            clickGame(screenOpts, clicks.noxApps, 1)
        pointer = (pointer[0] + 40, pointer[1] + 40)
        clickGame(screenOpts, pointer, 0.5)
        counter=0
        while True:
            time.sleep(5)
            counter+=1
            pointer = findImgOnScreen(screenOpts, 'res\\noticeClose.png')
            if pointer != 0:
                pointer = (pointer[0] + 30, pointer[1] + 30)
                clickGame(screenOpts, pointer, 0.5)
                break
            else:
                if counter > 30:
                    print("restart failed")
                    exit(1)

def joinBreach():
    print("Starting " + sys._getframe().f_code.co_name)
    pointer = findImgOnScreen(screenOpts, 'res\\events2.png')
    if pointer != 0:
        clickGame(screenOpts, pointer, 1)
        pointer = findImgOnScreen(screenOpts, 'res\\events2.png')
        if pointer != 0:
            clickGame(screenOpts, pointer, 1)
        pointer = findImgOnScreen(screenOpts, 'res\\breachAssault2.png')
        if pointer != 0:
            pointer = (pointer[0]+80,pointer[1]+40)
            clickGame(screenOpts, pointer, 0.5)
        if findImgOnScreen(screenOpts, 'res\\join.png') != 0:
            clickGame(screenOpts, clicks.joinBreach, 1)
        clickGame(screenOpts, clicks.eventsClose, 1)

def gatherResources():
    print("Starting " + sys._getframe().f_code.co_name)
    if findImgOnScreen(screenOpts, 'res\\starMap.png') != 0:
        print("switch to map")
        clickGame(screenOpts, clicks.starMap, 4)
    if findImgOnScreen(screenOpts, 'res\\armyList2.png') == 0:
        print("get army list")
        clickGame(screenOpts, clicks.armies, 1)
    if findImgOnScreen(screenOpts, 'res\\vacant.png') != 0:
        clickGame(screenOpts, clicks.mapSearch, 1)
        clickGame(screenOpts, clicks.mapSearch, 1)
        if findImgOnScreen(screenOpts, 'res\\explore.png') != 0:
            clickGame(screenOpts, nextRss(), 1)
            clickGame(screenOpts, clicks.mapExplore, 2)
            clickGame(screenOpts, clicks.mapCollect, 1)
            clickGame(screenOpts, clicks.mapDeploy, 1)
            gatherResources()
        else:
            print("ERROR - no explore")

def helpFlag():
    print("Starting " + sys._getframe().f_code.co_name)
    Yoffset=710
    pointer = findImgOnScreen(screenOpts, 'res\\helpFlag.png', 0.8, Yoffset)
    if pointer != 0:
        pointer = (pointer[0]+20,pointer[1]+20)
        clickGame(screenOpts, pointer, 0.5)

def dropship():
    print("Starting " + sys._getframe().f_code.co_name)
    #TODO: find list of images
    pointer = findImgOnScreen(screenOpts, 'res\\dropship3.png')
    if pointer != 0:
        pointer = (pointer[0]+20,pointer[1]+20)
        clickGame(screenOpts, pointer, 0.5)
        pointer2 = findImgOnScreen(screenOpts, 'res\\claim2.png')
        if pointer2 != 0:
            pointer2 = (pointer2[0]+20,pointer2[1]+20)
            clickGame(screenOpts, pointer2, 0.5)
        else:
            clickGame(screenOpts, pointer, 0.5)

def trainArmy():
    print("Starting " + sys._getframe().f_code.co_name)
    while True:
        pointer0 = findImgOnScreen(screenOpts, 'res\\trainButton.png')
        if pointer0 == 0:
            print("ERROR - trainButton")
            break
        clickGame(screenOpts, pointer0, 1)

        pointer = findImgOnScreen(screenOpts, 'res\\vacant.png', 0.8, 0, 330)
        if pointer != 0:
            pointer = (pointer[0] + 140, pointer[1] + 20)
            clickGame(screenOpts, pointer, 5)
        if pointer == 0:
            pointer = findImgOnScreen(screenOpts, 'res\\complete.png', 0.8, 0, 330)
            if pointer != 0:
                pointer = (pointer[0] + 140, pointer[1] + 0)
                clickGame(screenOpts, pointer, 5)
                # click building to get menu
                pointer = (int(screenOpts.x_len / 2), int(screenOpts.y_len / 2))
                clickGame(screenOpts, pointer, 2)

        if pointer != 0:
            time.sleep(2)
            pointer = findImgOnScreen(screenOpts, 'res\\trainUnit.png')
            if pointer != 0:
                pointer = (pointer[0] + 20, pointer[1] + 20)
                clickGame(screenOpts, pointer, 2)
                clickGame(screenOpts, clicks.trainButton, 2)
                pointer = findImgOnScreen(screenOpts, 'res\\goTraining.png')
                if pointer != 0:
                    print("not enough resources")
                    clickGame(screenOpts, clicks.back, 1)
                    clickGame(screenOpts, clicks.back, 1)
                    break
            else:
                print("ERROR - trainUnit")
                break
        else:
            clickGame(screenOpts, pointer0, 0.5) #close menu
            break

def mainLoop():
    #clickGame(screenOpts, clicks.windowBar)  # windowFocus
    if isWindowFocus(screenOpts):
        clickGame(screenOpts, clicks.windowBar)  # windowFocus

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
    else:
        playsound('res\\mario.mp3')
    loopDelay(300,-1,'res\\ding.mp3')

def main():
    updateWindow(screenOpts)
    clickGame(screenOpts,clicks.windowBar) #windowFocus

    #for testing single routines:
    #gatherResources()
    #joinBreach()
    #helpFlag()
    #dropship()
    #crashedApp()
    #trainArmy()
    #exit(0)

    while True:
        updateWindow(screenOpts)
        printCoords(screenOpts)
        time.sleep(1)

        mainLoop()



if __name__ == '__main__':
    main()

