"""
    Brittany Mazza
    CST 205 Multimedia Design and Programming
    
    Lab #9: Introduction to Sampling
    """
# Problem 1: 
def clip(source, start, end):
  samplingRate = getSamplingRate(source)
  soundClip = makeEmptySound(end + 1 - start, int(samplingRate))
  scale = getScale(source, soundClip)
  targetIndex = 0;
  for index in range(start, end + 1): # Should we be doing the end+1s?
    value = getSampleValueAt(source, index)
    setSampleValueAt(soundClip, targetIndex, value * scale)
    targetIndex = targetIndex + 1
  return soundClip

# Problem 2:
def copy(source, target, start):
  srcLen = getLength(source)
  targetLen = getLength(target)
  for index in range(0, srcLen):
    if start + index < targetLen:
      value = getSampleValueAt(source, index)
      setSampleValueAt(target, int(start + index), value)
  return target

"""
Use your clip and copy functions to create a sound collage that
combines at least five clips from other sounds into a new, 
never-before-heard sound :)

One thing you might end up wanting to do here is to insert some
silence in between different clips (no, silence doesn't count
as any of your five required sounds).  To include silence, you
just want to add some samples with the value 0 (0 is silence).
How many samples?

Call getSamplingRate(sound) on your sound. This will return the
number of samples in a second. You probably don't want a whole
second of slience since that is a pretty long time, so multiply
by something less than 1. 
For example: int(0.1 * getSamplingRate(sound)) will return the
number of samples you need for a tenth of a second of slience.  
Don't forget to add the length of the silence you add to the
overall length of your target sound
"""
# Problem 3;
def soundCollage():
  dontReversed = reverse(makeSound("khdont.wav"))
  brain = clip(makeSound("llbrain.wav"), 2392, 19642)
  memory = clip(makeSound("memory.wav"), 15900, 32700)
  glasses = clip(makeSound("glasses.wav"), 0, 16848)
  befriend = clip(makeSound("befriend.wav"), 48312, 62865)
  silenceLength = getSamplingRate(dontReversed) * 0.5
  totalLength = getLength(dontReversed) + getLength(brain) + getLength(memory)
  totalLength += getLength(glasses) + getLength(befriend) + (silenceLength*4)
  collage = makeEmptySound(int(totalLength), int(getSamplingRate(brain)))
  copy(dontReversed, collage, 0)
  copy(memory, collage, getLength(dontReversed) + silenceLength)
  copy(brain, collage, getLength(dontReversed) + getLength(memory) + (2*silenceLength))
  copy(glasses, collage, getLength(dontReversed) + getLength(brain) + getLength(memory) + (3*silenceLength))
  copy(befriend, collage, getLength(dontReversed) + getLength(brain) + getLength(memory) + getLength(glasses) + (4*silenceLength))
  return collage

# Problem 4:
def reverse(sound):
  samplingRate = getSamplingRate(sound)
  reversedSound = makeEmptySound(getLength(sound), int(samplingRate))
  """
  bitDepth = sound.lengthInBytes / sound.length
  targetBitDepth = targetSound / targetSound
  """
  scale = getScale(sound, reversedSound)
  targetIndex = getLength(sound)-1
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValueAt(reversedSound, targetIndex, value * scale)
    targetIndex = targetIndex - 1
  return reversedSound
  
# Helper function sincwe can't control the bit depth when we make a newe 
# sound
def getScale(sound, targetSound):
  bitDepth = sound.lengthInBytes / sound.length
  targetBitDepth = targetSound.lengthInBytes / targetSound.length
  return 2**(8*(targetBitDepth - bitDepth))
  
