from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth import forms as auth_form

from funnybag.core.models import Record
from funnybag.core.forms import JokeForm, ImageForm, QuoteForm, VideoForm
from annoying.decorators import render_to

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

@render_to('core/new.html')
def new(request):
    if request.method == 'POST':
        form = JokeForm(request.POST)
        if form.is_valid():
            record = form.save()
            return HttpResponseRedirect(record.get_absolute_url())
    else:
        joke_form = JokeForm()
        image_form = ImageForm()
        quote_form = QuoteForm()
        video_form = VideoForm()

    return {'joke_form': joke_form,
            'image_form': image_form,
            'quote_form' : quote_form,
            'video_form' : video_form}
