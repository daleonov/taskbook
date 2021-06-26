import random as rnd

import markdown

from django.shortcuts import render
from taskbook_app.models import Task
from django.http import HttpResponseNotFound


def _md_to_html(text_md):
    md = markdown.Markdown(extensions=['extra', 'codehilite'])
    text_html = md.convert(text_md)
    return text_html


def index(request):
    return render(request, 'index.html')


def contents(request):
    # TODO: Сделать сортировку по курсам и разделам

    tasks = []
    for task in Task.objects.all():

        entry = {
            'title': task.title,
            'course': 'Питон-1',
            'section': task.section,
            'page_name': task.title_machine_friendly
        }
        tasks.append(entry)
    return render(request, 'contents.html', {'data': tasks})


def single_task(request, title_machine_friendly):

    try:
        task = Task.objects.get(title_machine_friendly=title_machine_friendly)
    except Task.DoesNotExist:
        return HttpResponseNotFound("Нет такой задачи :(")
    else:
        #print(task)

        # Markdown -> HTML
        text_html = _md_to_html(task.text)

        entry = {
            'title': task.title,
            'text': text_html,
            'course': 'Питон-1',
            'section': task.section,
        }

        return render(request, 'single.html', {'task': entry})


def random(request):
    task = rnd.choice(Task.objects.all())
    return single_task(request, task.title_machine_friendly)


def all_on_one_page(request):
    tasks = []
    for task in Task.objects.all():

        # Markdown -> HTML
        text_html = _md_to_html(task.text)

        entry = {
            'title': task.title,
            'text': text_html,
            'course': 'Питон-1',
            'section': task.section,
        }
        tasks.append(entry)
    return render(request, 'all.html', {'data': tasks})
