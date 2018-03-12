class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)

        return cls.__instance


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
