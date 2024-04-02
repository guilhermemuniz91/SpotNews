from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category
from news.forms import CreateCategoriesForm

# Create your views here.


def index(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, id):
    context = {"news_details": get_object_or_404(News, id=id)}
    return render(request, "news_details.html", context)


def categories_form(request):
    form = CreateCategoriesForm()

    if request.method == "POST":
        form = CreateCategoriesForm(request.POST)

        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "categories_form.html", context)
