"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Написать функцию, которая возвращает значения в словаре
"""


def get_values(collection: dict):
    return collection.values()


if __name__ == '__main__':
    assert (100, 200) == tuple(get_values({1: 100, 2: 200}))
    print('Решено!')
