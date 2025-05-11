# Чтение файла через read() загружает все в память. Генераторы обрабатывают данные по частям

# Плохо для больших файлов: 
with open("huge.log") as f: 
    lines = f.readlines()  # Весь файл в памяти! 
 
# Хорошо: 
def read_lines(filename): 
    with open(filename) as f: 
        for line in f: 
            yield line  # По одной строке в памяти 
 
for line in read_lines("huge.log"): 
    process(line) 