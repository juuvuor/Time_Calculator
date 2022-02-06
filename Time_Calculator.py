import imp
from sqlite3 import Time
from tkinter import *
from tkinter.ttk import *
import datetime
import platform
import os
import time
import pandas as pd





start = time.time()
window = Tk()
window.title("Clock")
window.geometry('500x350')
start_time = 0

# shows clock in the window
def clock():
    date_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_label.config(text = date_time)
    time_label.after(1000, clock)


# changes time form to minutes
def split_time(aika):
    hour,min,sec = aika.split(':')
    hour = int (hour)
    min = int (min)
    sec = int (sec)
    minutes = min + (hour*60) + (sec/60)
    return minutes


# shapes time to look like in digital clock
def form_time(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    time_form = (("{0}:{1}:{2}".format(int(hours),int(mins),int (sec))))
    split_time(time_form)
    return("{0} h {1} min {2} sec".format(int(hours),int(mins),int (sec)))

# start time counting and shows text
def start():
    global start_time
    start_time = time.time()
    start_text = Label(window, text = "you start studying" )
    start_text.pack()

# this ends time counting, shows text and time in window
def end():
    end_time = time.time()
    global start_time
    total_time = end_time - start_time
    time_form = form_time(total_time)
    exel(time_form)
    text = "you studiet {}"
    aika = Label(window, text = text.format(time_form) )
    aika.pack()


#main
time_label = Label(font = 'calibri 40 bold', foreground = 'black')
time_label.pack(anchor='center')
start_tab = Button(command = start, text="start")
end_tab = Button(command = end, text="end")
start_tab.pack()
end_tab.pack()

#ecel 
def exel(time_form):
    df = pd.DataFrame({'Aika' : [time_form]})
    writer = pd.ExcelWriter('Time.xlsx', 
                   engine ='xlsxwriter')
    df.to_excel(writer, sheet_name ='Sheet1')
  
    # Close the Pandas Excel writer
    # object and output the Excel file.
    writer.save()

clock()
window.mainloop()
