from django.conf import settings
from django.views.generic import CreateView

from .forms import UserRegistrationForm


User = settings.AUTH_USER_MODEL


class UserRegistration(CreateView):
    """User Registration View."""
    model = User
    form_class = UserRegistrationForm
    template_name = 'registration/sign-up.html'
