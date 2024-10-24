import tkinter as tk

root = tk.Tk()
root.title("Movie Ticket Booking")
root.geometry("500x500")
root.configure(bg="#ADD8E6")  # Light Blue background color

def show_frame(frame):
    frame.pack()

def hide_frame(frame):
    frame.pack_forget()

def on_movie_selection(movie):
    # Handle the movie selection logic here
    global selected_movie
    selected_movie = movie
    print(f"Selected movie: {movie['name']}")

def on_done_movie():
    hide_frame(movie_frame)
    show_frame(seat_frame)

# Movies with resized images and larger dimensions
movies = [
    {"name": "Interstellar", "image_path": "D:/Coding/FULL CS PRJECT ARUN HARIHARAN 2024/interstellar.gif", "width": 200, "height": 200},
    {"name": "Gladiator", "image_path": "D:/Coding/FULL CS PRJECT ARUN HARIHARAN 2024/gladiator.gif", "width": 200, "height": 200},
    {"name": "Inception", "image_path":  "D:/Coding/FULL CS PRJECT ARUN HARIHARAN 2024/inception.gif", "width": 400, "height": 400},
    {"name": "Hacksaw Ridge", "image_path": "D:/Coding/FULL CS PRJECT ARUN HARIHARAN 2024/hacksaw_ridge.gif", "width": 400, "height": 400},
    {"name": "Whiplash", "image_path": "D:/Coding/FULL CS PRJECT ARUN HARIHARAN 2024/whiplash.gif", "width": 400, "height": 400},
    {"name": "Dunkirk", "image_path": "D:/Coding/FULL CS PRJECT ARUN HARIHARAN 2024/dunkirk.gif", "width": 400, "height": 400},
    {"name": "Tenet", "image_path": "D:/Coding/FULL CS PRJECT ARUN HARIHARAN 2024/tenet.gif", "width": 400, "height": 400},
    {"name": "Oppenheimer", "image_path": "D:/Coding/FULL CS PRJECT ARUN HARIHARAN 2024/oppenheimer.gif", "width": 400, "height": 400},
     {"name": "The Dark Knight", "image_path": "D:/Coding/FULL CS PRJECT ARUN HARIHARAN 2024/the_dark_knight.gif","width": 400, "height": 400}
]

# Movie Frame
movie_frame = tk.Frame(root, bg="#ADD8E6")  # Light Blue background color

