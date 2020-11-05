from django import template

register = template.Library()

'''
return the attr value of the object
'''
@register.filter
def get_object_value(dictionary, item):
    items = item.split('__')
    if len(items) == 1:
        return getattr(dictionary, item)
    if len(items) == 2:
        return getattr(
            getattr(dictionary, items[0]), 
            items[1]
        )
    #geater than 2? you m**th f**k
    if len(items) > 2:
        ans = dictionary
        for attr in items:
            ans = getattr(ans, attr)
        return ans