from django.urls import path
from . import views

urlpatterns = [
    path("courier/", views.CourierList.as_view(), name="courier-view-create"),
    path("courier/<int:pk>/",views.CourierRetrieveUpdateDestory.as_view(),name="update",),
]
