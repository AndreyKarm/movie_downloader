import os
from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter import messagebox
from selenium import webdriver  #Libraries

file_path = os.getcwd()     #File path
driver = webdriver.Chrome(file_path + 'chromedriver.exe')   #WebDriver path

def clicked():  #When "Search!" is clicked
    if var.get() == 1:  # Downloading
        messagebox.showerror('Downloading', 'Couldn`t find web site where you could dowload movies beacuse i`m lazy ¯\_(ツ)_/¯')
    elif var.get() == 2:    #Watching
        driver.get("https://rezka.ag/") #Opening movie website
        searchInput = driver.find_element_by_xpath("//*[@id='search-field']")   #Find a "Search" bar
        searchInput.send_keys(movie_name.get())     #Click on "Search" button
        search_button = driver.find_element_by_xpath("//*[@id='search']/button")    #Find a "Search" button
        search_button.click()   #Click on "Search" button
        search_button = driver.find_element_by_class_name("b-content__inline_item")     #Find a movie button
        search_button.click()   #Click on movie
        search_button = driver.find_element_by_xpath("//*[@id='oframecdnplayer']/pjsdiv[17]/pjsdiv[4]")     #Find a fullscreen button
        search_button.click()       #Click on a fullscreen button
    else:
        messagebox.showerror('Selection', 'Select one of two options!')     #Error message when none of options were selected

window = Tk()
window.title("Movie Downloader")    #App name
window.geometry('400x250')      #Window resolution
var = IntVar()
lbl = Label(window, text="Print a movie name: ", font=("Arial Bold", 10)) #"Print a movie name" text
lbl.grid(column=0, row=0)
movie_name = Entry(window, width=20, )      #Entry window
movie_name.grid(column=1, row=0)
btn = Button(window, text="Search!", command=clicked)       #Button
btn.grid(column=2, row=0)

rad1 = Radiobutton(window, text='Download', value=1, variable=var)      #Radiobuttons
rad2 = Radiobutton(window, text='Watch', value=2, variable=var)
rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)

window.mainloop()