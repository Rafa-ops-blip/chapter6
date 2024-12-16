#Glossary 2
def diction_ary():
  Programming_words = {'print' : 'It is used to display output on the screen', 'if' : 'Used to create a conditional statement', 'return' : 'Used in a function to send back a result', 'list' : 'A data structure used to store a collection of items', 'def' : 'used to define a function'}
  for key in Programming_words.keys():
    print(key)
  print("The following words above are python keywords")
  Programming_words['for'] = 'Used to create a loop that iterates over a sequence'
  Programming_words['pop'] = 'used to remove an item from a data structure'
  Programming_words['del'] = 'used to delete an item from a program'
  Programming_words['sort'] = 'used to arrange items in alphabetical order'
  
  for key in Programming_words.keys():
    print(key)
  print(Programming_words)

diction_ary()


#Types of river
def rivers():
  rivers_country = {'nile' : 'egypt', 'amazon' : 'brazil', 'yangtze' : 'china', 'mississippi' : 'USA', 'ganges' : 'india'}
  for k, v in rivers_country.items():
    print(f"I love to visit {v}")
    print(f"The {k.title()} river runs in {v.title()}\n")

  for k in rivers_country.keys():
    print(f"{k.title()} is a river.")
    print("I'd love to see it\n")

  for v in rivers_country.values():
    if 'USA' in v:
      print(f"{v.upper()} is such a beautiful country\n")
    else:
      print(f"{v.title()} is such a beautiful country\n")

rivers()


def fav_lang_poll():
  favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'rust',
  'phil': 'python',
  }
  names = ['fari', 'sally', 'hali', 'jen', 'edward']
  for name in names:
    if name in favorite_languages.keys():
      print(f"Hello {name}! Thank you for responding\n")
    else:
      print(f"Hello {name}! You're invited to take this poll\n")

fav_lang_poll()
    
    

