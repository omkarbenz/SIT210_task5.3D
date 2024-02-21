from time import sleep   # sleep is using for putting basic delay in our code
from tkinter import *    # tkinter is a library to make and see GUI
window = Tk()            # initialising gui named window
from gpiozero import LED # gpiozero used for initialising of led
import RPi.GPIO          #importing Genral input/output pin
led = LED(16)
Max_length=12
MORSE_CODE_DICT = {         # morse code dictionary
    'A':'.-',
    'B':'-...',
    'C':'-.-.',
    'D':'-..',
    'E':'.',
    'F':'..-.',
    'G':'--.',
    'H':'....',
    'I':'..',
    'J':'.---',
    'K':'-.-',
    'L':'.-..',
    'M':'--',
    'N':'-.',
    'O':'---',
    'P':'.--.',
    'Q':'--.-',
    'R':'.-.',
    'S':'...',
    'T':'-',
    'U':'..-',
    'V':'...-',
    'W':'.--',
    'X':'-..-',
    'Y':'-.--',
    'Z':'--..',
    '1':'.----',
    '2':'..---',
    '3':'...--',
    '4':'....-',
    '5':'.....',
    '6':'-....',
    '7':'--...',
    '8':'---..',
    '9':'----.',
    '0':'-----',
}

def builder():                        # making function that translates alphabates in to morse and join them as word
    print(text1.get())              #it will print the text that should be converted in to morse
    name = (text1.get()).upper()        #it will convert lowercase to uppercase
    if (name <=Max_length && name>0)
    arr = list(name)                #it will store all the characters into array/list
    MyWord = ''
    print(Myword)
    else 
    print("please netre valid number")
    for letter in arr:             #this for-loop will convert letters to morse and join them as word
        if letter != ' ':         # if letter was not space then 
            MyWord = MORSE_CODE_DICT[letter] + ' ' #it will build the morse code
            var = list(MyWord)      
            print(MyWord)         #and print them
            for var1 in var:          # for number or letters in morse code and 
                if(var1 == "-"):    # if sign is '-' then it will blink for 0.3 Second
                    led.on()
                    sleep(0.3)
                    led.off()
                    sleep(0.3)
                elif(var1 == "."):  # if sign is '.' then it will blink for 0.1 Second
                    led.on()
                    sleep(0.1)
                    led.off()
                    sleep(0.1)
                elif(var1 == " "): # if sign is ' ' then it will blink for 0.2 Second
                    led.on()
                    sleep(0.2)
                    led.off()
                    sleep(0.2)
        else:
            MyWord += ' '       
    return MyWord       
def close():
    root.destroy()       

root.geometry("300x175")

Box = Entry(root, width=15, textvariable = name)
Box.grid(row=1, column=1, padx=16, pady=12)
button = Button(root, text="SUBMIT" , bg="orange" , height=1, width=20, command = code)
button.grid(row=2, column=1, padx=12, pady=6)

exitButton = Button(root, text="Exit", bg="red" ,command=root.destroy, height=1, width=15).grid(row=3, column=1)

 

root.mainloop()
