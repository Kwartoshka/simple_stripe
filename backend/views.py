from django.shortcuts import render
import stripe
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"



from django.http import HttpResponse, JsonResponse
import datetime
from backend.models import Item

def buy(request, id):

    item = Item.objects.filter(id=id).first()
    now = datetime.datetime.now()
    session = stripe.checkout.Session.create(
          success_url="https://yandex.ru",
          cancel_url="https://google.com",
            line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount_decimal': item.price * 100,
            },
            'quantity': 1,
        }],
          mode="payment",
        )
    # html = f"<html><body>stripe id is {session.id}</body></html>"
    # return HttpResponse(html)
    return JsonResponse({'sessionId': session.id})

def item(request, id):

    item = Item.objects.filter(id=id).first()
    from django.shortcuts import render

    context = {
        'id': item.id,
        'name': item.name,
        'description': item.description,
        'price': item.price,
    }
    return render(request, 'a.html', context)


# class
# stripe.checkout.Session.create(
#   success_url="https://example.com/success",
#   cancel_url="https://example.com/cancel",
#   line_items=[
#     {
#       "price": "price_H5ggYwtDq4fbrJ",
#       "quantity": 2,
#     },
#   ],
#   mode="payment",
# )
# Create your views here.
'''
    GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item.
    При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос
    stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
    GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
    Пример реализации можно посмотреть в пунктах 1-3 тут

    Залить решение на Github, описать запуск в Readme.md'''