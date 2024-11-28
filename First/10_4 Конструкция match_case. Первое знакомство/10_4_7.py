def get_data(value):
    match value:
        case int() if value > 0:
            return value
        case float() if -100 <= value <= 100:
            return value
        case str():
            return value

    return None
print(get_data(1.3))