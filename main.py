import tkinter as tk
from tkinter import messagebox

all_habits = []

def save_habits():
    water = water_box.get()
    sleep = sleep_box.get()
    exercise = exercise_box.get()

    if water == "" or sleep == "" or exercise == "":
        messagebox.showwarning("Missing", "Please fill all the boxes.")
        return

    today = {"Water": water, "Sleep": sleep, "Exercise": exercise}
    all_habits.append(today)

    messagebox.showinfo("Saved", "Your habits are saved.")
    water_box.delete(0, tk.END)
    sleep_box.delete(0, tk.END)
    exercise_box.delete(0, tk.END)

def show_summary():
    if len(all_habits) == 0:
        messagebox.showinfo("No Data", "No habits saved yet.")
        return

    win = tk.Toplevel(main)
    win.title("Summary")
    win.geometry("360x300")

    for num, day in enumerate(all_habits, start=1):
        text = f"Day {num}: Water={day['Water']} glasses, Sleep={day['Sleep']} hrs, Exercise={day['Exercise']} mins"
        tk.Label(win, text=text, wraplength=330, justify="left").pack(pady=3)

main = tk.Tk()
main.title("Habit Tracker")
main.geometry("400x320")

tk.Label(main, text="Habit Tracker", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(main, text="Water (glasses):").pack()
water_box = tk.Entry(main)
water_box.pack()

tk.Label(main, text="Sleep (hours):").pack()
sleep_box = tk.Entry(main)
sleep_box.pack()

tk.Label(main, text="Exercise (minutes):").pack()
exercise_box = tk.Entry(main)
exercise_box.pack()

tk.Button(main, text="Save", command=save_habits, bg="#4CAF50", fg="white", width=20).pack(pady=10)
tk.Button(main, text="Summary", command=show_summary, bg="#2196F3", fg="white", width=20).pack(pady=5)
tk.Button(main, text="Exit", command=main.quit, bg="#F44336", fg="white", width=20).pack(pady=5)

main.mainloop()
