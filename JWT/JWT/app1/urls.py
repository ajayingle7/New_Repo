from django.urls import path
from .views import EmployeeDetail,EmployeeInfo


urlpatterns =[

    path("emp/", EmployeeDetail.as_view()),
    path("emp/<int:id>/", EmployeeInfo.as_view())


]