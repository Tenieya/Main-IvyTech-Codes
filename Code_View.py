class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

user1 = User("Alice", "Johnson")
user2 = User("Bob", "Smith")
user3 = User("Charlie", "Brown")
user4 = User("Diana", "Prince")
user5 = User("Ethan", "Hunt")

users = [user1, user2, user3, user4, user5]

for user in users:
    user.describe_user()
    user.greet_user()
