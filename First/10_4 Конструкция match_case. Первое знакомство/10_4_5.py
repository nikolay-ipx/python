cmd = input()

match cmd:
    case 'top' | 'Top' | 'TOP' :
        print(f"Команда top")
    case 'bottom' | 'Bottom' | 'BOTTOM':
        print(f"Команда bottom")
    case 'right' | 'Right' | 'RIGHT':
        print(f"Команда right")
    case 'left' | 'Left' | 'LEFT':
        print(f"Команда left")
    case _:
        print('Неверная команда')
