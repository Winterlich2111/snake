import tkinter as tk
import random

def key_handler(key):
    global current_key
    current_key = key.keysym

def change_color(coordinates, color):
    buttons[coordinates[0]][coordinates[1]].config(bg=color)


#Configurable Things
button_amount_per_row = 15
button_pixel_size = 40
button_gap_size = 5
button_start_at = 10
button_color = "#cce"
background_color = "lightblue"
snake_head_color = "#f00"
snake_tail_color = "#000"
apple_color = "#afa"


#Setup

root = tk.Tk()
root.title("SNAKE")
root.bind("<KeyPress>", key_handler)

screen_size = button_amount_per_row*(button_pixel_size+button_gap_size) + 2 * button_start_at - button_gap_size
current_key = "Right"
score = 0


root.geometry(str(screen_size) + "x" + str(screen_size)+"+50+50")
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

#Snake initialisieren
snake_spawn_point = int(round(button_amount_per_row/2-0.5))
snake_coordinates = [snake_spawn_point, snake_spawn_point]
change_color(snake_coordinates, snake_head_color)
current_direction = "Right"
spawn_new_tail = True
tail_list = []

#Ersten Apfel
while True:
    apple = [random.randint(0, button_amount_per_row-1), random.randint(0, button_amount_per_row-1)]
    if not apple in tail_list:
        break
change_color(apple, apple_color)

def main_loop():
    global spawn_new_tail, snake_coordinates, tail_list, current_direction, apple, score
    death = False

    #überprüfen dass er nicht 180° Drehung macht (oben nach unten, links nach rechts, etc.)
    if current_key in ["Left", "Right", "Up", "Down"]:
        directions = [current_direction, current_key]
        left_right = "Left" in directions and "Right" in directions
        up_down = "Up" in directions and "Down" in directions
        if not left_right and not up_down:
            current_direction = current_key #Richtung auf den aktuellen Key-Press ändern
    

    #Apple Management
    if snake_coordinates == apple:
        spawn_new_tail = True
        while True:
            apple = [random.randint(0, button_amount_per_row-1), random.randint(0, button_amount_per_row-1)]
            if not apple in tail_list and not apple == snake_coordinates:
                break
        change_color(apple, apple_color)
        score += 1


    #Tail aktualisieren
    if not spawn_new_tail:
        change_color(tail_list[0], button_color)
        tail_list.pop(0) 
    tail_list.append(snake_coordinates.copy())
    
    #Kopf aktualisieren
    if current_direction == "Right":
        snake_coordinates[0] += 1 
    elif current_direction == "Left":
        snake_coordinates[0] -= 1
    elif current_direction == "Up":
        snake_coordinates[1] -= 1
    elif current_direction == "Down":
        snake_coordinates[1] += 1

    snake_coordinates[0] = snake_coordinates[0] % button_amount_per_row 
    snake_coordinates[1] = snake_coordinates[1] % button_amount_per_row 

    if snake_coordinates in tail_list or current_key == "Escape":
        death = True

    if not death: 
        change_color(snake_coordinates, snake_head_color)
        for tail in tail_list:
            change_color(tail, snake_tail_color)

    
    spawn_new_tail = False

    if not death:
        root.after(200, main_loop)
    else:
        final_button = tk.Button(root, text="GAME OVER - SCORE: "+str(score), bg="#c79")
        final_button.place(relx=0.5,rely=0.4, width=200, height=100, anchor = "center")
        quit_button = tk.Button(root, text="QUIT", bg="#f55", command = root.destroy)
        quit_button.place(relx=0.5,rely=0.6, width=200, height=100, anchor = "center")

main_loop()
root.mainloop()