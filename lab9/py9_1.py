from __future__ import division
import Tkinter as tk
import logging


class Calculator(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.entry = tk.Entry(self)
        self.entry.grid(row = 0, column = 0, columnspan = 3, sticky = "news")
        self.make_buttons()

    def clear(self):
        self.entry.delete(0, tk.END)

    def action(self, args):
        self.entry.insert(tk.END, args)

    def equals(self):
        try:
            self.value = eval(self.entry.get())
            logging.info("Working as expected, result is {}".format(self.value))
        except SyntaxError:
            logging.error("Name Error!")
            self.entry.delete(0, tk.END)
            self.entry.insert(0, 'Invalid Input!')
        except NameErrror:
            logging.error("Syntax Error!")
            self.entry.delete(0, tk.END)
            self.entry.insert(0, 'Invalid Input!')
        else:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.value)

    def make_buttons(self):
        tk.Button(self ,text = "C", command = lambda:self.clear()).grid(row = 0, column = 3, sticky = "news")
        tk.Button(self ,text = "7", command = lambda:self.action(7)).grid(row = 1, column = 0, sticky = "news")
        tk.Button(self ,text = "8", command = lambda:self.action(8)).grid(row = 1, column = 1, sticky = "news")
        tk.Button(self ,text = "9", command = lambda:self.action(9)).grid(row = 1, column = 2, sticky = "news")
        tk.Button(self ,text = "/", command = lambda:self.action('/')).grid(row = 1, column = 3, sticky = "news")
        tk.Button(self ,text = "4", command = lambda:self.action(4)).grid(row = 2, column = 0, sticky = "news")
        tk.Button(self ,text = "5", command = lambda:self.action(5)).grid(row = 2, column = 1, sticky = "news")
        tk.Button(self ,text = "6", command = lambda:self.action(6)).grid(row = 2, column = 2, sticky = "news")
        tk.Button(self ,text = "x", command = lambda:self.action('*')).grid(row = 2, column = 3, sticky = "news")
        tk.Button(self ,text = "1", command = lambda:self.action(1)).grid(row = 3, column = 0, sticky = "news")
        tk.Button(self ,text = "2", command = lambda:self.action(2)).grid(row = 3, column = 1, sticky = "news")
        tk.Button(self ,text = "3", command = lambda:self.action(3)).grid(row = 3, column = 2, sticky = "news")
        tk.Button(self ,text = "-", command = lambda:self.action('-')).grid(row = 3, column = 3, sticky = "news")
        tk.Button(self ,text = "0", command = lambda:self.action(0)).grid(row = 4, column = 0, sticky = "news")
        tk.Button(self ,text = ".", command = lambda:self.action('.')).grid(row = 4, column = 1, sticky = "news")
        tk.Button(self ,text = "=", command = lambda:self.equals()).grid(row = 4, column = 2, sticky = "news")
        tk.Button(self ,text = "+", command = lambda:self.action('+')).grid(row = 4, column = 3, sticky = "news")


app = Calculator(None)
logging.basicConfig(filename = "logi.log", level=logging.INFO)
app.mainloop()
