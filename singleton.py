"""
Singleton stuff.
"""


class SingletonOne:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)

        return cls.__instance


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args,
                                                                     **kwargs)

        return cls._instances[cls]


class SingletonTwo(metaclass=SingletonMeta):
    pass


class Borg:
    """
    aka Monostate
    """

    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Initial'

    def __str__(self):
        return self.state
