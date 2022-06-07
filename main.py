# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import config
from tkinter import *
latlng=tuple()
ADDRESS = ""
# get latitude and longitude from an address
def get_ltd_lng():
    global ADDRESS
    ADDRESS = address_entry.get()
    #print(f"address: {ADDRESS}")
    canvas.itemconfig(card_word_input_address, text=f"{ADDRESS}", fill="Black")
    params = {
        'address': ADDRESS,
        'sensor': 'false',
        'region': 'india',
        'key': config.api_key,
    }
    response = requests.get(url="https://maps.googleapis.com/maps/api/geocode/json",params=params)
    response.raise_for_status()
    # TODO: check if response is OK then only proceed
    data = response.json()
    if data['status'] == 'OK':
        geodata = dict()
        geodata['lat'] = data['results'][0]['geometry']['location']['lat']
        geodata['lng'] = data['results'][0]['geometry']['location']['lng']
        #print(data)
        #print((geodata['lat'],geodata['lng']))
        return (geodata['lat'],geodata['lng'])
    else:
        return None


def get_zipcode():
    latlng = get_ltd_lng()
    if latlng:
        params = {
            'latlng': f"{latlng[0]},{latlng[1]}",
            'key': config.api_key,
        }
        response = requests.get(url="https://maps.google.com/maps/api/geocode/json",params=params)
        data = response.json()
        # TODO: check if response is OK then only proceed

        if data['status'] == 'OK':
            result = (data['results'][0]['address_components'])
            zipcode = ""
            for diction in result:
                if diction['types'] == ['postal_code']:
                    zipcode = diction['long_name']
                    break
            #canvas.itemconfig(card_word_input_address, text=f"{ADDRESS}", fill="Orange")
            canvas.itemconfig(card_word_result_zipcode, text=f"{zipcode}", fill="green")
            address_entry.delete(0, END)
    else:
        canvas.itemconfig(card_word_result_zipcode, text="You have entered incomplete address", fill="green")

#if __name__ == '__main__':


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Address to zipcode")
window.config(padx=50, pady=50)

# Add a canvas
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
address_text = canvas.create_text(150, 207, text="Address", width=250, font=("Arial", 30, "bold"), fill="white")
card_word_input_address = canvas.create_text(150, 250, text="", font=("Ariel", 10, "bold"))
card_word_result_zipcode = canvas.create_text(150, 263, text="", font=("Ariel", 10, "bold"))
canvas.grid(row=0, column=0)

# Address Entry
address_entry = Entry(width=35)
address_entry.grid(row=1, column=0)
address_entry.focus()

# TODO: get address from user via entry and send it to get_ltd_lng() to get the latitude and longitude
zipcode_button = Button(text="Get me the zip code", highlightthickness=0,command=get_zipcode)
zipcode_button.grid(row=2, column=0)
# TODO: press get the zip code button to get the zipcode for corresponding zipcode for the address
#latlng = get_ltd_lng()
#get_zipcode(latlng)
window.mainloop()
#latlng = get_ltd_lng()
#get_zipcode(latlng)
#print(f"latlng: {latlng}")
