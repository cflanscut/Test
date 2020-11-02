import random

a = 123
b = "Lanchaofan"
print("Lanchaofan"[3])
str(a)
print(a)

c = (1, 2, 3, 4)
d = [a, b, c]

len(d)

d.append("ssy")

for string1 in d:
    print(string1)


def get_int(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
            print(err)


# age = get_int("ennter your age:")

x = random.randint(1, 6)
y = random.choice(["apple", "banana", "cherry", "durian"])
