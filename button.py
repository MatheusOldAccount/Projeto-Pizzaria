import tkinter


class HoverButton(tkinter.Button):
    def __init__(self, master, **kw):
        tkinter.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = '#ba0601'

    def on_leave(self, e):
        self['background'] = self.defaultBackground
