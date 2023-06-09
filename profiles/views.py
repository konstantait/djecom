from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, UpdateView
from django.urls import reverse_lazy

from profiles.forms import PhoneVerificationForm, ProfileForm
from profiles.utils import store_key_hash_in_session, verify_key_hash_from_session # noqa
from profiles.models import User


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'profiles/update.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profiles:logout')

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])

    def form_valid(self, form):
        if 'phone' in form.changed_data:
            phone = form.cleaned_data['phone']
            store_key_hash_in_session(self.request.session, phone)
            User.objects.filter(id=self.kwargs['pk']).update(is_phone_valid=False) # noqa
            self.success_url = reverse_lazy('profiles:verification')
        return super().form_valid(form)


class PhoneVerificationView(FormView):
    template_name = "profiles/verification.html"
    form_class = PhoneVerificationForm
    success_url = reverse_lazy('profiles:logout')

    def form_valid(self, form):
        phone = verify_key_hash_from_session(self.request.session, form.cleaned_data['secret_key']) # noqa
        if phone:
            User.objects.filter(phone=phone).update(is_phone_valid=True)
        else:
            messages.error(self.request, 'Invalid code or timed out. Code has been sent again!') # noqa
            store_key_hash_in_session(self.request.session)
            self.success_url = reverse_lazy('profiles:verification')
        return super().form_valid(form)
