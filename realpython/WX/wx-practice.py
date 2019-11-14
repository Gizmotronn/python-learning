# https://realpython.com/python-gui-with-wxpython/
import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Hello World')
        self.Show()
        panel = wx.Panel(self) # panels are REQUIRED for WINDOWS
        my_sizer = wx.BoxSizer(wx.VERTICAL) # box sizer for absolute positioning & resizing windows/widgets

        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5)) # text control - allows text to be created & edited
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        my_btn = wx.Button(panel, label='Press Me', pos=(5, 55)) # creates button with wxPython library, label "Press Me". Where to place the button widget (pos function). This is called ABSOLUTE POSITIONING        
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Show() # from lines 11-16 (from self.text_ctrl to now (self.Show()), this resizes the text box in "Press Me")

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