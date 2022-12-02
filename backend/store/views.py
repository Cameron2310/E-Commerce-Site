from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
import os

# Create your views here.
load_dotenv()


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


# def home(request):
#     data = products.all_data
#     categories = []
#     pictures = {'first_pic': data[0]['image_url'], 'second_pic': data[1]
#                 ['image_url'], 'third_pic': data[2]['image_url']}

#     for i in range(len(data)):
#         if data[i]['category'] not in categories:
#             categories.append(data[i]['category'])

#     return render(request, 'index.html', {'data': data, 'name_categories': categories, 'pictures': pictures})


# def category(request, category):
#     category_products = products.filter_products('category', category)

#     return render(request, 'category.html', {'category': category, 'category_products': category_products})


# def product(request, category, product_id):
#     data = shopping_cart.all_data
#     items_to_buy = []
#     product = products.filter_products('id', str(product_id))

#     for i in range(len(data)):
#         item = products.filter_products('id', data[i]['id'])
#         items_to_buy.append(item[0])
#         items_to_buy[i]['quantity'] = data[i]['quantity']

#     return render(request, 'product.html', {'product': product[0], 'items_to_buy': items_to_buy})


# def add_to_cart(request, category, product_id):
#     if request.method == 'POST':
#         if request.POST.get('quantity'):
#             quantity = request.POST.get('quantity')
#             items_in_cart = shopping_cart.all_data

#             if items_in_cart:
#                 for i in range(len(items_in_cart)):
#                     if items_in_cart[i]['id'] == str(product_id):
#                         new_quantity = str(
#                             int(items_in_cart[i]['quantity']) + int(quantity))
#                         shopping_cart.update_quantity(product_id, new_quantity)
#                         break

#                     elif items_in_cart[i]['id'] != str(product_id) and i == len(items_in_cart) - 1:
#                         shopping_cart.append_one_row_to_file(
#                             {'id': product_id, 'quantity': quantity})
#             else:
#                 shopping_cart.append_one_row_to_file(
#                     {'id': product_id, 'quantity': quantity})

#     return HttpResponseRedirect(reverse('products', args=[category, product_id]))


# def cart(request):
#     total_cost = 0
#     produce = products.all_data
#     items_cart = shopping_cart.all_data
#     list_items = []

#     for i in range(len(items_cart)):
#         list_items.append(shopping_cart.get_by_id(
#             produce, items_cart[i]['id']))
#         list_items[i]['quantity'] = items_cart[i]['quantity']
#         list_items[i]['sub_total'] = str(
#             int(list_items[i]['quantity']) * int(list_items[i]['cost']))
#         total_cost += int(list_items[i]['sub_total'])

#     return render(request, 'shopping_cart.html', {'items_cart': list_items, 'total_cost': total_cost})


# def search(request):
#     """ search function  """
#     if request.method == "POST":
#         query_name = request.POST.get('name')

#         if query_name:
#             results = products.filter_products('name', query_name)
#             if not results:
#                 unavailable_item = query_name
#                 auth = OAuth1(os.environ['api_key'], os.environ['secret_key'])
#                 endpoint = f"http://api.thenounproject.com/icon/{query_name}"
#                 response = requests.get(endpoint, auth=auth)
#                 response = response.json()

#                 url = response['icon']['preview_url']

#                 return render(request, 'search.html', {"unavailable": unavailable_item, 'item_url': url})

#             return HttpResponseRedirect(reverse('products', args=[results[0]['category'], int(results[0]['id'])]))


# def update_cart(request, product_id):
#     if request.method == 'POST':
#         if request.POST.get('quantity'):
#             quantity = request.POST.get('quantity')
#             if int(quantity) > 0:
#                 shopping_cart.update_quantity(product_id, quantity)
#             else:
#                 shopping_cart.delete_row(product_id)

#     return HttpResponseRedirect(reverse('shopping_cart'))
