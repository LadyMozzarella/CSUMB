"""
Brittany Mazza
CST 205 Multimedia Design and Programming

Midterm

Topics:
* CSUMB-erize: This filter should transform your source picture to make it
  more CSUMBy. You have a lot of freedom to decide what that means. You
  just need to be able to explain how your filter serves this purpose.
* Selected topic: Buffy the Vampire Slayer.
"""

# Filter #1: CSUMB-erize
def csumberize(image):
  # Get pixel size
  maxX = getWidth(image)
  maxY = getHeight(image)
  # CSUMB school colors
  bayBlue = makeColor(0, 45, 75)
  valleyGreen = makeColor(70, 105, 90)
  goldenSand = makeColor(140, 125, 85)
  # CSUMB logo information
  logo = makePicture("midterm01.png")
  logoStartX = getWidth(image)-getWidth(logo)-20
  logoStartY = getHeight(image)-getHeight(logo)-20
  logoEndX = getWidth(image)-21
  logoEndY = getHeight(image)-21
  
  for x in range(0, maxX):
    for y in range(0, maxY):
      pixel = getPixel(image, x, y)
      applyWhiteWash(pixel)
      applyBorder(pixel, x, y, maxX, maxY, bayBlue, valleyGreen, goldenSand)
      applyLogo(logo, pixel, x, y, logoStartX, logoStartY, logoEndX, logoEndY)
  return image
  
# Helper methods for csumberize filter
def applyWhiteWash(pixel):
  newRed = getRed(pixel) * 1.6
  newBlue = getBlue(pixel) * 1.6
  newGreen =  getGreen(pixel) * 1.6
  if newRed > 255:
    newRed = 255
  if newBlue > 255:
    newBlue = 255
  if newGreen > 255:
    newGreen = 255
  setRed(pixel, newRed)
  setBlue(pixel, newBlue)
  setGreen(pixel, newGreen)
  
def applyBorder(pixel, x, y, maxX, maxY, bayBlue, valleyGreen, goldenSand):
  if isDistanceFromEdge(5, x, y, maxX, maxY):
    setColor(pixel, bayBlue)
  elif isDistanceFromEdge(10, x, y, maxX, maxY):
    setColor(pixel, valleyGreen)
  elif isDistanceFromEdge(15, x, y, maxX, maxY):
    setColor(pixel, goldenSand)
    
def applyLogo(logo, pixel, x, y, logoStartX, logoStartY, logoEndX, logoEndY):
  if isLogoApplicable(x, y, logoStartX, logoStartY, logoEndX, logoEndY):          
    logoPixel = getPixel(logo, x-logoStartX, y-logoStartY)
    logoPixelColor = getColor(logoPixel)
    if distance(black, logoPixelColor) > 50:
      setColor(pixel, logoPixelColor)
      
def isDistanceFromEdge(dist, x, y, maxX, maxY):
  return x < dist or y < dist or x > maxX-dist or y > maxY-dist
  
def isLogoApplicable(x, y, logoStartX, logoStartY, logoEndX, logoEndY):
  isInLogoRangeX = x >= logoStartX and x <= logoEndX
  isInLogoRangeY = y >= logoStartY and y <= logoEndY
  return isInLogoRangeX and isInLogoRangeY

# Filter #2: Buffy-erize
def buffyerize(image):
  width = getWidth(image)
  height = getHeight(image)
  mirrorWidth = width/4-1
  splatter = makePicture("midterm02.png")
  splatterWidth = getWidth(splatter)
  splatterHeight = getHeight(splatter)
  
  for x in range(0, width):
    for y in range(0, height):
      pixel = getPixel(image, x, y)
      # Apply mirror
      applyMirror(image, pixel, x, y, width, mirrorWidth)
      increaseRed(pixel)
      applySplatter(pixel, splatter, x, y, splatterWidth, splatterHeight)
  return image

# Helper methods for buffyerize filter
def applyMirror(image, pixel, x, y, width, mirrorWidth):
  if x < mirrorWidth:
    mirrorPix = getPixel(image, mirrorWidth*2-x, y)
    setColor(pixel, getColor(mirrorPix))
  if x > width-mirrorWidth:
    mirrorPix = getPixel(image, width-(2*mirrorWidth)+(width-x), y)
    setColor(pixel, getColor(mirrorPix))
    
def increaseRed(pixel):
  newRed = getRed(pixel) * 1.25
  if newRed > 255:
    newRed = 255
  setRed(pixel, newRed)
  setBlue(pixel, getBlue(pixel) * 0.75)
  setGreen(pixel, getGreen(pixel) * 0.75)
  
def applySplatter(pixel, splatter, x, y, splatterWidth, splatterHeight):
  if x < splatterWidth and y < splatterHeight:
    splatterPixel = getPixel(splatter, x, y)
    splatterPixelColor = getColor(splatterPixel)
    if distance(black, splatterPixelColor) > 50:
      setColor(pixel, getColor(splatterPixel))



