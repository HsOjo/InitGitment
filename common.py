import json
import os
import re
from io import StringIO

import yaml


def load_json(path, default=None):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf8') as io:
            data = json.load(io)
    else:
        data = default

    return data


def save_json(path, data):
    with open(path, 'w', encoding='utf8') as io:
        json.dump(data, io, ensure_ascii=False, indent=4)


def load_yaml(string):
    with StringIO(string) as io:
        data = yaml.load(io, yaml.FullLoader)

    return data


def hexo_info(content):
    reg_info = re.compile('---\n([\s\S]*?)\n---')
    [info_str] = reg_info.findall(content)
    info = load_yaml(info_str)
    return info
