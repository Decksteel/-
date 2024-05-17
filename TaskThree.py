#Задание 3:  Задача «Равные части».
Text = "кенгуру"

a= len(Text) // 2 + len(Text) % 2

print(Text[a:] + Text[:a])