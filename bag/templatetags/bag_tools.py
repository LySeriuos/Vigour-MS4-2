from django import template


# to register this filter create a variable called register
register = template.Library()

# the register filter decorator to register our function as a template filter
# https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity