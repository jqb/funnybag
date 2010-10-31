from django.conf.urls.defaults import *
from funnybag.core.views import AddRecordRating


urlpatterns = patterns('core.views',
                       url(r'^$', 'list', {'count': 2}, name="core-list"),
                       url(r'^all$', 'list', {'count': None}, name="core-all-list"),
                       url(r'^top/$', 'top', name="core-top-records"),
                       (r'^in_line/?$', 'list'),
                       (r'^(?P<record_id>\d+)$', 'details'),
                       url(r'^new/(?P<record_type>\w+)?/?$', 'new', name='core-new-record')
                       )

urlpatterns += patterns(
    '',
    url(r'rate_record/(?P<object_id>\d+)/(?P<score>\d+)/', AddRecordRating(), {
            'app_label': 'core',
            'model': 'record',
            'field_name': 'rating',
            }, name='core-rate-record'),
    )
