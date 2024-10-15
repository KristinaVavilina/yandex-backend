import requests

BASE_URL = 'https://fakestoreapi.com'

response_products = requests.get(f"{BASE_URL}/products")
response_categories = requests.get(f"{BASE_URL}/products/categories")
response_users = requests.get(f"{BASE_URL}/users")

products = response_products.json()
categories = response_categories.json()
users = response_users.json()

products_price = [product for product in products if product['price'] < 20]
products_category = [product for product in products if product['category'] == 'jewelery']

print(f'Продукты, цена которых < 20: {products_price}')
print(f'Все категории: {categories}')
print(f'Продукты с категорией "jewelery": {products_category}')
print(f'Все пользователи: {users}')

new_user = {
    "email": "mail@mail.ru",
    "username": "kavavilina",
    "name": {
        "firstname": "Kristina",
        "lastname": "Vavilina"
    }
}

response = requests.post(BASE_URL, json=new_user)
