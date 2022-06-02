from rest_framework.response import Response
from rest_framework import generics
# from .models import *
from .serializers import *
from datetime import datetime
from django.shortcuts import render, redirect


def layout(request):
    context = {}
    return render(request, 'layout/base.html', context)


class CityListView(generics.ListAPIView):
    serializer_class = CitySerializers
    queryset = City.objects.all()

    def handle_exception(self, exc):
        return Response({'Data': 'Bad'}, status=400)


class StreetViewSet(generics.ListAPIView):
    serializer_class = StreetSerializers

    def get_queryset(self):
        queryset = Street.objects.all()
        city_id = self.kwargs['city_id']
        if city_id is not None:
            queryset = queryset.filter(city_id=city_id)
        return queryset

    def handle_exception(self, exc):
        return Response({'Data': 'Bad'}, status=400)


class ShopView(generics.ListAPIView):
    serializer_class = ShopSerializers

    # queryset = Shops.objects.all()

    def get_queryset(self):
        print(self.request.query_params)
        queryset = Shops.objects.all()

        city = self.request.query_params.get('city', None)
        if city is not None:
            queryset = queryset.filter(city=city)

        street = self.request.query_params.get('street', None)
        if street is not None:
            queryset = queryset.filter(street=street)
        isopen = self.request.query_params.get('open', None)
        if isopen is not None:
            dt = datetime.now().time()
            open_shops = queryset.filter(opening_time__lt=dt).filter(
                closing_time__gt=dt)
            if isopen == '1':
                queryset = open_shops
            elif isopen == '0':
                queryset = queryset.exclude(id__in=open_shops)

        return queryset

    def handle_exception(self, exc):
        return Response({'Data': 'Bad'}, status=400)


class ShopCreateView(generics.CreateAPIView):
    serializer_class = ShopSerializers

    def validate(self, data):
        errors = {}
        required_fields = ['name', 'city', 'street', 'number_home_shop', 'opening_time', 'closing_time']
        for field in required_fields:
            if field not in data:
                errors[field] = 'This field is required.'

        if errors:
            return serializers.ValidationError(errors)

    def handle_exception(self, exc):
        return Response({'Data': 'Bad'}, status=400)
