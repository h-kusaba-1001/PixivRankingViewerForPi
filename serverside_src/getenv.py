import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')

# .envが存在する場合にのみ読み込む
if os.path.isfile(dotenv_path):
    load_dotenv(dotenv_path)
