"""
Brittany Mazza
CST 205 Multimedia Design and Programming

Lab #7 Homemade Thanksgiving
"""

# Warm up
def snowManDesert(imagePath):
  image = makePicture(iamgePath) # /original-images/13.jpg
  width = getWidth(image)-1
  height = getHeight(image)-1
  widthCell = width/20
  heightCell = height/40
  addOvalFilled(image, widthCell*7, heightCell*22, widthCell*6, heightCell*12, white)
  addOvalFilled(image, widthCell*8, heightCell*16, widthCell*4, heightCell*8, white)
  addOvalFilled(image, widthCell*9, heightCell*13, widthCell*2, heightCell*4, white)
  return image
  
# Problem 1 (Group Assignment)
"""
CSUMB CST 205: Multimedia Design and Programming
Lab #7 Homemade Thanksgiving

Team #6 - BITsoft: 
  Ashley Wallace
  John Lester
  Matthew Valancy (Crenshaw)
  Brittany Mazza
  
Notes:
  * All of the functions below rely on the 'mediaPath' variable being set
    correctly. Ensure 'mediaPath' is set to the correct directory 
    ('originals') prior to calling each function. If your environment
    allows you, you can use the 'setMediaPath' function that is loaded
    when this file is loaded. Alternatively, this can be done in the
    console by calling 'setMediaPath' (comment out method calls at bottom
    of file), like:
      # OSX
      mediaPath = setMediaPath("YOUR_PATH_HERE/HomemadeThanksgivingCards/originals/")
      # or Windows
      mediaPath = setMediaPath("YOUR_PATH_HERE\HomemadeThanksgivingCards\originals\")
    This allows us to simply call 
    "makePicture("{image in original folder}")" to get the image we'd like
    to use.
    
Requirements for each card:
  * Contain a message (text).
  * At least three different images.
"""

def generateCard1(): #John L
  bckgrnd = makePicture(getMediaPath("cardFrame.jpg"))
  pic = makePicture(getMediaPath("warmup.jpg"))
  if (getWidth(pic) > getWidth(bckgrnd)):
    pic = shrink(pic, int(getWidth(pic)/getWidth(bckgrnd)))
  else:
    bckgrnd = shrink(bckgrnd, int(getWidth(bckgrnd)/getWidth(pic)))
  pic = chromakey(pic, bckgrnd, 0, 0)
  pic = addThxMessage(pic, "Happy Thanksgiving")
  csumbLogo = makePicture(getMediaPath("csumb-logo-white.png"))
  pic = chromakey(csumbLogo, pic, getWidth(pic)-getHeight(csumbLogo)-10, getHeight(pic)-getHeight(csumbLogo)-10, True, 120)
  return pic

def generateCard2():
  card = getBlankCard()
  applyPumpkinPie(card)
  return card

def generateCard3(): #Matt V
  greenScreen = [50, 255, 50] # R G B values for green screen
  colorPrecision = 100 # how close the colors has to be to remove the alpha
  card = makePicture(getMediaPath("fatTurkey.jpg"))
  santas = makePicture(getMediaPath("santa.jpg"))
  dragon = makePicture(getMediaPath("dinosaur.jpg"))
  flamethrower = makePicture(getMediaPath("flamethrower.jpg"))
  
  textA = "Happy Thanksgiving! No, it's not Christmas yet."
  textB = "-Matt"
  
  pyCopyA(santas, card, 0, 290, greenScreen[0], greenScreen[1], greenScreen[2], 200)    
  pyCopyA(flamethrower, card, 140, 510, greenScreen[0], greenScreen[1], greenScreen[2], 200)    
  pyCopyA(dragon, card, -500, 400, greenScreen[0], greenScreen[1], greenScreen[2], 200)    

  addTextWithStyle(card, 60, 381, textA, makeStyle(serif, bold, 24))
  addTextWithStyle(card, 371, 420, textB, makeStyle(serif, bold, 24))
  
  return card
  
def generateCard4(): # Brittany Mazza
  card = getBlankCard()
  addSunshine(card)
  addGrass(card)
  applyTurkey1(card)
  addQuestionableHappyThanksgivingText(card)
  return card

"""
Methods below are used to generate cards 1, 2, and 4.
"""
def getBlankCard():
  # Create 5x7 card
  return makeEmptyPicture(945, 675)

"""
Methods below are used to generate card 1.
"""
def chromakey(newPic, bckPic, targetX = 0, targetY = 0, overRide = False, tolerance = 60):
  for x in range(0, getWidth(newPic)):
    if x + targetX < getWidth(bckPic):
      for y in range(0, getHeight(newPic)):
        if y + targetY < getHeight(bckPic):
          pix = getPixel(newPic, x, y)
          bPix = getPixel(bckPic, x + targetX, y + targetY)
          color = getColor(pix)
          bColor = getColor(bPix)
          if (distance(color, Color(0, 215, 0)) > tolerance) and ((distance(bColor, Color(0, 215, 0)) < 60) or (distance(bColor, Color(0, 131, 0)) < 60) or (distance(bColor, Color(45, 221, 45)) < 60) or overRide):
            newPix = getPixel(bckPic, x + targetX, y + targetY)
            setColor(bPix, color)
  return bckPic

