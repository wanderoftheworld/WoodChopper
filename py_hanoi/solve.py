import tkinter as tk
import time

def move_disks(n, source, auxiliary, target):
    # Base case: if the number of disks is 0, do nothing
    if n == 0:
        return
    
    # Step 1: Move n-1 disks from source to auxiliary
    move_disks(n - 1, source, target, auxiliary)
    
    # Step 2: Move the largest disk from source to target
    paint_disks(source, auxiliary)
    tk.update()
    time.sleep(1)
    paint_disks(target, source)
    tk.update()

    # Step 3: Move n-1 disks moved earlier to target
    move_disks(n - 1, auxiliary, source, target)

def paint_disks(pole1, pole2):
    disks = [disks[i] for i in range(len(disks)) if disks[i]["h"] > pole1.get()]
    if len(disks) > 0:
        for disk in disks:
            canvas.delete(disk["id"])
    disks = [disks[i] for i in range(len(disks)) if disks[i]["h"] > pole2.get()]
    for disk in disks:
            disk_id = canvas.create_rectangle(pole2.get() - 10, disk["h"] - disk["h"] / 3, pole2.get() + 10, disk["h"] + disk["h"] / 3, outline="black", fill="white")
            disk["id"] = disk_id
            disks[i]["id"] = disk_id

def start_game():
    play = input("Press 'y' to play the game: ").lower()
    if play == 'y':
        move_disks(3, "A", "B", "C")

# Define the canvas
canvas = tk.Canvas(width=700, height=500)
canvas.grid(row=0, column=0)
xa, ya, xb, yb, xc, yc = 100, 100, 100, 200, 100, 300

# Define the disks
disks = [[100, 100, 30], [115, 150, 15], [130, 200, 10]]

# Define the buttons
tk.Button(text="Start", command=start_game).grid(row=2, column=0)
tk.Button(text="Step", command=lambda: move_disks(3, "A", "B", "C")).grid(row=2, column=1)

tk.mainloop()

canvas.pack()
canvas.create_line(xa, ya, xb, ya, xc, xc, xa, ya)
canvas.create_line(xb, yb, xc, yc, xa, yc)
canvas.create_line(xa, ya, xa, yc)
canvas.create_line(xb, yb, xb, yc)
canvas.create_line(xc, yc, xc, ya)

# Fill each pole's canvas portions with disk's white color
canvas.create_rectangle(xa, ya, xa + 25, ya + 25, outline="black", fill="white")
canvas.create_rectangle(xb, yb, xb + 25, yb + 25, outline="black", fill="white")
canvas.create_rectangle(xc, yc, xc + 25, yc + 25, outline="black", fill="white")
