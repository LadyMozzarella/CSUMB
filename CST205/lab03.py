"""
Brittany Mazza
CST 205 Multimedia Design and Programming

Lab #3: Manipulating Images with Python
"""
def halfRed(image):
  lessRed(image, 50)
  
def noBlue(image):
  pixels = getPixels(image)
  for pixel in pixels:
    setBlue(pixel, 0)
  return image
    
def lessRed(image, amount):
  decPercent = 1 - amount * 0.01
  pixels = getPixels(image)
  for pixel in pixels:
    setRed(pixel, getRed(pixel) * decPercent)
  return image
    
def moreRed(image, amount):
  incPercent = 1 + amount * 0.01
  pixels = getPixels(image)
  for pixel in pixels:
    redAmount = getRed(pixel)
    # Set red amount at max red value if it is over the highest value possible
    if redAmount > 255:
      redAmount = 255
    setRed(pixel, redAmount * incPercent)
  return image
    
def roseColoredGlasses(image):
  pixels = getPixels(image)
  for pixel in pixels:
    setRed(pixel, getRed(pixel) * 1.25)
    setBlue(pixel, getBlue(pixel) * 0.75)
    setGreen(pixel, getGreen(pixel) * 0.75)
  return image
  
def lightenUp(image):
  pixels = getPixels(image)
  for pixel in pixels:
    newColor = makeLighter(getColor(pixel))
    setColor(pixel, newColor)
  return image
  
def makeNegative(originalImage):
  pixels = getPixels(originalImage)
  for pixel in pixels:
    setRed(pixel, 255 - getRed(pixel))
    setBlue(pixel, 255 - getBlue(pixel))
    setGreen(pixel, 255 - getGreen(pixel))
  return originalImage
  
def BnW(image):
  pixels = getPixels(image)
  for pixel in pixels:
    colorVal = (getRed(pixel) + getBlue(pixel) + getGreen(pixel)) / 3
    setRed(pixel, colorVal)
    setBlue(pixel, colorVal)
    setGreen(pixel, colorVal)
  return image
  
def betterBnW(image):
  pixels = getPixels(image)
  for pixel in pixels:
    colorVal = getRed(pixel) * 0.299
    colorVal = colorVal + getBlue(pixel) * 0.114
    colorVal = colorVal + getGreen(pixel) * 0.587
    setRed(pixel, colorVal)
    setBlue(pixel, colorVal)
    setGreen(pixel, colorVal)
  return image
