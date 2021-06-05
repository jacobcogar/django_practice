from challenges.views import monthly_challenge_by_number
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'), # /challenges/ view is triggered
    path('<int:month>', views.monthly_challenge_by_number), # can program different logic based on input and whether they are ints or strings.
    path('<str:month>', views.monthly_challenge, name='month-challenge') # using a dynamic path segment.
]
