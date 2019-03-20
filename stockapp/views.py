from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .models import APISettings
from .forms import SignUpForm


class SignUp(generic.CreateView):
    # form_class = UserCreationForm
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tests'] = {'var1': "56", 'var2': "89"}
        return context


@method_decorator(login_required, name='dispatch')
class SettingsList(ListView):
    model = APISettings

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['settings'] = APISettings.objects.all()
        return context


@method_decorator(login_required(), name='dispatch')
class ApiSettingsCreate(CreateView):
    model = APISettings
    fields = ['api_name', 'api_key', 'api_username', 'api_password', 'api_endpoint']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('stock_app:settings')


@method_decorator(login_required, name='dispatch')
class UploadData(TemplateView):
    template_name = 'home/upload.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tests'] = {'var1': "56", 'var2': "89"}
        return context
