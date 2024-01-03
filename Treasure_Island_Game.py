print("Welcome to the Treasure Island.\nYour mission is to find the treasure")

lr_choice = input("Where would you go left or right? l or r")
sw_choice = input("Do you wanna swim or wait here? s or w")
door_choice = input(
    "Which door would you like to open? Red, Blue or Yellow? r, b, y")

if lr_choice == 'l':
  if sw_choice == 'w':
    if door_choice == 'r':
      print("Burned by fire.\n Game Over.")
    elif door_choice == 'b':
      print("Eaten by beasts.\nGame Over.")
    elif door_choice == 'y':
      print("Game Over")
    else:
      print("Yayyyy. You Win!")
  elif sw_choice == 's':
    print("Attacked by trout.\nGame Over")
  else:
    print("Game Over")
elif lr_choice == 'r':
  print("Fall into a hole.\nGame Over")
else:
  print("Game Over")
