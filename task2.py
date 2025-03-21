#2

'''
Создайте класс Задача с атрибутами название, 
описание и статус (выполнено или нет). Напишите
методы для изменения статуса задачи на выполненную 
и вывода информации о задаче в виде
"Задача (название): (описание), статус - (статус)". 
Используйте магический метод `__str__` для вывода
информации о задаче.
'''

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True
        print(f"Задача '{self.title}' отмечена как выполненная.")

    def __str__(self):
        status = "выполнена" if self.completed else "не выполнена"
        return f"Задача '{self.title}': {self.description}, статус - {status}"

task1 = Task("Помыть посуду", "На кухне вечером", False)
task2 = Task("Погулять с собакой", "После ужина", True)
task3 = Task("Сделать домашнее задание", "Сделать задания по математике", False)

print(task1)
print(task2)
print(task3)

task1.mark_completed()
print(task1)