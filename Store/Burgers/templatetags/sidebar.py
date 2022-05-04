from django import template
from Burgers.models import Post, Tag

register = template.Library()

@register.inclusion_tag('Burgers/popular_post_tpl.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts':posts}