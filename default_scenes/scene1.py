VALUES = {
    'nr': 1,
    'name': 'Pomieszczenie na szczycie wieży',
    'beginning': 'Wbiegłeś tak szybko, jak to możliwe do pomieszczenia na samym szczycie wieży. Dyszysz bez '
                 'opamiętania, ale przynajmniej zostawiłeś w tyle tych zbirów. Nie masz wiele czasu, słyszysz jak '
                 'zaczynają wbiegać po schodach...',
    'description': 'Niewielkie pomieszczenie na szczycie wieży, przysypane sporą warstwą kurzu.',
    'items':
        [
            {
                'name': 'pałka',
                'collectible': True,
                'description': 'Gruba, dębowa pałka.',
                'actions': [
                    {
                        'target': 'szklana kula',
                        'result': 'Zbiłeś szklaną kulę, zauważasz, że w środku był klucz.',
                        'show_hidden_item': ['klucz'],
                        'destroy_item': ['szklana kula'],
                    }
                ]
            },
            {
                'name': 'klucz',
                'collectible': True,
                'hidden': True,
                'description': 'Pozłacany klucz ze zdobieniami.',
                'actions': [
                    {
                        'target': 'drzwi',
                        'result': 'Klucz pasuje, otworzyłeś drzwi i przechodzisz dalej.',
                        'new_event': 'next_scene',
                        'destroy_item': ['klucz', 'drzwi'],
                    }
                ]
            },
            {
                'name': 'drzwi',
                'description': 'Solidne drzwi zamknięte na klucz.'
            },
            {
                'name': 'szklana kula',
                'description': 'Duża, szklana kula. Zbyt ciężka by ją podnieść.'
            },
        ],
}
