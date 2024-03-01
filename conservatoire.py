import drivers
import Keypad   #import module Keypad
from time import sleep
from gpiozero.output_devices import LED
buzzer = LED(5)
led_verte = LED(16)
led_rouge = LED(20)

    
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
reponse = "A5796B4683C9214"

def buzztouches():
    buzzer.on()
    sleep(0.1)
    buzzer.off()
    
    
def buzzvictoire():
    for i in range(5):
        buzzer.on()
        led_verte.on()
        sleep(0.1)
        buzzer.off()
        led_verte.off()
        sleep(0.1)
    
    
def buzzdefaite():
    buzzer.on()
    sleep(1.3)
    buzzer.off()
          

    
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
print("Programme PRET")       
def loop():
    saisie = ""
    keypad = Keypad.Keypad(keys,rowsPins,colsPins,ROWS,COLS)    #creat Keypad object
    keypad.setDebounceTime(50)      #set the debounce time
    while(True):
        key = keypad.getKey()       #obtain the state of keys
        if(key != keypad.NULL):     #if there is key pressed, print its key code.
            buzztouches()
            if (key=="D"):
                saisie = saisie[:len(saisie)-1]

            else:    
                saisie += key
            display.lcd_clear()
            long_string(display, "Votre saisie :" , 1)
            long_string(display, "_______________" , 2) 
            long_string(display, "%s"%(saisie) , 2)
            
            if(len(saisie) == len(reponse)):
                display.lcd_clear()
                sleep(0.6)
                if(saisie == reponse):
                    long_string(display, "BRAVO, c'est un" ,1)
                    long_string(display, "sans faute !" ,2)
                    buzzvictoire()
                    sleep(3)
                    display.lcd_clear()
                    long_string(display, "Vous avez acces" ,1)
                    long_string(display, "au coffre !" ,2)
                    sleep(4)
                    display.lcd_clear()
                    long_string(display, "Le code du" ,1)
                    long_string(display, "cadenas est 5273" ,2)
                    sleep(5)
                    display.lcd_clear()
                    long_string(display, "----> 5273 <----" ,2)
                    sleep(5)
                    display.lcd_clear()                                                 
                else:
                    long_string(display, "HELAS... Le code" ,1)
                    long_string(display, "est inexact" ,2)
                    led_rouge.on()
                    buzzdefaite()
                    sleep(3)
                    display.lcd_clear()
                    if(saisie[:5]!=reponse[:5]):
                        long_string(display, "Erreur salle A" ,1)
                        long_string(display, "%s est faux"%(saisie[:5] ,2)
                        sleep(4)
                        display.lcd_clear()
                        
                    if(saisie[6:10]!=reponse[6:10]):
                        long_string(display, "Erreur salle B" ,1)
                        long_string(display, "%s est faux"%(saisie[6:10] ,2)
                        sleep(4)
                        display.lcd_clear()
                                    
                    if(saisie[11:15]!=reponse[11:15]):
                        long_string(display, "Erreur salle C" ,1)
                        long_string(display, "%s est faux"%(saisie[11:15] ,2)
                        sleep(4)
                        display.lcd_clear()            
 
                saisie = ""
                sleep(1.5)
                display.lcd_clear()
                led_rouge.off()
                long_string(display, "Jeu des 3 salles" , 1)
                long_string(display, "Entrez code svp" , 2)
                
# Message d'accueil
long_string(display, "Jeu des 3 salles" , 1)
long_string(display, "Entrez code svp" , 2)

loop()
