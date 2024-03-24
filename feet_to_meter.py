#!/usr/bin/env python3

"""\
Original: https://tkdocs.com/tutorial/firstexample.html

型エラーが複数出るものをなくしつつglobal変数をなくした
"""

# ttk is a newer "themed widgets" that were added to Tk in 8.5.
from tkinter import ttk, StringVar, Tk


def main():
    def _calculate(*args):
        try:
            value = float(feet.get())
            value_in_meter = int(0.3048 * value * 10000.0 + 0.5) / 10000.0
            meters.set(str(value_in_meter))
        except ValueError:
            pass

    # Set up the main application window, giving it the title "Feet to Meters."
    root = Tk()
    root.title("Feet to Meters")

    # Create a frame widget, which will hold the contents of our user interface.
    #
    # Detail:
    # We could just put the other widgets in our interface directly into the main application window
    # without the intervening content frame. That's what you'll see in older Tk programs.
    # However, the main window isn't itself part of the newer "themed" widgets.
    # Its background color doesn't match the themed widgets we will put inside it.
    # Using a "themed" frame widget to hold the content ensures that the background is correct.
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky="nwes")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Create the first widget itself and then place it onscreen.
    feet = StringVar()
    feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
    feet_entry.grid(column=2, row=1, sticky="we")

    meters = StringVar()
    ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky="we")

    ttk.Button(mainframe, text="Calculate", command=_calculate).grid(column=3, row=3, sticky="w")

    ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky="w")
    ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky="e")
    ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky="w")

    # Walk through all the widgets contained within our content frame and adds a little bit of padding around each
    # so that they aren't so scrunched together.
    # We could have added these options to each grid call when we first put the widgets onscreen.
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    feet_entry.focus()
    root.bind("<Return>", _calculate)

    root.mainloop()


if __name__ == "__main__":
    main()
