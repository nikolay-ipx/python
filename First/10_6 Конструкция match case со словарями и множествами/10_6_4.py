def parse_json(data):
    match data:
        case {'access': bool() as acce, 'data': list() as dat}:
            return (acce, dat[0])

        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            return ids, login

    return None

json_data = {'id': 2, 'access': False,
            'data': ['26.05.2023',
            {'login': '1234', 'email': 'xxx@mail.com'},
            2000, 56.4]}
print(parse_json(json_data))