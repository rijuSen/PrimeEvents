from selectOption import selectOption
import os
def displayPage(pageName,pageMenuDict):
    os.system('clear') 
    print('='*40)
    print('{0:^40}'.format(pageName))
    print('='*40)
    print('Input key to select corresponding option')
    print('='*40)
    print('{0:<30}{1:<15}'.format('Options','Keys'))
    print('='*40)
    #display menu
    for key, option in pageMenuDict.items():
        print('{0:<30}{1:<15}'.format(option,key))
    print('='*40)
    #selection variable can be used further when rest of the system would be developed
    flag,selection = selectOption(pageName,pageMenuDict)
    if flag == 1:
        displayPage(pageName,pageMenuDict)
