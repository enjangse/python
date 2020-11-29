name = ''
while name == '':
    print ('Please input your name')
    name = input()
    if bool('name') == True:
        print ('Hello ' + name)
        print ('Thank you!')
        break
