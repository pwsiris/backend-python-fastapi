import random
from datetime import datetime
from types import SimpleNamespace

from utils.errors import HTTPabort


class ListCounter:
    def __init__(self, input=[]):
        self.counter = 0
        if input:
            self.counter = len(input)

        self.data = {int(i + 1): input[i] for i in range(len(input))}

        self._lock = False

    def locking(function):
        def decorator(self, *args, **kwargs):
            while self._lock:
                pass
            self._lock = True
            result = function(self, *args, **kwargs)
            self._lock = False
            return result

        return decorator

    @locking
    def add_item(self, item):
        if item in self.data.values():
            HTTPabort(409, "Item already exists")
        self.counter += 1
        self.data[self.counter] = item
        return self.counter

    @locking
    def remove_item(self, index):
        if index not in self.data:
            HTTPabort(404, "Item not found")
        del self.data[index]

    @locking
    def update_item(self, index, new_item):
        if index not in self.data:
            HTTPabort(404, "Item not found")
        self.data[index] = new_item

    @locking
    def get_all_items(self):
        return self.counter, self.data

    def get_random_element(self):
        random.seed(datetime.now().timestamp())
        return self.data[random.choice(list(self.data.keys()))]

    def has_item(self, item):
        return item in self.data.values()


class Bite:
    def __init__(self, bot_list=[], action_list=[], place_list=[], body_part_list=[]):
        self.cheats = False
        self.bots = ListCounter(bot_list)
        self.actions = ListCounter(action_list)
        self.places = ListCounter(place_list)
        self.body_parts = ListCounter(body_part_list)


def get_categoty_list_object(type, in_memory_data):
    if type == "save_choices":
        return in_memory_data.SAVE_CHOICES
    elif type == "bite_bots":
        return in_memory_data.BITE.bots
    elif type == "bite_actions":
        return in_memory_data.BITE.actions
    elif type == "bite_places":
        return in_memory_data.BITE.places
    elif type == "bite_body_parts":
        return in_memory_data.BITE.body_parts
    else:
        HTTPabort(404, "Wrong type")


in_memory_data = SimpleNamespace()

in_memory_data.SAVE_CHOICES = ListCounter(
    [
        "Назвался стримером - пошёл сохранился",
        "Сделал дело — пошёл сохранился",
        "Баба с возу — пошла сохранилась",
        "И волки сохранились, и овцы сохранились",
        "Хотел как лучше, а пошёл сохраняться",
        "Дают — бери, а бьют — сохраняйся",
        "Последствия последствиями, а ты сохранись",
        "Чья бы корова мычала, а ваша бы сохранилась",
        "Учень свет, а ты сходи сохранись",
        "Семь раз отмерь, один раз сохранись",
        "Скажи мне, кто твой друг, и оба сохранитесь",
        "Чем бы дитя не тешилось, лишь бы сохранялось",
        "Пришли беда - пошла сохраняться",
        "Готовь сани летом, а зимой сохранись",
        "Со своим уставом сохраняться ходят",
        "Встречают по одёжке, а провожают по сохранениям",
        "Слово не воробей вылетит — не сохранишься",
        "Не плюй в колодец — не сохранишься в нём больше",
        "Если гора не идёт к Магомеду, то Магомед идёт сохраняться",
        "Не так страшен чёрт, как не сохраниться перед ним",
        "Спасибо вашему дому, а нам пора сохраниться",
        "Рыбы ищут где глубже, а ты где сохраниться",
        "Один в поле идёт сохраняться",
        "На безрыбье и сохранение рыба",
        "Работа не волк, сохраняться не убежит",
        "Любишь кататься — люби и сохраняться",
        "Кто рано встаёт, тот сохраняться идёт",
    ]
)

in_memory_data.BITE = Bite(
    bot_list=[
        "streamelements",
        "mrtukoffka",
        "creatisbot",
        "moobot",
        "nightbot",
        "soundalerts",
        "commanderroot",
    ],
    action_list=[
        "залез",
        "ворвался",
        "прокрался",
        "забежал",
        "втиснулся",
        "залетел со скоростью света",
    ],
    place_list=[
        "подвал",
        "комнату",
        "ванну",
        "квартиру",
        "дом",
        "бассейн",
        "подвал",
        "кровать",
        "шкаф",
        "душ",
    ],
    body_part_list=[
        "ляшку",
        "пальчик",
        "ушко",
        "носик",
        "ногу",
        "руку",
        "плечо",
        "жэпку",
        "щечку",
        "титечку",
        "пиписку",
        "бочек, как волчок",
        "ASS",
        "пятку",
    ],
)
