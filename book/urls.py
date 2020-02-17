from django.urls import path
from .views import ReferBookView

urlpatterns = [
    path('books/', ReferBookView.as_view(), name='books')
]
