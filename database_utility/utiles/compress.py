import gzip
import shutil

import os

def compress_file(file_path):
    compressed_path=file_path+ ".gz"

    with open(file_path,"rb") as f_in:
        with gzip.open(compressed_path,"wb") as f_out:
            shutil.copyfileobj(f_in,f_out)


    os.remove(file_path)

    return compressed_path