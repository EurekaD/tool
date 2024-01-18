import hashlib
from urllib.parse import quote

def md5_hash(input_string):
    md5 = hashlib.md5()
    md5.update(input_string.encode('utf-8'))
    return md5.hexdigest()


request_json = {
    "page": 1,
    "type": 'search_news',
    "order": 1,
    "keyword": '赖清德'
}

def ksort(input_dict, sort_flags='SORT_REGULAR'):
    tmp_dict = {}
    keys = list(input_dict.keys())
    sorter = None

    # Define sorter function based on sort_flags
    if sort_flags == 'SORT_STRING':
        sorter = lambda x: str(x)
    elif sort_flags == 'SORT_NUMERIC':
        sorter = lambda x: float(x)
    else:
        sorter = lambda x: x

    keys.sort(key=sorter)

    strict_for_in = False
    populate_dict = {}

    # Rebuild dictionary with sorted key names
    for k in keys:
        tmp_dict[k] = input_dict[k]
        if strict_for_in:
            del input_dict[k]

    for k, v in tmp_dict.items():
        populate_dict[k] = v

    return input_dict if strict_for_in else populate_dict


def get_request_str(data):
    query_params = []

    for key, value in data.items():
        if value:
            query_params.append(f"{key}={value}")

    return '&'.join(query_params) if query_params else ''


def get_gczs(request_json):
    json = ksort(request_json)
    str = get_request_str(json)
    ys = 'e10adc3949ba59abbe52313057asd0f883e'
    str = quote(str)+ys
    print(md5_hash(str).upper())

get_gczs(request_json)