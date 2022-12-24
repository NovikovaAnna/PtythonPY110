
from random import random, randint, uniform, choice
from json import dumps
from typing import Iterator
from faker import Faker
from conf import MODEL


FAKE = Faker('ru')


def main():
    """
    Список из 100 книг, запись в файл JSON.

    """
    books = book_gen()
    library = [next(books) for _ in range(100)]
    with open('library.json', 'w', encoding='utf8') as file:
        file.write(dumps(library, indent=4, ensure_ascii=False))
    return


def title():
    """
    Возвращает случайно выбранное название из списка в файле.
    :return: str
    """
    with open('books.txt', encoding='utf8') as file:
        return choice(file.readlines()).rstrip()



def year() -> int:
    """
    Возвращает случайный год; диапазон 2000-2022.
    :return: int
    """
    return randint(2000, 2022)


def pages() -> int:
    """
    Возвращает случайное число страниц; диапазон 100 - 1000.
    :return: int
    """
    return randint(100, 1000)


def isbn() -> str:
    """
    Возвращает случайный ISBN.
    :return: str
    """
    return FAKE.isbn13()


def rating() -> float:
    """
    Возвращает случайный рейтинг
    :return: float
    """
    return round(uniform(0, 5), 2)


def price() -> float:
    """
    Возвращает случайную цену
    :return: float
    """
    return round(uniform(400, 1500), 1)


def authors() -> list:
    mr = f'{FAKE.first_name_male()} {FAKE.last_name_male()}'
    mrs = f'{FAKE.first_name_female()} {FAKE.last_name_female()}'
    res = [mr, mrs]
    return [choice(res) for _ in range(randint(1, 3))]

def book_gen(pk: int = 1) -> Iterator[dict]:
    """
    Генератор книг.
    :param pk: Стартовое значение для книги, по-умолчанию 1
    :return: dict
    """
    while True:
        yield {
            'model': MODEL,
            'pk': pk,
            'fields': {
                "title": title(),
                "year": year(),
                "pages": pages(),
                "isbn13": isbn(),
                "rating": rating(),
                "price": price(),
                "author": authors()
            }
        }
        pk += 1


if __name__ == '__main__':
    main()