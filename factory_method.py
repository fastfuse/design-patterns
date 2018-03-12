import random
from singleton import Singleton, Borg


class Void:
    pass


CLASSES = {
    'void': Void,
    'singleton': Singleton,
    'borg': Borg
}


def factory_method(cls='void'):
    return CLASSES.get(cls)()


objects = []

for _ in range(10):
    objects.append(factory_method(random.choice(list(CLASSES.keys()))))

print()
