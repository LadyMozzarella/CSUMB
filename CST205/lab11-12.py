# ------------------------------------------------------------------------------------------------------------
# ----------------------------------------------  Program information    -------------------------------------
# ------------------------------------------------------------------------------------------------------------
# The ultimate adventure game  
# Written by: CSIT group BitSoft

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Function header template   -----------------------------------
# ------------------------------------------------------------------------------------------------------------
# Function: What does it do
# Params: What does it accept
# Returns: What does it return

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Configuration Flags   ----------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Set to True to launch the game after code executes instead of having to type play() after launching
autoStart = False

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Command Line vs JES   ----------------------------------------
# ------------------------------------------------------------------------------------------------------------

#
# ---------------- PrintNow() in case you don't use JES  -----------------------
# Comment this out if you use JES, otherwise leave it in so you don't get errors
# For using with online python ide like http://www.tutorialspoint.com/execute_python_online.php
#
#def printNow(string):
#  print(string)

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Player variables  --------------------------------------------
# ------------------------------------------------------------------------------------------------------------

winner = False
hasSpaceSuit = False
isSlideDoorOpen = False
hasGun = False
lastRoom = 0
alienAlive = True

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Play game  ---------------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Function: Start the game here, run the game loop while room > 0 (you're alive and on the ship)
# Params: (none)
# Returns: (none)
def play():
  global hasSpaceSuit
  global isSlideDoorOpen
  global winner
  global hasGun
  global lastRoom
  global alienAlive
  global isDead
  
  alienAlive = True
  hasSpaceSuit = False
  isSlideDoorOpen = False
  hasGun = False
  exiting = False
  winner = False
  room = 1 # Begin game in room 1 (medical bay)
  lastRoom = 0
  isDead = False
  
  displayHelp() # Welcome message and directions
  while room > 0:
    printNow("")
    if room == 1:
      room = roomOne()
    elif room == 2:
      room = roomTwo() 
    elif room == 3:
      room = roomThree()
    elif room == 4:
      room = roomFour()
    elif room == 5:
      room = roomFive()
    elif room == 6:
      room = roomSix()
  if winner:
    printNow(" Safe in the missile with your space suit, you brace yourself for the engine to fire. It's only")
    printNow(" a matter of time before you are back on earth with your family again. Who knows what your next")
    printNow(" adventure will be...\n *")
  elif isDead == True:
    printNow(" This would be a great time to reflect on the poor decision you've made...except you're dead.")
    printNow(" Try again.")
  elif room == -2: 
    printNow(" You've managed to get yourself stuck on a space station. At least you have time to reflect on")
    printNow(" your decisions.")

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Room functions   ---------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #1 (A.K.A. "Medical Bay").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 1
#   Room name   -> "Medical Bay"
#   Exits       -> East (utility tunnel)               to room 2 ("Space Walk Utility Room")
#               -> South (airlock)                     to room 4 ("Transit Bay")
#               -> [hidden exit] North (sliding panel) to room 6 ("Drug Closet")
def roomOne():
  global isSlideDoorOpen

  if not isAndUpdateLastRoom(1):
    printNow(" -----  Medical Bay  -----")
    printNow(" You are standing in the medical bay. To the south is an airlock. To the east is the utility tunnel.")
    printNow(" To the north is a medical cabinet that looks like it has already been plundered for supplies.\n")

  cmd = getDirection()
  if cmd == "search cabinet":
    printNow(" It looks like the cabinet might be able to slide if you pushed it.\n")
    cmd = getDirection()
  if "cabinet" in cmd and ("slide" in cmd or "push" in cmd): 
    printNow(" You push the cabinet out of the way, opening a door to the north. It will spring shut if you walk")
    printNow(" away, so be careful.")
    isSlideDoorOpen = True
    return 6

  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 1
  elif cmd == "east" or cmd == "e":
    return 2
  elif cmd == "south" or cmd == "s":
    return 4
  elif cmd == "north" or cmd == "n":
    if isSlideDoorOpen:
      printNow(" You sneak into the hidden medical closet.")
      return 6
    else:
      printNow(" You run into the medical cabinet and it shakes a bit, maybe you should search it more closely.")  
  else:
    displayInvalidDirection()
  return 1

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #2 (A.K.A. "Space Walk Utility Room").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 2
#   Room name   -> "Space Walk Utility Room"
#   Exits       -> West (utility tunnel)               to room 1 ("Medical Bay")
#               -> South (airlock)                     to room 3 ("Cafeteria")
#   * User can grab the space suit to win the game here (set hasSpaceSuit to True).
def roomTwo():
  global hasSpaceSuit

  if not isAndUpdateLastRoom(2):
    printNow(" -----  Space Walk Utility Room  -----")
    printNow(" You are standing in the space walk utility room. To the north is the utility tunnel to the medical")
    printNow(" bay. To the south is an airlock.\n")

  if hasSpaceSuit == False: 
    printNow(" There is a space suit here.")
  cmd = getDirection() 
  if "get" in cmd and "suit" in cmd and not hasSpaceSuit: # Looking for something like "get space suit"
     hasSpaceSuit = True
     printNow(" You have picked up the space suit.")
     cmd = getDirection() 
  if cmd == "north" or cmd == "n": 
     return 1
  elif cmd == "south" or cmd == "s":
     return 3
  elif isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 2
  displayInvalidDirection()
  return 2

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #3 (A.K.A. "Cafeteria").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 3
#   Room name   -> "Cafeteria"
#   Exits       -> North (airlock)                     to room 2 ("Space Walk Utility Room")
#               -> West (catwalk)                      to room 4 ("Transit Bay")
def roomThree():
  global hasGun
  global alienAlive # Don't go shooting up the place if the alien is dead
  global isDead

  if not isAndUpdateLastRoom(3):
    printNow(" -----  Cafeteria  -----")
    printNow(" You are standing in the cafeteria. To the west is a catwalk that looks like it could be sketchy. To")
    printNow(" the north is an airlock.\n")

    if alienAlive:
       printNow(" In the corner of the room there is a shadow of what looks like a person. Possibly a survivor?\n")

  cmd = getDirection()
  if "alien" in cmd and "attack" in cmd:
    if not hasGun:
	    printNow(" Attack with what? Uh oh, he's noticed you...")
    cmd = "hello"
  elif alienAlive and "hello" in cmd: # Why would you tell hello at an alien, somebody has to die now...
    if hasGun:
      printNow(" You say hello and the dark figure turns around slowly to reveal a large alien with a hideous insect-like face.")
      printNow(" Before you can take a breath you have shot the gun and fired again and again for what seems like")
      printNow(" minutes, but is actually only a few seconds. The alien falls to the ground and shrivels into a round mass")
      printNow(" of inert exoskeleton.")
      alienAlive = false
      cmd = getDirection()
    else:
      printNow(" You say hello and the dark figure turns around slowly to reveal a large alien with a hideous insect-like ")
      printNow(" face. It looks at you for what feels like an eternity then raises what could be an arm and. Something ")
      printNow(" spear like shoots from it and peirces your abdomen. As you fall to the ground, the alien lands on your back ")
      printNow(" forcing you to the ground. You can feel him begin to eat the flesh from your back as the world goes dark.\n")
      isDead = true
      return -2

  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 3
  if cmd == "north" or cmd == "n":
    return 2
  if cmd == "west" or cmd == "w":
    return 4
  displayInvalidDirection()
  return 3

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #4 (A.K.A. "Transit Bay").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 4
#   Room name   -> "Transit Bay"
#   Exits       -> East (catwalk)  to room 3 ("Cafeteria")
#               -> North (airlock) to room 1 ("Medical Bay")
#               -> West (ladder)   to room 5 ("Missile Room")
def roomFour():
  global hasGun

  if not isAndUpdateLastRoom(4):
    printNow(" -----  Transit Bay  -----")
    printNow(" You are standing in the transit bay. To the east is a catwalk. To the north is an airlock. There")
    printNow(" is a ladder here as well.\n")
    if not hasGun:
      printNow(" On the ground there is a gun that has been abandoned.\n")

  cmd = getDirection()
  if ("take" in cmd or "pick up" in cmd or "get" in cmd) and "gun" in cmd and not hasGun:
    hasGun = True
    printNow(" You have picked up the gun. Better to have this just in case.")
    cmd = getDirection()
  elif isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 4 
  elif cmd == "use ladder" or cmd == "go up" or cmd == "climb ladder":
    if hasSpaceSuit:
      printNow(" It is a bit awkward with the space suit, but you make your way up the ladder.")
    return 5
  elif cmd == "north" or cmd == "n":
    return 1 
  elif cmd == "east" or cmd == "e":
    return 3
  displayInvalidDirection()
  return 4

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #5 (A.K.A. "Missile Room").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 5
#   Room name   -> "Missile Room"
#   Exits       -> South (ladder) to room 4 ("Transit Bay")
def roomFive():
  global hasSpaceSuit
  global winner

  if not isAndUpdateLastRoom(5):
    printNow(" -----  Missile Room  -----")
    printNow(" You are standing in the missile room. There is a big red button here and a ladder leading back")
    printNow(" down to the transit bay.\n")

  cmd = getDirection()
  if "button" in cmd and "press" in cmd:
    if hasSpaceSuit:
      printNow(" You press the red button and hop into the missile.")
      winner = True
      return -1
    else:
      printNow(" Well, you fired the rocket, without being in it... great.")
      return -2
  if "down" in cmd or "ladder" in cmd:
    return 4
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 5
  else:
    displayInvalidDirection()
  return 5

# Function: Allows user to manipulate their direction, collect items, or win the game (if possible) from room
#           #6 (A.K.A. "Medical Closet").
# Params: (none)
# Returns:
#   -1          -> User requested help.
#   0           -> User won the game.
#   integer > 0 -> The next room number to move to.
# Notes: 
#   Room number -> 6
#   Room name   -> "[hidden] Medical Closet"
#   Exits       -> South (sliding panel) to room 1 ("Medical Bay")
def roomSix():
  global isDead
  
  if not isAndUpdateLastRoom(6):
    printNow(" -----  Medical Closet  -----")
    printNow(" You are standing in the medical supply closet. To the south is the medical bay.")
    printNow(" Most of the medicines look like they have been taken. In the corner, you see a large")
    printNow(" slime covered blob rifling through a pile of empty bottles and boxes. The alien seems")
    printNow(" occupied and has not noticed you entering the closet yet.")

  cmd = getDirection()
  if "alien" in cmd or "attack" in cmd:
    printNow(" The alien turns around suddenly. It lunges in your direction, covering you in a mucus-like")
    printNow(" slime from head to toe. The world starts to spin and slowly you notice the tingling feeling")
    printNow(" as the slime begins to burn. The room begins to spin and then goes dark...\n")
    isDead = true
    return -2
  if isQuit(cmd):
    return -1
  elif isHelp(cmd):
    return 6
  elif cmd == "south" or cmd == "s":
    return 1
  displayInvalidDirection()
  return 6

# ------------------------------------------------------------------------------------------------------------
# --------------------------------------------  Helper functions   -------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Function: Compare the current room to the last room and then update the last room to the current room.
# Params:
#   currentRoom -> The room (integer representation) that the user is currently in.
# Returns: True if the user entered the same room they were already in, false otherwise.
def isAndUpdateLastRoom(currentRoom):
  global lastRoom
  isLastRoom = lastRoom == currentRoom
  lastRoom = currentRoom
  return isLastRoom

# Function: Gets instructions from user.
# Params: (none)
# Returns: The user's instructions as raw text.
def getDirection():
  printNow("\n What would you like to do?")
  userDirection = raw_input(" >>> ").lower()
  printNow("")
  return userDirection

# Function: Prints a goodbye message if the user wishes to quit.
# Params:
#   command -> The command the user input.
# Returns: What does it return
#   True -> User wishes to quit.
#   False -> User doesn't with to quit.
def isQuit(command):
  if command == "quit":
    printNow(" Luckily, you hid a cyanide capsule in your pocket. You pull it out and bite down on it. Goodbye.")
    return True
  return False

# Function: Prints helpful instructions if the user requests help.
# Params:
#   command -> The command the user input.
# Returns:
#   True -> User requested help.
#   False -> User did not request help.
def isHelp(command):
  if command == "help":
    displayHelp()
    return True
  return False

# Function: Displays helpful instructions.
# Params: (none)
# Returns: (none)
def displayHelp():
  printNow("\n *----  Welcome to Marooned in Space!  -----*")
  printNow(" |  You're in a large space station. A few hundred people used to live here, but they were attacked")
  printNow(" |  by an unknown threat. Everyone evacuated. You are still here because you were in the medical")
  printNow(" |  unit recovering from an explosion that heppened during routine maintenance. You were")
  printNow(" |  unconscious when the attack happened and missed the action. Explore the ship, stay alive, find")
  printNow(" |  your way back to earth...")
  printNow(" *-----  Directions  -----*")
  printNow(" |  Movement: north (n), south (s), east (e), west (w).")
  printNow(" |  Items: get, press. Ex. \"get space suit\", \"press button\"")
  printNow(" |  Quit: \"quit\"")
  printNow(" |  Help: \"help\"")
  printNow(" *")

# Function: Displays invalid direction notification.
# Params: (none)
# Returns: (none)
def displayInvalidDirection():
  printNow(" Whoops, you can't do that.")

# Start the game automatically if we set the flat at the top of the code  
if autoStart == True:
  play()
