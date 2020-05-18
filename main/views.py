from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import (
    TemplateView, FormView, ListView, UpdateView
)
from django.utils.crypto import get_random_string

from django.http import HttpResponseRedirect

from .models import AppInfo, LoginPasswordInfo
from .forms import AppLoginPasswordForm, LoginPasswordForm

# Create your views here.

class MainIndexView(ListView):
    template_name = 'main/index.html'
    queryset = AppInfo.objects.all()
    context_object_name = 'appsinfo'


class LoginPasswordView(ListView):
    template_name = 'main/logins_passwords.html'
    context_object_name = 'loginpasswords'

    def get_queryset(self):
        self.appinfo = AppInfo.objects.get(name_app=self.kwargs['appinfo'])
        return LoginPasswordInfo.objects.filter(appinfo=self.appinfo)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['current_app'] = self.appinfo
        return context


class AppLoginPasswordView(FormView):
    form_class = AppLoginPasswordForm
    template_name = 'main/add.html'
    success_url = '/'

    def get_form_kwargs(self):
        user = self.request.user
        form_kwargs = super().get_form_kwargs()
        form_kwargs['user'] = user
        return form_kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# Переписать на класс, вероятно лучше в js
def loginpasswordedit(request, id_l):
    loginpassword = LoginPasswordInfo.objects.get(id=id_l)
    if request.method != 'POST':
        form = LoginPasswordForm(instance=loginpassword)
    else:
        form = LoginPasswordForm(instance=loginpassword, data=request.POST)
        if 'cancel' in request.POST:
            login = request.POST['login']
            form.data = {'login': login, 'password': get_random_string()} # - работает
        else:  
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('main:index'))
    context = {'loginpassword': loginpassword, 'form': form}
    return render(request, 'main/update.html', context)