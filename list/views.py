from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Business

class IndexView(generic.ListView):
    template_name = "list/index.html"
    #context_object_name = "business_list"

    def get_queryset(self):
        return Business.objects.order_by("verified_date")

class DetailView(generic.DetailView):
    model = Business
    template_name = "list/detail.html"

def add(request):
   business = Business(name=request.POST["business_name"]) 
   business.save()

   return HttpResponseRedirect(reverse("list:index"))
