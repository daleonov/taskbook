import re
import datetime
import json
from collections import defaultdict

import requests
from transliterate import translit

url = 'https://raw.githubusercontent.com/daleonov/specialist-python-1/master/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%BD%D0%B8%D0%BA.md'
taskbook_md = requests.get(url).text


re_task = r"## [^#]*"
re_section = r"# (\d+)\.? (.+)\n"

re_title_and_text = r'^## (\d+)\.(\d+) ([^\n]+)\n(.*)'


# Номера и имена разделов
section_names = {int(num): name for num, name in re.findall(re_section, taskbook_md)}
# print(section_names)

# Разбивка текста на задачи
tasks_md = re.findall(re_task, taskbook_md)
# print(len(tasks_md))

title_max_length = 0
text_max_length = 0
section_max_length = len(max(section_names.values(), key=len))

# data
# - course
# -- section
# --- task
out = {
    'data': {
        'Питон-1': defaultdict(list)
    },
    'meta': None
}

for task_md in tasks_md:
    m_title_and_text = re.search(re_title_and_text, task_md, re.DOTALL)
    
    if m_title_and_text:

        title = m_title_and_text.group(3)

        section_num = int(m_title_and_text.group(1))
        section_name = section_names[section_num]
        
        text = m_title_and_text.group(4).strip('\n ')

        # TODO: проверять имена на уникальность
        # (а ещё лучше генерить на уровне сервера, а не тут)
        title_machine_friendly = (
                'Python1_'
                + translit(section_name, 'ru', reversed=True)
                + '_'
                + translit(title, 'ru', reversed=True)
        )
        title_machine_friendly = title_machine_friendly.replace(' ', '_')

        if len(title) > title_max_length:
            title_max_length = len(title)

        if len(text) > text_max_length:
            text_max_length = len(text)

        entry = {
            'title': title,
            'title_machine_friendly': title_machine_friendly,
            # 'section': section_name,
            'text': text,
        }

        out['data']['Питон-1'][section_name].append(entry)

    else:
        print('???', task_md[:10])

out['meta'] = { 
    'date': str(datetime.date.today()),
    'tasks': len(tasks_md),
    'title_max_length': title_max_length,
    'text_max_length': text_max_length,
    'section_max_length': section_max_length,
}

f = open('../data/tasks_python1.json', 'w', encoding='utf8')
json.dump(out, f, ensure_ascii=False, indent = 2)
f.close()

print('Готово')