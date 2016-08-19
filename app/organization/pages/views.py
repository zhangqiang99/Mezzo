from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from dal import autocomplete
from dal_select2_queryset_sequence.views import Select2QuerySetSequenceView
from mezzanine_agenda.models import Event
from organization.core.models import BasicPage
from organization.core.views import SlugMixin
from organization.magazine.models import Article, Topic, Brief
from organization.pages.models import Home

class HomeView(SlugMixin, ListView):

    model = Home
    template_name = 'index.html'
    briefs = Brief.objects.all() # with .published, order by isn't working anymore
    context_object_name = 'home'

    def get_queryset(self, **kwargs):
        return self.model.objects.published().latest("publish_date")

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['briefs'] = self.briefs
        return context



class DynamicContentHomeSliderView(Select2QuerySetSequenceView):
    def get_queryset(self):

        articles = Article.objects.all()
        basicpage = BasicPage.objects.all()
        events = Event.objects.all()

        if self.q:
            articles = articles.filter(title__icontains=self.q)
            basicpage = basicpage.filter(title__icontains=self.q)
            events = events.filter(title__icontains=self.q)

        qs = autocomplete.QuerySetSequence(articles, basicpage, events )

        if self.q:
            # This would apply the filter on all the querysets
            qs = qs.filter(title__icontains=self.q)

        # This will limit each queryset so that they show an equal number
        # of results.
        qs = self.mixup_querysets(qs)

        return qs

class DynamicContentHomeBodyView(Select2QuerySetSequenceView):
    def get_queryset(self):

        articles = Article.objects.all()
        basicpage = BasicPage.objects.all()
        events = Event.objects.all()
        briefs = Brief.objects.all()

        if self.q:
            articles = articles.filter(title__icontains=self.q)
            basicpage = basicpage.filter(title__icontains=self.q)
            events = events.filter(title__icontains=self.q)
            briefs = briefs.filter(title__icontains=self.q)

        qs = autocomplete.QuerySetSequence(articles, basicpage, events, briefs)

        if self.q:
            # This would apply the filter on all the querysets
            qs = qs.filter(title__icontains=self.q)

        # This will limit each queryset so that they show an equal number
        # of results.
        qs = self.mixup_querysets(qs)

        return qs
