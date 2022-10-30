import requests
BASE_URL = 'https://fakestoreapi.com'

#Get Request
print("=============Get Request==============")
response = requests.get(f"{BASE_URL}/products")
print(response.json())
print("=============Status Of Request==============")
print(response.status_code)

#Post Request
print("=============Post Request==============")
new_product = {
    "title": 'test product',
    "price": 13.5,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}
response = requests.post(f"{BASE_URL}/products", json=new_product)
print(response.json())
print("=============Status Of Request==============")
print(response.status_code)