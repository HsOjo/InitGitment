import json

import requests


def new_issue(site, username, repo, token, title, labels, body):
    headers = {
        "Accept": "application/vnd.github.squirrel-girl-preview, application/vnd.github.html+json",
        'Origin': site,
        "Referer": site,
        'Authorization': 'token %s' % token
    }
    payload = {
        'title': title,
        'labels': labels,
        'body': body
    }
    payload_json = json.dumps(payload)
    resp = requests.post('https://api.github.com/repos/' + username + '/' + repo + '/issues', headers=headers,
                         data=payload_json)
    return resp


def check_exist(username, repo, labels):
    url = 'https://api.github.com/repos/%s/%s/issues' % (username, repo)
    params = {
        'creator': username,
        'labels': ','.join(labels),
    }
    resp = requests.get(url, params)
    return resp.json()
