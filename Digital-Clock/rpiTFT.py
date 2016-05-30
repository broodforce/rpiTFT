from Tkinter import *
import time

def quit(event):
    print "you pressed control-forwardslash"
    root.quit()

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S',time.localtime())
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
        master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

root = Tk()
root.overrideredirect(True)

root.bind('<Control-slash>', quit)      # forward-slash
root.bind('<Control-c>', quit)      # forward-slash
root.config(cursor="none")

time1 = ''
clock = Label(root, font=('times', 48, 'bold'),fg='white', bg='black')
clock.pack(fill=BOTH, expand=1)
tick()
app=FullScreenApp(root)
root.mainloop()
