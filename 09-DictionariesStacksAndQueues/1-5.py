#Utwórz tablicę z 5 słownikami, z których każdy zawiera nazwę kraju i jego populację.
#Następnie wyświetl zawartość tablicy.
#Przykładowy wynik:
#COUNTRY  POPULATION
#Poland   38000000
#…        …
#…        …
#…        …
#…        …
countries = [
{"name":"Poland", "population":38000000},
    {"name":"Brazil", "population":102000000},
    {"name":"Portugal", "population":50200000},
    {"name":"Spain", "population":61000000},
    {"name":"France", "population":52000000},
]

print('COUNTRY  POPULATION')
for x in countries:
    
    print(f"{x['name']:<8} {x['population']}")