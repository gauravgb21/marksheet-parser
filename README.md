# Marksheet-parser
 A marksheet-parser which can parse marksheets of class 10th and 12th of any recognized education board of india. 

## Prerequisites
Download python 3.6

Add the python folder to the path variable to run the python file from commandline.

Download Tesseract OCR and install it in your system

Install pillow

pillow is an image processing library in python

```
pip install pillow
```

Install pytesseract

```
pip install pytesseract
```

## Input
Student data should be stored in the "inputcsv.csv" file in the following format:

Student ID , First Name , Last Name , Marksheet Image Name

Image folder will contain marksheet images referred by the "inputcsv.csv" file. Images should be in black and white form with a minimum image resolution of 300dpi to get the best result.
Images should be in jpg format.
## Output
"outputcsv.csv" will contain the information of each student in the following format:

Student ID , First Name , Last Name , Marksheet Image Name , Board Name

## Running the file
open command prompt 

move to the directory where the "app.py" file is present

type the following command:
```
python app.py
```
