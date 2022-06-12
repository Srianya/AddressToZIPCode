from tkinter import *
from ltld_zip import ZipCode


class Interface:

    def __init__(self,zipcode: ZipCode):
        self.zip = zipcode
        self.window = Tk()
        self.window.title("Address to zipcode")
        self.window.config(padx=50, pady=50)

        # Add a canvas
        self.canvas = Canvas(width=300, height=414)
        self.background_img = PhotoImage(file="background.png")
        self.canvas.create_image(150, 207, image=self.background_img)
        self.address_text = self.canvas.create_text(150, 100, text="Address", width=250, font=("Arial", 30, "bold"), fill="white")
        self.card_word_input_address = self.canvas.create_text(150, 150, text="", font=("Ariel", 10, "bold"))
        self.card_word_result_zipcode = self.canvas.create_text(150, 263, text="", font=("Ariel", 10, "bold"))
        self.canvas.grid(row=0, column=0)

        # Address Entry
        self.address_entry = Entry(width=35)
        self.address_entry.grid(row=1, column=0)
        self.address_entry.focus()

        # get address from user via entry and send it to get_ltd_lng() to get the latitude and longitude
        self.zipcode_button = Button(text="Get me the zip code", highlightthickness=0, font=("Ariel", 10, "bold"), command=self.button_pressed)
        self.zipcode_button.grid(row=2, column=0)
        # press get the zip code button to get the zipcode for corresponding zipcode for the address
        self.window.mainloop()

    def button_pressed(self):

        if self.zip.get_zipcode(self.address_entry.get()):
            self.canvas.itemconfig(self.card_word_input_address, text=f"{self.zip.ADDRESS}", fill="Black")
            self.canvas.itemconfig(self.card_word_result_zipcode, text=f"{self.zip.zipcode}", fill="green")
            self.address_entry.delete(0, END)
        else:
            self.canvas.itemconfig(self.card_word_input_address, text=f"{self.zip.ADDRESS}", fill="Black")
            self.canvas.itemconfig(self.card_word_result_zipcode,
                                             text="You have entered incomplete address",
                                             fill="green")
            self.address_entry.delete(0, END)

