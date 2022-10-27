# Напишите программу, удаляющую из текста все слова, содержащие "abc".
# Примечание Текст находится в файле. Его надо считать, текст исправить, исправленный текст записать в новый файл.
# Использовать вложенный менеджер контекста
import os
os.system('cls||clear')


def write_to_file(source_str: str, file_name: str) -> None:
    with open(file_name, mode="w", encoding="utf-8") as file:
        file.write(source_str)


def read_source_text(filename: str) -> str:
    with open(filename, "r", encoding = "utf-8") as data:
        text_to_work = data.read().split()        
    return text_to_work


my_str = 'Напишите программу abc, удаляющую из текста все слова, содержащие abc '
write_to_file(my_str, "source_text.txt")

text_to_work = read_source_text("source_text.txt")

result_text =' '.join(filter(lambda x: 'abc' not in x, my_str.split()))
write_to_file(result_text, "result_text.txt")

# print(my_str)
# print(result_text)

