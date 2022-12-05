from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *

# Create your views here.


def index(request, *args, **kwargs):
    index_file = open('./static/index.html').read()
    return HttpResponse(index_file)


class ProductsAPIView(APIView):
    serializer_class = ProductsSerializer

    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)

        return Response(serializer.data)


class UserAPIView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        email = request.query_params["email"]
        password = request.query_params["password"]

        if email != None:
            user = User.objects.get(email=email).__dict__

            if password != user['password']:
                response = 'Wrong Password'

                return Response(response)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self, request):
        data = request.data

        user_email = data['params']['email']
        user_password = data['params']['password']

        new_user = User.objects.create(
            email=user_email, password=user_password)

        new_user.save()

        serializer = UserSerializer(new_user)

        return Response(serializer.data)


class ShoppingCartAPIView(APIView):
    serializer_class = ShoppingCartSerializer

    def get(self, request):
        items = ShoppingCart.objects.all()
        serializer = ShoppingCartSerializer(items, many=True)

        return Response(serializer.data)

    # def post(self, request):
    #     data = request.data

    #     user_email = data['params']['email']
    #     user_password = data['params']['password']

    #     new_user = User.objects.create(
    #         email=user_email, password=user_password)

    #     new_user.save()

    #     serializer = UserSerializer(new_user)

    #     return Response(serializer.data)
