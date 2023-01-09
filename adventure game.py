def start_game():
  # Introduction
  print("Welcome to the adventure game!")
  print("You are a brave adventurer exploring an ancient temple.")
  print("As you enter the temple, you see a long hallway stretching out in front of you.")
  print("At the end of the hallway, you see a door with strange markings on it.")
  print("To your left, you see a small room with a torch flickering in the corner.")
  print("What do you do? Type 'go left' to investigate the room or 'go right' to continue down the hallway.")
  
  # Get player's choice
  choice = input(">> ")
  
  # Respond to player's choice
  if choice == "go left":
    print("You cautiously approach the room and peek inside.")
    print("You see a treasure chest in the corner and decide to open it.")
    print("Inside, you find a golden amulet. You pocket the amulet and continue on your journey.")
  elif choice == "go right":
    print("You continue down the hallway towards the door.")
    print("As you get closer, you hear a faint rumbling sound.")
    print("Suddenly, the door bursts open and a giant ogre appears, blocking your way.")
    print("What do you do? Type 'fight' to attack the ogre or 'flee' to run away.")
    
    # Get player's choice
    choice = input(">> ")
    
    # Respond to player's choice
    if choice == "fight":
      print("You bravely draw your sword and engage the ogre in combat.")
      print("After a fierce struggle, you emerge victorious.")
      print("You continue through the door and find a magical artifact that will aid you on your quest.")
    elif choice == "flee":
      print("You turn and run as fast as you can, your heart racing.")
      print("You escape the temple and return home, vowing never to return.")
      print("You live out the rest of your days in safety, but always wonder what could have been.")
  else:
    print("Invalid choice. Please try again.")
    start_game()

# Start the game
start_game()
