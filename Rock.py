# A python code for the working of my table lamp
# It has two options, we can turn on the night light or normal light or both at the same time
# Normal light has three levels of brightness, lets call them 1, 2 and 3
# if we click the normal light button fourth time, it gets off.
# Lets get started

print('\nCommand Options...\n')
print('Normal Mode - [L/l]')
print('Night Mode - [N/n]')
print('Turn Off - [O/o]')
print('Quit Program - [Q/q]')
print('Current State - [C\c]')

def setDefault():

    global nightMode, normal, lampState, quitt

    nightMode = 'Off'
    lampState = 'Off'
    quitt = False
    normal = 'Off'

setDefault()

while not quitt:

    get = input('\nEnter a Command - ')

    if nightMode == 'Off' and normal == 'Off': lampState = 'Off'
    else: lampState = 'On'

    if get.lower() != 'q':

        if get.lower() == 'n':

            if nightMode == 'Off': 

                nightMode = "On"
                print('\nNight Light Is On!')

            else: 
                nightMode = 'Off'
                print('\nNight Light Is Now Off!')

        elif get.lower() == 'c':

            print('\nCurrent Working States of Lamp - ')
            print('Lamp is -',lampState)
            print('Normal Light Level -',normal)
            print('Night Mode is -',nightMode)

        elif get.lower() == 'o': setDefault()

        elif get.lower() == 'l':

            if normal == 'Off': normal = 1
            elif normal == 1 or normal < 3: normal += 1
            elif normal == 3: normal = 'Off'

            print('\nNormal Light Level -',normal)

        else: print('\nInvalid Input!')

    else: setDefault(); quitt = True
