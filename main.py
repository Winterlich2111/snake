import tkinter as tk
import time


root = tk.Tk()
root.title("SNAKE")

button_amount_per_row = 15
button_pixel_size = 40
button_gap_size = 5
button_start_at = 10
button_color = "#cce"
background_color = "lightblue"
snake_head_color = "#605"
snake_tail_color = "#a37"
screen_size = button_amount_per_row*(button_pixel_size+button_gap_size) + 2 * button_start_at - button_gap_size

def change_color(coordinates, color):
    buttons[coordinates[0]][coordinates[1]].config(bg=color)






root.geometry(str(screen_size) + "x" + str(screen_size))
root.config(bg=background_color)

#Eine 2 dimensionale Liste für die Buttons machen
buttons = [[None for _ in range(button_amount_per_row)] for _ in range(button_amount_per_row)]

for line in range(button_amount_per_row):
    for row in range(button_amount_per_row):
        button = tk.Button(root, bg=button_color)
        x = button_start_at + row*(button_pixel_size+button_gap_size)
        y = button_start_at + line*(button_pixel_size+button_gap_size)
        button.place(x=x, y=y, width = button_pixel_size, height = button_pixel_size)
        buttons[row][line] = button

time.sleep(1.5)

print("hi 1.5")

#Snake initialisieren
snake_spawn_point = int(round(button_amount_per_row/2-0.5))
snake_coordinates = [snake_spawn_point, snake_spawn_point]
change_color(snake_coordinates, snake_head_color)
current_direction = "right"
spawn_new_tail = True
tail_list = [snake_coordinates]
def main_loop(spawn_new_tail):
    print("anfang schleife")
    root.after(300, main_loop)
    tail_list.append(snake_coordinates)
    if not spawn_new_tail:
        tail_list.pop[0] 
        
    if current_direction == "right":
        snake_coordinates[0] += 1
    
    elif current_direction == "left":
        snake_coordinates[0] -= 1

    elif current_direction == "up":
        snake_coordinates[1] += 1
    
    elif current_direction == "down":
        snake_coordinates[1] -= 1

    snake_coordinates[0] = snake_coordinates[0] % button_amount_per_row 
    snake_coordinates[1] = snake_coordinates[1] % button_amount_per_row 

    

    change_color(snake_coordinates, snake_head_color)
    for tail in tail_list:
        change_color(tail, snake_tail_color)

    print(snake_coordinates)
    print(tail_list)

    print("ende schleife")
    
    #spawn_new_tail = False 

    root.mainloop()

main_loop(spawn_new_tail)