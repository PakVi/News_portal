from django import template


register = template.Library()


@register.filter()
def censor(value):
   words = ['хуета', 'суета', 'визажистка']

   for word in value.split():
      if word.lower() in words:
         value = value.replace(word, f'{word[0]}{"*" * (len(word)-1)}')
   return value