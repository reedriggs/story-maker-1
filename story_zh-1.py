#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:29:42 2021

@author: Reed Riggs
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
    