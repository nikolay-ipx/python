def parse_json(data) -> str:
    match data:
        case {'data': dat, 'access': True} if type(dat[1]['login']) == str and type(dat[1]['email']) == str:
            return (dat[1]['login'],dat[1]['email'])

        case {'id': ids, 'data': [_, {'login': login}, _, _]}:
            print('222')
            return ids, login

    return None

json_data = {'id': 2, 'access': True,
            'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'},
            2000, 56.4]}
print(parse_json(json_data))