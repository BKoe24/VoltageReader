# VoltageReader
Voltage reader using Arduino UNO

FOR Chem E car:

Make sure you have python downloaded

type python -m venv .venv to create a virtual environment

type ./Scripts/Activate.ps1 to enter the virtual environment (you should see (.venv) next to your path in the terminal

type pip install requirements.txt to install the required packages to run the project

You can change the delay value in the arduino code to change the sampling rate

check which usb port the arduino is plugged into in the bottom right corner of the editor

make sure everything is connected to the proper pins

if it's COM3 you're good, if not go into main.py and change it to the whatever port you have it in

upload the arduino code to the arduino then close the arduino editor

in config.py you can change the amount of samples and the bounds of what is an acceptable voltage

by now you should be able to run the code

to run type: python main.py


