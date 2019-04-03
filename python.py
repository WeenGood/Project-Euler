import tkinter as tk

class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.firstButton = tk.Button(self, text = 'Гоу', command = self.filesCreate)
        self.firstButton.grid()
        self.entrS = tk.Entry(self)
        self.entrS.grid()
        self.entr = tk.Entry(self)
        self.entr.grid()
        self.quitButton = tk.Button(self, text = 'Quit', command = self.quit)
        self.quitButton.grid()
        
    def filesCreate(self):
        name = 'solution'
        i = self.entrS.get()
        end = self.entr.get()
        while i < int(end):
            name = name + str(i) + '.py'
            open(name, 'w')
            name = 'solution'
            i += 1
        

app = Application()
app.master.title('Sample application')
app.mainloop()