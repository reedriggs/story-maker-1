#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:29:42 2021

@author: Reed Riggs
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
