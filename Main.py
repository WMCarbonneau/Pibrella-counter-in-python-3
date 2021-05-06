import pibrella
import time
# text to speech import (import required to run may need to install espeak: sudo apt-get install espeak)
import pyttsx3


# text to speech function
def tts(speech):
    engine = pyttsx3.init()
    engine.say(speech)
    engine.runAndWait()


def lights():
    global snumber
    global number
    global rings
    # reset function if button held for 0.2 seconds
    time.sleep(0.2)
    if pibrella.button.read() == 1:
        rings = 0
        number = 0
        snumber = 0
        pibrella.light.red.off()
        pibrella.light.yellow.off()
        pibrella.light.green.off()
        time.sleep(0.15)
    # increment lights
    if number == 1:
        pibrella.light.green.off()
        pibrella.light.red.on()
    elif number == 2:
        pibrella.light.red.off()
        pibrella.light.yellow.on()
    elif number == 3:
        # final light has buzzer function to count
        pibrella.light.yellow.off()
        pibrella.light.green.on()
        rings += 1
        for a in range(rings):
            pibrella.buzzer.fail()
            time.sleep(0.3)
            pibrella.buzzer.off()
            time.sleep(0.05)
        # reset number for lights to continue incrementing from red again
        number = 0

    time.sleep(0.2)


def codeMain():
    global number
    global snumber
    global rings
    # Detect button press to run code
    while True:
        if pibrella.button.read() == 1:
            # increment variables, run text to speech (tts) and lights
            number += 1
            snumber += 1
            tts(snumber)  # even with multiprocessing, tts will run before the rest of the code, so it is not being run with multiprocessing
            lights()


# text to speech counter variable
snumber = 0
# light counter variable
number = 0
# buzzers counter variable
rings = 0

# runs main code (Multiprocessing did not yield more performance so it is now in a function because we didn't change it)
codeMain()