def shrink(origPic, factor):
  if factor <= 1:
    return origPic
  width = getWidth(origPic)
  height = getHeight(origPic)
  newPic = makeEmptyPicture(int(width / factor), int(height / factor))
  oldX = 0
  for newX in range(0, getWidth(newPic)):
    oldY = 0
    for newY in range(0, getHeight(newPic)):
      oldPix = getPixel(origPic, oldX, oldY)
      newPix = getPixel(newPic, newX, newY)
      setColor(newPix, getColor(oldPix))
      oldY += factor
    oldX += factor
  return newPic

def addThxMessage(pic, text):
  size = 48  #centering only kinda works with 48pt text
  xPos = int((getWidth(pic)/2) - (len(text) * 12.6))
  yPos = size
  style = makeStyle('Palatino Linotype', italic + bold, size)
  addTextWithStyle(pic, xPos+2, yPos+2, text, style, black)
  addTextWithStyle(pic, xPos+1, yPos+1, text, style, gray)
  addTextWithStyle(pic, xPos, yPos, text, style, orange)
  return pic
"""
Methods below are used to generate card 2.
"""
# Apply pumpkin pie to card.
def applyPumpkinPie(card):
  piePic = makePicture("pumpkin-pie.jpg")
  # Apply to bottom right corner of card
  startX = getWidth(card) - getWidth(piePic)
  startY = getHeight(card) - getHeight(piePic)
  for x in range(0, getWidth(piePic)-1):
    for y in range(0, getHeight(piePic)-1):
      piePixel = getPixel(piePic, x, y)
      piePixelColor = getColor(piePixel)
      setColor(getPixel(card, startX + x, startY + y), piePixelColor)

"""
Methods below are used to generate card 3.
"""
# Function: python copy with alpha, copy source image to target image and remove transparent pixels
# Params: source image, target image, target x for 0, target y for 0 
# Returns: Resized picture
def pyCopyA(source, target, targetX, targetY, alphaR, alphaG, alphaB, precision):
  targetWidth = target.getWidth()
  targetHeight = target.getHeight()

  for y in range( 0, source.getHeight() ): # work from top to bottom
    if (y + targetY < targetHeight) and (y + targetY > 0): #Y range check so we can go crazy and not worry
      for x in range( 0, source.getWidth() ):
        if (x + targetX < targetWidth) and (x + targetX > 0): #X range check so we can go crazy and not worry
          sourcePixel = getPixel(source, x, y)
          sourceColor = getColor(sourcePixel)
          if ( abs(sourceColor.getRed() - alphaR) + abs(sourceColor.getBlue() - alphaB) + abs(sourceColor.getGreen() - alphaG) ) > precision: 
            destPixel = getPixel(target, x + targetX, y + targetY)
            destPixel.setColor(sourceColor)

"""
Methods below are used to generate card 4.
"""
# Add "Happy Thanksgiving?" text to card.
def addQuestionableHappyThanksgivingText(card):
  text = "Happy Thanksgiving?"
  textStyle = makeStyle(serif, bold, 13)
  startX = (getWidth(card)/20)*11
  startY = (getHeight(card)/20)*7
  textColor = makeColor(153, 0, 0)
  addTextWithStyle(card, startX, startY, text, textStyle, textColor)

# Apply the turkey holding the sign to a card.
def applyTurkey1(card):
  turkeyPic = makePicture("turkey1.jpg")
  # Apply to center of card.
  startX = (getWidth(card) - getWidth(turkeyPic))/2
  startY = (getHeight(card) - getHeight(turkeyPic))/2
  for x in range(0, getWidth(turkeyPic)-1):
    for y in range(0, getHeight(turkeyPic)-1):
      turkeyPixel = getPixel(turkeyPic, x, y)
      turkeyPixelColor = getColor(turkeyPixel)
      # Don't copy over white pixels to treat turkey background as if it
      # were transparent.
      if distance(turkeyPixelColor, white) > 0.75:
        cardPixel = getPixel(card, startX + x, startY + y)
        setColor(cardPixel, turkeyPixelColor)

# Add sunshine to card.
def addSunshine(card):
  sunshinePic = makePicture("sunshine.jpg")
  # Apply to top of card.
  for x in range(0, getWidth(sunshinePic)):
    for y in range(0, getHeight(sunshinePic)):
      pixel = getPixel(card, x, y)
      sunshineColor = getColor(getPixel(sunshinePic, x, y))
      setColor(pixel, sunshineColor)

# Add grass to card.
def addGrass(card):
  grassPic = makePicture("grass.png")
  # Apply to base of card.
  startY = getHeight(card) - getHeight(grassPic)
  for x in range(0, getWidth(grassPic)):
    for y in range(0, getHeight(grassPic)):
      grassColor = getColor(getPixel(grassPic, x, y))
      # Only color if grass image doesn't look black, which is how 
      # getColor interprets the transparency.
      if distance(grassColor, black) > 0.25:
        setColor(getPixel(card, x, startY + y), grassColor)
