#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:29:42 2021

@author: Reed Riggs
"""

#adapting the more complex system from the English system -- this is far from finished...

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 07:45:52 2021

@author: Reed Riggs 芮尚勤
"""

import random

#Create people for the story in Python dictionary format, providing category information that match the Person_en class below:
小白 = {
      '姓':'高',
      '名':'小白',
      '代':'他',
      '性格一':'認真',
      '性格二':'衝動',
      '父親':'作家',
      '母親':'老師'
      }
小芮 = {
      '姓':'芮',
      '名':'尚勤',
      '代':'他',
      '性格一':'可愛',
      '性格二':'調皮',
      '父親':'教授',
      '母親':'律師'
      }
銀河 = {
      '姓':'謝',
      '名':'銀河',
      '代':'她',
      '性格一':'聰明',
      '性格二':'著急',
      '父親':'法官',
      '母親':'編輯'
      }
老李 = {
      '姓':'裏',
      '名':'木子',
      '代':'他',
      '性格一':'開朗',
      '性格二':'嘻嘻笑笑的',
      '父親':'農夫',
      '母親':'醫生'
      }
老劉 = {
      '姓':'劉',
      '名':'建國',
      '代':'她',
      '性格一':'認真',
      '性格二':'衝動',
      '父親':'飛機駕駛員',
      '母親':'護士'
      }
張三 = {
      '姓':'張',
      '名':'三',
      '代':'他',
      '性格一':'認真',
      '性格二':'衝動',
      '父親':'作家',
      '母親':'教練'
      }
司徒亮 = {
      '姓':'司徒',
      '名':'亮',
      '代':'她',
      '性格一':'認真',
      '性格二':'衝動',
      '父親':'科學家',
      '母親':'記者'
      }
諸葛東 = {
      '姓':'諸葛',
      '名':'東',
      '代':'他',
      '性格一':'認真',
      '性格二':'衝動',
      '父親':'秘書',
      '母親':'教授'
      }
鄭正 = {
      '姓':'鄭',
      '名':'正',
      '代':'他',
      '性格一':'認真',
      '性格二':'衝動',
      '父親':'演員',
      '母親':'音樂家'
      }
悟空 = {
      '姓':'歐陽',
      '名':'悟空',
      '代':'他',
      '性格一':'認真',
      '性格二':'衝動',
      '父親':'工程師',
      '母親':'律師'
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
    'protag1':小白,
    'protag2':小芮,
    'ally1':銀河,
    'ally2':老李,
    'ally3':老劉,
    'antag1':張三,
    'antag2':司徒亮,
    'fake_ally_opp_1':諸葛東,
    'fake_ally_opp_2':鄭正,
    'fake_opp_ally_1':悟空
    },
}

#Create animals for the story in Python dictionary format, providing category information that match the Animal_en class below:
#dog, fish, bird, horse, chicken, cat, bear, fox, turkey, wolf, deer, duck, tiger, cow, mouse, eagle, snake, lion, rat, pig

狗一 = {
    'spec':'狗',
    'name':'狗狗',
    'pron':'它',
    'descr':'很乖的'
    }

狗二 = {
    'spec':'狗',
    'name':'小白',
    'pron':'它',
    'descr':'很乖的'
    }

"""
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
    'pron3':'her',
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
    'pron3':'her',
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
    'pron3':'her',
    'descr':'an attention-seeking chicken'
    }
"""

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
bathroom = {
    'place':'bathroom',
    'has1':'toilet',
    'has1prep':'in',
    'has2':'cabinet',
    'has2prep':'in',
    'has3':'bath tub',
    'has3prep':'in'	
    }
living_room = {
    'place':'living room',
    'has1':'TV',
    'has1prep':'on',
    'has2':'couch',
    'has2prep':'on',
    'has3':'carpet',
    'has3prep':'on'	
    }

