from django.urls import path
from hello import views

urlpatterns=[
    path('sh/',views.show,name='s-view'),
    path('sc/',views.school,name='sc-view'),
    path('con/',views.contact,name='con-view'),
]