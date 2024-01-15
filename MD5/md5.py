import hashlib


def md5_hash(input_string):
    md5 = hashlib.md5()
    md5.update(input_string.encode('utf-8'))
    return md5.hexdigest()


print(md5_hash('page=1&type=search_news&order=1&keyword=赖清德').upper())
# D8601786D00FA8B0FB2F900F28D7927E
# CAA2E65240639AB590C2F5FA039B0860

