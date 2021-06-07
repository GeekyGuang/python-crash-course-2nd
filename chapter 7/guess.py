prompt = "Enter a number less than 10"
prompt += "\nEnter 0 to end the game: "

i = 0
while i < 10:
  guess = int(input(prompt))

  if guess == 0:
      break
  elif guess > 10:
    i += 1
    continue
  else:
    print("once again")