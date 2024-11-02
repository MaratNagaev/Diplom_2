from generators import *


class IngredientsData:
    burger_1 = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6c',
                '61c0c5a71d1f82001bdaaa77', '61c0c5a71d1f82001bdaaa78']

    burger_2 = ['61c0c5a71d1f82001bdaaa75', '61c0c5a71d1f82001bdaaa6d',
                '61c0c5a71d1f82001bdaaa7a', '61c0c5a71d1f82001bdaaa6e']

    invalid_hash_ingredient = '61c0c5a71d1f1234567890112'


class DataUser:
    username = 'Marat'
    email = 'marat_nagaev_13_111@yandex.ru'
    password = 'yandex1'
    creds_with_empty_fields = [
        {'email': '',
         'password': create_random_password(),
         'name': create_random_name()
         },
        {'email': create_random_email(),
         'password': '',
         'name': create_random_name()
         },
        {'email': create_random_email(),
         'password': create_random_password(),
         'name': ''
         }
    ]
