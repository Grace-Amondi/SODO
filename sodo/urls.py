# -*- coding: utf-8 -*-
# This technical data was produced for the U. S. Government under Contract No. W15P7T-13-C-F600, and
# is subject to the Rights in Technical Data-Noncommercial Items clause at DFARS 252.227-7013 (FEB 2012)

from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from sodo.core.views import Dashboard

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Dashboard.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sodo/', include('sodo.core.urls')),
    url(r'^maps/', include('sodo.maps.urls')),
    url(r'^mage/', include('sodo.mage.urls')),
    url(r'^feedback/', include('sodo.feedback.urls')),
    url(r'^accounts/', include('sodo.accounts.urls')),
    url(r'^proxy/', include('sodo.proxy.urls', namespace="proxy")),
    url(r'^training/', include('sodo.training.urls', namespace="training")),
    url(r'^recolor/', include('sodo.recolor.urls')),
    url(r'^messages/', include('userena.contrib.umessages.urls'), name='userena_messages'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
