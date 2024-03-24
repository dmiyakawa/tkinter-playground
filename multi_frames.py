from tkinter import ttk, Tk

# c.f. https://stackoverflow.com/questions/15235794

"""\
"""

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("複数のフレームの切り替え")
        self.geometry("400x300")

        self.container = ttk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="スタートページ", font=("Arial", 18))
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="ページ1へ",
                             command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="ページ2へ",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="ページ1", font=("Arial", 18))
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="スタートページへ",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()


class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="ページ2", font=("Arial", 18))
        label.pack(pady=10, padx=10)

        button = ttk.Button(self, text="スタートページへ",
                            command=lambda: controller.show_frame(StartPage))
        button.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
