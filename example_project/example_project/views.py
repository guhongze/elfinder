from django.views.generic.base import View
from django.shortcuts import render_to_response
from django.contrib.auth.mixins import LoginRequiredMixin

class finder(LoginRequiredMixin,View):
    def get(self,request):
        return render_to_response('finder.html',locals())