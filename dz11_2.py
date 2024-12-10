''' Задача2.Магия
Для одной игры необходимо реализовать механику магии, где при соединении
 двух элементов получается новый. У нас есть четыре базовых элемента:
 «Вода», «Воздух», «Огонь», «Земля». Из них получаются новые: «Шторм»,
 «Пар», «Грязь», «Молния», «Пыль», «Лава».
 Таблица преобразований:
 ● Вода+Воздух =Шторм; Water+Air =Storm
 ● Вода+Огонь=Пар;     Water+Fire=Steam
 ● Вода+Земля=Грязь;   Water+Earth=Mud
 ● Воздух +Огонь = Молния;   Air +Fire = Lightning
 ● Воздух +Земля = Пыль;     Air +Earth = Dust
 ● Огонь+Земля =Лава.        Fire+Earth =Lava

  Напишите программу, которая реализует все эти элементы. Каждый элемент
 необходимо организовать как отдельный класс. Если результат не определён,
 то возвращается None'''

from random import randint, choice

class Water:
    title = 'Вода'
    def __add__(self, other):
        if isinstance(other, Air):
            return Shtorm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None

class Earth:
    title = 'Земля'
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        else:
            return None

class Fire:
    title = 'Огонь'
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        else:
            return None

class Air:
    title = 'Воздух'
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Fire):
            return Lightning()
        else:
            return None

class Shtorm:
    title = 'Шторм'
    def __str__(self):
        return 'Шторм'


class Steam:
    title = 'Пар'
    def __str__(self):
        return 'Пар'


class Dirt:
    title = 'Грязь'
    def __str__(self):
        return 'Грязь'


class Lightning:
    title = 'Молния'
    def __str__(self):
        return 'Молния'


class Dust:
    title = 'Пыль'
    def __str__(self):
        return 'Пыль'


class Lava:
    title = 'Лава'
    def __str__(self):
        return 'Лава'


class Fog:
    title = 'Tуман'
    def __add__(self, other):
        if isinstance(other, Water):
            return None
        elif isinstance(other, Earth):
            return None
        elif isinstance(other, Fire):
            return None
        elif isinstance(other, Air):
            return None
    def __str__(self):
        return 'Туман'

def main():
    elements = [Water(), Earth(), Fire(), Air(), Fog()]
    element_1 = choice(elements)
    element_2 = choice(elements)
    print(element_1.title)
    print(element_2.title)
    result = element_1 + element_2
    if result is None:
        print('None')
        #return None
    else:
        print(f"Смешиваем '{element_1.title}' c '{element_2.title}' и получаем '{result}'")
        #return result

main()
#print(f"Смешиваем '{f.title}' c '{a.title}' и получаем '{s}'")
