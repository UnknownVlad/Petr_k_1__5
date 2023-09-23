import glob
import secrets
import string

import os
from tkinter.filedialog import asksaveasfile



from tkinter import END, filedialog, messagebox
from tkinter import ttk


import customtkinter
import pygame

from game_logic.control import control
from game_logic.game_board import Game_board
from some_data import data


class App(customtkinter.CTk):
    def __init__(self):




        super().__init__()

        self.protocol('WM_DELETE_WINDOW', self.on_close)

        self.title("image_example.py")
        self.geometry("200x220")


        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        #self.entry_row.grid(row=0, column=0, sticky = 'nw', padx=(20, 0), pady=20)

        self.button_start = customtkinter.CTkButton(master=self, text="Start", width=100,
                                                    command=self.start,
                                                    font=customtkinter.CTkFont(family='Calibry', size=20), fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.button_start.grid(row=0, column=0, padx=10, pady=20, sticky ='sw')




        self.entry_row = customtkinter.CTkEntry(master=self, width=100,
                                                font=customtkinter.CTkFont(family='Calibry', size=15),
                                                placeholder_text="ROW")
        self.entry_row.grid(row=1, column=0, padx =10, pady=10, sticky ='sw')

        self.entry_col = customtkinter.CTkEntry(master=self, width=100,
                                                font=customtkinter.CTkFont(family='Calibry', size=15),
                                                placeholder_text="COL")
        self.entry_col.grid(row=2, column=0, padx=10, pady=10, sticky ='sw')

        self.entry_score = customtkinter.CTkEntry(master=self, width=100,
                                                font=customtkinter.CTkFont(family='Calibry', size=15),
                                                placeholder_text="SCORE")
        self.entry_score.grid(row=3, column=0, padx=10, pady=10, sticky='sw')

    def start(self):
        r = 10
        c = 10
        s = 12345

        if self.entry_row.get() != '':
            r = int(self.entry_row.get())

        if self.entry_col.get() != '':
            c = int(self.entry_col.get())

        if self.entry_score.get() != '':
            s = int(self.entry_score.get())
        self.destroy()

        pygame.init()
        screen = pygame.display.set_mode((r*2*data.r(), c*2*data.r()))

        b = Game_board(r, c, s)
        c = control()
        winner = False
        while c.events(b):
            screen.fill(data.background_color())
            b.output(screen)
            if b.tmp_score >= b.score:
                winner = True
            pygame.display.flip()
            if winner:
                pygame.display.set_caption("WINNER")
            else:
                pygame.display.set_caption(str(b.tmp_score) + " is "+str(b.score))

        print("Ur win")
    def on_close(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
