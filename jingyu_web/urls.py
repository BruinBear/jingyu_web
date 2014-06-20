from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jingyu_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Static pages
    url(r'^$', include('hello.urls')),
    url(r'^about$', TemplateView.as_view(template_name='hello/about.html'), name='about'),
    url(r'^work$', TemplateView.as_view(template_name='hello/work.html'), name='work'),
    url(r'^blog$', TemplateView.as_view(template_name='hello/blog.html'), name='blog'),
    url(r'^contact$', TemplateView.as_view(template_name='hello/contact.html'), name='contact'),
    

    # Admin site
    url(r'^admin/', include(admin.site.urls)),
)
