class Action:
    def __init__(self, **kwargs):
        self.target = kwargs['target']
        self.result = kwargs['result']
        try:
            self.show_hidden_item_names = kwargs['show_hidden_item']
        except KeyError:
            self.show_hidden_item_names = None
        try:
            self.new_event_name = kwargs['new_event']
        except KeyError:
            self.new_event_name = None
        try:
            self.destroy_item_names = kwargs['destroy_item']
        except KeyError:
            self.destroy_item_names = None
