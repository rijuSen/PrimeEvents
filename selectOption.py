import time
def selectOption(pageName,pageMenuDict):
    #prompt user to select option
    selection = input('Enter your selection: ')
    if selection in pageMenuDict.keys():
        print('Your selection: {}'.format(pageMenuDict.get(selection)))
        return 0,selection
    else:
        print('Selection {} is not a valid. Kindly provide a valid selection'.format(selection))
        time.sleep(2)
        return 1,''
        

