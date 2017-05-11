import sys
import os
from io import BytesIO
from configparser import ConfigParser
from mriya.data_connector import get_conn_param

MRIYA_CONFIG_ROOT = '/mriya_service/mriya-master/'

def config_name(username):
    return os.path.join(MRIYA_CONFIG_ROOT, str(username) + '-config.ini')

def config_choices(username):
    items = config_items(username)
    return [(name, items[name].url_prefix)for name in items]

def config_items_f(config_fp):
    res= {}
    config = ConfigParser()
    config.read_file(config_fp)
    config_fp.seek(0)
    sys.stderr.write(str(config.keys()))
    for name in config:
        if 'DEFAULT' != name.upper():
            res[name] = get_conn_param(config[name])
    return res

def config_items(username):
    conf_path = config_name(username)
    try:
        with open(conf_path, 'r') as conf_f:
            return config_items_f(conf_f)
    except IOError:
        return {}

def save_uploaded_config_f(f, username):
    conf_path = config_name(username)
    with open(conf_path, 'w') as new_f:
        for chunk in f.chunks():
            new_f.write(chunk)

