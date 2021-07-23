from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.urls import reverse_lazy


class AdListView(OwnerListView):
    model = Ad


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'text', 'price']
    success_url=reverse_lazy('ads:all')


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text', 'price']
    success_url=reverse_lazy('ads:all')


class AdDeleteView(OwnerDeleteView):
    model = Ad
    success_url=reverse_lazy('ads:all')
