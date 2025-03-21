#5

'''
Опишите класс Book, заданный названием, автором, 
издательством и годом издания. Включить в описание класса методы: 
вывода информации о книге на экран, проверки, является ли книга новой 
(изданной в последние 5 лет).
'''

class Book():
    def __init__ (self, name, autor, home, year):
        self.name=name
        self.autor=autor
        self.home=home
        self.year=year
        self._genre = None
        
    def printt(self):
        print(f'Название: {self.name}')
        print(f'Автор: {self.autor}')
        print(f'Издательство: {self.home}')
        print(f'Год издания: {self.year}')
        print(f'Жанр: {self._genre}')

    def new(self):
        if self.year>=2020:
            print("Новая")
        else:
            print("Cтарая")

    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, value):
        self._genre = value

d1 = Book('Война и мир', 'Л.Н. Толстой', 'АСТ', 2023)
d1.genre = "Роман"
d2 = Book('Вишнёвый сад', 'А. П. Чехов', 'ЭКСМО', 2002)
d2.genre = "Комедия"
d3 = Book('Мёртвые души', 'Н. В. Гоголь', 'АСТ', 2022)
d3.genre = "Повесть"

d1.printt()
d1.new()