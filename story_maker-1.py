
#This can be a class-ier way to substitute story elements.

class Protag_en:
  def __init__(self, name, pron1, pron2, pron3):
    self.name = name
    self.pron1 = pron1
    self.pron2 = pron2
    self.pron3 = pron3


protag1 = Protag_en("Jim", "he", "him", "his")
protag2 = Protag_en("Jen", "she", "her", "hers")


print("Our hero is " + protag1.name + ". One day", protag1.pron1, "had a thought.", protag1.pron1.capitalize(), "wanted to go for a swim.", "At the lake", protag1.name, "saw", protag2.name + ".", protag2.pron1.capitalize(), "looked at", protag1.name + ".")




"""
import string

friend1 = "Sarah"
friend2 = "Tony"
item1 = "fridge"
use1 = "get whatever I want whenever I want it"
item2 = "dishwasher"
use2 = "get dishes clean quickly"


story_text1 = f"{friend1} and {friend2} were moving. They were especially excited about the new kitchen." + "\n" + "\n" + f"{friend1} said, \"I am excited about the {item1} so we can {use1}!" + "\n" + "\n" + f"{friend2} said, \"That sounds nice! I am also excited about the {item1}, and also the {item2}. I am really looking forward to being able to {use2}."

print(story_text1)


#the rest of this was trial and error, until I realized i could just use the simple f-string above.
"""
"""
#story_text1 = 
friend1 and friend2 were moving. They were especially excited about the new kitchen. /n friend1 said, "I am excited about the item1 so we can use1!" /n friend2 said, "That sounds nice! I am also excited aboit the item1, and also the item2. I am really looking forward to being able to use2."


def replace_text(text):
  out_text = text.replace('friend1', friend1)
  return out_text

done_text = replace_text(story_text1)
print(done_text)

def token_list(text):
  list = []
  split_text = text.split()
  for x in split_text:
    list.append(x)
  return list

tok_story_text = token_list(story_text1)
#print(tok_story_text)

def replace_words(list, friend1, friend2, item1, item2, use1, use2):
  while 'friend1' in list:
    index = list.index('friend1')
    list[index] = friend1
  while 'friend2' in list:
    index = list.index('friend2')
    list[index] = friend2
  while 'item1' in list:
    index = list.index('item1')
    list[index] = item1
  while 'item2' in list:
    index = list.index('item2')
    list[index] = item2
  while 'use1' in list:
    index = list.index('use1')
    list[index] = use1
  while 'use2' in list:
    index = list.index('use2')
    list[index] = use2
  return list
  #list = list.replace('friend1', str(friend1))
  #list = list.replace('friend2', str(friend2))
  #list = list.replace('item1', str(item1))
  #list = list.replace('item2', str(item2))
  #list = list.replace('use1', str(use1))
  #list = list.replace('use2', str(use2))
  #return list

replaced_list = replace_words(tok_story_text, friend1, friend2, item1, item2, use1, use2)
#print(replaced_list)

def ready_text(rep_words, friend1, friend2, item1, item2, use1, use2):
  text = replace_words(friend1, friend2, item1, item2, use1, use2)
  text.join(" ")
  return text



#ready_story = replace_words(story_text_1, friend1, friend2, item1, item2, use1, use2)

"""

