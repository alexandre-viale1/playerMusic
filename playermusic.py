import tkinter as tk
import pygame
from tkinter import filedialog

def bt_play():
    pygame.mixer.music.play()

def bt_pause():
    pygame.mixer.music.pause()

def bt_stop():
    pygame.mixer.music.stop()

def bt_volume_plus():
    volume = pygame.mixer.music.get_volume()
    if volume < 1.0:
        pygame.mixer.music.set_volume(volume + 0.1)

def bt_volume_moins():
    volume = pygame.mixer.music.get_volume()
    if volume > 0.0:
        pygame.mixer.music.set_volume(volume - 0.1)

def bt_loop():
    pygame.mixer.music.play(-1)

def bt_choix():
    track = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    pygame.mixer.music.load(track)

def bt_ajouter_piste():
    track = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
    listbox_musique.insert(tk.END, track)

def bt_supprimer_piste():
    selection = listbox_musique.curselection()
    if selection:
        listbox_musique.delete(selection[0])

fenetre = tk.Tk()
fenetre.title("Audio Player")
fenetre.geometry("220x235")

bouton_play = tk.Button(fenetre, text="Play", command=bt_play)
bouton_play.grid(row=0,column=1, padx=5, pady=5)
bouton_pause = tk.Button(fenetre, text="Pause", command=bt_pause)
bouton_pause.grid(row=1,column=1, padx=5, pady=5)
bouton_stop = tk.Button(fenetre, text="Stop", command=bt_stop)
bouton_stop.grid(row=2,column=1, padx=5, pady=5)
bouton_volume_plus = tk.Button(fenetre, text="Volume +", command=bt_volume_plus)
bouton_volume_plus.grid(row=1,column=0, padx=5, pady=5)
bouton_volume_moins = tk.Button(fenetre, text="Volume -", command=bt_volume_moins)
bouton_volume_moins.grid(row=2,column=0, padx=5, pady=5)
bouton_loop = tk.Button(fenetre, text="Loop", command=bt_loop)
bouton_loop.grid(row=1,column=2, padx=5, pady=5)
bouton_choix_musique = tk.Button(fenetre, text="Choose Track", command=bt_choix)
bouton_choix_musique.grid(row=2,column=2, padx=5, pady=5)

listbox_musique = tk.Listbox(fenetre, height=5)
listbox_musique.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

bouton_ajouter_piste = tk.Button(fenetre, text="Add Track", command=bt_ajouter_piste)
bouton_ajouter_piste.grid(row=4, column=0, padx=5, pady=5)
bouton_supprimer_piste = tk.Button(fenetre, text="Remove Track", command=bt_supprimer_piste)
bouton_supprimer_piste.grid(row=4, column=2, padx=5, pady=5)

pygame.mixer.init()
fenetre.mainloop()