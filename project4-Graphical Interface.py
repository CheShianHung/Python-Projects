#!C:\Users\a2219\AppData\Local\Programs\Python\Python35-32\ python

import tkinter

import rps2
import hangman
import pokerdice

root = tkinter.Tk()
root.title('3-in-1 Game Collection')

mainframe = tkinter.Frame(root, height=250, width=500, bg='gray')
mainframe.pack_propagate(0)
mainframe.pack(padx=2, pady=2)

intro = tkinter.Label(mainframe, text='Welcome. Please select one of the following games to play.', bg='gray')
intro.pack(side='top', pady=15)

rps_button = tkinter.Button(mainframe, text='Rock Paper Scissors', command=rps2.gui,
                            bg='black', fg='white')
rps_button.pack(side='top', pady=10)

hangman_button = tkinter.Button(mainframe, text='Hangman', command=hangman.game, bg='black', fg='white')
hangman_button.pack(side='top', pady=10)

pd_button = tkinter.Button(mainframe, text='Poker Dice', command=pokerdice.game, bg='black', fg='white')
pd_button.pack(side='top', pady=10)

exit_button = tkinter.Button(mainframe, text='Exit', command=root.destroy, fg='red', bg='black')
exit_button.pack(side='top', pady=10)

root.mainloop()
