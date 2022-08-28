import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .models import *


# Create your views here.


def nutrition(request):
    queryset = Recipe.objects.get_queryset()
    context = {'recipes': queryset}
    return render(request, 'nutrition.html', context=context)


def nutrition_details(request, id_recipe):
    queryset = Recipe.objects.get(pk=id_recipe)
    queryset2 = Fact.objects.filter(recipe_id=id_recipe)
    context = {'recipe': queryset, 'facts': queryset2}
    return render(request, 'nutritionDetails.html', context=context)


def muscle_groups(request):
    queryset = MuscleGroup.objects.get_queryset()
    context = {'muscle_groups': queryset}
    return render(request, 'muscleGroups.html', context=context)


def muscle_group_details(request, id_muscle_group):
    muscleGroup = MuscleGroup.objects.get(pk=id_muscle_group)
    exercises = Exercise.objects.filter(muscleGroup_id=id_muscle_group)
    context = {'muscleGroup': muscleGroup, 'exercises': exercises}
    return render(request, 'muscleGroupDetails.html', context=context)


def exercise(request, id_exercise):
    queryset = Exercise.objects.get(pk=id_exercise)
    context = {'exercise': queryset}
    return render(request, 'exercise.html', context=context)


def quizzes(request):
    queryset = Test.objects.filter(level='low')
    queryset2 = Test.objects.filter(level='medium')
    queryset3 = Test.objects.filter(level='advance')
    test_users = TestUser.objects.filter(fitnessUser=request.user)
    queryset4 = [test_user.test for test_user in test_users]
    context = {'lowLevelQuizzes': queryset, 'mediumLevelQuizzes': queryset2, 'advanceLevelQuizzes': queryset3,
               'finishedTests': queryset4}
    return render(request, 'quizzes.html', context=context)


def quiz(request, id_quiz):
    if request.method == "POST":
        completedTests = TestUser.objects.filter(fitnessUser=request.user).filter(test=id_quiz)
        score = completedTests[0].score
        return render(request, "yourScore.html", context={'score': score})
    queryset = Question.objects.filter(test_id__in=id_quiz)
    tmp = [i.possibleAnswers.all() for i in queryset]
    queryset2 = [tmp[i] for i in range((len(tmp) - 1), -1, -1)]
    queryset3 = Test.objects.get(pk=id_quiz).level
    tmp2 = [i.theAnswer for i in queryset]
    queryset4 = [tmp2[i] for i in range((len(tmp2) - 1), -1, -1)]
    queryset5 = id_quiz
    context = {'questions': queryset, 'answers': queryset2, 'level': queryset3,
               'theAnswers': queryset4, 'testId': queryset5}
    return render(request, 'quizDetails.html', context=context)


def your_score(request, the_score):
    context = {'score': the_score}
    # request.COOKIES.clear()
    return render(request, "yourScore.html", context=context)


@csrf_protect
def requestt(request):
    scoree= ""
    if request.method == "POST":
        a = str(request.body).split('"')
        scoree = a[3]
        level = a[7]
        testId = a[11]
        testUser = TestUser(score=scoree, level=level)
        testUser.fitnessUser = request.user
        testUser.test = Test.objects.get(pk=testId)
        testUser.save()
    return render(request, "yourScore.html", context={'score': '2'})
