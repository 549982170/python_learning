from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'atcui.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # Django ATC API
    url(r'^api/v1/', include('atc_api.urls')),
    # Django ATC Demo UI
    url(r'^atc_demo_ui/', include('atc_demo_ui.urls')),
    # Django ATC profile storage
    url(r'^api/v1/profiles/', include('atc_profile_storage.urls')),
    url(r'^$', RedirectView.as_view(url='/atc_demo_ui/', permanent=False)),    
)
