# put your python code here
from string import ascii_lowercase
counter = 0
while counter < 50:
    for i in ascii_lowercase:
        if counter >= 50:
            break

        generator = (j for j in ascii_lowercase)
        for j in generator:
            if counter >= 50:
                break

            print(i + j, end=" ")
            counter += 1