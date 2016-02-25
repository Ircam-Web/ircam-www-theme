from django.shortcuts import render
from django.views.generic import *
from django.views.generic.base import *

from festival.models import *


class ArtistListView(ListView):

    model = Artist
    template_name='festival/artist_list.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistListView, self).get_context_data(**kwargs)
        return context


class ArtistDetailView(DetailView):

    model = Artist
    template_name='festival/artist_detail.html'
    context_object_name = 'artist'

    def get_context_data(self, **kwargs):
        context = super(ArtistDetailView, self).get_context_data(**kwargs)
        return context


class VideoListView(ListView):

    model = Video
    template_name='festival/video_list.html'

    def get_context_data(self, **kwargs):
        context = super(VideoListView, self).get_context_data(**kwargs)
        return context


class VideoDetailView(DetailView):

    model = Video
    template_name='festival/video_detail.html'
    context_object_name = 'video'

    def get_context_data(self, **kwargs):
        context = super(VideoDetailView, self).get_context_data(**kwargs)
        return context
