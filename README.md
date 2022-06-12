Download [here](https://github.com/Asaxena-2120/API-Address-to-zipcode/releases)
- get an API key
- how to format API key to pass it as a parameters
- how to send lat and long values together in latlng paramater of reverse geocing api request
- tried sending latlng as a tuple- didn't work
- then tried sending them as individual values and directly embedding them into the url
- didn't work
- converted it to f string - it worked
- to hide the api_key - created a config file and added that file to .gitignore folder
- used TKinter to make a UI with a canvas
- Adding requirements.txt using 
  - pip install pipreqs
  - pipreqs . 
  - INFO: Successfully saved requirements file in .\requirements.txt
- Added the main.exe as executable file -- pyinstaller --onefile -w main.py
- then copy the file from dist folder to the folder where all the dependencies are paresent
- added status check for returned JSON data.
- Added message if user entered an incomplete address.
- Making code modular
- Resources used
  - https://learnpython.com/blog/python-requirements-file/ - to add requirements.txt
  - https://developers.google.com/maps/documentation/geocoding/requests-geocoding - to get latitude and longitude from address
  - https://developers.google.com/maps/documentation/geocoding/requests-reverse-geocoding#required_parameters - to get zipcode from latitude and longitude
  - https://medium.com/black-tech-diva/hide-your-api-keys-7635e181a06c - hiding the keys using .gitignore
  - https://stackoverflow.com/questions/5585957/get-latlng-from-zip-code-google-maps-api
  - https://www.youtube.com/watch?v=UZX5kH72Yx4 - use pyinstaller to convert main into .exe
  - nsis- to convert full .exe plus dependents into one folder
