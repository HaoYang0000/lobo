import json
import xconfig


def get(name, folder=None):
    """ Simple utility to fetch configs in /afn

    To get a config at /afn/config/env.json, pass 'env', folder=''
    To get a config at /afn/config/your_app/foo.json pass 'foo'

    Args:
        name (str): Name and/or path to the config inside of /afn/config/{app_folder}/
        folder (str): Optional path to config inside of /afn/config/

    Returns:
        dict. A dictionary of the json object in the config

    Raises:
        IOError: If the config doesn't exist
    """
    if folder is None:
        folder = xconfig.APP_CONFIG_FOLDER
    with open("/afn/config/{folder}/{name}.json".format(name=name, folder=folder), 'r') as fp:
        return json.load(fp)
