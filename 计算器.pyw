try:
    from tkinter import *

    class App(Tk):
        def __init__(self):
            self.master = Tk()
            self.master.title("计算器")
            self.master.resizable(0, 0)
            self.initWidgets()
            self.expr = None
            self.master.mainloop()

        def initWidgets(self):
            Label(text='双击“=”清屏').pack(side=TOP)
            self.show = Label(relief=SUNKEN,
                              font=('Courier New', 29),
                              width=19,
                              bg='white',
                              anchor=E)
            self.show.pack(side=TOP, pady=10)
            p = Frame(self.master)
            p.pack(side=TOP)
            names = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+',
                     '-', '*', '/', '.', '=')
            for i in range(len(names)):
                b = Button(p, text=names[i], font=(
                    'Verdana', 20), width=6, fg='black', bg='white')
                b.grid(row=i // 4, column=i % 4)
                b.bind('<Button-1>', self.click)
                if b['text'] == '=':
                    b.bind('<Double-1>', self.clean)

        def click(self, event):
            if (event.widget['text'] in ('0', '1', '2', '3', '4', '5', '6',
                                         '7', '8', '9', '.')):
                self.show['text'] = self.show['text'] + event.widget['text']
            elif (event.widget['text'] in ('+', '-', '*', '/')):
                if self.expr is None:
                    self.expr = self.show['text'] + event.widget['text']
                else:
                    self.expr = self.expr + self.show['text'] + event.widget[
                        'text']
                self.show['text'] = ''
            elif (event.widget['text'] == '=' and self.expr is not None):
                self.expr = self.expr + self.show['text']
                self.show['text'] = str(eval(self.expr))
                self.expr = None

        def clean(self, event):
            self.expr = None
            self.show['text'] = ''
    App()
except Exception as e:
    print(e)
