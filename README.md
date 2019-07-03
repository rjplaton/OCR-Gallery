# OCR-Gallery
A Python static site generator that generates an image gallery based on a directory of images and also detects text and faces within each image.



### Current tech stack:
- Python
	- Tesseract / Pytesseract (Optical Character Recognition Library)
	- dlib (Machine Learning / “AI” library)
	- face_recognition (Face Recognition Library)
	- Pillow (Imaging Library)
- Bootstrap
- CSS
- HTML


### Instructions on updating the website:
1. Add jpg files to /images/: 
2. Run build.py to automtically apply changes to all user facing "full pages" in /docs/ including running Tesseract and Face Recognition
```sh
$ python3 build.py
```
