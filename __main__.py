import os

import api
import common

F_CONFIG = './config.json'
F_CHECK = './check.json'
config = common.load_json(F_CONFIG, {
    'site': '',
    'username': '',
    'repo': '',
    'token': '',
    'dir_post': '',
})
check = common.load_json(F_CHECK, {})  # type: dict

for f in os.listdir(config['dir_post']):
    if f[-3:].lower() == '.md':
        name = f[:-3]
        path = '%s/%s' % (config['dir_post'], f)
        with open(path, 'r', encoding='utf8') as io:
            content = io.read()

        info = common.hexo_info(content)

        link = '/%04d/%02d/%02d/%s/' % (
            info['date'].year,
            info['date'].month,
            info['date'].day,
            name,
        )

        data = {
            'site': config['site'],
            'username': config['username'],
            'repo': config['repo'],
            'token': config['token'],
            'title': info['title'],
            'labels': ['gitment', link],
            'body': '%s%s' % (config['site'], link)
        }

        if check.get(link) is None:
            r_check = api.check_exist(config['username'], config['repo'], data['labels'])
            if len(r_check) == 0:
                api.new_issue(**data)
                print('Create issue %s.' % data['title'])
            check[link] = True

        common.save_json(F_CHECK, check)
