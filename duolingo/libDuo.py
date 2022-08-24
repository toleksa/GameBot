import easyocr
from googletrans import Translator
import numpy as np

class word(object):
    __slots__ = ['loc', 'word', 'lang', 'translation', 'used']
    def __init__(self, loc='', word='', lang='', translation='', used=0):
        self.loc = loc
        self.word = word
        self.lang = lang
        self.translation = translation
        self.used = used
    def __str__(self):  # pragma: nocover
        return self.__unicode__()
    def __unicode__(self):  # pragma: nocover
        return (
            u'(loc={loc}, word={word}, lang={lang}, translation={translation}, '
            u'used={used})'.format(
                loc=self.loc, word=self.word, lang=self.lang,
                translation=self.translation, used=self.used
            )
        )

def quiz():
    #global window,windowNameAndroid
    #windowName = windowNameAndroid
    #window = win32gui.FindWindow(None,windowName)
    #updateWindow()
    clickAbsolute(screenOpts,Clicks.windowBar) #windowFocus
    print("Starting " + sys._getframe(  ).f_code.co_name)
    de = []
    en = []
    #Yoffset=430 #android
    Yoffset=450 #nox
    ptr = findImgOnScreen(screenOpts,'res\\quiz-tapThePairs.png')
    Yoffset = ptr[1] + 30
    print('offset: ' + str(Yoffset))
    #grabGameWindow(Yoffset)
    reader = easyocr.Reader(['de','en'])
    arr=reader.readtext(np.array(grabGameWindow(screenOpts,Yoffset,250,True)), detail = 1)
    for i in range(len(arr)):
        ele=arr[i]
        if(ele[1]=='CONTINUE'):
            continue
        coo=ele[0]
        print(coo[0],ele[1])
        translator = Translator()
        result=translator.translate(ele[1].lower(), dest='en')
        wor=word(coo[0],ele[1],result.src,result.text)
        #print(wor)
        if(result.src=='de'):
            de.append(wor)
        else:
            result=translator.translate(ele[1].lower(), dest='de')
            wor.translation=result.text
            en.append(wor)
        #print(result.text)
        #print(result.src)

    print('matching: ')
    for i in range(len(de)):
        ele=de[i]
        print(ele)
        for j in range(len(en)):
            ele2=en[j]
            if(ele2.word.lower() == ele.translation.lower()):
                print('=> ',ele2)
                clickGame(screenOpts,(ele.loc[0],ele.loc[1]),0.5,Yoffset)
                clickGame(screenOpts,(ele2.loc[0],ele2.loc[1]),0.,Yoffset)
                en[j].used=1
                de[i].used=1
                #en.remove(en[j])
                #de.remove(de[i])
                break
    print('reverse matching: ')
    for i in range(len(en)):
        if(en[i].used==1):
            continue
        print(en[i])
        for j in range(len(de)):
            if(de[j].used==1):
                continue
            if(en[i].translation.lower() == de[j].word.lower()):
                print('=> ',de[j])
                clickGame(screenOpts,en[i].loc,0.5,Yoffset)
                clickGame(screenOpts,de[j].loc,0.5,Yoffset)
                en[i].used=1
                de[j].used=1
                break

    print("=======================================")
    print('de: ')
    for i in range(len(de)):
        ele=de[i]
        print(ele)
    print('en: ')
    for i in range(len(en)):
        ele=en[i]
        print(ele)

    for i in reversed(en):
        if(i.used==1):
            en.remove(i)
    for i in reversed(de):
        if(i.used==1):
            de.remove(i)
    print("=======================================")
    print('de: ')
    for i in range(len(de)):
        ele=de[i]
        print(ele)
    print('en: ')
    for i in range(len(en)):
        ele=en[i]
        print(ele)
    #something is left
    if((len(de)>0) or (len(en)>0)):
        if(len(de)!=len(en)):
            print("error, lists len doesn't match - ultra bruteforce")
            lista=de+en
            for i in range(len(lista)-1):
                done=0
                for j in range(i+1,len(lista)):
                    clickGame(screenOpts,lista[i].loc,0.5,Yoffset)
                    clickGame(screenOpts,lista[j].loc,0.5,Yoffset)
                    #ptr = checkClick('00-continueAndroid.png',0.8,0)
                    ptr = findImgOnScreen(screenOpts,'res\\continue.png',0.8,0)
                    if(ptr!=0):
                        print("quiz - continue")
                        clickAbsolute(screenOpts, ptr)

                        done=1
                        break
                    time.sleep(1)
                if(done==1): break
        else:
            print("Brutforcing")
            for i in range(len(de)):
                done=0
                for j in range(len(en)):
                    clickGame(screenOpts,de[i].loc,0.5,Yoffset)
                    clickGame(screenOpts,en[j].loc,0.5,Yoffset)
                    #ptr = checkClick('00-continueAndroid.png',0.8,0)
                    ptr = findImgOnScreen(screenOpts,'res\\continue.png',0.8,0)
                    if(ptr!=0):
                        print("quiz - continue")
                        clickAbsolute(screenOpts,ptr)
                        done=1
                        break
                    time.sleep(1)
                if(done==1): break
    else:
        print("we're done")