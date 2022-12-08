#MEME Project
This project uses Python to demonstrate 
1. read in image files, resize, and add a text on top of the image.
2. import texts from different types of files - csv, pdf, txt, and doc, the imported texts will be the texts used on the images
3. lastly, use Flask to present the information on the web interface

##Getting Started
This project uses virtual environment to manage the required packages. To run this project with the required packages, 
1. create virtual env by typing python3 -m venv venv
2. type source venv/bin/activate
3. type pip install -r requirements.txt

To run this project from Web UI, at command prompt, type 
* python app.py, this should display some messages on the screen saying your app is available at localhost:5000 
* from the web browser, type localhost:5000, the meme UI should show up

To run this project from command prompt, type 
* python meme.py.  Meme.py takes 3 optional parameters below.  If you choose not to provide any parameters, it will pick a random image from src/_data/photos/dog, and a random quote from src/_data/DogQuotes
  * --path this is the image you want to use
  * --quote this is the quote you want to print on the image
  * --author this is the quote author you want to print on the image
  
* Example to use specified image/quote/author:
  * python meme.py --path 'imgs/nature.jpg' --author Anonymous --quote 'Amazing Nature'
  * The output image will be stored under src/tmp/

##Project Folder Layout 
1. src/_data
   * DogQuotes contains all the quotes/author files will be imported, one of these will be randomly picked and displayed on the image 
   * photos/dog contain all images will be picked randomly 
2. src/fonts
   * fonts used on the image text
3. src/imgs
   * test images used when I ran meme.py with a specified image
4. src/MemeEngine
   * MemeEngine.py - this program includes a MemeEngine class, this class read in an image file, resize the image and generate a meme with text on it
   * You could run python MemeEngine/MemeEngine.py to generate a meme in src/static folder
5. src/QuoteEngine
   * Ingester.py - this class will choose the correct document type py to use based on document type
   * IngesterInterface.py - abstract base class with a single parse method to import the quotes
   * CSVImporter.py - realizing the IngesterInterface class, import csv type of quotes
   * DocxImporter.py - realizing the IngesterInterface class, import docx type of quotes
   * PDFImporter.py - realizing the IngesterInterface class, import pdf type of quotes
   * TxtImporter.py - realizing the IngesterInterface class, import txt type of quotes
6. src/static
   * web UI output images
7. src/templates
   * web files provided by Udacity to display the images from web browser
8. src/tmp
   * meme.py output images
9. app.py - web main program
10. meme.py - command prompt main program
11. requirements.txt - installation requirement
12. testQuote.py

##Technologies used
1. Python
2. HTML

##Author
Lisa Wang

##Credits
Initial base code is provided by Udacity
Pet Images and quote sources are also provided by Udacity 

##Versions
This is the first version 

