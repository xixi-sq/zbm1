import json

from django.http import HttpResponse
from django.conf import settings


def render_json(data=None, code=0,message=None):
    result = {
        'data': data,
        'code': code,
        'message':message
    }

    if settings.DEBUG:
        json_str = json.dumps(result, ensure_ascii=False,
                              sort_keys=True, indent=4)
    else:
        json_str = json.dumps(result, ensure_ascii=False,
                              separators=[',', ':'])
    return HttpResponse(json_str)
