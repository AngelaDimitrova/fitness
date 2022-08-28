from django.contrib import admin
from .models import *
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Recipe, RecipeAdmin)


class FactAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Fact, FactAdmin)


class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(MuscleGroup, MuscleGroupAdmin)


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Exercise, ExerciseAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('content', )


admin.site.register(Answer, AnswerAdmin)


class TestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Test, TestAdmin)


class TestUserAdmin(admin.ModelAdmin):
    list_display = ('fitnessUser', 'test', )


admin.site.register(TestUser, TestUserAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content',)


admin.site.register(Question, QuestionAdmin)


class FitnessUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(FitnessUser, FitnessUserAdmin)
