class PersonEx:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("This player have just run")



ivan = PersonEx("IvanOrso", 23)

print(ivan.run())