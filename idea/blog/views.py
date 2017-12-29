from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.template.loader import render_to_string
from .models import Blog, BlogTag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# Create your views here.
class BlogView(DetailView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        blog = Blog.objects.get(slug=self.kwargs.get('slug'))
        blog_tags = blog.tags.all()
        recommended = Blog.objects.filter(tags__in=blog_tags).exclude(title=blog.title).distinct()
        print recommended
        context = super(BlogView, self).get_context_data(**kwargs)
        context['tags'] = blog_tags
        context['recommended'] = recommended
        return context



    
class BlogList(TemplateView):
    
    template_name = "blog/blog_list.html"

    def get_context_data(self, **kwargs):
        
        tags = BlogTag.objects.all()
        print tags
        
        try:
            tag = self.request.GET['tag']
        except:
            tag = None

        if self.request.method == 'GET' and tag:
            #tag = self.request.GET['tag']
            blogs = Blog.objects.filter(tags__in = tag)
        else:
            blogs = Blog.objects.all()

        #blogs = Blog.objects.all()
        paginator = Paginator(blogs, 16)
        page = self.request.GET.get('page')
        blogs = paginator.page(1)
        print blogs.paginator.page_range

        if page:
           # blogs = Blog.objects.all()
            paginator = Paginator(blogs, 16)
            page = self.request.GET.get('page')
            blogs = paginator.page(page)
            #print page

        #print dir(Paginator.num_pages)
        context = super(BlogList, self).get_context_data(**kwargs)
        context['blogs'] = blogs
        context['tags'] = tags
        return context

