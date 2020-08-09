from rest_auth.views import LoginView


class CustomAuth(LoginView):
    def get_response(self):
        orginal_response = super().get_response()
        return orginal_response
