from django.contrib import admin
from django.urls import path
from currency_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('converter/',views.covert_currrency),
    path('liverate/',views.live_exchange_rates),
    path('history/',views.conversion_history),
]
