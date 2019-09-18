from collections import namedtuple

individual= namedtuple("individual", "name age height")
user = individual(name="homer", age=37, height=178)
print(user)
print(user.name)


