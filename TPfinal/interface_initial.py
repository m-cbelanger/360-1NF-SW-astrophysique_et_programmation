import tkinter as tk

def effacer_tout(form1, form2,form3,form4,label1,y_min,y_max):
    form1.delete(0, tk.END)
    form2.delete(0, tk.END)
    form3.delete(0, tk.END)
    form4.delete(0, tk.END)
    form4.insert(0,"0")
    label1.config(text = "")
    y_min.delete(0, tk.END)
    y_max.delete(0, tk.END)
    y_min.insert(0,"-10")
    y_max.insert(0,"10")



def affichage_fenetre():
    
    fenetre = tk.Tk()
    fenetre.title("Résolution d'équations")
    fenetre.geometry("500x350")

    choix = tk.IntVar(value=1)

    # Les 3 Entry où entrer les équations
    form1 = tk.Entry(fenetre, width=30)
    form2 = tk.Entry(fenetre, width=30)
    form3 = tk.Entry(fenetre, width=30)

    # Les 2 endroits où modifier le maximum et minimum en y
    ymin_label = tk.Label(fenetre, text="y min")
    ymax_label = tk.Label(fenetre, text="y max")
    ymin_entry = tk.Entry(fenetre, width=10)
    ymax_entry = tk.Entry(fenetre, width=10)
    ymin_entry.insert(0, "-10")
    ymax_entry.insert(0, "10")

    # La valeur initiale pour la résolution d'équations avec méthode de Newton
    form4 = tk.Entry(fenetre, width=10)
    label4 = tk.Label(fenetre, text="Valeur initiale", width=15, height=2)
    form4.insert(0, "0")
    
    # Pour afficher les réponses
    label1 = tk.Label(fenetre, text="")
    
    # Bouton radio pour indiquer si on a une ou 2 équations (se sélectionne dès qu'on clique dans l'une des Entry en-dessous
    radio1 = tk.Radiobutton(fenetre, text="Une équation", variable=choix, value=1)
    radio2 = tk.Radiobutton(fenetre, text="Deux équations", variable=choix, value=2)
    # Obliger le radio bouton à changer selon la boîte de texte choisie.
    form1.bind("<FocusIn>", lambda event: choix.set(1))
    form2.bind("<FocusIn>", lambda event: choix.set(2))
    form3.bind("<FocusIn>", lambda event: choix.set(2))
    
    # Étiquette invisible dans laquelle apparaîtra la réponse
    reponse = tk.Label(fenetre, text="")

    # boutons qui déclenchent les actions de résoudre la ou les équations, créer le graphique ou effacer tout.
    # Aucune action associée pour le moment
    btn1 = tk.Button(fenetre, text="Résoudre", width=10, height=2)
    btn2 = tk.Button(fenetre, text="Graphique", width=10, height=2)
    btn3 = tk.Button(fenetre, text="Effacer tout", width=10, height=2,
                     command=lambda: effacer_tout(form1, form2, form3, form4, label1,ymin_entry,ymax_entry))

    # Disposition des objets dans la fnêtre
    fenetre.grid_columnconfigure(0, weight=1)
    fenetre.grid_columnconfigure(1, weight=1)
    fenetre.grid_columnconfigure(2, weight=1)

    radio1.grid(row=0, column=0, sticky="w", padx=10, pady=5)
    radio2.grid(row=0, column=1, sticky="w", padx=5, pady=5)

    form1.grid(row=1, column=0, padx=10, pady=5)
    form2.grid(row=1, column=1, padx=5, pady=5)

    ymin_label.grid(row=2, column=0, sticky="w", padx=10)
    ymin_entry.grid(row=2, column=0, padx=(70, 5), pady=2)

    form3.grid(row=2, column=1, padx=5, pady=5)

    ymax_label.grid(row=3, column=0, sticky="w", padx=10)
    ymax_entry.grid(row=3, column=0, padx=(70, 5), pady=2)

    label4.grid(row=4, column=0, padx=5, pady=10, sticky="w")
    form4.grid(row=4, column=1, padx=5, pady=10)

    reponse.grid(row=5, columnspan=3, padx=10, pady=10, sticky="ew")

    btn1.grid(row=6, column=0, padx=10, pady=10, sticky="ew")
    btn2.grid(row=6, column=1, padx=10, pady=10, sticky="ew")
    btn3.grid(row=7, column=0, padx=10, pady=10, sticky="ew")

    fenetre.mainloop()
    
# Appel de fonction à déplacer
affichage_fenetre()
