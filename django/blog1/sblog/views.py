# Create your views here.
from django.shortcuts import render_to_response
from sblog.models import Blog
from django.http import Http404
from sblog.models import Tag
def blog_list(request):
    blogs=Blog.objects.all()
    return render_to_response("blog_list.html",{"blogs":blogs})
def blog_show(request,id=''):
    try:
        blog=Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html",{"blog":blog})
def blog_filter(request, id=''):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=id)
    blogs = tag.blog_set.all()
    return render_to_response("blog_filter.html",{"blogs": blogs, "tag": tag, "tags": tags})
def blog_list1(request):
    
    return render_to_response("blog_list1.html")