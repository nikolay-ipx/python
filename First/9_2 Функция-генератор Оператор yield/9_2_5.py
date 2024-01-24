def prime_numbers(quantity):
    counter = 0
    generator = (number for number in range(2, 1_001))
    while counter < quantity:
        guess = next(generator)
        flag = 'Balakirev'

        for i in range(2, guess):
            if guess % i == 0:
                flag = 'Sergey'
                break

        if flag == 'Balakirev':
            counter += 1
            yield guess


N = 20
print(*prime_numbers(N))