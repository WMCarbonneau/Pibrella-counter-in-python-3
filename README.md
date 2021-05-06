# Pibrella-counter-in-python-3
A simple counter app in python 3 using the Pibrella expansion module for the raspberry pi.

## Simple base 3 counter
It will count up infinitely, or at least until the pi crashes, in multiples of three. 
Every time the button is pressed, it will count up. This is shown by the lights incrementing from red to green. After green, it goes back to red and counts up again.
To keep track of this, every time it hits green it will buzz the amount of times it has hit green starting at 1 and incrementing after that. There is also text to speech that narrates the current number every time the button is pressed.
If you hold the button for at least 0.2 seconds, then the counter will reset, along with the lights, amount of buzzer rings and the text to speech.

### Requirements
python 3

pibrella and pibrella module

pyttsx3 you may need to install espeak
