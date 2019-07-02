pages = []

#discover all the jpg files in the /images/ directory and save as a list
import glob
all_jpg_files = glob.glob("images/*.jpg")

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
        "output_path": "docs/" + name_only + ".html",
        "output_filename": name_only + ".html",
    })
    #copy file over to the /docs/images/ path
    shutil.copy(file_path, "docs/images/" + file_name)
    print('pages list item added for:', file_path)

#using jinja templating, update values per image page and save them into an html file withing /docs/ 
print(pages)
from jinja2 import Template
for page in pages:
    template_html = open("templates/image_base.html").read()
    template = Template(template_html)
    output = template.render(
        image_source=page['image_path'],
        title=page['title'],
        image_text= 'image text will go here',
    )
    open(page['output_path'], 'w+').write(output)
    print('Successfully processed:', page['image_path'], ' | Saved to:', page['output_path'])