from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from .models import Cart, User
import telegram

bot = telegram.Bot(token='1998336097:AAHgwopnSqcXCYijJ1CbbYWrDMVKQHFjuz4')


@receiver(post_save, sender=Cart)
def post_save_product(sender, instance, create, **kwargs):
    if create:
        Cart.objects.create(user=instance)
        print('sdsd')

    bot.send_message(chat_id='990254417', text=f'product: {instance.name}')
