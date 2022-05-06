from django import template
from Burgers.models import Post

register = template.Library()

@register.inclusion_tag('Burgers/pinned_tpl.html')
def show_pinned():
    posts = Post.objects.filter(is_pinned=True)
    return {'posts':posts}