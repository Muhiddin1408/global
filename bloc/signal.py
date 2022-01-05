from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from .models import Product
import telegram

bot = telegram.Bot(token='1998336097:AAHgwopnSqcXCYijJ1CbbYWrDMVKQHFjuz4')


@receiver(pre_save, sender=Product)
def post_save_product(sender, instance, **kwargs):
    print('ghhb', sender)

    bot.send_message(chat_id='990254417', text=f'product: {instance.name}')
