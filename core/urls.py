from django.conf.urls.defaults import *
from djangoratings.views import AddRatingFromModel


urlpatterns = patterns('core.views',
                       (r'^$', 'list'),
                       (r'^in_line/?$', 'list'),
                       (r'^(?P<record_id>\d+)$', 'details'),
                       (r'^new/(?P<record_type>\w+)?/?$', 'new')
                       )

urlpatterns += patterns(
    '',
    url(r'rate_record/(?P<object_id>\d+)/(?P<score>\d+)/', AddRatingFromModel(), {
            'app_label': 'core',
            'model': 'record',
            'field_name': 'rating',
            }),
    )
