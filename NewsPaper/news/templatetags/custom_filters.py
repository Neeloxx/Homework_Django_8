from django import template


register = template.Library()


CENSORED_WORDS = ['редиска']


@register.filter(name='censor')
def censor(text):
    for word in CENSORED_WORDS:
        if word in text:
            text = text.replace(word[1:len(word)], f'{len(word) * "*"}')
            return text
        else:
            return text