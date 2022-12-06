
from django.contrib import admin
from django.urls import path
from app.views import index, form, create, view, edit, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),

]