for i, movie in enumerate(movies):
    # Use PhotoImage to load and display images
    img = tk.PhotoImage(file=movie["image_path"])
    
    # Resize the image by subsampling
    img = img.subsample(5)  # Change the factor as needed
    
    button = tk.Button(movie_frame, image=img, text=movie["name"], compound="top", command=lambda m=movie: on_movie_selection(m), font=("Helvetica", 12, "bold"))
    button.img = img  # To prevent image from being garbage collected
    button.grid(row=i // 3, column=i % 3, padx=10, pady=10)  # Reduced padding

# ... (the rest of your existing code)

done_button_movie = tk.Button(movie_frame, text="Done", command=on_done_movie, font=("Helvetica", 12, "bold"))
done_button_movie.grid(row=(len(movies) // 3) + 1, column=0, columnspan=3, pady=10)  # Place the "Done" button below the movie buttons

# Initial frame to show
show_frame(movie_frame)

# Seat Frame
seat_frame = tk.Frame(root, bg="#FFDAB9")  # Peachpuff
seat_frame.grid_rowconfigure(9, weight=1)
seat_frame.grid_columnconfigure(10, weight=1)

def create_seat_buttons():
    seat_buttons = []
    for row in range(8):
        for col in range(10):
            button = tk.Button(seat_frame, text=f"{chr(65 + row)}{col + 1}", bg="#FFE4B5", command=lambda r=row, c=col: select_seat(r, c))
            button.grid(row=row, column=col, padx=5, pady=5)
            seat_buttons.append(button)
    return seat_buttons

selected_seats = []

def select_seat(row, col):
    seat = f"{chr(65 + row)}{col + 1}"
    if seat in selected_seats:
        selected_seats.remove(seat)
        seat_buttons[row * 10 + col].config(bg="#FFE4B5")
    else:
        selected_seats.append(seat)
        seat_buttons[row * 10 + col].config(bg="#90EE90")  # Light Green

# Create seat buttons
seat_buttons = create_seat_buttons()

done_button_seat = tk.Button(seat_frame, text="Next", command=lambda: on_done_seat(), font=("Helvetica", 12, "bold"), bg="#90EE90")  # Light Green
done_button_seat.grid(row=9, column=0, columnspan=10, sticky="nsew", padx=20, pady=10)

def on_done_seat():
    hide_frame(seat_frame)
    show_frame(snack_frame)

# Snack Frame
snacks = {"Popcorn": 150, "Coke": 50, "Nachos": 150, "Fries": 150, "Burger": 200}
snack_frame = tk.Frame(root, bg="#87CEEB")  # SkyBlue
snack_frame.grid_rowconfigure(len(snacks) + 2, weight=1)

selected_snacks = []
total_price = 0  # Initialize total_price globally

def update_price():
    global total_price
    number_of_seats=len(selected_seats)
    total_price = 350*number_of_seats # Movie ticket cost
    total_price += sum(snacks[snack] for snack in selected_snacks)
    total_price_label.config(text=f"Total Price: ₹{total_price}")

def on_check(snack):
    if snack in selected_snacks:
        selected_snacks.remove(snack)
    else:
        selected_snacks.append(snack)
    update_price()

frame_label = tk.Label(snack_frame, text="Select Snacks", font=("Helvetica", 20, "bold"), bg="#87CEEB", fg="white")
frame_label.grid(row=0, column=0, columnspan=len(snacks), sticky="nsew")

# Create snack checkboxes
for i, (snack, price) in enumerate(snacks.items()):
    checkbox = tk.Checkbutton(snack_frame, text=f"{snack} - ₹{price}", variable=tk.IntVar(), command=lambda s=snack: on_check(s), font=("Helvetica", 12), bg="#87CEEB", fg="white")
    checkbox.grid(row=i + 1, column=0, padx=20, pady=10)

total_price_label = tk.Label(snack_frame, text="Total Price: ₹0", font=("Helvetica", 14), bg="#87CEEB", fg="white")
total_price_label.grid(row=len(snacks) + 1, column=0, columnspan=len(snacks), pady=10)

done_button_snack = tk.Button(snack_frame, text="Next", command=lambda: on_done_snack(), font=("Helvetica", 14, "bold"), bg="#90EE90")  # Light Green
done_button_snack.grid(row=len(snacks) + 2, column=0, columnspan=len(snacks), sticky="nsew", padx=20, pady=10)

def on_done_snack():
    hide_frame(snack_frame)
    show_frame(ticket_frame)
    generate_ticket()

# Ticket Frame
ticket_frame = tk.Frame(root, bg="#F08080")  # Light Coral
ticket_frame.grid_rowconfigure(9, weight=1)
ticket_frame.grid_columnconfigure(0, weight=1)

def generate_ticket():
    global selected_movie
    ticket_label = tk.Label(ticket_frame, text="--- Movie Ticket ---\nMovie: {}\nSeats: {}\nSnacks: {}\nTotal Price: ₹{}".format(
        selected_movie["name"], ", ".join(selected_seats), ", ".join(selected_snacks), total_price
    ), font=("Helvetica", 16), bg="#F08080", fg="white")
    ticket_label.pack()

done_button_ticket = tk.Button(ticket_frame, text="Done", command=lambda: on_done_ticket(), font=("Helvetica", 12, "bold"), bg="#90EE90")  # Light Green
done_button_ticket.pack(pady=20)

def on_done_ticket():
    hide_frame(ticket_frame)

# Initial frame to show
show_frame(movie_frame)

root.mainloop()
