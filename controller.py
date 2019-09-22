import os
import time
#controller class
def displayPage(pageName,pageMenuDict,pageNavDict):
    os.system('clear') 
    #Display Page Name
    print('='*40)
    print('{0:^40}'.format(pageName))
    print('='*40)
    #Menu Options format
    print('Input key to select corresponding option')
    print('='*40)
    print('{0:^10}{1:^30}'.format('[Keys]','Options'))
    print('='*40)
    #display menu
    for key, option in pageMenuDict.items():
        print('{0:>4}{1}{2:<5}{3:^30}'.format('[', key, ']', option))
    print('='*40)
    #navigation panel
    print('='*40)
    if not len(pageNavDict) == 0:
        for key, option in pageNavDict.items():
            print('{0}{1}{2}{3:>2}'.format('[',key,']',option), end = '')
        print()
    print('='*40)


    #selection variable can be used further when rest of the system would be developed
    flag,selection = selectOption(pageMenuDict,pageNavDict)
    if flag == 1:
        displayPage(pageName,pageMenuDict,pageNavDict)
    else:
        return selection


def selectOption(pageMenuDict,pageNavDict):
    #prompt user to select option
    selection = input('Enter your selection: ')
    if selection in pageMenuDict.keys():
        print('Your selection: {}'.format(pageMenuDict.get(selection)))
        return 0,selection
    elif selection in pageNavDict.keys():
        print('Your selection: {}'.format(pageNavDict.get(selection)))
        return 0,selection
    else:
        print('Selection {} is not a valid. Kindly provide a valid selection'.format(selection))
        time.sleep(2)
        return 1,''
        

