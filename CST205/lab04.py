"""
Brittany Mazza
CST 205 Multimedia Design and Programming

Lab #4: Modifying pictures pixel by pixel
"""
# Warm up
def halfBetter():
  image = makePicture(pickAFile())
  for x in range((getWidth(image)/2), getWidth(image)):
    for y in range(0, getHeight(image)):
      pixel = getPixel(image, x, y)
      setGreen(pixel, getGreen(pixel) * 0.5)
  return image

# Problem 1
def leftToRightMirror(image):
  totalX = getWidth(image) - 1
  totalY = getHeight(image) - 1
  for x in range(0, (totalX/2)):
    for y in range(0, totalY):
      currentPixel = getPixel(image, x, y)
      rightPixel = getPixel(image, totalX - x, y)
      color = getColor(currentPixel)
      setColor(rightPixel, color)
  return image
  
def topToBottomMirror(image):
  totalX = getWidth(image) - 1
  totalY = getHeight(image) - 1
  for x in range(0, totalX):
    for y in range(0, (totalY/2)):
      currentPixel = getPixel(image, x, y)
      bottomPixel = getPixel(image, x, totalY - y)
      color = getColor(currentPixel)
      setColor(bottomPixel, color)
  return image
  
def bottomToTopMirror(image):
  totalX = getWidth(image) - 1
  totalY = getHeight(image) - 1
  for x in range(0, totalX):
    for y in range(totalY/2, totalY):
      currentPixel = getPixel(image, x, y)
      topPixel = getPixel(image, x, totalY - y)
      color = getColor(currentPixel)
      setColor(topPixel, color)
  return image

def quadrupleMirror(image):
  totalX = getWidth(image) - 1
  totalY = getHeight(image) - 1
  for x in range(0, (totalX/2)):
    for y in range(0, (totalY/2)):
      currentPixel = getPixel(image, x, y)
      rightPixel = getPixel(image, totalX - x, y)
      bottomPixel = getPixel(image, x, totalY - y)
      diagonalPixel = getPixel(image, totalX - x, totalY - y)
      color = getColor(currentPixel)
      setColor(rightPixel, color)
      setColor(bottomPixel, color)
      setColor(diagonalPixel, color)
  return image

# Problem 2
def simpleCopy(image):
  width = getWidth(image)
  height = getHeight(image)
  pic = makeEmptyPicture(width, height)
  for x in range (0, width):
    for y in range (0, height):
      color = getColor(getPixel(image, x, y))
      setColor(getPixel(pic, x, y), color)
  return pic

# Problem 3
def rotatePic(image):
  width = getWidth(image)
  height = getHeight(image)
  pic = makeEmptyPicture(height, width)
  for x in range (0, width):
    for y in range (0, height):
      color = getColor(getPixel(image, x, y))
      setColor(getPixel(pic, y, x), color)
  return pic
  
# Problem 4
def shrink(image):
  width = getWidth(image)
  height = getHeight(image)
  pic = makeEmptyPicture(width/2, height/2)
  for x in range (0, width-1, 2):
    for y in range (0, height-1, 2):
      color = getColor(getPixel(image, x, y))
      setColor(getPixel(pic, x/2, y/2), color)
  return pic