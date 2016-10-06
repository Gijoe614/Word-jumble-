import random

cars = ["BENTLEY", "WRANGLER", "VOLVO", "CHEVY", "TOYOTA", "DODGE", "INFINITI", "ACURA", "HONDA", "AUDI", "FERRARI", "ASTON MARTIN", "NISSAN", "PORSCHE", "KIA MOTORS", "TESLA", "ROLLS ROYCE", "SAAB", ]



selection = random.choice(cars)
answer = selection
print selection

jumble = list(selection)
print jumble



for current_index in range(len(jumble)):
    random_index = random.randrange(0, len(jumble))
    temp = jumble[current_index]
    jumble[current_index] = jumble[random_index]
    jumble[random_index] = temp

for letter in jumble:
    print letter,


guess = raw_input("\nWhat kind of car brand is jumbled?")
guess = guess.upper()

if guess == answer:
    print ("Got It")
else:
    print (answer)