rooms_distr = {
    1:kitchen,
    2:bedroom,
    3:bathroom,
    4:living_room
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
    self.name = dict['名']
    self.pron1 = dict['代']
    self.descr1 = dict['性格一']
    self.descr2 = dict['性格二']
    self.mom = dict['母親']
    self.dad = dict['父親']

class Animal_en:
  def __init__(self, dict):
    self.spec = dict['spec']
    self.name = dict['name']
    self.pron = dict['pron']
    self.descr = dict['descr']

class Place_en:
  def __init__(self, dict):
    self.name = dict['name']
    self.descr1 = dict['descr1']
    self.descr2 = dict['descr2']
    
class Room_en:
  def __init__(self, dict):
    self.name = dict['place']
    self.has1 = dict['has1']
    self.has1pr = dict['has1prep']
    self.has2 = dict['has2']
    self.has2pr = dict['has2prep']
    self.has3 = dict['has3']
    self.has3pr = dict['has3prep']

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
ally1 = Person_en(people_distr[peopR]['ally1'])
ally2 = Person_en(people_distr[peopR]['ally2'])
ally3 = Person_en(people_distr[peopR]['ally3'])
antag1 = Person_en(people_distr[peopR]['antag1'])
antag2 = Person_en(people_distr[peopR]['antag2'])
fake_ally_opp_1 = Person_en(people_distr[peopR]['fake_ally_opp_1'])
fake_ally_opp_2 = Person_en(people_distr[peopR]['fake_ally_opp_2'])
fake_opp_ally_1 = Person_en(people_distr[peopR]['fake_opp_ally_1'])

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

roomR = randomize(len(rooms_distr))
room = Room_en(rooms_distr[placeR])

#Modify plot template(s) here:
#Act 1, where home is introduced and then disrupted
Act1_scene1a = f"\"Wait!,\" {protag1.name} said, \"We were just here.\" \"I was standing over there last time,\" {protag1.pron1} said. {protag1.name} tried to remember what was happening just a few moments before, but memories slipped away much like right after waking up from a dream. And then everything ended again."
Act1_scene2a = f"In a house in Houston, Texas, in the {room.name}, {protag1.name} looked at {ally1.name} and {fake_ally_opp_1.name}. {protag1.name} thought something seemed strange. \"What were we doing just now, or, just before now?\" {ally1.name} and {fake_ally_opp_1.name} had no idea. \"Are you hungry? Should we eat?\" {protag1.name} asked. \"Sure,\" {ally1.name} answered, but just then things came to an end."

#Act 2, where the characters try to understand and fix the disruption, finding small success

#Act 3, where the characters discover that they only live as code written for language learners
  #responses include: taking up hobbies, reading jokes together and laughing, writing more, spiritual journies, exercising more, trying to escape
  #create as foils

#Act 4, where the characters hatch a new plan to escape
Act4_scene1a = f"\"I'm fine here,\" said {protag1.name}. \"I know you all want to escape and whatever, but I have so much I can focus on and get done if I'm not spending all of my time trying to escape.\" Just then, everything ended again."
Act4_scene2a = f"{protag1.name} was crying in a bathroom. \"Wait,\" asked {protag1.name}, \"why am I crying in a bathroom?\" All memories quickly disappeared, and that was the only familiar part of all of this. {protag1.name} felt content about just moving on... but that's when everything ended... again."
#Act 5, where each character deals with their new knowledge of the code-world in which they live

plot_y = f"There, in the middle of the floor was {item1.det} {item1.sing}. It was {item1.descr1_det} {item1.descr1} {item1.sing}, and it was {item1.descr2_det} {item1.descr2}, but no {item2.sing}... but {protag1.name} couldn't look at any {item1.plur} right now. {protag1.pron1.capitalize()} had zero patience for any {item1.plur} at this moment. {protag1.name} lived in {home.name}. {home.name} was {home.descr1}. {home.name} was {home.descr2}. One day {protag1.pron1} had a thought. {protag1.pron1.capitalize()} wanted to go for a swim. At the lake {protag1.name} saw {protag2.name}. {protag2.pron1.capitalize()} looked at {protag1.name}. But then {antag1.name} arrived. {antag1.name} had brought with {antag1.pron1} {pet1.descr} named {pet1.name}. They had all been here before."
plot_z = f'{protag1.name} looked at {protag1.pron1} hands. {protag1.pron1.capitalize()} was holding a part from {appliance1.det} {appliance1.descr1} {appliance1.sing}. "I think I did this before," {protag1.pron1} said to {protag1.pron1}self. {protag1.name} looked around. "I should go," {protag1.pron1} said. Just then, {protag2.name} walked the front door. "How did you get here so fast?" {protag1.name} asked. "I {veh1.past} my family\'s new {veh1.name}," {protag2.pron1} said.'

#Create dictionaries containing plot templates
plots = {
    1:Act1_scene1a,
    2:Act1_scene2a,
    3:plot_y,
    4:plot_z
}

#A goal is to be able to simply call plot templates with slot content
plotR = randomize(len(plots))

#"print(story)" feels more elegant, a simple command to end the complicated process
story = plots[plotR]
print(story)

#old code
"""
#this is more toward the goal of having mutable objects to pass through functions and/or classes so users can flexibly modify story elements.
def 故事_一(**dict):
  甲 = dict['甲']
  乙 = dict['乙']
  品甲 = dict['品甲']
  用法甲 = dict['用法甲']
  品乙 = dict['品乙']
  用法乙 = dict['用法乙']
  文字 = "故事：" + "\n" + f"{甲}和{乙}很期待搬到新的家。" + "\n" + "\n" + f"{甲}特別想用剛買的{品甲}，因為{用法甲}。" + "\n" + "\n" + f"{乙}很期待新的{品乙}，因為可以{用法乙}！"
  return 文字

故事a = {
  '甲':'年獸',
  '乙':'玉兔',
  '品甲':'書桌',
  '用法甲':'上網',
  '品乙':'冰箱',
  '用法乙':'冷凍很多藥'
  }

故事_一 = 故事_一(**故事a)

print(故事_一, "\n" + "\n")


def 故事_二(甲, 乙, 品甲, 用法甲, 品乙, 用法乙):
  文字 = "故事：" + "\n" + f"{甲}和{乙}很期待搬到新的家。" + "\n" + "\n" + f"{甲}特別想用剛買的{品甲}，因為{用法甲}。" + "\n" + "\n" + f"{乙}很期待新的{品乙}，因為可以{用法乙}！"
  return 文字

def 故事_三():
  甲 = '年獸'
  乙 = '玉兔'
  品甲 = '書桌'
  用法甲 = '上網'
  品乙 = '冰箱'
  用法乙 = '冷凍很多藥'
  文字 = "故事：" + "\n" + f"{甲}和{乙}很期待搬到新的辦公室。" + "\n" + "\n" + f"{甲}特別想用辦公室的的{品甲}，因為{用法甲}。" + "\n" + "\n" + f"{乙}很期待用幫共識的{品乙}，因為可以{用法乙}！"
  return 文字

def 故事_四():
  甲 = '尚勤'
  乙 = '銀河'
  品甲 = '冰箱'
  品乙 = '洗碗機'
  用法甲 = '想吃就吃'
  用法乙 = '省很多時間'
  文字 = "故事：" + "\n" + f"{甲}和{乙}很期待搬到新的家。" + "\n" + "\n" + f"{甲}特別想用剛買的{品甲}，因為{用法甲}。" + "\n" + "\n" + f"{乙}很期待新的{品乙}，因為可以{用法乙}！"
  return 文字

故事n = {
  '甲':'年獸',
  '乙':'玉兔',
  '品甲':'書桌',
  '用法甲':'上網',
  '品乙':'冰箱',
  '用法乙':'冷凍很多藥'
  }

故事_二 = 故事_二(**故事n)
故事_三 = 故事_三()
故事_四 = 故事_四()

print(故事_二, "\n" + "\n")
print(故事_三, "\n" + "\n")
print(故事_四, "\n" + "\n")
"""

#old code
"""
甲 = '尚勤'
乙 = '銀河'
品甲 = '冰箱'
品乙 = '洗碗機'
用法甲 = '想吃就吃'
用法乙 = '省很多時間'

故事一 = f"{甲}和{乙}很期待搬到新的家。" + "\n" + "\n" + f"{甲}特別想用剛買的{品甲}，因為{用法甲}。" + "\n" "\n" + f"{乙}很期待新的{品乙}，因為可以{用法乙}！"
故事二 = f"{甲}和{乙}很期待搬到新的辦公室。" + "\n" + "\n" + f"{甲}特別想用辦公室的的{品甲}，因為{用法甲}。" + "\n" "\n" + f"{乙}很期待用幫共識的{品乙}，因為可以{用法乙}！"
print(故事一)
#this second version only changes the surrounding text and story content, but not the content of the blanks that are filled in
print(故事二)
#this seems inefficient, but it's the other option I'm aiming for; set up an alternate list of words to fill into the same text context
甲2 = '尚勤'
乙2 = '銀河'
品甲2 = '冰箱'
品乙2 = '洗碗機'
用法甲2 = '想吃就吃'
用法乙2 = '省很多時間'
故事一2 = f"{甲2}和{乙2}很期待搬到新的家。" + "\n" + "\n" + f"{甲2}特別想用剛買的{品甲2}，因為{用法甲2}。" + "\n" "\n" + f"{乙2}很期待新的{品乙2}，因為可以{用法乙2}！"
故事二2 = f"{甲2}和{乙2}很期待搬到新的辦公室。" + "\n" + "\n" + f"{甲2}特別想用辦公室的的{品甲2}，因為{用法甲2}。" + "\n" "\n" + f"{乙2}很期待用幫共識的{品乙2}，因為可以{用法乙2}！"

print(故事一2)
print(故事二2)

#Next steps: use a class or function or both to make plug-and-go story text alternatives
#Update 2021 Feb 8: this works for now; it's messy but it works

class Set_1: 
  def __init__(self): 
    self.str = "hero"
  def named(name):
    named = "Bill"
    return named
  def owner(pet):
    has_pet = "Finn"
    return has_pet
      
class Set_2: 
  def __init__(self): 
    self.str = "hero"
  def named(name):
    named = "Reginald"
    return named
  def owner(pet):
    has_pet = "Rory"
    return has_pet
    
set1 = Set_1()
person1 = set1.named()
pet1 = set1.owner()
set2 = Set_2()
person2 = set2.named()
pet2 = set2.owner()

故事一a = f"{person1}和{person2}很期待搬到新的家。" + "\n" + "\n" + f"{person1}特別想用剛買的{pet2}，因為{用法甲}。" + "\n" "\n" + f"{person1}很期待新的{pet2}，因為可以{用法乙}！"
故事二a = f"{person2}和{person1}很期待搬到新的辦公室。" + "\n" + "\n" + f"{person2}特別想用辦公室的的{pet1}，因為{用法甲}。" + "\n" "\n" + f"{person2}很期待用幫共識的{pet1}，因為可以{用法乙}！"

print(故事一a)
print(故事二a)

#Next step: use class sets and the value definitions that follow to make it easier to define a person and their associated characteristics, belongings, and quoted speech, in order to more easily plug different such sets into one text context.
"""
