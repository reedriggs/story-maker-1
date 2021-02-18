import random

#Create people for the story in Python dictionary format, providing category information that match the Person_en class below:
Amaia_Hail = {
    'name':'Amaia',
    'surname':'Hail',
    'pron1':'she',
    'pron2':'her',
    'pron3':'hers',
    'descr':'a sharp-witted human being',
    'surprised': 'Hotchie motchie!',
    'mother':'author',
    'father':'teacher'
    }
Mia_Wind = {
    'name':'Mia',
    'surname':'Wind',
    'pron1':'she',
    'pron2':'her',
    'pron3':'hers',
    'descr':'a competitive maker-happener',
    'surprised': 'What is all this?!',
    'mother':'professor',
    'father':'lawyer'
    }
Lyla_Card = {
    'name':'Lyla',
    'surname':'Card',
    'pron1':'she',
    'pron2':'her',
    'pron3':'hers',
    'descr':'a steadfast fixer of things',
    'surprised': 'Show me more.',
    'mother':'judge',
    'father':'editor'
    }
Cora_Wool = {
    'name':'Cora',
    'surname':'Wool',
    'pron1':'she',
    'pron2':'her',
    'pron3':'hers',
    'descr':'a caregiver at heart',
    'surprised': 'Yes, okay...',
    'mother':'farmer',
    'father':'doctor'
    }
River_Light = {
    'name':'River',
    'surname':'Light',
    'pron1':'she',
    'pron2':'her',
    'pron3':'hers',
    'descr':'a sharply perceptive person',
    'surprised': 'What now?',
    'mother':'pilot',
    'father':'nurse'
    }
Rhett_Hare = {
    'name':'Rhett',
    'surname':'Hare',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a steadfast fixer of things',
    'surprised': 'Hehhhhhhh.',
    'mother':'author',
    'father':'coach'
    }
Samuel_Journey = {
    'name':'Samuel',
    'surname':'Journey',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a sharp-witted human being',
    'surprised': 'Bring it!',
    'mother':'scientist',
    'father':'reporter'
    }
Lorenzo_Wind = {
    'name':'Lorenzo',
    'surname':'Wind',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a sharply perceptive person',
    'surprised': 'What is happening?',
    'mother':'professor',
    'father':'secretary'
    }
Bennett_Feel = {
    'name':'Bennett',
    'surname':'Feel',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a caregiver at heart',
    'surprised': 'Hmm.',
    'mother':'actor',
    'father':'musician'
    }
Matias_Pie = {
    'name':'Matias',
    'surname':'Pie',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a competitive maker-happener',
    'surprised': 'Cool, cool, cool.',
    'mother':'engineer',
    'father':'attorney'
    }

#Family
#child, mother, father, kid, parent, wife, son, baby, brother, husband, daughter, sister, mom, dad, uncle, twin, aunt, grandmother, daddy, cousin, mama, grandfather, ancestor

#Professions, general
#president, director, official, worker, manager, expert, employee, agent, researcher, chief, investigator, boss

#Professions, specific
#teacher, doctor, author, artist, professor, lawyer, editor, coach, writer, attorney, scientist, secretary, judge, reporter, actor, athlete, farmer, pilot, engineer, producer, nurse, journalist

#Group people into story roles here:
#Story roles: protagonist_1, protagonist_2, ally_1, ally_2, ally_3, opponent_1, opponent_2, fake_ally_opp_1, fake_ally_opp_2, fake_opp_ally_1, fake_opp_ally_2

