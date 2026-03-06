import tkinter as tk

    
n_iterations = 300
facteur = 200

xmin = -2.1
xmax = 0.6
ymin = -1.2
ymax = 1.2

taille_x = int((xmax - xmin)*facteur)
taille_y = int((ymax - ymin)*facteur)

dx = float((xmax - xmin)/taille_x)
dy = float((ymax - ymin)/taille_y)

fenetre = tk.Tk()
canvas = tk.Canvas(fenetre, width = taille_x, height = taille_y)
canvas.pack()

y = ymax
for j in range(taille_y):
    x = xmin
    for i in range(taille_x):

        c = complex(x,y)
        c0 = c

        for k in range(n_iterations):
            c = c*c + c0
            if abs(c) > 2:
                break

            if k == n_iterations-1:
                canvas.create_line(i,j,i,j+1)

        x += dx

    y -= dy
    canvas.update()

fenetre.mainloop()