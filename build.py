pages = []

#discover all the jpg files in the /images/ directory and save as a list
import glob
all_jpg_files = glob.glob("images/*.jpg")



#extract useful information from each jpg file to create pages list
import os
import shutil
from PIL import Image
import pytesseract

for jpg_file in all_jpg_files:
    file_path = jpg_file
    file_name = os.path.basename(file_path)
    name_only, extension = os.path.splitext(file_name)
    
    #use tesseract to extract text from the page and append to pages list
    image = Image.open(jpg_file)
    detected_text = pytesseract.image_to_string(image, lang="eng")
    if detected_text == '':
        image_text = ("Could not find text in the image")
    else:
	    image_text = (detected_text)
    
    #append jpg file information to a dict in the pages list
    pages.append({
        "image_path": file_path,
        "image_path_docs": "docs/" + file_path,
        "title": name_only,
        "output_path": "docs/" + name_only + ".html",
        "output_filename": name_only + ".html",
        "image_text": image_text,
    })
    #copy file over to the /docs/images/ path
    shutil.copy(file_path, "docs/images/" + file_name)
    print('pages list item added for:', file_path)


#using jinja templating, update values per image page and save them into an html file withing /docs/ 
from jinja2 import Template
for page in pages:
    template_html = open("templates/image_base.html").read()
    template = Template(template_html)
    output = template.render(
    	pages=pages,
        image_source=page['image_path'],
        title=page['title'],
        image_text=page['image_text'],
    )
    open(page['output_path'], 'w+').write(output)
    print('Successfully processed:', page['image_path'], ' | Saved to:', page['output_path'])