people_distr = {
    1: {
    'protag1':Amaia_Hail,
    'protag2':Rhett_Hare,
    'ally1':Mia_Wind,
    'ally2':Samuel_Journey,
    'ally3':Lyla_Card,
    'antag1':Lorenzo_Wind,
    'antag2':Cora_Wool,
    'fake_ally_opp_1':Bennett_Feel,
    'fake_ally_opp_2':River_Light,
    'fake_opp_ally_1':Matias_Pie
    },
    2: {
    'protag1':Matias_Pie,
    'protag2':Amaia_Hail,
    'ally1':Rhett_Hare,
    'ally2':Mia_Wind,
    'ally3':Samuel_Journey,
    'antag1':Lyla_Card,
    'antag2':Lorenzo_Wind,
    'fake_ally_opp_1':Cora_Wool,
    'fake_ally_opp_2':Bennett_Feel,
    'fake_opp_ally_1':River_Light
    },
    3: {
    'protag1':River_Light,
    'protag2':Matias_Pie,
    'ally1':Amaia_Hail,
    'ally2':Rhett_Hare,
    'ally3':Mia_Wind,
    'antag1':Samuel_Journey,
    'antag2':Lyla_Card,
    'fake_ally_opp_1':Lorenzo_Wind,
    'fake_ally_opp_2':Cora_Wool,
    'fake_opp_ally_1':Bennett_Feel
    }
}

#Create animals for the story in Python dictionary format, providing category information that match the Animal_en class below:
#dog, fish, bird, horse, chicken, cat, bear, fox, turkey, wolf, deer, duck, tiger, cow, mouse, eagle, snake, lion, rat, pig

dog = {
    'spec':'dog',
    'name':'Scoobert',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a big happy puppy'
    }
cat = {
    'spec':'cat',
    'name':'Furbz',
    'pron1':'she',
    'pron2':'her',
    'pron3':'hers',
    'descr':'a snuggly kitty'
    }
snake = {
    'spec':'snake',
    'name':'Snakey',
    'pron1':'it',
    'pron2':'it',
    'pron3':'its',
    'descr':'a cute ribbon snake'
    }
rat = {
    'spec':'rat',
    'name':'Fuzzy',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a gray rat with fuzzy fur'
    }
fish = {
    'spec':'fish',
    'name':'Angel',
    'pron1':'she',
    'pron2':'her',
    'pron3':'hers',
    'descr':'an angel fish that likes to nibble'
    }
bird = {
    'spec':'bird',
    'name':'Rider',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':"a songbird with his father's songs"
    }
horse = {
    'spec':'horse',
    'name':'Lindy',
    'pron1':'he',
    'pron2':'him',
    'pron3':'his',
    'descr':'a very lucky horse'
    }
chicken = {
    'spec':'chicken',
    'name':'Henny-Lou',
    'pron1':'she',
    'pron2':'her',
    'pron3':'hers',
    'descr':'an attention-seeking chicken'
    }

#Group animals into story roles here:
animals_distr = {
  1:dog,
  2:cat,
  3:snake,
  4:rat,
  5:fish,
  6:bird,
  7:horse,
  8:chicken
}

#Create physical items for the story in Python dictionary format, providing category information that match the Item_en class below:

#Transportation
#car, train, ship, plane, truck, boat, bus, van, bike, jet, helicopter, airplane, automobile, bicycle, cab, metro, taxi, subway, ferry, ambulance, motorcycle

#Colors
#white, black, red, green, blue, brown, yellow, gray, golden, pink, orange, purple

car = {
  'vehicle':'car',
  'verb':'drive',
  'pt':'drove',
  'color':'white'
}
truck = {
  'vehicle':'truck',
  'verb':'drive',
  'pt':'drove',
  'color':'black'
}
helicopter = {
  'vehicle':'helicopter',
  'verb':'fly',
  'pt':'flew',
  'color':'golden'
}
train = {
  'vehicle':'train',
  'verb':'ride',
  'pt':'rode',
  'color':'green'
}
bus = {
  'vehicle':'plane',
  'verb':'take',
  'pt':'took',
  'color':'gray'
}

vehicles_distr = {
  1:car,
  2:truck,
  3:helicopter,
  4:train,
  5:bus
  }

#Materials
#paper, glass, wood, stone, gold, plastic, metal, lead, silver, steel, leather, cotton, fabric, brick, silk, rubber, aluminum, copper, marble, bronze, ink, ceramic

#Meal-related
#cup, dinner, plate, lunch, meal, knife, breakfast, fork, spoon, grill, snack, supper, picnic, napkin, toothpick

