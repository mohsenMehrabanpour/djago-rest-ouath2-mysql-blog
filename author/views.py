from typing import FrozenSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from author.models import Author
from django.contrib.auth import get_user_model
from author.serializers import AuthorSerializer
from rest_framework.parsers import JSONParser

User = get_user_model()


class profile(APIView):
    permission_classes = (IsAuthenticated, )
    parser_classes = (JSONParser, )

    def get(self, request):

        author = Author.objects.get(user_id=request.user.id)
        data = {
            'first_name': author.user.first_name,
            'last_name': author.user.last_name,
            'phone_number': author.phone_number,
            'email': author.user.email,
            'last_login':
            author.user.last_login.strftime('%a - %d/%b/%Y - %H:%M')
        }
        return Response(data)

    def put(self, request):
        author = Author.objects.get(user_id=request.user.id)
        author_user = User.objects.get(id= request.user.id)
        if request.data.get('first_name') is not None:
            author_user.first_name = request.data['first_name']
        if request.data.get('last_name') is not None:
            author_user.last_name = request.data['last_name']
        if request.data.get('email') is not None:
            author_user.email = request.data['email']
        if request.data.get('phone_number') is not None:
            author.phone_number = request.data['phone_number']
        author.save()
        author_user.save()
        data = {
            'first_name': author_user.first_name,
            'last_name': author_user.last_name,
            'phone_number': author.phone_number,
            'email': author_user.email,
            'last_login':
            author.user.last_login.strftime('%a - %d/%b/%Y - %H:%M')
        }
        return Response(data)
