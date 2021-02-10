
#Create story people here:
protag1 = {
    'name':'Jim',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a simple sort of man'
    }

protag2 = {
    'name':'Jen',
    'pron1':'she',
    'pron2':'her',
    'pron3':'her',
    'descr':'a sharply perceptive woman'
    }

antag1 = {
    'name':'Reginald',
    'pron1':'they',
    'pron2':'them',
    'pron3':'their',
    'descr':'a mean, untrusting type of person'
    }

#This is back end stuff to leave alone.
class Person_en:
  def __init__(self, dict):
    self.name = dict['name']
    self.pron1 = dict['pron1']
    self.pron2 = dict['pron2']
    self.pron3 = dict['pron3']
    self.descr = dict['descr']

protag1 = Person_en(protag1)
protag2 = Person_en(protag2)
antag1 = Person_en(antag1)

#Create animals here:
animal1 = {
    'spec':'dog',
    'name':'Scoobert',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a big happy puppy'
    }

#Leave alone.
class Animal_en:
  def __init__(self, dict):
    self.spec = dict['spec']
    self.name = dict['name']
    self.pron1 = dict['pron1']
    self.pron2 = dict['pron2']
    self.pron3 = dict['pron3']
    self.descr = dict['descr']

pet1 = Animal_en(animal1)

#Create places here:
place1_features = {
    'name':'Atlanta',
    'descr1':'a very green and very sunny place to live',
    'descr2':'a place where childhood memories would remimain, but was not a home to adventure'
    }

#Leave alone.
class Place_en:
  def __init__(self, dict):
    self.name = dict['name']
    self.descr1 = dict['descr1']
    self.descr2 = dict['descr2']

home = Place_en(place1_features)

#Create physical items for the story:
count_item1 = {
	'sing':'mug',
	'plur':'mugs',
	'determiner':'a',
	'description1':'medium sized',
	'descr1_det':'a',
	'description2':'thing filled with memories',
	'descr2_det': 'a',
	}

mass_item1 = {
    'sing':'water',
    'plur':'water',
    'determiner':'some',
    'description1':'cool, refreshing',
    'descr1_det':'some',
    'description2':'thing filled with memories',
    'descr2_det': 'a',
    }

#leave alone
class Item:
  def __init__(self, dict):
    self.sing = dict['sing']
    self.plur = dict['plur']
    self.det = dict['determiner']
    self.descr1 = dict['description1']
    self.descr1_det = dict['descr1_det']
    self.descr2 = dict['description2']
    self.descr2_det = dict['descr2_det']         
    
item1 = Item(count_item1)
item2 = Item(mass_item1)

#Modify plot template(s) here:
print(f"There, in the middle of the floor was {item1.det} {item1.sing}. It was {item1.descr1_det} {item1.descr1} {item1.sing}, and it was {item1.descr2_det} {item1.descr2}, but no {item2.sing}.")
print(f"... but {protag1.name} couldn't look at any {item1.plur} right now. {protag1.pron1.capitalize()} had zero patience for any {item1.plur} at this moment. {protag1.name} lived in {home.name}. {home.name} was {home.descr1}. {home.name} was {home.descr2}. One day {protag1.pron1} had a thought. {protag1.pron1.capitalize()} wanted to go for a swim. At the lake {protag1.name} saw {protag2.name}. {protag2.pron1.capitalize()} looked at {protag1.name}. But then {antag1.name} arrived. {antag1.name} had brought with {antag1.pron2} {pet1.descr} named {pet1.name}.")
