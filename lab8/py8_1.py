import Tkinter as tk

class App(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)

        self.color_var = tk.StringVar(value = "1")
        self.r_button1 = self.makeRadioButton("red")
        self.r_button2 = self.makeRadioButton("green")
        self.r_button3 = self.makeRadioButton("blue")

        self.button = tk.Button(self, text = "button")
        self.button.pack(anchor = "n")

    def changeColor(self):
        self.button.config(fg = self.color_var.get())

    def makeRadioButton(self, color):
        radio_button = tk.Radiobutton(self, text = color, variable = self.color_var, value = color, command = self.changeColor)
        radio_button.pack(anchor="nw")
        return radio_button


app = App(None)
app.mainloop()
