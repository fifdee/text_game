from classes.Item import Item


class Scene:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.nr = kwargs['nr']
        self.beginning = kwargs['beginning']
        self.description = kwargs['description']

        self.items = [Item(**item) for item in kwargs['items']]

    def remove_item(self, item):
        try:
            self.items.remove(item)
        except ValueError:
            ...

    def show_beginning_text(self):
        print('--------------------------------------')
        print(self.beginning)

    def describe(self):
        print(self.description)
        print('Przedmioty, które widzisz dookoła:')
        if len(self.items) > 0:
            for item in self.items:
                if not item.hidden:
                    print(item.description)
        else:
            print('Nic szczególnego.')

    def tell_items_names(self):
        for item in self.items:
            if not item.hidden:
                print(item.name, end=', ')
        print()

    def __str__(self):
        return self.name
