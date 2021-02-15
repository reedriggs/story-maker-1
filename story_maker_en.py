import random

#Create people for the story in Python dictionary format, providing category information that match the Person_en class below:
Amaia_Hail = {
    'name':'Amaia',
    'surname':'Hail',
    'pron1':'she',
    'pron2':'her',
    'pron3':'hers',
    'descr':'a sharp-witted human being',
    'surpised': 'Hotchie motchie!'
    }
Mia_Wind = {
    'name':'Mia',
    'surname':'Wind',
    'pron1':'she',
    'pron2':'her',
    'pron3':'hers',
    'descr':'a competitive maker-happener',
    'surpised': 'What is all this?!'
    }
Lyla_Card = {
    'name':'Lyla',
    'surname':'Card',
    'pron1':'she',
    'pron2':'her',
    'pron3':'hers',
    'descr':'a steadfast fixer of things',
    'surpised': 'Show me more.'
    }
Cora_Wool = {
    'name':'Cora',
    'surname':'Wool',
    'pron1':'she',
    'pron2':'her',
    'pron3':'hers',
    'descr':'a caregiver at heart',
    'surpised': 'Yes, okay...'
    }
River_Light = {
    'name':'River',
    'surname':'Light',
    'pron1':'she',
    'pron2':'her',
    'pron3':'hers',
    'descr':'a sharply perceptive person',
    'surpised': 'What now?'
    }
Rhett_Hare = {
    'name':'Rhett',
    'surname':'Hare',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a steadfast fixer of things',
    'surpised': 'Hehhhhhhh.'
    }
Samuel_Journey = {
    'name':'Samuel',
    'surname':'Journey',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a sharp-witted human being',
    'surpised': 'Bring it!'
    }
Lorenzo_Wind = {
    'name':'Lorenzo',
    'surname':'Wind',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a sharply perceptive person',
    'surpised': 'What is happening?'
    }
Bennett_Feel = {
    'name':'Bennett',
    'surname':'Feel',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a caregiver at heart',
    'surpised': 'Hmm.' 
    }
Matias_Pie = {
    'name':'Matias',
    'surname':'Pie',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a competitive maker-happener',
    'surpised': 'Cool, cool, cool.' 
    }

#Family
#child, mother, father, kid, parent, wife, son, baby, brother, husband, daughter, sister, mom, dad, uncle, twin, aunt, grandmother, daddy, cousin, mama, grandfather, ancestor

#Professions, general
#president, director, official, worker, manager, expert, employee, agent, researcher, chief, investigator, boss

#Professions, specific
#teacher, doctor, author, artist, professor, lawyer, editor, coach, writer, attorney, scientist, secretary, judge, reporter, actor, athlete, farmer, pilot, engineer, producer, nurse, journalist

#Group people into story roles here:
people_distr = {
    1: {
    'protag1':Amaia_Hail,
    'protag2':Rhett_Hare,
    'antag1':Lyla_Card
    },
    2: {
    'protag1':Samuel_Journey,
    'protag2':Mia_Wind,
    'antag1':River_Light
    },
    3: {
    'protag1':Mia_Wind,
    'protag2':Bennett_Feel,
    'antag1':Lyla_Card
    },
    4: {
    'protag1':Lorenzo_Wind,
    'protag2':River_Light,
    'antag1':Cora_Wool
    },
    5: {
    'protag1':Cora_Wool,
    'protag2':Matias_Pie,
    'antag1':Lorenzo_Wind
    }
}

#Create animals for the story in Python dictionary format, providing category information that match the Animal_en class below:
#dog, fish, bird, horse, chicken, cat, bear, fox, turkey, wolf, deer, duck, tiger, cow, mouse, eagle, snake, lion, rat, pig

Scoobert = {
    'spec':'dog',
    'name':'Scoobert',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a big happy puppy'
    }
Furbz = {
    'spec':'cat',
    'name':'Furbz',
    'pron1':'she',
    'pron2':'her',
    'pron3':'her',
    'descr':'a snuggly kitty'
    }
Snakey = {
    'spec':'snake',
    'name':'Snakey',
    'pron1':'it',
    'pron2':'it',
    'pron3':'its',
    'descr':'a cute ribbon snake'
    }
Fuzzy = {
    'spec':'rat',
    'name':'Fuzzy',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a gray rat with fuzzy fur'
    }

#Group animals into story roles here:
animals_distr = {
  1:Scoobert,
  2:Furbz,
  3:Snakey,
  4:Fuzzy
}

#Create physical items for the story in Python dictionary format, providing category information that match the Item_en class below:

#Transportation
#car, train, ship, plane, truck, boat, bus, van, bike, jet, helicopter, airplane, automobile, bicycle, cab, metro, taxi, subway, ferry, ambulance, motorcycle

#Materials
#paper, glass, wood, stone, gold, plastic, metal, lead, silver, steel, leather, cotton, fabric, brick, silk, rubber, aluminum, copper, marble, bronze, ink, ceramic

#Meal-related
#cup, dinner, plate, lunch, meal, knife, breakfast, fork, spoon, grill, snack, supper, picnic, napkin, toothpick

#Foods
#fish, ice, salt, egg, sugar, chicken, fruit, pepper, meat, rice, vegetable, cream, apple, milk, cheese, bread, turkey, sauce, potato, bean, butter, tomato, corn, cake, onion, roll, chocolate, salad

Mug = {
    'sing':'mug',
    'plur':'mugs',
    'determiner':'a',
    'description1':'medium sized',
    'descr1_det':'a',
    'description2':'thing filled with memories',
    'descr2_det': 'a'
    }

