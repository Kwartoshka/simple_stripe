from django.shortcuts import render
import stripe
import socket




from django.http import JsonResponse
from backend.models import Item

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
def buy(request, id):
    host = request.META['HTTP_HOST']
    print(host)
    # domain = 'localhost:8000'
    item = Item.objects.filter(id=id).first()
    session = stripe.checkout.Session.create(
          success_url=f'http://{host}/success/',
          cancel_url=f'http://{host}/fail/',
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
    return render(request, 'item.html', context)
