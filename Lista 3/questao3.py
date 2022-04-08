class Auth:
    def __init__(self, *args, user, password, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.password = password

    def authenticate(self, user, password):
        return self.user == user and self.password == password


class Permission:
    def __init__(self, *args, role, **kwargs):
        super().__init__(*args, **kwargs)
        self.role = role

    def getPermission(self, role):
        return self.role == role


class AuthRole(Auth, Permission):
    def login(self):
        super().login()


print(AuthRole.mro())
user = AuthRole(user="jose", password="123", role=1)

print(user.authenticate(user="jose", password="123"))
print(user.getPermission(role=1))


