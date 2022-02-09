from django.shortcuts import render
from rest_framework.generics import  ListAPIView
from rest_framework.response import Response
from .serializers import *
from api.models import keyword
# Create your views here.


class search_ApiView(ListAPIView):
    serializer_class = keyword_Serializer

    def get_queryset(self):
        try:
            searchText=self.request.query_params.get('search', None)
            title = self.request.query_params.get('title', None)
            user_name = self.request.query_params.get('user', None)
            time = self.request.query_params.get('time', None)
            
            queryset = keyword.objects.filter().order_by()
            print(str(title))
            print(searchText)
            if searchText:
                try:
                    queryset = queryset.filter(title__icontains=str(searchText))
                except Exception as e:
                    queryset = []
            if title:
                try:
                    queryset = queryset.filter(title=title)
                except Exception as e:
                    queryset = []
            if user_name:
                try:
                    queryset = queryset.filter(user_name=user_name)
                except Exception as e:
                    queryset = []
            if time:
                try:
                    queryset = queryset.filter(app_date_tiem=time)
                except Exception as e:
                    queryset = []
            return queryset
        except Exception as e:
            content = {
            'error': str(e)}
            print(content)