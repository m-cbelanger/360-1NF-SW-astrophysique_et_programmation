import tkinter as tk


n_iterations = 50
facteur = 200

xmin = -1
xmax = 1
ymin = -1.2
ymax = 1.2

taille_x = int((xmax - xmin)*facteur)
taille_y = int((ymax - ymin)*facteur)

dx = float((xmax - xmin)/taille_x)
dy = float((ymax - ymin)/taille_y)

c0 = complex(0.285, 0.010)


fenetre = tk.Tk()
canvas = tk.Canvas(fenetre, width = taille_x, height = taille_y)
canvas.pack()

y = ymax
for j in range(0, taille_y):
    x = xmin
    for i in range(0,taille_x+1):
        c = complex(x,y)
        for k in range(0, n_iterations):
            c = c*c + c0
            if abs(c) > 2:
                break
            if k == (n_iterations -1):
                canvas.create_line(i,j,i,j+1)
        x = x + dx
    y = y - dy
    canvas.update()
    
    
fenetre.mainloop()

