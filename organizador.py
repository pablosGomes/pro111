import os

import shutil

fromdir = 'users/pablo/documents'

todir = 'users/pablo/documents/arquivo_documentos'

list_of_files = os.listdir(todir)
print(list_of_files)