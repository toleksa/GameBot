from ..libBot import *
import inspect

# TODO: change class to dictionary
class Clicks:
    windowBar = (200,-20)
    damage = (216, 706)
    speed = (488, 719)
    atkrange = (209, 938)
    meter = (488, 932)
    
    shoppingList = []
    shoppingCounter = 0

def mainLoop():
    screenOpts.debug=1
    #clickGame(screenOpts, clicks.windowBar)  # windowFocus
    if isWindowFocus(screenOpts):
        #clickGame(screenOpts, Clicks.windowBar)  # windowFocus

        #enabled routines:
        #crashedApp()
        pointer = findImgOnScreen(screenOpts, 'theTower\\hogar.png')
        if pointer != 0:
            pointer = (pointer[0] + 30, pointer[1] + 30)
            clickAbsolute(screenOpts, pointer, 0.5)
            
        pointer = findImgOnScreen(screenOpts, 'theTower\\battle.png')
        if pointer != 0:
            pointer = (pointer[0] + 30, pointer[1] + 30)
            clickAbsolute(screenOpts, pointer, 0.5)
            
        #clickGame(screenOpts, Clicks.damage)
        #clickGame(screenOpts, Clicks.speed)
        #clickGame(screenOpts, Clicks.atkrange)
        #clickGame(screenOpts, Clicks.meter)

        clickGame(screenOpts, Clicks.shoppingList[Clicks.shoppingCounter % len(Clicks.shoppingList) - 1])

    #else:
        #playsound('res\\mario.mp3')
    #loopDelay(300,-1,'res\\ding.mp3')

def main():
    updateWindow(screenOpts)
    clickGame(screenOpts,Clicks.windowBar) #windowFocus

    Clicks.shoppingList = [Clicks.damage, Clicks.speed, Clicks.atkrange, Clicks.meter]

    #for testing single routines:
    #gatherResources()
    #joinBreach()
    #helpFlag()
    #dropship()
    #crashedApp()
    #trainArmy()
    #exit(0)
    for i in inspect.getmembers(Clicks):
      
        # to remove private and protected
        # functions
        if not i[0].startswith('_'):
          
            # To remove other methods that
            # doesnot start with a underscore
            if not inspect.ismethod(i[1]): 
                print(i)

    while True:
        updateWindow(screenOpts)
        printCoords(screenOpts)
        time.sleep(1)

        mainLoop()
        Clicks.shoppingCounter+=1



if __name__ == '__main__':
    main()

