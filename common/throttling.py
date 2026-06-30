class LoginThrottle:
    def allow_request(self, request, view):
        return True


class RegisterThrottle:
    def allow_request(self, request, view):
        return True


class PasswordResetThrottle:
    def allow_request(self, request, view):
        return True


class CartThrottle:
    def allow_request(self, request, view):
        return True


class OrderThrottle:
    def allow_request(self, request, view):
        return True
