import drivers
import Keypad   #import module Keypad
from time import sleep


# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = drivers.Lcd()
display.lcd_clear()

ROWS = 4        # number of rows of the Keypad
COLS = 4        #number of columns of the Keypad
keys =  [   '1','2','3','A',    #key code
            '4','5','6','B',
            '7','8','9','C',
            '*','0','#','D'     ]
rowsPins = [18, 23, 24, 25]     #connect to the row pinouts of the keypad
colsPins = [10, 22, 27, 17]     #connect to the column pinouts of the keypad

# Variables
reponse = "A1B2C3D4"


def long_string(display, text='', num_line=1, num_cols=16):
    """ 
    Parameters: (driver, string to print, number of line to print, number of columns of your display)
    Return: This function send to display your scrolling string.
    """
    if len(text) > num_cols:
        display.lcd_display_string(text[:num_cols], num_line)
        sleep(1)
        for i in range(len(text) - num_cols + 1):
            text_to_print = text[i:i+num_cols]
            display.lcd_display_string(text_to_print, num_line)
            sleep(0.2)
        sleep(1)
    else:
        display.lcd_display_string(text, num_line)
        
def loop():
    saisie = ""
    keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)    #creat Keypad object
    keypad.setDebounceTime(50)      #set the debounce time
    while(True):
        key = keypad.getKey()       #obtain the state of keys
        if(key != keypad.NULL):     #if there is key pressed, print its key code.
            saisie += key
            display.lcd_clear()
            long_string(display, "Votre saisie :" , 1)
            long_string(display, "________" , 2) 
            long_string(display, "%s"%(saisie) , 2)
            
            if(len(saisie) == len(reponse)):
                display.lcd_clear()
                sleep(0.2)
                if(saisie == reponse):
                    long_string(display, "Bravo !" ,1)
                    long_string(display, "C'est un sans faute !" ,2)
                    
                else:
                    long_string(display, "Helas !" ,1)
                    long_string(display, "Code errone !" ,2)
                saisie = ""
                sleep(2)
                display.lcd_clear()
                long_string(display, "Jeu des patios" , 1)
                long_string(display, "Saisissez code" , 2)
                
# Message d'accueil
long_string(display, "Jeu des patios" , 1)
long_string(display, "Saisissez code" , 2)

loop()