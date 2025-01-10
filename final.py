
username = input("Введите ваше имя:")
content =input("Введите описание заметки:")
status =input("Введите статус заметки (актианая,завершена и т.д.):")
created_date =input("Введите дату создания заметки (дд-мм-гггг):")
issue_date =input("Введите дату окончания заметки (дд-мм-гггг):")
all_titles=[
    input("Введите заголовок заметки 1:"),
    input("Введите заголовок заметки 2:"),
    input("Введите заголовок заметки 3:")]
note=[username,content,status,created_date,issue_date,all_titles]

#вывод данных
print("Ваше имя:", note[0])
print("Заголовок 1:", all_titles[0])
print("Заголовок 2:", all_titles[1])
print("Заголовок 3:", all_titles[2])
print("Описание заметки:", note[1])
print("Статус:", note[2])
print("Дата создания заметки:", (note[3][0:5]))
print("Дата окончания заметки:", (note[4][0:5]))