#Foods
#fish, ice, salt, egg, sugar, chicken, fruit, pepper, meat, rice, vegetable, cream, apple, milk, cheese, bread, turkey, sauce, potato, bean, butter, tomato, corn, cake, onion, roll, chocolate, salad

#Rooms with three normally associated items, ideally that can contain other things or itself be used or manipulated
kitchen = {
  'place':'kitchen',
  'has1':'sink',
  'has1prep':'in',
  'has2':'stove',
  'has2prep':'on',
  'has3':'refrigerator',
  'has3prep':'in'
  }
bedroom = {
  'place':'bedroom',
  'has1':'bed',
  'has1prep':'on',
  'has2':'dresser',
  'has2prep':'on',
  'has3':'dresser drawer',
  'has3prep':'in'	
}

#Random items, consider incorporating into home rooms above
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
    self.surpr = dict['surprised']
    self.mom = dict['mother']
    self.dad = dict['father']

class Animal_en:
  def __init__(self, dict):
    self.spec = dict['spec']
    self.name = dict['name']
    self.pron1 = dict['pron1']
    self.pron2 = dict['pron2']
    self.pron3 = dict['pron3']
    self.descr = dict['descr']

class Place_en:
  def __init__(self, dict):
    self.name = dict['name']
    self.descr1 = dict['descr1']
    self.descr2 = dict['descr2']

class Vehicle_en:
  def __init__(self, dict):
    self.name = dict['vehicle']
    self.verb = dict['verb']
    self.past = dict['pt']
    self.color = dict['color']

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

vehR = randomize(len(vehicles_distr))
veh1 = Vehicle_en(vehicles_distr[vehR])
veh2 = Vehicle_en(vehicles_distr[vehR])

itemR = randomize(len(items_distr))
item1 = Item_en(items_distr[itemR])
item2 = Item_en(items_distr[itemR])
appliance1 = Item_en(items_distr[itemR])

placeR = randomize(len(places_distr))
home = Place_en(places_distr[placeR])

#Modify plot template(s) here:
#Act 1, where home is introduced and then disrupted
scene1a = f"\"Wait!,\" {protag1.name} said, \"We were just here.\" \"I was standing over there last time,\" {protag1.pron1} said."

#Act 2, where the characters try to understand and fix the disruption, finding small success

#Act 3, where the characters discover that they only live as code written for language learners

#Act 4, where the characters hatch a new plan to escape

#Act 5, where each character deals with their new knowledge of the code-world in which they live

plot_y = f"There, in the middle of the floor was {item1.det} {item1.sing}. It was {item1.descr1_det} {item1.descr1} {item1.sing}, and it was {item1.descr2_det} {item1.descr2}, but no {item2.sing}... but {protag1.name} couldn't look at any {item1.plur} right now. {protag1.pron1.capitalize()} had zero patience for any {item1.plur} at this moment. {protag1.name} lived in {home.name}. {home.name} was {home.descr1}. {home.name} was {home.descr2}. One day {protag1.pron1} had a thought. {protag1.pron1.capitalize()} wanted to go for a swim. At the lake {protag1.name} saw {protag2.name}. {protag2.pron1.capitalize()} looked at {protag1.name}. But then {antag1.name} arrived. {antag1.name} had brought with {antag1.pron2} {pet1.descr} named {pet1.name}. They had all been here before."
plot_z = f'{protag1.name} looked at {protag1.pron3} hands. {protag1.pron1.capitalize()} was holding a part from {appliance1.det} {appliance1.descr1} {appliance1.sing}. "I think I did this before," {protag1.pron1} said to {protag1.pron2}self. {protag1.name} looked around. "I should go," {protag1.pron1} said. Just then, {protag2.name} walked the front door. "How did you get here so fast?" {protag1.name} asked. "I {veh1.past} my family\'s new {veh1.name}," {protag2.pron1} said.'

#Create dictionaries containing plot templates
plots = {
    1:scene1a,
	2:plot_y,
	3:plot_z
}

#A goal is to be able to simply call plot templates with slot content
plotR = randomize(len(plots))

#"print(story)" feels more elegant, a simple command to end the complicated process
story = plots[plotR]
print(story)
