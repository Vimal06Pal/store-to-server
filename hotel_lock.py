##
##
##
##from tkinter import Tk,Button,Entry
##import random
##
##class hotel:
##    def __init__(self,win):
##        self.win=win
##        win.title('first gui')
##
##        self.entry=Entry(win)
##        self.entry.pack()
##
##        self.click_button=Button(win,text='click',command=self.click)
##        self.click_button.pack()
##        
##        self.confirm_button=Button(win,text='click',command=self.confirm)
##        self.confirm_button.pack()
##
##    def click(self):
##        self.r=str(random.randint(0,100000))
##        print(self.r)
##
##    def confirm(self):
##        if self.r==self.entry.get():
##            print('access')
##        else:
##            print('retry')
##
##root=Tk()
##my_gui_hotel=hotel(root)
##root.mainloop()
##
##        
from tkinter import Tk,Button,Entry
from Adafruit_IO import Client, RequestError, Feed
import os
import webbrowser
import urllib.request as url
import random
import time
ADAFRUIT_IO_KEY = '7eb04125db3b4b68874eeb02c0843e21'

ADAFRUIT_IO_USERNAME = 'Vivek_sharma'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    foo = aio.feeds('happy')
except RequestError: # Doesn't exist, create a new feed
    feed = Feed(name="happy")
    foo = aio.create_feed(feed)

class hotel:
    def __init__(self,win):
        self.win=win
        win.title('first gui')

        self.entry=Entry(win)
        self.entry.pack()

        self.click_button=Button(win,text='click',command=self.click)
        self.click_button.pack()
        
        self.confirm_button=Button(win,text='click',command=self.confirm)
        self.confirm_button.pack()

    def click(self):
        self.r=str(random.randint(1111,9999))
        aio.send_data(foo.key, self.r)
        data = aio.receive(foo.key)
        data=data.value
        print(data)
        print(self.r)
        self.s=time.time()
    def confirm(self):
        a=time.time()
        d=a-self.s;
        print(int(d),'sec')
        if d<=90:
            if self.r==self.entry.get():
                print('access')
            else:
                print('retry')
        elif d>90:
            print('expire')
            print('retry')

root=Tk()
my_gui_hotel=hotel(root)
root.mainloop()
