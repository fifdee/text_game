import scene1


class Game:
    class GameState:
        WAITING = 'waiting'
        START = 'start'
        PLAYING = 'playing'
        FINISHED = 'finished'

    state = GameState.START
    player = None
    current_scene = None

    @classmethod
    def help(cls):
        ...

    @classmethod
    def start_new(cls):
        cls.player = Player()
        cls.current_scene = Scene(**scene1.VALUES)

    @classmethod
    def update(cls):
        if cls.state == cls.GameState.START:
            cls.start_new()
            print(cls.current_scene)

    @classmethod
    def finish(cls):
        ...


class Player:
    def __init__(self):
        self.items = []

    def show_items(self):
        ...

    def use_item(self, item):
        pass

    def take_item(self, item):
        pass


class Scene:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.nr = kwargs['nr']
        self.description = kwargs['description']

        self.items = [Item(**item) for item in kwargs['items']]

    def describe(self):
        print(self.description)

    def __str__(self):
        return self.name


class Item:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        try:
            self.collectible = kwargs['collectible']
        except KeyError:
            self.collectible = False
        try:
            self.hidden = kwargs['hidden']
        except KeyError:
            self.hidden = False
        self.description = kwargs['description']

        self.taken = False

        self.actions = []

    def __add__(self, other):
        ...  #

    def __str__(self):
        return self.name


class Action:
    def __init__(self, **kwargs):
        self.target = kwargs['target']
        self.result = kwargs['result']
        self.show_hidden_item_name = kwargs['show_hidden_item']
        self.new_event_name = kwargs['new_event']
        self.destroy_item_name = kwargs['destroy_item']

    def perform(self):
        ...