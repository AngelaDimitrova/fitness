from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Answer(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class Test(models.Model):
    level = models.CharField(max_length=20)
    questionQuantity = models.IntegerField()

    def __str__(self):
        return self.level + " " + str(self.pk)


class TestUser(models.Model):
    score = models.FloatField(null=True, blank=True)
    fitnessUser = models.ForeignKey(User, on_delete=models.CASCADE,  blank=True, null=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE,  blank=True, null=True)
    level = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.fitnessUser.first_name) + " " + str(self.test.pk)


class Question(models.Model):
    content = models.TextField()
    possibleAnswers = models.ManyToManyField(Answer,  related_name='possible_answers', blank=True)
    theAnswer = models.OneToOneField(Answer, on_delete=models.CASCADE, primary_key=True,  related_name='the_answer')
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class FitnessUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pictures", blank=True, null=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.user.email


class Recipe(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=30)
    time = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.name


class Fact(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class MuscleGroup(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=30)
    shortDescription = models.CharField(max_length=250)
    description = models.TextField()
    primaryImage = models.ImageField()
    explanatoryImage = models.ImageField(blank=True)
    muscleGroup = models.ForeignKey(MuscleGroup, on_delete=models.CASCADE, default='', blank=True, null=True)

    def __str__(self):
        return self.name


