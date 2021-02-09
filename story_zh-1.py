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
