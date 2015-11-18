"""
Brittany Mazza
CST 205 Multimedia Design and Programming

Lab #6: Changing regions of pictures
"""
# Warm up
def eyeCorrection(color, imagePath):
  image = makePicture(imagePath) # /original-images/10.jpg'
  for x in range (0, getWidth(image)-1):
    for y in range (0, getHeight(image)-1):
      currentPixel = getPixel(image, x, y)
      currentColor = getColor(currentPixel)
      if (x > 155 and x < 295) and (y > 160 and y < 215):
        if distance(currentColor, red) < 150:
          setColor(currentPixel, color)
  return image

# Problem 1
def sepiaTone(image):
  image = betterBnW(image)
  for x in range (0, getWidth(image)-1):
    for y in range (0, getHeight(image)-1):
      currentPixel = getPixel(image, x, y)
      currentColor = getColor(currentPixel)
      colorDistance = distance(currentColor, red)
      if colorDistance < 63:
        setRed(currentPixel, getRed(currentPixel) * 1.1)
        setBlue(currentPixel, getBlue(currentPixel) * 0.9)
      elif colorDistance > 191:
        newRed = getRed(currentPixel) * 1.08
        if newRed > 255:
          setRed(currentPixel, 255)
        else:
          setRed(currentPixel, newRed)
        setBlue(currentPixel, getBlue(currentPixel) * 0.93)
      else:
        setRed(currentPixel, getRed(currentPixel) * 1.15)
        setBlue(currentPixel, getBlue(currentPixel) * 0.85)
  return image
  
# Problem 2
def artify(image):
  for x in range (0, getWidth(image)-1):
    for y in range (0, getHeight(image)-1):
      currentPixel = getPixel(image, x, y)
      redColor = getRed(currentPixel)
      greenColor = getGreen(currentPixel)
      blueColor = getBlue(currentPixel)
      if (redColor < 64):
        redColor = 31
      elif (redColor > 63 and redColor < 128):
        redColor = 95
      elif (redColor > 127 and redColor < 192):
        redColor = 159
      elif (redColor > 191 and redColor < 256):
        redColor = 223
      if (greenColor < 64):
        greenColor = 31
      elif (greenColor > 63 and greenColor < 128):
        greenColor = 95
      elif (greenColor > 127 and greenColor < 192):
        redColor = 159
      elif (greenColor > 191 and greenColor < 256):
        greenColor = 223
      if (blueColor < 64):
        blueColor = 31
      elif (blueColor > 63 and blueColor < 128):
        blueColor = 95
      elif (blueColor > 127 and blueColor < 192):
        blueColor = 159
      elif (blueColor > 191 and blueColor < 256):
        blueColor = 223
      setRed(currentPixel, redColor)
      setGreen(currentPixel, greenColor)
      setBlue(currentPixel, blueColor)
  return image

# Problem 3
# image:      /original-images/11.jpg
# background: /original-images/12.jpg
def chromaKey(image, background):
  for x in range (0, getWidth(image)-1):
    for y in range (0, getHeight(image)-1):
      currentPixel = getPixel(image, x, y)
      currentColor = getColor(currentPixel)
      if distance(currentColor, green) < 150.0:
        bgColor = getColor(getPixel(background, x, y))
        setColor(currentPixel, bgColor)
  repaint(image)
  return image