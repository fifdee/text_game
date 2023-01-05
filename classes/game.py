import sys

from default_scenes import scene1, scene2
from classes.player import Player
from classes.scene import Scene
from classes.file_manager import FileManager


class Game:
    class GameState:
        START = 'start'
        PLAYING = 'playing'

    ALLOWED_COMMANDS = ['h', 'd', 'i', 'u', 't', 'q']

    state = GameState.START
    player = None
    current_scene = None
    scene_number = 1

    @classmethod
    def help(cls):
        print('h - pomoc (help)')
        print('d - opisz pomieszczenie (describe)')
        print('i - wyświetl przedmioty z plecaka (inventory)')
        print('u - użyj przedmiot (use)')
        print('t - zabierz przedmiot (take)')
        print('q - zakończ program (quit)')

    @classmethod
    def start(cls):
        # FileManager.default_scene_dump(scene1.VALUES)  # Do stworzenia pliku json z zawartością danej sceny
        # FileManager.default_scene_dump(scene2.VALUES)  # Standardowo program pobiera dane z plików json

        cls.scene_number = FileManager.load_scene_number()
        if FileManager.is_scene_available(cls.scene_number):
            cls.player = Player()
            values = FileManager.get_scene_values(cls.scene_number)
            cls.current_scene = Scene(**values)
            cls.set_inventory()
            cls.current_scene.show_beginning_text()

            cls.state = cls.GameState.PLAYING

            cls.help()
        else:
            print('Gratulacje! Przeszedłeś wszystkie dostępne sceny.')
            print('Chcesz zacząć od nowa? Wpisz "reset".')
            if input() == 'reset':
                FileManager.save_scene_number(1)
            else:
                sys.exit()

    @classmethod
    def set_inventory(cls):
        inventory_items = [item for item in cls.current_scene.items if item.starts_in_inventory]
        for item in inventory_items:
            cls.player.take_item(item, silent=True)
            cls.current_scene.remove_item(item)

    @classmethod
    def update(cls):
        while True:
            if cls.state == cls.GameState.START:
                cls.start()
            elif cls.state == cls.GameState.PLAYING:
                print(f'Dostępne komendy: {cls.ALLOWED_COMMANDS}')
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
                            if len(cls.player.items) > 0:
                                chosen_item, target_item = cls.get_chosen_and_target_item()
                                if chosen_item and target_item:
                                    actions = cls.player.use_item(chosen_item, target_item)
                                    cls.perform_actions(actions)
                            else:
                                print('Nie masz żadnych przedmiotów w plecaku, które można byłoby użyć.')

                        case 't':
                            print('Wpisz nazwę przedmiotu, który chcesz włożyć do plecaka:')
                            cls.current_scene.tell_items_names()
                            chosen_item = cls.get_item_by_input_name(cls.current_scene.items)
                            if chosen_item:
                                if cls.player.take_item(chosen_item):
                                    cls.current_scene.remove_item(chosen_item)

    @classmethod
    def get_item_by_input_name(cls, items_list, provided_name=None, include_hidden=False):
        if len(items_list) > 0:
            items_to_choose = []
            for item in items_list:
                if not include_hidden:
                    if not item.hidden:
                        items_to_choose.append(item)
                else:
                    items_to_choose.append(item)
            if not provided_name:
                chosen_item_name = input()
            else:
                chosen_item_name = provided_name
            if chosen_item_name not in [item.name for item in items_to_choose]:
                if not provided_name:
                    print(f'Wprowadzono niepoprawną nazwę przedmiotu: {chosen_item_name}')
                return None
            chosen_item = [item for item in items_to_choose if item.name == chosen_item_name][0]
            return chosen_item
        return None

    @classmethod
    def get_chosen_and_target_item(cls):
        print('Wpisz nazwę przedmiotu, który chcesz użyć.')
        cls.player.show_items()
        chosen_item = cls.get_item_by_input_name(cls.player.items)

        if chosen_item:
            print(f'Wpisz nazwę przedmiotu, na którym chcesz użyć przedmiot {chosen_item}:')
            target_list = [item for item in cls.player.items + cls.current_scene.items if
                           not item.hidden and chosen_item != item]
            for item in target_list:
                print(item, end=', ')
            print()
            target_item = cls.get_item_by_input_name(target_list)

            return chosen_item, target_item
        return None, None

    @classmethod
    def perform_actions(cls, actions):
        if len(actions) > 0:
            for action in actions:
                if action.show_hidden_item_names:
                    for hidden_name in action.show_hidden_item_names:
                        item_to_show = cls.get_item_by_input_name(
                            cls.current_scene.items,
                            provided_name=hidden_name,
                            include_hidden=True)

                        if not item_to_show:
                            item_to_show = cls.get_item_by_input_name(
                                cls.player.items,
                                provided_name=hidden_name,
                                include_hidden=True)

                        if item_to_show:
                            item_to_show.hidden = False

                if action.destroy_item_names:
                    for destroy_name in action.destroy_item_names:
                        item_to_destroy = cls.get_item_by_input_name(
                            cls.current_scene.items + cls.player.items,
                            provided_name=destroy_name
                        )
                        cls.player.remove_item(item_to_destroy)
                        cls.current_scene.remove_item(item_to_destroy)

                if action.new_event_name:
                    if action.new_event_name == 'next_scene':
                        cls.finish()

    @classmethod
    def finish(cls):
        FileManager.save_scene_number(cls.scene_number + 1)
        cls.state = cls.GameState.START
