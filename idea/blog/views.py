from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from .models import Blog, BlogTag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response,redirect
from info.models import Subscriber
import json




# Create your views here.
class BlogView(DetailView):
    model = Blog

    def get_queryset(self):
        return Blog.objects.filter(slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        blog = Blog.objects.get(slug=self.kwargs.get('slug'))
        blog_tags = blog.tags.all()
        recommended = Blog.objects.filter(subtitle_tag=blog.subtitle_tag).exclude(slug=self.kwargs.get('slug'))
        context = super(BlogView, self).get_context_data(**kwargs)
        detail = True

        if self.request.session.get(blog.title, False):
            voted = True
        else:
            voted = False

        context['voted'] = voted
        context['detail'] = detail
        context['tags'] = blog_tags
        context['recommended'] = recommended[:3]
        render(self.request,"includes/head.html",context)
        return context


def update_rating(request, slug):
    blog = Blog.objects.get(slug=slug)
    request.session[blog.title] = True
    if request.is_ajax():
        if request.method == 'POST':
            percent = request.POST.get('percent', '')
            print percent
            blog.votes = blog.votes + 1
            if int(percent) == 20:
                blog.rating = blog.rating + 1
            elif int(percent) == 40:
                blog.rating = blog.rating + 2
            elif int(percent) == 60:
                blog.rating = blog.rating + 3
            elif int(percent) == 80:
                blog.rating = blog.rating + 4
            elif int(percent) == 100:
                blog.rating = blog.rating + 5
            blog.save()
            return redirect('blog.views.BlogView', slug=slug)

class BlogList(TemplateView):

    template_name = "blog/blog_list.html"

    def get_context_data(self, **kwargs):

        tags = BlogTag.objects.all()
        seo_category = False
        print tags

        try:
            tag = self.request.GET['tag']
        except:
            tag = None


        try:
            page =  self.request.GET.get('page')
        except:
            page = None

        if self.request.method == 'GET' and tag:
            tag = BlogTag.objects.get(tag_en = tag)
            print tag.id
            blogs = Blog.objects.filter(tags__in = str(tag.id))
            seo_category = True
        else:
            blogs = Blog.objects.all()



        if page:
            paginator = Paginator(blogs, 12)
            blogs = paginator.page(page)
        else:
            paginator = Paginator(blogs, 12)
            blogs = paginator.page(1)

            # print page

        #print dir(Paginator.num_pages)
        context = super(BlogList, self).get_context_data(**kwargs)
        context['seo_category'] = seo_category
        context['tag'] = tag
        context['blogs'] = blogs
        context['tags'] = tags
        return context
