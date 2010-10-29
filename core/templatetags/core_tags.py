# -*- coding: utf-8 -*-
from django import template

register = template.Library()


def record_rating(user, record):
    return {
        'user': user,
        'record': record,
        }
register.inclusion_tag('core/_record_rating.html')(record_rating)
