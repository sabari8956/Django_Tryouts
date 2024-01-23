from allauth.account.forms import SignupForm
class MyCustomSignupForm(SignupForm):

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)
        print(user)
        # Add your own processing here.

        # You must return the original result.
        return user
    
from allauth.account.forms import LoginForm
class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):

        # Add your own processing here.
        print(*args, **kwargs)
        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)

