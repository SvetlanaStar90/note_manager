title_name = []
title = input("Введите заголовок (или оставьте пустым для завершения) :")
while title != ""  :
    print(title)
    title_name.append(title)
    title = input("Введите заголовок (или оставьте пустым для завершения) :")
print("Заголовок заметки :")
for title in title_name :
   print("-", title)

