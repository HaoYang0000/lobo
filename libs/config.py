import json
import os


def get(name):
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
    with open(f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/config/{name}.json", 'r') as fp:
        return json.load(fp)
