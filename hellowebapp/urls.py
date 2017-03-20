"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import (TemplateView, 
    RedirectView,
)
from django.contrib.auth.views import (
   password_reset, 
   password_reset_done,
   password_reset_confirm,
   password_reset_complete
)
from collection import views
# add this to the top
from collection.backends import MyRegistrationView

urlpatterns = [
    url(
        regex=r'^$', 
        view=views.index,
        name='home',
    	),
    url(
    	regex=r'^about/$',
        view=TemplateView.as_view(template_name='about.html'),
        name='about',
        ),
    url(
    	regex=r'^contact/$', 
        view=TemplateView.as_view(template_name='contact.html'),
        name='contact',
        ),

    url(
        regex=r'^things/$', 
        view=RedirectView.as_view(pattern_name='browse', permanent=True),
        ),

    url(
    	regex=r'^things/(?P<slug>[-\w]+)/$', 
    	view=views.thing_detail, 
        name='thing_detail',
        ),
    url(
    	regex=r'^things/(?P<slug>[-\w]+)/edit/$', 
        view=views.edit_thing,
        name='edit_thing',
        ),

    url(
        regex=r'^browse/$', 
        view=RedirectView.as_view(pattern_name='browse', permanent=True),
        ),
    # our new browse flow
    url(
        regex=r'^browse/name/$',
        view=views.browse_by_name, 
        name='browse',
        ),
    url(
        regex=r'^browse/name/(?P<initial>[-\w]+)/$', 
        view=views.browse_by_name, 
        name='browse_by_name',
        ),


	# the new password reset URLs
    url(r'^accounts/password/reset/$', 
        password_reset,
        {'template_name':
        'registration/password_reset_form.html'},
        name="password_reset"),
    url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name':
        'registration/password_reset_done.html'},
        name="password_reset_done"),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        password_reset_confirm,
        {'template_name':
        'registration/password_reset_confirm.html'},
        name="password_reset_confirm"),
    url(r'^accounts/password/done/$', 
        password_reset_complete,
        {'template_name':
        'registration/password_reset_complete.html'},
        name="password_reset_complete"),

	url(
		regex=r'^accounts/register/$', 
	    view=MyRegistrationView.as_view(),
	    name='registration_register',
	    ),
	url(
		regex=r'^accounts/create_thing/$', 
		view=views.create_thing, 
	    name='registration_create_thing',
	    ),


    url(
        regex=r'^accounts/', 
        view=include('registration.backends.simple.urls'),
        ),
    url(
        regex=r'^admin/', 
        view=admin.site.urls,
        ),
]











