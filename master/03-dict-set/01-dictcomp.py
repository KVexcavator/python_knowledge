# Словарное включение (dictcomp) строит объект dict, порождая пары key:value из произвольного итерируемого объекта.

dial_codes = [
  (880, 'Bangladesh'),
  (55, 'Brazil'),
  (86, 'China'),
  (91, 'India'),
  (62, 'Indonesia'),
  (81, 'Japan'),
  (234, 'Nigeria'),
  (92, 'Pakistan'),
  (7, 'Russia'),
  (1, 'United States'),
]
country_dial = {country: code for code, country in dial_codes}
print(country_dial)
# {'Bangladesh': 880, 'Brazil': 55, 'China': 86, 'India': 91, 'Indonesia': 62, 'Japan': 81, 'Nigeria': 234, 'Pakistan': 92, 'Russia': 7, 'United States': 1}