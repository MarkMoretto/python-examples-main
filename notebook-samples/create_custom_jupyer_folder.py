
"""
Purpose: Create custome jupyter javascript path.
Date created: 2020-03-14

Contributor(s):
    Mark M.
"""

import os
from time import sleep
from jupyter_core.paths import jupyter_config_dir as jcd


if __name__ == "__main__":

    js_text = 'alert("hello world from custom.js!")'

    # Get
    jupyter_dir = jcd()
    
    custom_js_folder = os.path.join(jupyter_dir, "custom")
    custom_js_path = os.path.join(custom_js_folder, "custom.js")
    if os.path.isdir(custom_js_folder):
        if os.path.isfile(custom_js_path):
            print("Found custom.js file!")
            with open(custom_js_path) as f:
                print(f.read())
    else:
        print("Custom\custom.js not found. Create new? [Y or N]")
        user_input = input(">>>")
        if user_input[:1].lower() in ('y'):
            while True:
                os.makedirs(custom_js_folder, exist_ok=True)
                break
            with open(custom_js_path, "w") as f:
                f.write(js_text)
            print(f"New custom.js file created at '{custom_js_path}'!")
        print("Goodbye!")
        sleep(2)
        exit(1)


