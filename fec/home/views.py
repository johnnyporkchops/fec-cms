from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
from operator import attrgetter
from home.models import DigestPage
from home.models import RecordPage
from home.models import PressReleasePage

def replace_dash(string):
  return string.replace('-', ' ')

def replace_space(string):
  return string.replace(' ', '-')

def updates(request):
    digests = ''
    records = ''
    press_releases = ''
    categories = ''

    # Get values from query
    update_types = request.GET.getlist('update_type', None)
    category_list = request.GET.getlist('category', '')
    year = request.GET.get('year', '')

    category_list = list(map(replace_dash, category_list))

    # If there's a query, only get the types in the query
    if update_types:
      if 'fec-record' in update_types:
        records = RecordPage.objects.all()
        if category_list:
          for category in category_list:
            records = records.filter(category=category)
        if year:
          records = records.filter(date__year=year)
      if 'press-release' in update_types:
        press_releases = PressReleasePage.objects.all()
        if category_list:
          for category in category_list:
            press_releases = press_releases.filter(category=category)
        if year:
          press_releases = press_releases.filter(date__year=year)
      if 'weekly-digest' in update_types:
        digests = DigestPage.objects.all()
        if year:
          digests = digests.filter(date__year=year)

    else:
      # Get everything and filter by year if necessary
      records = RecordPage.objects.live()
      digests = DigestPage.objects.live()
      press_releases = PressReleasePage.objects.live()

      if year:
        records = records.filter(date__year=year)
        press_releases = press_releases.filter(date__year=year)
        digests = digests.filter(date__year=year)

    # Chain all the QuerySets together
    # via http://stackoverflow.com/a/434755/1864981
    updates = sorted(
      chain(press_releases, digests, records),
      key=attrgetter('date'),
      reverse=True
    )

    # Handle pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(updates, 20)
    try:
        updates = paginator.page(page)
    except PageNotAnInteger:
        updates = paginator.page(1)
    except EmptyPage:
        updates = paginator.page(paginator.num_pages)

    page_context = {
      'title': 'Latest updates',
    }

    category_list = list(map(replace_space, category_list))

    return render(request, 'home/latest_updates.html', {
        'page_context': page_context,
        'category_list': category_list,
        'update_types': update_types,
        'updates': updates,
        'year': year
    })
