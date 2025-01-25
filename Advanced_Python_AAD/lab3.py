with open("1.txt", "r") as file:
    for line in file:
        print(line.strip())

-------------------------------------

def write_array(array, file_name):
    file = open(file_name, 'w')
    file.write(array)
    file.close()

file = open("tmp.txt", "r")
a = file.read()
file.close()
write_array(a, '2.txt')

------------------------------------------
def write_array(array, file_name):
    file = open(file_name, 'w')
    arr = map (lambda x: x + '\n', array)
    file.writelines(arr)
    file.close()

a = ['12345', 'asdfghgd', 'v9v9v9']
write_array(a, '2.txt')
------------------------------------------
def write_array(array, file_name):
    file = open(file_name, 'w')
    file.write("\n".join(array))
    file.close()

a = ['12345', 'asdfghgd', 'v9v9v9']
write_array(a, '2.txt')
------------------------------------------

import os
import zipfile

path = input()
try:
    os.path.abspath(path)
except FileNotFoundError:
    print('Неправильный путь')
    
#zzip = zipfile.ZipFile('путь к файлу')
#zzip.extractall('куда распаковывать')
#zzip.close()

arr = []
    
    
try:
    for current_dir, dirs, files in os.walk("~/tmp"):
        if str(files).count('.py'):
            arr.append(current_dir)
    arr.sort()
except Exeption:
    print('Ошибка при попытке открытия файла с архивов')
        

try:
    with open(path, 'w') as file:
        file.write('\n'.join(arr))
except Exeption:
    print('Нет прав')
