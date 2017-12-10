from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import PostForm
from .models import Post

def post_create(request):
    form = PostForm(request.POST or None)

    context = {
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        # print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Creation Unsuccessful!")

    # if request.method == 'POST':
    #     print(request.POST.get("title"))
    #     title = request.POST.get("title")
    #     print(request.POST.get("content"))
    #     Post.objects.create(title=title)

    return render(request, "post_form.html", context)

def post_list(request):
    queryset = Post.objects.all()

    context = {
        "object_list" : queryset,
        "title" : "List"
    }

    # if request.user.is_authenticated():
    #     context = {
    #         "title" : "My User List"
    #     }
    # else:
    #     context = {
    #         "title" : "List"
    #     }

    return render(request, "index.html", context)
    # return HttpResponse("<h1>List</h1>")

def post_detail(request, id=None):
    # instance = Post.objects.get(10)
    instance = get_object_or_404(Post, id=id)
    context = {
        "title" : instance.title,
        "instance" : instance,
    }

    return render(request, "post_detail.html", context)
    # return HttpResponse("<h1>Detail</h1>")

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)

    form = PostForm(request.POST or None, instance=instance)
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

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Post Deleted Successfully")
    return redirect("posts:list")
