from rest_framework import serializers
from items.models import Item, FavoriteItem

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'first_name', 'last_name']

class ListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name='item-detail',
		lookup_field= 'id',
		lookup_url_kwarg= 'item_id',
		)
	added_by = UserSerializer()
	favorited = serializers.SerializerMethodField()
	class Meta:
		model = Item
		fields = ['id','image','name','description', 'detail','added_by', 'favorited']
	def get_favorited(self, obj):
		return obj.favoriteitem_set.all().count() #test this

class DetailSerializer(serializers.ModelSerializer):
	list_of_favs = serializers.SerializerMethodField()
	class Meta:
		model = Item
		fields = ['id', 'image','name','description', 'list_of_favs']

	def get_list_of_favs(self, obj):
		objs = obj.favoriteitem_set.all()
		# print(objs)
		users = []
		for fave in objs:
			usres.append(face.user)
		return UserSerializer(users, many=True).data


