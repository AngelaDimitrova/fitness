"""fitness_guide URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from fitness_app.views import *

urlpatterns = [
    path("login/", login_request, name="login_request"),
    path("logout", logout_request, name="logout_request"),
    path("yourScore/<the_score>/", your_score, name="your_score"),
    path("requestt/", requestt, name='requestt'),
    path('admin/', admin.site.urls),
    path('nutrition/', nutrition, name='nutrition'),
    path('nutritionDetails/<id_recipe>/', nutrition_details, name='nutrition_details'),
    path('muscleGroups/', muscle_groups, name='muscleGroups'),
    path('muscleGroupDeatils/<id_muscle_group>/', muscle_group_details, name='muscle_group_details'),
    path('muscleGroups/<id_exercise>/', exercise, name='exercise'),
    path('quizzes/', quizzes, name='quizzes'),
    path('quizzes/<id_quiz>/', quiz, name='quiz'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
