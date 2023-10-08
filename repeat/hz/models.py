from django.db import models

# Create your models here.
from django.db import models

class School(models.Model):
    fullname = models.CharField("Полное наименование", max_length=100)
    class Meta:
        verbose_name = "Школа"
        verbose_name_plural = "Школы"
    def __str__(self):
        return self.fullname

class Teacher(models.Model):
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    image = models.ImageField("Изобажение", upload_to="teachers/")
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name + " " + self.surname + " " + str(self.school)

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

class Student(models.Model):
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    image = models.ImageField("Изобажение", upload_to="students/")
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"


