def get_data(value):
    match value:
        case int():
            return value
        case float():
            return value
        case str():
            return value

    return None
print(get_data(2))