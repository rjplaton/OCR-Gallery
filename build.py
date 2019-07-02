pages = []


#discover all the jpg files in the /images/ directory and save as a list
import glob
all_jpg_files = glob.glob("images/*.jpg")
#print(all_jpg_files)


#extract useful information from each jpg file
import os
import shutil
for jpg_file in all_jpg_files:
    file_path = jpg_file
    file_name = os.path.basename(file_path)
    name_only, extension = os.path.splitext(file_name)
    #append jpg file information to a dict in the pages list
    pages.append({
        "image_path": file_path,
        "image_path_docs": "docs/" + file_path,
        "title": name_only,
        "output": "docs/" + name_only + ".html",
        "output_filename": name_only + ".html",
    })
    #copy file over to the /docs/images/ path
    shutil.copy(file_path, "docs/images/" + file_name)
    print('Successfully processed:', file_path)
