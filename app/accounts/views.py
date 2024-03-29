from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import RedirectView
from accounts.models import OnlineShopUser
from accounts.forms import SignUpForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class MyProfileView(DetailView):
    model = OnlineShopUser
    template_name = 'my-profile.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.request.user.id)
        return queryset


class SingUpView(CreateView):
    model = OnlineShopUser
    template_name = "sing_up.html"
    success_url = reverse_lazy("home-link")
    form_class = SignUpForm

    def form_valid(self, form):
        from django.contrib import messages
        messages.info(self.request, 'Thank for sign up! Please, check email')
        return super().form_valid(form)


class ActivateView(RedirectView):
    pattern_name = 'home-link'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop("username")
        user = get_object_or_404(OnlineShopUser, username=username, is_active=False)
        user.is_active = True
        from django.contrib import messages
        user.save(update_fields=('is_active',))
        messages.info(self.request, 'Your accaunts is activated')
        user.refresh_from_db()
        return super().get_redirect_url(*args, **kwargs)
