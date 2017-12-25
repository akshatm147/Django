from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import MyUrl
from .forms import SubmitUrlForm

# Create your views here.

def home_view_fbv(request, *args, **kwargs):
    if request.method== 'POST':
        print(request.POST)
    return render(request, "shortener/home.html", {})

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title" : "My URL Shortener",
            "form" : the_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

        context = {
            "title" : "My URL Shortener",
            "form" : form
        }
        return render(request, "shortener/home.html", context)


class MyCBView(View): #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(MyUrl, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)


'''
def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view FBV
    #print(request.user)
    #print(request.user.is_authenticated())\
    print('method is \n')
    print(request.method)
    #obj = KirrURL.objects.get(shortcode=shortcode)
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    #obj_url = obj.url
    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()
    # obj_url = None
    # qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url
    return HttpResponse("hello {sc}".format(sc=obj.url))
'''
