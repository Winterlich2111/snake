import tkinter as tk
import time

root = tk.Tk()
root.title("SNAKE")

button_amount_per_row = 15
button_pixel_size = 40
button_gap_size = 5
button_start_at = 10
button_color = "#cce"
screen_size = button_amount_per_row*(button_pixel_size+button_gap_size) + 2 * button_start_at - button_gap_size

root.geometry(str(screen_size) + "x" + str(screen_size))

#Eine 2 dimensionale Liste für die Buttons machen
buttons = [[None for _ in range(button_amount_per_row)] for _ in range(button_amount_per_row)]

for line in range(button_amount_per_row):
    for row in range(button_amount_per_row):
        button = tk.Button(root, bg=button_color)
        x = button_start_at + row*(button_pixel_size+button_gap_size)
        y = button_start_at + line*(button_pixel_size+button_gap_size)
        button.place(x=x, y=y, width = button_pixel_size, height = button_pixel_size)
        buttons[row][line]

time.sleep(1.5)

root.mainloop()