class Player:
    def __init__(self):
        self.items = []

    def show_items(self):
        if len(self.items) > 0:
            print('Przedmioty w plecaku:')
            for item in self.items:
                if not item.hidden:
                    print(item)
        else:
            print('Nie masz nic w plecaku.')

    def use_item(self, chosen_item, target_item):
        actions = [action for action in chosen_item.actions if action.target == target_item.name]
        if len(actions) == 0:
            print(f'Używasz {chosen_item} na {target_item}. Nie przyniosło to żadnego rezultatu.')
        else:
            for action in actions:
                print(action.result)
        return actions

    def take_item(self, item, silent=False):
        if item.collectible:
            self.items.append(item)
            if not silent:
                print(f'Nowy przedmiot w plecaku: {item}')
            return True
        else:
            print(f'Próbujesz schować przedmiot "{item}" do plecaka, bez sukcesu.')
            return False

    def remove_item(self, item):
        try:
            self.items.remove(item)
        except ValueError:
            ...
