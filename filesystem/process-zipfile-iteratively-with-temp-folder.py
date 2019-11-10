
"""
Purpose: 
Date created: 2019-09-18

Contributor(s):
    Mark M.
"""

from os import path
import zipfile
import tempfile
import pandas as pd

### Replace with path to zipfile, including extension
full_zip_path = r'C:\path\to\zipfile.zip'

def process_zipfile():
    ### Using try-except in the event that a file doesn't exist.
    try:
        ### Using nested with statements to keep temp folder open
        ### while each file processs.
        with tempfile.TemporaryDirectory() as temp_dir:
            with zipfile.ZipFile(full_zip_path, 'r') as zf:
                file_list = [i.filename for i in zf.infolist()]
                zf.extractall(temp_dir)
                
            ### Filename is static, but could be formatted based on zipfile contents.
            filename = 'my-file-name.txt'
            
            ### Dataframe isn't necessary; process a file however you'd like.
            df = pd.read_csv(path.join(temp_dir, filename), low_memory = False)
        try:
            zf.close()
        except:
            pass

        return df

    except FileNotFoundError:
        ### Print out a bit of info if an error is raised.
        tmp_name = full_zip_path.split('\\')[-1]
        print(f'Could not find File in zipfile {tmp_name}')
        pass
