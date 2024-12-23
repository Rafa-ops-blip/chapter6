#Dictionary of different people
def personality():
  person_0 = {'first_name' : 'farida', 'last_name' : 'bashir', 'age' : 25, 'city' : 'osogbo'}
  person_1 = {'first_name' : 'aliya', 'last_name' : 'aliyu', 'age' : 22, 'city' : 'kwara'}
  person_2 = {'first_name' : 'carly', 'last_name' : 'sanni', 'age' : 19, 'city' : 'ibadan'}
  people = [person_0, person_1, person_2]
  for person in people:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}" )
    print(f"City: {person['city']}\n")


personality()

#Pets
def pet_owner():
  pet_1 = {'type' : 'tabby cat', 'owner' : 'john'}
  pet_2 = {'type' : 'british short hair', 'owner' : 'charlie'}
  pet_3 = {'type' : 'bull dog', 'owner' : 'amanda'}
  pet_4 = {'type' : 'birman cat', 'owner' : 'johnny'}
  pet_5 = {'type' : 'chihuahua', 'owner' : 'trevor'}

  pets = [pet_1, pet_2, pet_3, pet_4, pet_5]
  for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['type'].title()} pet and I'm scared of visiting their home\n")


pet_owner()

#Favourite Place
def fav_places():
  favorite_places = {
    'fari' : ['saudi', 'maldives', 'cuba'],
    'salma' : ['dubai', 'zanzibar', 'united kingdom'], 
    'rafa' : ['qatar', 'maldives', 'lagos']
    }
  for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are: ")
    for place in places:
      print(f"{place.title()}")

    print()


fav_places()


#Favorite number
def friends_fav_number():
  favourite_numbers = {
    'Farida' : [4, 5, 10],
    'Aishah' : [3, 50, 300], 
    'Fatima' : [20, 400,200], 
    'Rabi' : [404, 419, 440],
    'Lana' : [60, 44, 3]
    }
  for k, v in favourite_numbers.items():
    print(f"\nName : {k}")
    print(f"Favorite number : {v}\n")

friends_fav_number()


#Cities
def great_cities():
  cities = {
    'kyoto' : {
      'country' : 'japan', 
      'population' : '1.45 million', 
      'fact' : 'It is known as a city of ten thousand shrines.'
      },
    'cape town' : {
      'country' : 'south africa', 
      'population' : '4.8 million', 
      'fact' : 'It is home to table mountain, one of the new seven wonders of nature.'
      },
    'barcelona' : {
      'country' : 'spain', 
      'population' : '1.6 million', 
      'fact' : 'it is famous for its unique arcitecture.'
      }
  	}
  for city, info in cities.items():
    print(f"{city.title()}:")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print()
		
     

great_cities()



