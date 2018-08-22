#!/bin/python3

import sys, os

import curses

def test(stdscr):
    # Definition du curseur
    cursor_x = 0
    cursor_y = 0

    # Netoyage de l'ecran
    stdscr.clear()
    stdscr.refresh()

    # Boucle tant qu'on appuis pas sur 'q'
    k = 0
    while (k != ord('q')):

        # Efface l'affichage
        stdscr.clear()

        # Initialisation des valeurs
        height, width = stdscr.getmaxyx()

        if (k == curses.KEY_DOWN):
            cursor_y = cursor_y + 1
        elif (k == curses.KEY_UP):
            cursor_y = cursor_y - 1
        elif (k == curses.KEY_RIGHT):
            cursor_x = cursor_x + 1
        elif (k == curses.KEY_LEFT):
            cursor_x = cursor_x - 1

        # Si le curseur sort de l'ecran
        cursor_x = max(0, cursor_x)
        cursor_x = min(width - 1, cursor_x)

        cursor_y = max(0, cursor_x)
        cursor_y = min(height - 1, cursor_y)

        # Definition du texte
        title = "Titre"

        # Calcul des positions
        title_pos_x = int((width // 2) - (len(title) // 2) - (len(title) % 2))
        title_pos_y = int((height // 2) - 1)

        # Affichage
        stdscr.addstr(title_pos_y, title_pos_x, title)

        # Affichage a l'ecran
        stdscr.refresh()

        # Attente d'une nouvelle touche
        k = stdscr.getch()

curses.wrapper(test)
