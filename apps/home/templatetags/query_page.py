from django import template
import urllib

register = template.Library()

'''
return the url with page and current query string.
'''
@register.simple_tag(takes_context=True, name='querypage')
def query_page(context, *args, **ops):
    query = context['request'].GET.copy()
    query['page'] = ops.get('page',1)
    return urllib.parse.urlencode(query)

'''
sample simple tag
return localtime with timezone
'''
'''
@register.simple_tag
def current_time(formmat_string):
    from django.utils import timezone
    now = timezone.now()
    now = timezone.localtime(now)
    return now.strftime(formmat_string)
'''