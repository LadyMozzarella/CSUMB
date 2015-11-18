"""
Brittany Mazza
CST 205 Multimedia Design and Programming

Lab #5: Modifying pictures pixel by pixel
"""
# Warm up
def copyToLargerCanvas(image):
  width = getWidth(image)
  height = getHeight(image)
  pic = makeEmptyPicture(width+300, height+300)
  for x in range (0, width-1):
    for y in range (0, height-1):
      color = getColor(getPixel(image, x, y))
      setColor(getPixel(pic, x+150, y+150), color)
  return pic

# Problem 1
def pyCopy(source, target, targetX, targetY):
  height = getHeight(source)
  for x in range (0, getWidth(source)-1):
    tempTargetY = targetY
    for y in range (0, height-1):
      targetPixel = getPixel(target, targetX, tempTargetY)
      color = getColor(getPixel(source, x, y))
      setColor(targetPixel, color)
      tempTargetY += 1
    targetX += 1
  return target
  
# Problem 2
def makeCollage():
  collage =  makeEmptyPicture(1260, 900) # 5x7
  pic1 = makePicture(pickAFile()) # /original-images/01.JPG
  pic2 = makePicture(pickAFile()) # /original-images/02.JPG
  pic3 = makePicture(pickAFile()) # /original-images/03.JPG
  pic4 = makePicture(pickAFile()) # /original-images/04.JPG
  pic5 = makePicture(pickAFile()) # /original-images/05.JPG
  pic6 = makePicture(pickAFile()) # /original-images/06.JPG
  pic7 = makePicture(pickAFile()) # /original-images/07.JPG
  pic8 = makePicture(pickAFile()) # /original-images/08.jpg
  pic9 = makePicture(pickAFile()) # /original-images/09.jpeg
  pic3Rotated = rotatePic(pic3)
  pic6Rotated = rotatePic(pic6)
  pic7Resized = shrink(shrink(pic7))
  pic8Resized = shrink(shrink(shrink(pic8)))
  pyCopy(pic6Rotated, collage, 672, 507)
  pyCopy(roseColoredGlasses(pic5), collage, 886, 0)
  pyCopy(makeNegative(pic9), collage, 0, 0)
  pyCopy(pic2, collage, 50, 204)
  pyCopy(moreRed(pic7Resized, 50), collage, 0, 578)
  pyCopy(quadrupleMirror(pic1), collage, 418, 480)
  pyCopy(noBlue(pic3Rotated), collage, 255, 0)
  pyCopy(betterBnW(pic8Resized), collage, 693, 90)
  pyCopy(leftToRightMirror(pic4), collage, 325, 290)
  return collage
