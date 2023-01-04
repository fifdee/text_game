import scene1


class Game:
    class GameState:
        WAITING = 'waiting'
        START = 'start'
        PLAYING = 'playing'
        FINISHED = 'finished'

    ALLOWED_COMMANDS = ['h', 'd', 'i', 'u', 't', 'q']

    state = GameState.START
    player = None
    current_scene = None

    @classmethod
    def help(cls):
        print('h - dostępne komendy')
        print('d - opisz pomieszczenie')
        print('i - wyświetl przedmioty z plecaka')
        print('u - użyj przedmiot')
        print('t - zabierz przedmiot')
        print('q - zakończ program')

    @classmethod
    def start_new(cls):
        cls.player = Player()
        cls.current_scene = Scene(**scene1.VALUES)
        cls.current_scene.show_beginning_text()
        cls.help()

    @classmethod
    def update(cls):
        while True:
            if cls.state == cls.GameState.START:
                cls.start_new()
                cls.state = cls.GameState.PLAYING
            elif cls.state == cls.GameState.PLAYING:
                command = input()
                if command not in cls.ALLOWED_COMMANDS:
                    print('Podano niepoprawną komendę')
                else:
                    match command:
                        case 'q':
                            print('kończę działanie programu...')
                            break
                        case 'h':
                            cls.help()
                        case 'd':
                            cls.current_scene.describe()
                        case 'i':
                            cls.player.show_items()
                        case 'u':
                            ...
                        case 't':
                            print('Wpisz nazwę przedmiotu, który chcesz włożyć do plecaka:')
                            items_to_choose = []
                            for item in cls.current_scene.items:
                                if not item.hidden:
                                    items_to_choose.append(item)
                                    print(f'{item}')
                            chosen_item_name = input()
                            while chosen_item_name not in [item.name for item in items_to_choose]:
                                print('Wprowadź poprawną nazwę przedmiotu.')
                                chosen_item_name = input()
                            chosen_item = [item for item in items_to_choose if item.name == chosen_item_name][0]
                            cls.player.take_item(chosen_item)
                            cls.current_scene.remove_item(chosen_item)

    @classmethod
    def finish(cls):
        ...


class Player:
    def __init__(self):
        self.items = []

    def show_items(self):
        if len(self.items) > 0:
            print('Przedmioty w plecaku:')
            for item in self.items:
                print(item)
        else:
            print('Nie masz nic w plecaku.')

    def use_item(self, item):
        pass

    def take_item(self, item):
        if item.collectible:
            self.items.append(item)
            print(f'Nowy przedmiot w plecaku: {item}')
            return True
        else:
            print(f'Próbujesz schować przedmiot "{item}" do plecaka, bez sukcesu.')
            return False


class Scene:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.nr = kwargs['nr']
        self.beginning = kwargs['beginning']
        self.description = kwargs['description']

        self.items = [Item(**item) for item in kwargs['items']]

    def remove_item(self, item):
        if item.collectible:
            self.items.remove(item)

    def show_beginning_text(self):
        print(self.beginning)

    def describe(self):
        print(self.description)
        print('Przedmioty, które widzisz dookoła:')
        for item in self.items:
            if not item.hidden:
                print(item.description)

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

        try:
            self.actions = [Action(**action) for action in kwargs['actions']]
        except KeyError:
            self.actions = None

    def __add__(self, other):
        ...  #

    def __str__(self):
        return self.name


class Action:
    def __init__(self, **kwargs):
        self.target = kwargs['target']
        self.result = kwargs['result']
        try:
            self.show_hidden_item_name = kwargs['show_hidden_item']
        except KeyError:
            self.show_hidden_item_name = None
        try:
            self.new_event_name = kwargs['new_event']
        except KeyError:
            self.new_event_name = None
        try:
            self.destroy_item_name = kwargs['destroy_item']
        except KeyError:
            self.destroy_item_name = None
