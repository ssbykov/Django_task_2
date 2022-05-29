from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from csv import DictReader
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        paginator = Paginator(list(DictReader(csvfile)), 10)
        page = paginator.page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        # 'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
