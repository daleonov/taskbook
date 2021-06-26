from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Course(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Task(models.Model):
    section = models.CharField(max_length=128)
    course = models.CharField(max_length=128)
    text = models.CharField(max_length=20000)
    title = models.CharField(max_length=64)
    title_machine_friendly = models.CharField(max_length=256)
    # TODO: добавить прикреплённые текстовые файлы, картинки, теги

    # TODO: сделать связь с курсом и разделом:
    # section = models.ForeignKey(Section, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.__class__.__name__}(\'{self.title}\')'
