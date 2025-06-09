# Декартово произведение последовательности трех достоинств карт и последовательности четырех мастей дает последовательность, состоящую из двенадцати пар
# пример, декартово произведения с помощью спискового включения

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts) # [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]