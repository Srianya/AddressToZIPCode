# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import config
from tkinter import *

# get latitude and longitude from an address
def get_ltd_lng():
    params = {
        'address': 'oshiwara industerial center goregaon west mumbai',
        'sensor': 'false',
        'region': 'india',
        'key': config.api_key,
    }
    response = requests.get(url="https://maps.googleapis.com/maps/api/geocode/json",params=params)
    response.raise_for_status()
    data = response.json()
    geodata = dict()
    geodata['lat'] = data['results'][0]['geometry']['location']['lat']
    geodata['lng'] = data['results'][0]['geometry']['location']['lng']
    #print(data)
    return (geodata['lat'],geodata['lng'])


def get_zipcode(latlng):

    params = {
        'latlng': f"{latlng[0]},{latlng[1]}",
        'key': config.api_key,
    }
    response = requests.get(url="https://maps.google.com/maps/api/geocode/json",params=params)
    data = response.json()
    print(data)

if __name__ == '__main__':
    latlng = get_ltd_lng()
    get_zipcode(latlng)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Address to zipcode")
window.config(padx=50, pady=50)

# Add a canvas
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
address_text = canvas.create_text(150, 207, text="Address", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Address Entry
address_entry = Entry(width=35)
address_entry.grid(row=1, column=0)
address_entry.focus()

zipcode_button = Button(text="Get me the zip code", highlightthickness=0)
zipcode_button.grid(row=2, column=0)
window.mainloop()
