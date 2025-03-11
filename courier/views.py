from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Courier
from .serializers import CourierSerializer


class CourierList(generics.ListCreateAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

    def delete(self, request, *args, **kwargs):
        Courier.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourierRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
    lookup_field = "pk"