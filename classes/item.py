from classes.action import Action


class Item:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        try:
            self.collectible = kwargs['collectible']
        except KeyError:
            self.collectible = False
        try:
            self.starts_in_inventory = kwargs['starts_in_inventory']
        except KeyError:
            self.starts_in_inventory = False
        try:
            self.hidden = kwargs['hidden']
        except KeyError:
            self.hidden = False
        self.description = kwargs['description']

        try:
            self.actions = [Action(**action) for action in kwargs['actions']]
        except KeyError:
            self.actions = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
