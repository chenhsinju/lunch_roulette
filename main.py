from enum import Enum
from typing import Annotated

from fastapi import FastAPI, Query

from roulette import Roulette


app = FastAPI()

lunch_list = [
    '六條通魷魚羹',
    '雲記速食便當（環保餐盒）',
    '金好呷-土雞便當/雞肉飯/中山美食/外送便當(cc: 銷魂雞肉飯)',
    '虹越小館越南美食',
    '3條通蔬食(cc: 素食便當)',
    '豪季水餃專賣店（台北車站店）',
    '梁記嘉義雞肉飯',
]
dinner_list = [
    '全之鄉池上木盒便當',
    '金名號雞肉飯-天津店',
    '潭村台南虱目魚',
    '鴻門燒臘',
    '七條通蕭家魚湯',
    '21街冰棧(cc: 雞肉鍋燒意麵)',
    'Subway 淡水捷運站店',
    '學府銀記桂林米粉',
]


class Meal(str, Enum):
    lunch = 'lunch'
    dinner = 'dinner'


class Method(str, Enum):
    append = 'append'
    remove = 'remove'


@app.get('/{meal}/')
def get_restaurant(meal: Meal):
    choice_list = []
    if meal is Meal.lunch:
        choice_list = lunch_list
    elif meal is Meal.dinner:
        choice_list = dinner_list

    choice_result = Roulette(choice_list=choice_list).roulette()
    return {'restaurant': choice_result}


@app.post('/{meal}/{method}/')
def edit_restaurant(
        meal: Meal,
        method: Method,
        restaurant_name_list: Annotated[list[str], Query()] = None):
    choice_list = []
    if meal is Meal.lunch:
        choice_list = lunch_list
    elif meal is Meal.dinner:
        choice_list = dinner_list

    restaurant_name_list = list(set(restaurant_name_list))

    if method is Method.append:
        choice_list.extend(restaurant_name_list)
    elif method is Method.remove:
        for restaurant_name in restaurant_name_list:
            choice_list.remove(restaurant_name)

    choice_list = list(set(choice_list))

    return {method.name: restaurant_name_list,
            'choice_list': choice_list}
