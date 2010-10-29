from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from django.contrib.auth import forms as auth_form
from django.http import Http404, HttpResponseRedirect

from annoying.decorators import render_to
from djangoratings.views import AddRatingFromModel

from funnybag.core.models import Record
from funnybag.core.forms import JokeForm, ImageForm, QuoteForm, VideoForm


@render_to('core/details.html')
def details(request, record_id):
    return {'record': get_object_or_404(Record, pk=record_id) }

@render_to('core/list.html')
def list(request):
    records = Record.objects.order_by('-created_time')
    login_form = auth_form.AuthenticationForm()
    return {'records': records ,
            'login_form' : login_form,
            'login_next' : "/"}

@render_to('core/top.html')
def top(request):
    records = Record.objects.get_top(5)
    login_form = auth_form.AuthenticationForm()
    return {'records': records ,
            'login_form' : login_form,
            'login_next' : "/"}

@render_to('core/new.html')
def new(request, record_type):
    Form = dict(joke=JokeForm, quote=QuoteForm,
                image=ImageForm, video=VideoForm,
                ).get(record_type, None)

    if not Form:
        return {'form': None, 'form_action': ''}

    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            item = form.save()
            record = item.get_record()
            return HttpResponseRedirect(record.get_absolute_url())
    else:
        form = Form()

    return {'form': form, 'form_action': record_type}


# class based view used because of django-ranting plugin.
# It's not well documented but code is clear and simple.
# http://github.com/dcramer/django-ratings/blob/master/djangoratings/views.py
class AddRecordRating(AddRatingFromModel):
    def rating_added_response(self, request, context):
        response = HttpResponseRedirect(reverse('core-list'))
        return response
