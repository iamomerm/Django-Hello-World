#### <ins>What is Django ?</ins>
Django is an Open-Source Python Web Framework <br>
Popular applications that uses Django: Instagram, Pinterest, Bitbucket, Udemy, Mozilla and more <br>
Website: https://www.djangoproject.com/

<ins>Advantages of Django</ins> <br>
1. Solid Structure: Django has a well-defined structure
2. Built-in Features: Admin Interface, ORM, Authentication, Debugging, and more
3. Large Community: Django has a large community of developers

<ins>Disadvantages of Django</ins> <br>
1. Steep Learning Curve: Django has a lot of features and can be overwhelming for beginners
2. Performance: Django is not as fast as other frameworks like Flask
3. May not be the best choice for small projects

#### <ins>Commands</ins>
1. Install Django: _pip install django_
2. Install Django Debug Toolbar: _pip install django-debug-toolbar_
3. Create a new Django Project: _django-admin startproject project_name_
4. Create a Superuser: _python manage.py createsuperuser_
5. Create a new Django App: _python manage.py startapp app_name_
6. Run the Development Server: _python manage.py runserver <Port (Default: 8000)>_
7. Manage.py Shell: _python manage.py shell_
8. Apply Migrations: _python manage.py migrate_
9. Make Migrations: _python manage.py makemigrations_

#### <ins>Run Server</ins>
`_python manage.py runserver` command is used to run the development server <br>
Each modification will be automatically applied to the running server <br>
Development server will be available at: _http://localhost:8000/_ by default <br>

#### <ins>Project Structure</ins>
1. _project_name_: Main project folder
2. _app_name_: App folder
3. _manage.py_: Command-line utility that lets you interact with Django
4. _settings.py_: Contains all the settings for the project
5. _urls.py_: Contains all the URL patterns for the project

#### <ins>Applications</ins>
Django project is a collection of applications <br>
Applications are reusable web applications that are responsible for a single functionality (Unix Agenda: _"Do One Thing, Do It Well"_) <br>
Each application will have its own models, views, templates, and URLs <br>

#### <ins>URLs</ins>
_urls.py_ file contains all the URL patterns for the project <br>
path() function is used to define a URL pattern, it accepts 2 main arguments:
1. Route: URL pattern (E.G. _admin/_)
2. View: Function that will be called when the URL pattern is matched
```
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls), # Admin URL (E.G. http://localhost:8000/admin/)
]
```

#### <ins>Views</ins>
Views are functions that take a web request and return a web response <br>
Each Django app will have its own views.py file, but a main views.py file can be created in the project folder <br>
```
# <Main>/views.py
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home Page', status=200)  # Status is optional

# <Main>/urls.py
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
]
```

#### <ins>Templates</ins>
Templates are HTML files that are rendered by Django <br>
Templates are stored in the _templates_ folder inside the app folder or the project folder <br>
Templates directories should be added to the _TEMPLATES_ setting in _settings.py_ file <br>
```
# <Main>/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                (...)
            ],
        },
    },
]

- - - - - - - - - - 

# <Main>/templates/home.html
<!DOCTYPE html>
<html>
<head>
    <title>Home Page</title>
</head>
<body>
    <h1>Home Page {{ name }}</h1>
</body>
</html>

# <Main>/views.py
def home(request):
    return render(request, 'home.html', {'name': 'John Smith'})  # Parameters: Request, Template, Context
```

#### <ins>Static Folder</ins>
Static files are files that are served directly to the user (E.G. CSS, JS, Images) <br>
Static files are stored in the _static_ folder inside the app folder or the project folder <br>
Static directories should be added to the _STATICFILES_DIRS_ setting in _settings.py_ file <br>
```
# <Main>/settings.py
from os import path

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    path.join(BASE_DIR, 'static')
]

- - - - - - - - - - 

# <Main>/static/style.css
body {
    font-size: 24px;
    color: red;
    background-color: yellow;
}

- - - - - - - - - - 

# <Main>/static/script.js
alert('Hello World');

- - - - - - - - - - 

# <Main>/templates/home.html
<!DOCTYPE html>
{% load static %}
<html>
<head>
    <title>Home Page</title>
    <link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">
    <script src="{% static 'script.js' %}"></script>
</head>
<body>
    <h1>Home Page - {{ name }}</h1>
</body>
</html>
```

