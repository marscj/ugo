default_app_config = 'app.authorization.apps.AuthorizationConfig'

class UserType:
    Customer = 1
    Staff = 2

    CHOISE = [
        (Customer, '用户'),
        (Staff, '员工'),
    ]
