# https://realpython.com/python-gui-with-wxpython/
import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
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