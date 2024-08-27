# Converter

A site for all types of conversions using python libraries and **flask** as backend framework with python.

## Features

1. Document Converter
2. Image Converter
3. LibreOffice Converter - **Specially for office Documents**
4. Media Converter

## Dependancies Used

1. ImageMagick: For image conversions.
2. Pandoc: For document conversions (e.g., Markdown to PDF).
3. FFmpeg: For audio/video conversions.
4. LibreOffice: For converting office documents (e.g., DOCX to PDF).

##Prerequisites

1. Install Python: Ensure **Python** is installed on your system.
2. Install Flask: You can install **Flask** using pip.
   'pip install Flask'
    
# Installation

Install the dependancies by running the following command
'sudo apt-get install imagemagick pandoc ffmpeg libreoffice texlive unoconv'

1. Clone this repository in your home directory
   'git clone https://github.com/setupbox/conversions.git'
   'cd conversions'

2. Choose which service you want

A. Document Converter

1. 'cd image_converter'
2. 'python3 app.py'

B. Image Converter

1. 'cd image_converter'
2. 'python3 app.py'

C. LibreOffice Converter

1. 'cd libreoffice_converter'
2. 'python3 app.py'

D. Media Converter

1. 'cd media_converter'
2. 'python3 app.py'

Then now you can go to 'localhost:5000' on your system to acces the application and start converting your files.

#Note

Feel free to change the ports for each service in the app.py file in the last line of the host part to your preferred ports.

