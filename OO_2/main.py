import random

from modelo import *
vingadores = Filme("Vingadores",2020,147)
supernatural = Serie("Supernatural",2013,9)
driver = Serie("Driver", 2013, 9)
beleza_americana = Filme("American Beauty", 2018, 124)
filmes_e_series = [vingadores, supernatural,beleza_americana,driver]

fds = Playlist("Fim de semana", filmes_e_series)
for x in range(0,150):
    random.choice(filmes_e_series).adicionar_like()

print(vingadores in fds)

for programa in fds:
    print(programa)

print(len(fds))