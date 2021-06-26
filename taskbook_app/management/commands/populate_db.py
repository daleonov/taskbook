#  https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database

import json

from django.core.management.base import BaseCommand
from taskbook_app.models import Task
# from taskbook_app.models import Section, Course


class Command(BaseCommand):
    args = ''
    help = 'usage: py -3 manage.py populate_db --fp=<json_path>'

    def add_arguments(self, parser):
        parser.add_argument('--fp', nargs='+', type=str, help='json file path')

    def handle(self, *args, **options):
        # print(args, options)
        json_path = options['fp']
        with open(json_path[0], encoding='utf8') as f:
            data = json.load(f)

        # print(data.keys())
        for course in data['data']:
            # print(course)
            for section in data['data'][course]:
                # print(section)
                for task in data['data'][course][section]:

                    # section_entry = Section(name=section) #, id=hash(section))
                    # course_entry = Course(name=course) #, id=hash(course))

                    # section_entry.save()
                    # course_entry.save()

                    # TODO: Более осмысленные id для задач
                    task_id = hash((course, section, task['title']))

                    task_entry = Task(
                        title=task['title'],
                        title_machine_friendly=task['title_machine_friendly'],
                        text=task['text'],
                        id=task_id,
                        section=section,
                        course=course
                    )
                    print(task_entry)
                    task_entry.save()
        print('Готово')