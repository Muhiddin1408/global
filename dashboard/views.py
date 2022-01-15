from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Club
# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')





class ClubChartView(TemplateView):
    template_name = 'dashboard/template/charts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Club.objects.all()
        return context