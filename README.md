# Address-to-Zipcode

Address-to-Zipcode is a GUI-based, desktop-executable, offline-storage compatible,
Python application.

## Features

- Use your Google API geocoding and reverse-geocoding keys
- Get latitude and longitude from address
- Get zipcode from latitude and longitude
- Returns zipcode

## Tech

Address-to-Zipcode uses a number of modules to work properly:

- [Tkinter] -  standard Python interface to the Tcl/Tk GUI toolkit!
- [Python] - Programming language.
- [Google API: geocoding] - give information about latitude and longitude using given address
- [Google API: reverse geocoding] - give zipcode using latitude and longitude values
- [Pyinstaller] - to convert file into .exe

## Prerequisites

Before you continue, ensure you have met the following requirements:
1. You have installed the version of Python3.
2. Replace "api_key" in config.py with your own google API key.
```bash
touch config.py
api_key = YOUR GOOGLE API KEY
key = config.api_key 
```
## Quickstart
1. Run on command-line
    ```bash
    python3 main.py
    ```
    or 
Clone and run main.py
    ```
    git clone https://github.com/Asaxena-2120/API-Address-to-zipcode.git
    ```
2. Download the executable from [here](https://github.com/Asaxena-2120/API-Address-to-zipcode/releases)

## Installation
1. Install requests, Tkinter modules
 - Address-to-Zipcode requires [Python](https://www.python.org/downloads/) to run.
 - Address-to-Zipcode requires [requests](https://pypi.org/project/requests/) to run.
 - Address-to-Zipcode requires [Tkinter](https://docs.python.org/3/library/tkinter.html) to run.

    Install the dependencies.

    ```sh
    pip install requests
    pip install tk
    ```
## Repository Overview

├── README.md
├── main.py
├── ltld_zip.py
├── background.png
├── ui.py
├── requirements.txt
└── main.exe

## Additional Resources
 - https://learnpython.com/blog/python-requirements-file/ - to add requirements.txt
  - https://medium.com/black-tech-diva/hide-your-api-keys-7635e181a06c - hiding the keys using .gitignore
  - https://stackoverflow.com/questions/5585957/get-latlng-from-zip-code-google-maps-api
  - https://www.youtube.com/watch?v=UZX5kH72Yx4 - use pyinstaller to convert main into .exe
  - Adding requirements.txt using 
    ```
    pip install pipreqs
    run pipreqs command in the project folder
    INFO: Successfully saved requirements file in \requirements.txt.
   ```
   ```
Adding the main.exe as executable file
   ```
   pyinstaller --onefile -w main.py
   ```
   
## Issues

| Issue| Solution  | 
| :---:   | :-: | 
| Get and API key | [link](https://support.google.com/googleapi/answer/6158862?hl=en)| 
| How to pass API_key as a parameter | store it as a string| 
| sending latitude and longitude values together in latlng paramater of reverse geocing api request | convert them into an format string|
| Hide your api key | created a config file and added that file to .gitignore|


**Individual Contributor!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Python]: <https://www.python.org/downloads/>
   [Tkinter]: <https://docs.python.org/3/library/tkinter.html>
   [Google API: geocoding]: <https://developers.google.com/maps/documentation/geocoding/requests-geocoding>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [Google API: reverse geocoding]: <https://developers.google.com/maps/documentation/geocoding/requests-reverse-geocoding#required_parameters>
   [Pyinstaller]: <https://www.youtube.com/watch?v=UZX5kH72Yx4>
  
 
