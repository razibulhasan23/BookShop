from rest_framework import serializers
from .models import ReferPages, ReferBook


class ReferPagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReferPages
        fields = '__all__'


class ReferBookSerializer(serializers.ModelSerializer):
    refer_books = ReferPagesSerializer(many=True)

    class Meta:
        model = ReferBook
        fields = ['id', 'isbn', 'title', 'refer_books']