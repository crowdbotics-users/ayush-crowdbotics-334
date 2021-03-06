from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'satchless', 'url': 'http://pypi.python.org/pypi/satchless/1.1.3'},
	{'name':'django-tastypie', 'url': 'http://pypi.python.org/pypi/django-tastypie/0.14.0'},
	{'name':'django-app-metrics', 'url': 'http://pypi.python.org/pypi/django-app-metrics/0.9.0'},
	{'name':'django-experiments', 'url': 'http://pypi.python.org/pypi/django-experiments/1.2.0'},
	{'name':'django-request', 'url': 'http://pypi.python.org/pypi/django-request/1.5.4'},
	{'name':'django-trackstats', 'url': 'http://pypi.python.org/pypi/django-trackstats/0.5.0'},
	{'name':'django-analytical', 'url': 'http://pypi.python.org/pypi/django-analytical/2.4.0'},
	{'name':'djangorestframework', 'url': 'http://pypi.python.org/pypi/djangorestframework/3.7.7'},
	{'name':'django-bootstrap4', 'url': 'http://pypi.python.org/pypi/django-bootstrap4/0.0.5'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
