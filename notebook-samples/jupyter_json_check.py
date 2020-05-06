
"""
Purpose: 
Date created: 2020-05-05

Contributor(s):
    Mark M.
"""


import glob
import os
import json
from jupyter_core.paths import jupyter_config_path


def check_all():
    for folder in jupyter_config_path():
        for root, _, files in os.walk(folder):
            for f in files:
                if f.endswith("json"):
                    json_pth = os.path.join(root, f)
                    try:
                        with open(json_pth, 'r') as f:
                            json.load(f)
                        print(f"File {json_pth} is OK.")
                    except json.decoder.JSONDecodeError:
                        print('Failed JSON file is: ', json_pth)


if __name__ == "__main__":
    check_all()