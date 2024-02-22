from django import template
from cart.models import CartItem


register = template.Library()


@register.simple_tag(takes_context=True)
def cart_item_count(context):
    request = context['request']
    user = request.user
    count = CartItem.objects.filter(user=user).count()
    return count
