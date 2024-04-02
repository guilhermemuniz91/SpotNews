from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Category
from news.forms import CreateCategoriesForm, CreateNewsForm
from rest_framework import viewsets
from news.serializers import CategorySerializer

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


def news_form(request):
    form = CreateNewsForm()

    if request.method == "POST":
        form = CreateNewsForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            author = form.cleaned_data["author"]
            created_at = form.cleaned_data["created_at"]
            image = form.cleaned_data["image"]
            categories = form.cleaned_data["categories"]

            news = News.objects.create(
                title=title,
                content=content,
                author=author,
                created_at=created_at,
                image=image,
            )

            news.categories.set(categories)

            return redirect("home-page")

    context = {"form": form, "categories": Category.objects.all()}

    return render(request, "news_form.html", context)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
