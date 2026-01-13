
"""Problem statement
Build a system that creates and manages users in three ways:
Guest user
Registered user
User created from stored data

Every user has username, email, role, is_active

Guest users have default values

Registered users must pass data

Data-based creation must use a class method

Constructor must not contain business logic

Follow Single Responsibility and Dependency Inversion lightly

"""



class User:
    def __init__(self,username , email ,role = "Guest", is_active = True):
        self.username = username
        self.email = email 
        self.role = role 
        self.is_active = is_active

    @classmethod
    def guest(cls):
        return cls("guest" ,"guest@gmail.com")
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data.get("username"),
            email=data.get("email"),
            role=data.get("role", "Registered"),
            is_active=data.get("is_active", True)
        )
    
    def deactive_user(self):
        self.is_active = False
class UserManager:
    def __init__(self, users=None):
        self.users = users if users else []

    def add_user(self, user):
        self.users.append(user)

    def list_active_users(self):
        return [u for u in self.users if u.is_active]


# Example usage
# user input valdiation can be added as neede
# Create users
guest_user = User.guest()
registered_user = User("john_doe", "john@example.com", "Registered")
dict_user = User.from_dict({"username": "alice", "email": "alice@example.com", "role": "Admin"})

# Initialize manager and add users
manager = UserManager()
manager.add_user(guest_user)
manager.add_user(registered_user)
manager.add_user(dict_user)

# Display active users
print("Active users:")
for user in manager.list_active_users():
    print(f"  {user.username} ({user.email}) - Role: {user.role}")

# Deactivate a user
registered_user.deactive_user()
print(f"\nAfter deactivating {registered_user.username}:")
for user in manager.list_active_users():
    print(f"  {user.username} ({user.email})")

# Output:
# Active users:
#   guest (guest@gmail.com) - Role: Guest
#   john_doe (john@example.com) - Role: Registered
#   alice (alice@example.com) - Role: Admin

# After deactivating john_doe:
#   guest (guest@gmail.com) - Role: Guest
#   alice (alice@example.com) - Role: Admin

# Note: The UserManager class is used to manage the users and provides methods to add users and list active users. The User class is used to create user objects with attributes such as username, email, role, and is_active. The class also provides class methods to create guest users and users from dictionaries. The deactive_user method is used to deactivate a user.