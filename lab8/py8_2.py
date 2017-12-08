import Tkinter as tk
import tkMessageBox

class App(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.entry = tk.Entry(self, justify = "center", width = 0, font="Helvetica 20")
        self.button = tk.Button(self, text = "START", command = self.count_down)

        self.grid()
        self.entry.grid(row=0, column=0, sticky="EW")
        self.button.grid(row=1, column=0, sticky="EW")

    def count_down(self):
        value = int(self.entry.get())
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value-1)
        if(value > 1):
            self.entry.after(1000, self.count_down)
        else:
            tkMessageBox.showinfo("The countdown has ended", "Time is up!")


app = App(None)
app.mainloop()
