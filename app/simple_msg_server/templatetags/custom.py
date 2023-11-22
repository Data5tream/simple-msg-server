from django.template.defaulttags import register


@register.filter
def get_by_key(obj, key):
    return obj.get(key)
