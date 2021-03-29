import os

dir_path = "../../PDFs"

for root, dirs, files in os.walk(dir_path):
    continue
print(files)