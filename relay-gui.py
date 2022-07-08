#!/usr/bin/python

"""Relay Commander GUI.

GUI Program for controlling HID USB relay boards.

Usage:
    python relay-gui.py
"""

from functools import partial

import tkinter as tk
import tkinter.ttk as ttk

import relay


def main() -> None:
    """Main.
    """

    # Relay Commander instance.
    rcmd = relay.Relay()
    status = rcmd.state(0)
    print(status)
    # Window.
    window = tk.Tk()

    # General font.
    general_font = "Calibri"

    # Label.
    lbl = tk.Label(window,
                   text="Relay Channels",
                   font=(general_font,
                         16))
    lbl.place(x=140,
              y=16)

    # Styles.
    sto = ttk.Style()
    # ON
    sto.configure('W.TButton',
                  font=(general_font,
                        10),
                  foreground='Green')
    # OFF
    sto.configure('TButton',
                  font=(general_font,
                        10),
                  foreground='Red')

    # Buttons
    for i in range(0, 8):
        btn = ttk.Button(window,
                         text="{0} ON ".format(i + 1),
                         width=5,
                         style='W.TButton',
                         command=partial(rcmd.state,
                                         i + 1,
                                         1))
        btn.place(x=i * 48 + 20,
                  y=64)

    for i in range(0, 8):
        btn = ttk.Button(window,
                         text="{0} OFF".format(i + 1),
                         width=5,
                         style='TButton',
                         command=partial(rcmd.state,
                                         i + 1,
                                         0))
        btn.place(x=i * 48 + 20,
                  y=92)

    btn = ttk.Button(window,
                     text="ALL ON",
                     width=53,
                     style='W.TButton',
                     command=partial(rcmd.state,
                                     0,
                                     1))
    btn.place(x=20,
              y=142)

    btn = ttk.Button(window,
                     text="ALL OFF",
                     width=53,
                     style='TButton',
                     command=partial(rcmd.state,
                                     0,
                                     0))
    btn.place(x=20,
              y=170)

    # Window settings.
    window.title('Relay Commander GUI')
    window.geometry("420x220+10+20")
    window.resizable(False,
                     False)
    window.mainloop()


if __name__ == "__main__":
    main()