from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from .models import Order, Cart
import telegram

bot = telegram.Bot(token='1998336097:AAHgwopnSqcXCYijJ1CbbYWrDMVKQHFjuz4')


@receiver(post_save, sender=Order)
def post_save_product(sender, instance, **kwargs):
    text = ''
    buy = 0
    for i in Cart.objects.all():
        text += f'{i.product.name} --{i.quantity} ta --{i.quantity * i.product.price} so\'m\n'
        buy += i.quantity * i.product.price
    buy = str(buy)
    bot.send_message('@onlin_bozor_m', text=
    f'\nBuyurtmachi: {instance.user}\nManzil:{instance.address}\nNomer:{instance.user.phone} \nStatusi:{instance.status}\n nomi:-- soni--narx:\n'+text+'umumiy narx:'+buy)
