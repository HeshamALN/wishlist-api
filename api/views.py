from django.shortcuts import render
from items.models import Item
from .serializers import ListSerializer, DetailSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .permissions import IsStaffOrOwner
# Create your views here.

from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated


class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ListSerializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter]
	search_fields = ['name']

class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = DetailSerializer
	permission_classes = [IsAuthenticated,IsStaffOrOwner]
	lookup_field= 'id'
	lookup_url_kwarg= 'item_id'