Kitchen_sink = {
    'sing':'kitchen sink',
    'plur':'kitchen sinks',
    'determiner':'a',
    'description1':'large',
    'descr1_det':'a',
    'description2':'well functioning',
    'descr2_det': 'a'
    }
    
Water = {
    'sing':'water',
    'plur':'water',
    'determiner':'some',
    'description1':'cool, refreshing',
    'descr1_det':'some',
    'description2':'thing filled with memories',
    'descr2_det': 'a'
    }

items_distr = {
  1: Mug,
  2: Kitchen_sink,
  3: Water
}

#Create places here:

#Weather, adjectives
#hot, cold, cool, warm, dry, mild, sunny, damp, icy, chilly, windy, cloudy, humid, foggy, overcast, scorching

#Weather, nouns
#rain, snow, flood, shower, hail, thunder, drizzle, season, sun, heat, wind, ice, sky, storm, temperature, cloud, dust, climate, hurricane, breeze, forecast, lightning, fog, drought, rainbow, sunshine, haze, avalanche, tornado, humidity, pollen, thermometer...Ferenheit...Celcius

places_distr = {
  1: {
    'name':'Atlanta',
    'descr1':'a very green and very sunny place to live',
    'descr2':'a place where childhood memories would remimain, but was not a home to adventure'
    },
  2: {
    'name':'Boise',
    'descr1':'a quiet place',
    'descr2':'a very boring place'
    },
}

#Body
#hand, eye, head, face, back, arm, hair, leg, shoulder, finger, mouth, ear, foot, knee, neck, lip

#Clothing
#suit, shoe, ring, shirt, dress, hat, tie, coat, jacket, boot, belt, pants, glove, uniform, skirt, jeans, sock, sweater

#Colors
#white, black, red, green, blue, brown, yellow, gray, golden, pink, orange, purple

#Emotions, positive:
#happy, glad, confident, pleased, excited, satisfied, hopeful, loving

#Emotions, neutral:
#surprised, shy, cautious, thoughtful, tense, puzzled, energetic, exhausted

#Emotions, negative:
#sorry, afraid, angry, crazy, guilty, nervous, scared, desperate, worried, bitter, uncomfortable, anxious, lonely



#Class categories make story-related words substitutable in the plot template texts, below.
class Person_en:
  def __init__(self, dict):
    self.name = dict['name']
    self.pron1 = dict['pron1']
    self.pron2 = dict['pron2']
    self.pron3 = dict['pron3']
    self.descr = dict['descr']

class Animal_en:
  def __init__(self, dict):
    self.spec = dict['spec']
    self.name = dict['name']
    self.pron1 = dict['pron1']
    self.pron2 = dict['pron2']
    self.pron3 = dict['pron3']
    self.descr = dict['descr']

#Leave alone.
class Place_en:
  def __init__(self, dict):
    self.name = dict['name']
    self.descr1 = dict['descr1']
    self.descr2 = dict['descr2']

#leave alone
class Item_en:
  def __init__(self, dict):
    self.sing = dict['sing']
    self.plur = dict['plur']
    self.det = dict['determiner']
    self.descr1 = dict['description1']
    self.descr1_det = dict['descr1_det']
    self.descr2 = dict['description2']
    self.descr2_det = dict['descr2_det']         

#This helps randomize story elements and plot templates in each story print-out:
def randomize(n):
  random_int = random.randint(1,n)
  return random_int

#These objects pull randomized people from the dictionaries above, plug them into the classes above, and makes them callable by story role
peopR = randomize(len(people_distr))
protag1 = Person_en(people_distr[peopR]['protag1'])
protag2 = Person_en(people_distr[peopR]['protag2'])
antag1 = Person_en(people_distr[peopR]['antag1'])

animR = randomize(len(animals_distr))
pet1 = Animal_en(animals_distr[animR])

itemR = randomize(len(items_distr))
item1 = Item_en(items_distr[itemR])
item2 = Item_en(items_distr[itemR])
appliance1 = Item_en(items_distr[itemR])

placeR = randomize(len(places_distr))
home = Place_en(places_distr[placeR])

#Modify plot template(s) here:
plot1 = f"There, in the middle of the floor was {item1.det} {item1.sing}. It was {item1.descr1_det} {item1.descr1} {item1.sing}, and it was {item1.descr2_det} {item1.descr2}, but no {item2.sing}... but {protag1.name} couldn't look at any {item1.plur} right now. {protag1.pron1.capitalize()} had zero patience for any {item1.plur} at this moment. {protag1.name} lived in {home.name}. {home.name} was {home.descr1}. {home.name} was {home.descr2}. One day {protag1.pron1} had a thought. {protag1.pron1.capitalize()} wanted to go for a swim. At the lake {protag1.name} saw {protag2.name}. {protag2.pron1.capitalize()} looked at {protag1.name}. But then {antag1.name} arrived. {antag1.name} had brought with {antag1.pron2} {pet1.descr} named {pet1.name}. They had all been here before."
plot2 = f'{protag1.name} looked at {protag1.pron3} hands. {protag1.pron1.capitalize()} was holding a part from {appliance1.det} {appliance1.descr1} {appliance1.sing}. "I think I did this before," {protag1.pron1} said to {protag1.pron2}self. {protag1.name} looked around. "I should go," {protag1.pron1} said. '

#Create dictionaries containing plot templates
plots = {
	1:plot1,
	2:plot2
}

#A goal is to be able to simply call plot templates with slot content
plotR = randomize(len(plots))

#"print(story)" feels more elegant, a simple command to end the complicated process
story = plots[plotR]
print(story)
