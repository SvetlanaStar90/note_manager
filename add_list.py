username = input("Введите ваше имя:")
title1 =input("Введите заголовок заметки 1:")
title2=input("Введите заголовок заметки 2:")
title3=input("Введите заголовок заметки 3:")
all_titles = [title1, title2, title3]
content =input("Введите описание заметки:")
status ="активна"
created_date =input("Введите дату создания заметки (дд-мм-гггг):")
issue_date =input("Введите дату окончания заметки (дд-мм-гггг):")
#вывод данных
print("Ваше имя:", username)
print("Заголовок 1: " + all_titles[0],
      "Заголовок 2: " + all_titles[1],
      "Заголовок 3: " + all_titles[2], sep="\n")
print("Описание заметки:",content)
print("Статус:", status)
print("Дата создания заметки:", created_date[0:5])
print("Дата окончания заметки:", issue_date[0:5])
