VALUES = {
    'nr': 2,
    'name': 'Pokój za drzwiami',
    'beginning': 'Wchodzisz do ciemnego pokoju. Przedzierasz się przez pajęczyny ale nadal niewiele widać. '
                 'Dobrze, że zabrałeś ze sobą krzesiwo i pochodnię.',
    'description': 'Pokój za drzwiami. Jeszcze więcej kurzu i mnóstwo pajęczyn.',
    'items':
        [
            {
                'name': 'krzesiwo',
                'starts_in_inventory': True,
                'collectible': True,
                'description': 'Krzesiwo idealne do podpalania.',
                'actions': [
                    {
                        'target': 'pochodnia',
                        'result': 'Podpaliłeś pochodnię i dostrzegasz coś pośrodku pokoju.',
                        'show_hidden_item': ['płachta', 'płonąca pochodnia'],
                        'destroy_item': ['krzesiwo', 'pochodnia'],
                    }
                ]
            },
            {
                'name': 'pochodnia',
                'starts_in_inventory': True,
                'collectible': True,
                'description': 'Pochodnia, nadaje się do podpalenia.',
                'actions': [
                    {
                        'target': 'krzesiwo',
                        'result': 'Uderzasz pochodnią w krzesiwo ale nic to nie daje. '
                                  'Może powinieneś to zrobić odwrotnie?',
                    }
                ]
            },
            {
                'name': 'płonąca pochodnia',
                'starts_in_inventory': True,
                'hidden': True,
                'collectible': True,
                'description': 'Płonąca pochodnia, daje sporo światła i ciepła.',
                'actions': [
                    {
                        'target': 'płachta',
                        'result': 'Podpalasz płachtę i po kilku chwilach nie wierzysz własnym oczom. '
                                  'Aktywny portal - idealna okazja żeby stąd uciec! Ale gdzie on prowadzi? '
                                  'Tego nie wiesz, ale postanawiasz zaryzykować i przejść...',
                        'new_event': 'next_scene',
                    }
                ]
            },
            {
                'name': 'płachta',
                'collectible': False,
                'hidden': True,
                'description': 'Stara płachta skrywająca coś sporych rozmiarów. Nie nadaje się do zabrania.',
            },
        ],
}
