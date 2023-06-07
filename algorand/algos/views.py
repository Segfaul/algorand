from io import BytesIO
import base64

from django.contrib.auth import logout, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, CreateView
import numpy as np
import matplotlib.pyplot as plt

from .algo_dir.algo import *
from .forms import LoginUserForm, RegisterUserForm


class PlotAlgorithmPerformanceView(UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_authenticated

    def get(self, request):

        sizes = [500_000, 2_000_000, 5_000_000, 10_000_000]
        data = []
        for size in sizes:
            # data.append(np.random.randint(low=0, high=100, size=size))
            data.append(np.unique(np.arange(size)))

        times_algorithm = {
            'interpolation_search': [],
            'fibonacci_search': [],
            'binary_search': []
        }

        for arr in data:
            arr.sort()
            print(arr)
            search_value = arr[0]
            times_algorithm['interpolation_search'].append(
                measure_execution_time(interpolation_search, arr, search_value)
            )
            times_algorithm['fibonacci_search'].append(
                measure_execution_time(fibonacci_search, arr, search_value)
            )
            times_algorithm['binary_search'].append(
                measure_execution_time(binary_search, arr, search_value)
            )

        plt.clf()

        plt.figure(figsize=(20, 12))

        plt.plot(
            sizes,
            times_algorithm['interpolation_search'],
            label='interpolation_search',
            linestyle='-',
            color='blue'
        )
        plt.plot(
            sizes,
            times_algorithm['fibonacci_search'],
            label='fibonacci_search',
            linestyle='--',
            color='green'
        )
        plt.plot(
            sizes,
            times_algorithm['binary_search'],
            label='binary_search',
            linestyle=':',
            color='red'
        )
        plt.xlabel('Array Size')
        plt.ylabel('Execution Time')
        plt.title('Algorithm Performance')
        plt.legend()

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()

        return render(request, 'algos/algos.html', {'graphic': image_base64})


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

