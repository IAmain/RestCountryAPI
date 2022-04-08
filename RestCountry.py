import tkinter as tk
import requests
import json

def getinfo(head):
    user_rqst = txt_box.get()
    api = "https://restcountries.com/v3.1/name/" + user_rqst
    rqst = requests.get(api)
    rqst_data = json.loads(rqst.text) # List with dict inside
    #currency =  (rqst_data[0]["currencies"]["PEN"]["name"])
    timezones = rqst_data[0]["timezones"][0]
    capital = rqst_data[0]["capital"][0]
    population = str(rqst_data[0]["population"])
    region = rqst_data[0]["region"]
    sub_region = rqst_data[0]["subregion"]

    final_display = "\n"+ "Time Zone: " + timezones + "\n" + "Capital: " + capital + "\n" + "Population: " + population + "\n" + "Region: " + region  + "\n" + "Sub-region: " + sub_region

    label1.config(text = final_display) # display to screen for user


head = tk.Tk()

head.geometry("500x400")
head.title("Country Information Guide")

txt_font = ("poppins",12,"bold")
txt_font_2 = ("Times",14,"bold")

txt_box = tk.Entry(head, font = txt_font ) # Making of text box
txt_box.pack(pady=30) # Putting space between the space box and other widgets
txt_box.insert(0,"Enter Country")
txt_box.focus()
txt_box.bind('<Return>',func = getinfo)

label1 = tk.Label(head, font = txt_font_2)
label1.pack()

head.mainloop()
