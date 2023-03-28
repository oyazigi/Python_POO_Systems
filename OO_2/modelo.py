from abc import ABC
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def adicionar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,valor):
        self._nome = valor.title()

    def __str__(self):
        return f'Ano de lançamento: {self.ano}. Nome: {self._nome}. Likes:{self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Ano de lançamento: {self.ano}, Nome: {self._nome}, Duração: {self.duracao} Minutos, Likes:{self._likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Ano de lançamento: {self.ano}, Nome: {self._nome}, Temporadas: {self.temporadas}, Likes:{self._likes}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas
