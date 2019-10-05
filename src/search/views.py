from django.shortcuts import render
from blog.models import Post
from .models import SearchQuery
from django.db.models import Q
import datetime

def search_view(request):
    query = request.GET.get('q', None)
    template_name = 'search/search_view.html'
    user = None
    if request.user.is_authenticated:
        user = request.user
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        posts = Post.objects.filter(Q(publish_status='publish'), Q(post_title__icontains=query) | Q(post_description__icontains=query))
    now = datetime.datetime.now()
    context = {'query': query, 'posts':posts, 'now': now}

    return render(request, template_name, context)