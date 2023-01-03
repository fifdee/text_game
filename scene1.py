VALUES = {
    'nr': 1,
    'name': 'Pomieszczenie na szczycie wieży',
    'description': 'Wbiegłeś tak szybko, jak to możliwe do pomieszczenia na samym szczycie wieży. Dyszysz bez '
                   'opamiętania, ale przynajmniej zostawiłeś w tyle tych zbirów. Nie masz wiele czasu, słyszysz jak '
                   'zaczynają wbiegać po schodach...',
    'items':
        [
            {
                'name': 'pałka',
                'collectible': True,
                'description': 'Gruba, dębowa pałka.',
                'actions': [
                    {
                        'target': 'szklana kula',
                        'result': 'zbiłeś szklaną kulę, w środku znalazłeś klucz',
                        'show_hidden_item': 'klucz',
                        'destroy_item': 'szklana kula',
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
                        'result': 'klucz pasuje, otworzyłeś drzwi i przechodzisz dalej',
                        'new_event': 'next_scene',
                        'destroy_item': 'klucz',
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
