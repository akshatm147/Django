from urllib.parse import quote_plus

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import PostForm
from .models import Post

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser or not request.user.is_authenticated():
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        # print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }

    # if request.method == 'POST':
    #     print(request.POST.get("title"))
    #     title = request.POST.get("title")
    #     print(request.POST.get("content"))
    #     Post.objects.create(title=title)

    return render(request, "post_form.html", context)

def post_list(request):
    queryset_list = Post.objects.all() #.order_by("-timestamp")

    paginator = Paginator(queryset_list, 5) # Show 25 queryset_list per page

    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list" : queryset,
        "title" : "List",
        "page_request_var" : page_request_var
    }

    # if request.user.is_authenticated():
    #     context = {
    #         "title" : "My User List"
    #     }
    # else:
    #     context = {
    #         "title" : "List"
    #     }

    return render(request, "post_list.html", context)
    # return HttpResponse("<h1>List</h1>")

def post_detail(request, slug=None):
    # instance = Post.objects.get(10)
    instance = get_object_or_404(Post, slug=slug)
    share_string = quote_plus(instance.content)
    context = {
        "title" : instance.title,
        "instance" : instance,
        "share_string" : share_string,
    }

    return render(request, "post_detail.html", context)
    # return HttpResponse("<h1>Detail</h1>")

def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser or not request.user.is_authenticated():
        raise Http404

    instance = get_object_or_404(Post, slug=slug)

    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title" : instance.title,
        "instance" : instance,
        "form" : form,
    }

    return render(request, "post_update.html", context)

def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser or not request.user.is_authenticated():
        raise Http404

    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Post Deleted Successfully")
    return redirect("posts:list")
