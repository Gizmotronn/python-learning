# https://realpython.com/python-gui-with-wxpython/
import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        self.Show()
        panel = wx.Panel(self)

        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        my_btn = wx.Button(panel, label='Press Me', pos=(5, 55)) # creates button with wxPython library, label "Press Me"        

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop() # main loop for app - waits for events to occur and then executes what's in the loop       




"""
app = wx.App() # Creates & Intializes an app
frame = wx.Frame(parent=None, title="Hello World") # app window with title/caption "Hello World"
frame.Show() # displays frame
app.MainLoop() # main loop for app - waits for events to occur and then executes what's in the loop
"""