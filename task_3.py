# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Создать функцию сжатия строки и функцию восстановления строки.
# Пример:
# ABCABCABCDDDFFFFFF ->1A1B1C1A1B1C1A1B1C3D6F -> ABCABCABCDDDFFFFFF
# WWJJJHDDDDDPPGRRR -> 2W3J1H5D2P1G3R -> WWJJJHDDDDDPPGRRR
#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
import os
os.system('cls||clear')


def read_source_text(filename: str) -> list:
    with open(filename, "r", encoding = "utf-8") as data:
        text_for_work = list(data.read())       
        return text_for_work

def write_to_file(result_str: str, file_name: str) -> None:
    with open(file_name, mode="a", encoding="utf-8") as file:
        file.write(f'{result_str}'+'\n')   

def zip_file(source_lst: list) -> str:
    counter = 1
    zip_text =''

    for i in range (len(source_lst)-1):
        if i == len(source_lst) - 2:
            zip_text += str(counter + 1) + source_lst[i]  
        else:
            if source_lst[i] == source_lst[i+1]:
                counter += 1
            else: 
                zip_text += str(counter) + source_lst[i] 
                counter = 1
    return zip_text

def unzip_file(zipText: str) -> str:
    unzip_text =''

    for i in range(0, len(zipText), 2):
           unzip_text = unzip_text + (zipText[i + 1] * int(zipText[i]))
    return unzip_text
 
my_str = 'ABCABCABCDDDFFFFFF'
write_to_file(my_str, "source_text_task_3.txt")

sourse_text = read_source_text('source_text_task_3.txt')
zip_text=zip_file(sourse_text)
unzip_text = unzip_file(zip_text)

# print(f"Zipped text is: {zip_text}")
# print(f"Unipped text is: {unzip_text}")

write_to_file(zip_text , 'result_text_task_3.txt')
write_to_file(unzip_text, 'result_text_task_3.txt')


