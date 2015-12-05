"""
Lab #8: Getting started with sound
Pair Partners: Ashley Wallace & Brittany Mazza (Team #6)
"""

def decreaseVolume(sound):
    for sample in range(0, getLength(sound)):
        value = getSampleValueAt(sound, sample)
        setSampleValueAt(sound, sample, value/2)
    return sound
        
def changeVolume(sound, factor):
    for sample in range(0, getLength(sound)):
        value = getSampleValueAt(sound, sample)
        setSampleValueAt(sound, sample, value * factor)
    return sound

def maxSample(sound):
    maxVal = 0
    for sample in range(0, getLength(sound)):
        value = getSampleValueAt(sound, sample)
        maxVal = max(maxVal, value)
    return maxVal

def maxVolume(sound):
    factor = 32767 / float(maxSample(sound))
    for sample in range(0, getLength(sound)):
        value = getSampleValueAt(sound, sample)
        setSampleValueAt(sound, sample, value * factor)
    return sound

def goToEleven(sound):
    for sample in range(0, getLength(sound)):
        if getSampleValueAt(sound, sample) > 0:
            setSampleValueAt(sound, sample, 32767)
        elif getSampleValueAt(sound, sample) < 0:
            setSampleValueAt(sound, sample, -32768)
    return sound

# Helper functions
def getSound():
    filename = pickAFile()
    sound = makeSound(filename)
    print filename
    return sound