#### <ins>App</ins>
Django app is a collection of models, views, templates, and URLs <br>
To create a new app: _python manage.py startapp app_name_ <br>
Each app will have its own models.py, views.py, urls.py, and templates folder <br>
To add an app to the project, it should be added to the _INSTALLED_APPS_ setting in _settings.py_ file <br>
```
# <Main>/settings.py
INSTALLED_APPS = [
    'app_name',
    (...)
]
```

<ins>App Views</ins> <br>
```
# <App>/views.py
from django.shortcuts import render

def posts_list(request):
    return render(request, 'posts/posts_list.html')
```

<ins>App URLs</ins> <br>
urls.py file should be created manually in the app folder <br>
App urls.py file should be included in the project urls.py file <br>
```
# <App>/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts_list),  # '' is the root URL (/posts/ in this case)
]

- - - - - - - - - -

# <Main>/urls.py
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('posts/', include('posts.urls')),
]
```

<ins>Data Models</ins> <br>
Models are classes that represent database tables <br>
Models are stored in the models.py file inside the app folder <br>
Models should inherit from the _models.Model_ class <br>

<ins>Field Types</ins> <br>
- CharField: Character field - max_length is required (Used for short strings)
- TextField: Text field - max_length is not required (Used for long strings)
- SlugField: Slug field - max_length is required (Used for URLs)
- IntegerField: Integer field
- FloatField: Float field
- BooleanField: Boolean field
- DateField: Date field
- DateTimeField: Date and time field - auto_now_add=True (Used for creation date) - auto_now=True (Used for last update date)
- EmailField: Email field
(...)

```
<App>/models.py
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField(max_length=75, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

<ins>Migrations</ins> <br>

```
"You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): (...)"
```
When running the server, this message may appear <br>
Django migrations are used to apply changes to the database schema <br>
This message will be displayed if there are migrations that are not applied <br>
Applying a migration refers to updating the database schema <br>
to apply the migrations: _python manage.py migrate_ <br>
Before applying a new migration, it is recommended to create a new migration: _python manage.py makemigrations_ <br>

_Example for creating a new migration for an app named "posts"_
```
(.venv) > python manage.py makemigrations
Migrations for 'posts':
  posts\migrations\0001_initial.py
    - Create model Post

- - - - - - - - - - -

# <posts>/migrations/0001_initial.py
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('body', models.TextField()),
                ('slug', models.SlugField(max_length=75, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
```

_* For every change in the models.py file, a new migration should be created and applied_
```
(.venv) > python manage.py makemigrations
(.venv) > python manage.py migrate
```
#### <ins>ORM - Object-Relational Mapping</ins>
ORM (Object-Relational Mapping) is a programming technique that maps objects to database tables <br>
Django ORM is used to interact with the database <br>
ORM uses SQLite as a default database, but it can be changed to other databases like Aerospike, MySQL, PostgreSQL, MongoDB, and more <br>
```
(.venv) > python manage.py shell
(InteractiveConsole)
>>> from posts.models import Post
>>> p = Post()
>>> p.title = 'My First Post!'
>>> p.save()  # Database Action
>>> Post.objects.all() # Database Action
<QuerySet [<Post: My First Post!>]>
```

<ins>Example - view.py and template.html</ins> <br>
```
# <App>/views.py
from django.shortcuts import render
from .models import Post


def posts_list(request):
    posts = Post.objects.all()  # a Dict of all the posts
    return render(request, 'posts_list.html', {'posts': posts})

- - - - - - - - - -

# <App>/templates/posts_list.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Posts List</title>
</head>
<body>
    <h1>Posts List</h1>
    {% for post in posts %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.body }}</p>
        <h2>{{ post.date }}</h2>
    {% endfor %}
</body>
</html>
```

#### <ins>Admin Interface</ins>
Django Admin Interface is a built-in feature that allows you to manage the database <br>
Admin Interface is available at: _http://localhost:8000/admin/_ by default <br>
To access the Admin Interface, a superuser should be created: _python manage.py createsuperuser_ <br>
By default the Admin Interface shows only Users and Groups, to add a data model to the Admin Interface, it should be registered in the app's admin.py file <br>

<ins>Admin Interface Configuration</ins> <br>
The Admin Interface can be used as CMS (Content Management System) <br>
Each data model can be integrated to the Admin Interface <br>
Once integrated, the data model can be managed through the Admin Interface - Create, Delete, Edit <br>

```
# <App>/admin.py
from django.contrib import admin

from .models import Post

admin.site.register(Post)
```
