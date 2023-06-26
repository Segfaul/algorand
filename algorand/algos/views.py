from django.contrib.auth import logout, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView, TemplateView, FormView

from .algo_dir.algo import *
from .forms import *


class PlotAlgorithmPerformanceView(UserPassesTestMixin, TemplateView):
    template_name = 'algos/algos.html'
    login_url = reverse_lazy('plot_algorithm_performance')

    raise_exception = True

    def test_func(self):
        return self.request.user.is_authenticated


class ArraySearchView(UserPassesTestMixin, FormView):
    template_name = 'algos/input_arr.html'
    form_class = ArraySearchForm
    raise_exception = True

    def test_func(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        array = form.cleaned_data['array']
        target = form.cleaned_data['target']

        context = {
            'interpolation_search': measure_execution_time(interpolation_search, array, target),
            'fibonacci_search': measure_execution_time(fibonacci_search, array, target),
            'binary_search': measure_execution_time(binary_search, array, target)
        }

        return render(self.request, 'algos/input_arr_results.html', {'context': context})


class RegisterUserView(UserPassesTestMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'algos/auth/register.html'
    success_url = reverse_lazy('login')

    def test_func(self):
        return not self.request.user.is_authenticated

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('plot_algorithm_performance')


class LoginUserView(UserPassesTestMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'algos/auth/login.html'

    def test_func(self):
        return not self.request.user.is_authenticated

    def get_success_url(self):
        return reverse_lazy('plot_algorithm_performance')


def logout_user(request):
    logout(request)
    return redirect('login')


def tr_handler404(request, exception):
    """
    404 Error handler
    """
    return render(request=request, template_name='algos/exceptions/error_page.html', status=404, context={
        'title': 'Page not found: 404',
        'error_message': 'Unfortunately, such a page was not found, or was moved',
    })


def tr_handler500(request):
    """
    500 Error handler
    """
    return render(request=request, template_name='algos/exceptions/error_page.html', status=500, context={
        'title': 'Server error: 500',
        'error_message': 'Internal site error, go back to the home page, '
                         'we will send an error report to the site administration',
    })


def tr_handler403(request, exception):
    """
    403 Error handler
    """
    if request.user.is_authenticated:
        return redirect('plot_algorithm_performance')
    else:
        return redirect('login')
    # return render(request=request, template_name='posts/exceptions/error_page.html', status=403, context={
    #     'title': 'Access error: 403',
    #     'error_message': 'Access to this page is restricted',
    # })


def tr_handler405(request, exception):
    """
    405 Error handler
    """
    if request.user.is_authenticated:
        return redirect('plot_algorithm_performance')
    else:
        return redirect('login')

