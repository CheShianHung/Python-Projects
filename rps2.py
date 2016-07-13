#!C:\Users\a2219\AppData\Local\Programs\Python\Python35-32\ python

import tkinter
import random


def gui():

    player_choice=tkinter.IntVar()

    rps_window = tkinter.Toplevel()
    rps_window.title('Rock, Paper, Scissors')

    rps_frame = tkinter.Frame(rps_window, padx=3, pady=12, width=300, height=250)
    rps_frame.grid(column=0, row=0, sticky=('N' + 'W' + 'E' + 'S'))
    rps_frame.columnconfigure(0, weight=1)
    rps_frame.rowconfigure(1, weight=1)

    tkinter.Label(rps_frame, text='Player').grid(column=1, row=1, sticky='W')
    tkinter.Radiobutton(rps_frame, text='Rock', variable=player_choice, value=1).grid(column=1, row=2, sticky='W')
    tkinter.Radiobutton(rps_frame, text='Paper', variable=player_choice, value=2).grid(column=1, row=3, sticky='W')
    tkinter.Radiobutton(rps_frame, text='Scissors', variable=player_choice, value=3).grid(column=1, row=4, sticky='W')

if __name__ == '__main__':
    gui()
