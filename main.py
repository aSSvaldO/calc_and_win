class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color

    def describe(self, full=False):
        if full is False:
            return super().describe()
        return (f'Попугай name — заметная птица, окрас её перьев — {self.color}, '
                f'а размер — {self.size}. Интересный факт: попугаи чувствуют ритм, '
                f'а вовсе не бездумно двигаются под музыку. Если сменить композицию, '
                f'то и темп движений птицы изменится.')


class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full=False):
        if full is False:
            return super().describe()
        return (f'Размер пингвина {self.name} из рода {self.genus} — {self.size}. '
                f'Интересный факт: однажды группа геологов-разведчиков '
                f'похитила пингвинье яйцо, и их принялась преследовать вся стая, '
                f'не пытаясь, впрочем, при этом нападать. Посовещавшись, похитители '
                f'вернули птицам яйцо, и те отстали.')


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
kesha.describe()
kowalski.describe(True)
