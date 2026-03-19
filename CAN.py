import tkinter as tk
import random
from PIL import Image, ImageTk

def START():
        def START():
            for widgets in root.winfo_children():
                widgets.destroy()
        
        canvas = tk.Canvas(root, width=width, height=height, bg="white")
        canvas.pack()
    
        BOX = canvas.create_rectangle(450, 450, 1450, 850, outline="black", width=5)
    
        # Correct positions for CANs
        correct_positions = [
            (550, 500),   # CAN1
            (800, 500),   # CAN2
            (1050, 500),  # CAN3
            (1300, 500)   # CAN4
        ]
    
        # Randomize initial positions
        can_positions = correct_positions.copy()
        random.shuffle(can_positions)
    
        cans = []
    
        status_label = tk.Label(root, text="", font=("Arial", 20), bg="white", fg="black")
        status_label.place(x=width//2 - 150, y=400)
    
        def check_win():
            correct = sum([can_positions[i] == correct_positions[i] for i in range(4)])
            if correct == 4:
                status_label.config(text="You Win!")
            else:
                status_label.config(text=f"{correct} CAN(s) correctly placed")
    
        def on_can_click(idx):
            nonlocal selected_can
            if selected_can is None:
                selected_can = idx
            else:
                # Swap positions
                x1, y1 = can_positions[selected_can]
                x2, y2 = can_positions[idx]
                cans[selected_can].place(x=x2, y=y2)
                cans[idx].place(x=x1, y=y1)
                can_positions[selected_can], can_positions[idx] = can_positions[idx], can_positions[selected_can]
                selected_can = None
                check_win()
    
        selected_can = None
    
        CAN1 = tk.Button(root, image=REDBULL_CAN, bg="white", borderwidth=0, command=lambda: on_can_click(0))
        CAN1.place(x=can_positions[0][0], y=can_positions[0][1])
        cans.append(CAN1)
    
        CAN2 = tk.Button(root, image=MONSTER_CAN, bg="white", borderwidth=0, command=lambda: on_can_click(1))
        CAN2.place(x=can_positions[1][0], y=can_positions[1][1])
        cans.append(CAN2)
    
        CAN3 = tk.Button(root, image=HELL_CAN, bg="white", borderwidth=0, command=lambda: on_can_click(2))
        CAN3.place(x=can_positions[2][0], y=can_positions[2][1])
        cans.append(CAN3)
    
        CAN4 = tk.Button(root, image=PRIME_CAN, bg="white", borderwidth=0, command=lambda: on_can_click(3))
        CAN4.place(x=can_positions[3][0], y=can_positions[3][1])
        cans.append(CAN4)
    
        back_btn = tk.Button(root, text="BACK", font=("Arial", 20), fg="BLACK", command=BACK, bg=rand_2)
        back_btn.place(x=width//2 - 90, y=height//2 + 320, width=220, height=80)
    
        check_win()

def HOW_TO_PLAY():
    for widgets in root.winfo_children():
        widgets.destroy()

    inst = tk.Label(
        root,
        text="Instructions:\n"
             "1) Use the mouse to select the CAN which you want to move.\n"
             "2) Now click another CAN where you want to place the first CAN.\n"
             "3) If you place all the CANs in correct position you win the game.",
        bg=rand_1, fg="WHITE", font=("Arial", 24)
    )
    inst.place(x=480, y=250)

    back_btn = tk.Button(root, text="BACK", font=("Arial", 20), fg="BLACK", command=BACK, bg=rand_2)
    back_btn.place(x=width//2 - 90, y=height//2 + 300, width=220, height=80)

def BACK():
    for widgets in root.winfo_children():
        widgets.destroy()
    main_menu()

def main_menu():
    PLAY_btn = tk.Button(root, text="PLAY", font=("Arial", 24), fg="WHITE", command=START, bg=rand_1)
    PLAY_btn.place(x=width//2 - 90, y=height//2 - 60, width=220, height=80)

    H_T_Pbtn = tk.Button(root, text="HOW TO PLAY", font=("Arial", 20), fg="WHITE", command=HOW_TO_PLAY, bg=rand_2)
    H_T_Pbtn.place(x=width//2 - 90, y=height//2 + 40, width=220, height=80)

    TITLE = tk.Label(root, text="Place the CAN on correct position", font=("Arial", 36), fg="Black", bg=rand_3)
    TITLE.place(x=width//2 - 340, y=height//2 - 500)

root = tk.Tk()
root.title("Place the CAN on correct position")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}")

COLOURS = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan", "magenta", "lime"]
rand_1 = random.choice(COLOURS)
rand_2 = random.choice(COLOURS)
rand_3 = random.choice(COLOURS)

# Load and resize images
REDBULL = Image.open("redbull.png")
REDBULL_CAN = ImageTk.PhotoImage(REDBULL.resize((200, 120)))

MONSTER = Image.open("monster.png")
MONSTER_CAN = ImageTk.PhotoImage(MONSTER.resize((120, 120)))

HELL = Image.open("hell.png")
HELL_CAN = ImageTk.PhotoImage(HELL.resize((120, 120)))

PRIME = Image.open("prime.png")
PRIME_CAN = ImageTk.PhotoImage(PRIME.resize((80, 160)))  # Reduced size

main_menu()
root.mainloop()