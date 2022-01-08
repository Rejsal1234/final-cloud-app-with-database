from django.template.defaulttags import register

@register.filter
def get_key(dictionary, key):
    return dictionary.get(key)