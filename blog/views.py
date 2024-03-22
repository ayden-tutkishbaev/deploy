from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .models import *
from .forms import *

def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()

    context = {
        "title": "Главная страница",
        "categories": categories,
        "articles": articles
    }

    return render(request, "blog/index.html", context)


def category_page_view(request, category_id):
    articles = Article.objects.filter(
        category=category_id
    ).order_by(
        '-created_at'
    )
    trends = Article.objects.all().order_by('-views')

    context = {
        "title": f"Категория: {Category.objects.get(id=category_id)}",
        'articles': articles,
        'trends': trends
    }

    return render(request, "blog/category_page.html", context)


def about_us_page_view(request):
    return render(request, "blog/about_us.html")


def our_team_page_view(request):
    return render(request, "blog/our_team.html")




def services_page_view(request):
    return render(request, "blog/services.html")

def article_detail_page_view(request, article_id):
    article = Article.objects.get(id=article_id)
    last_articles = Article.objects.all().order_by('-created_at')[:3]
    if article.author != request.user:
        article.views += 1
        article.save()

    context = {
        "title": f"Статья: {article.title}",
        "article": article,
        "last_articles": last_articles
    }

    return render(request, "blog/article_detail.html", context)


def add_article_view(request):
    if request.method == 'POST':
        form = AddArticleForm(data=request.POST,
                              files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', article.pk)
        else:
            # TODO: ERROR MESSAGE
            pass
    elif request.method == 'GET':
        form = AddArticleForm()

    context = {
        'title': 'Добавить статью',
        'form': form
    }

    return render(request, "blog/add_article.html", context)


def register_user_view(request):
    if request.method == 'POST':
        form = RegistrationUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile_user = Profile.objects.create(user=user)
            profile_user.save()
            return redirect('login')
        else:
            # TODO: ERROR MESSAGE
            pass
    else:
        form = RegistrationUserForm()

    context = {
        'title': "Регистрация пользователя",
        'form': form
    }

    return render(request, "blog/register.html", context)
def login_user_view(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('index')
            else:
                # TODO: ERROR MESSAGE
                pass
        else:
            # TODO: ERROR MESSAGE
            pass


    else:
        form = LoginUserForm()

    context = {
        'title': "Вход пользователя",
        'form': form
    }

    return render(request, "blog/login.html", context)

def logout_user_view(request):
    logout(request)
    return redirect('index')


def search_view(request):
    word = request.GET.get('q')
    categories = Category.objects.all()
    articles = Article.objects.filter(
        title__iregex=word
    )

    context = {
        "title": "Результаты поиска",
        "categories": categories,
        "articles": articles
    }

    return render(request, "blog/index.html", context)


def update_article_view(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        form = AddArticleForm(instance=article,
                              data=request.POST,
                              files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("article_detail", article.id)
        else:
            # TODO: ERROR MESSAGE
            return redirect("update_article", article.id)
    else:
        form = AddArticleForm(instance=article)
    context = {
        "form": form,
        "title": "Изменить статью"
    }
    return render(request, "blog/add_article.html", context)


def delete_article_view(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method == "POST":
        article.delete()
        return redirect("index")

    context = {
        "article": article,
        "title": "Удалить статью"
    }

    return render(request, "blog/delete_article.html", context)


def check_profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile_user = Profile.objects.get(user=user)
    articles = Article.objects.filter(author=user_id).order_by('-views')[:4]

    context = {
        "title": "Профиль",
        "user": user,
        "profile": profile_user,
        "articles": articles
    }

    return render(request, "blog/profile.html", context)


def update_profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        pass
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "title": "Изменить профиль"
    }

    return render(request, "blog/edit_profile.html", context)