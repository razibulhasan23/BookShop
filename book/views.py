from rest_framework import status
from rest_framework.response import Response

from .models import ReferBook, ReferPages
from .Serializers import ReferBookSerializer
from rest_framework.views import APIView


class ReferBookView(APIView):
    @staticmethod
    def get(request):
        books = ReferBook.objects.all().prefetch_related('refer_books')
        serializers = ReferBookSerializer(books, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)