alien_0 = {'x_position' : 4, 'y_position' : 0, 'speed' : 'medium'}
print(f"original position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
  x_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
else:
  x_increment = 5

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
noda_position = alien_0.get('points')
print(noda_position)


#Someone I know
def persons():
  person = {'first_name' : 'farida', 'last_name' : 'bashir', 'age' : 25, 'city' : 'osogbo'}
  print(person)
  print(person['first_name'])
  print(person['last_name'])
  print(person['age'])
  print(person['city'])

persons()


#My friend's favourite number
def friends_fav_number():
  favourite_numbers = {'Farida' : 4, 'Aishah' : 3, 'Fatima' : 20, 'Rabi' : 400, 'Lana' : 6}
  for k, v in favourite_numbers.items():
    print(f"\nkey : {k}")
    print(f"Value : {v}\n")

friends_fav_number()


#Glossary
def diction_ary():
  Programming_words = {'print' : 'It is used to display output on the screen', 'if' : 'Used to create a conditional statement', 'return' : 'Used in a function to send back a result', 'list' : 'A data structure used to store a collection of items', 'def' : 'used to define a function'}
  for k, v in Programming_words.items():
    print(f"Programming word: {k.title()}")
    print(f"Meaning: {v.title()}\n")

diction_ary()
