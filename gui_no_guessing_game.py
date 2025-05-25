import tkinter as tk
from tkinter import ttk # Import ttk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        # Configure padding for the main window
        self.master.configure(padx=20, pady=20)

        # Use ttk themed style
        style = ttk.Style()
        style.theme_use('clam') # Example theme, others like 'alt', 'default', 'classic' exist

        # --- Difficulty Frame --- 
        difficulty_frame = ttk.LabelFrame(master, text="Difficulty", padding=(10, 5))
        difficulty_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)

        self.difficulty_var = tk.IntVar()
        self.difficulty_var.set(1)

        ttk.Radiobutton(difficulty_frame, text="Easy (1-50)", variable=self.difficulty_var, value=1).grid(row=0, column=0, sticky="w", padx=5)
        ttk.Radiobutton(difficulty_frame, text="Medium (1-100)", variable=self.difficulty_var, value=2).grid(row=1, column=0, sticky="w", padx=5)
        ttk.Radiobutton(difficulty_frame, text="Hard (1-200)", variable=self.difficulty_var, value=3).grid(row=2, column=0, sticky="w", padx=5)

        # --- Game Control --- 
        self.start_button = ttk.Button(master, text="Start/Restart Game", command=self.start_game)
        self.start_button.grid(row=1, column=0, columnspan=2, pady=5)

        # --- Guessing Area --- 
        guessing_frame = ttk.Frame(master, padding=(10, 5))
        guessing_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)

        ttk.Label(guessing_frame, text="Enter your guess:").grid(row=0, column=0, padx=5, pady=5)
        self.guess_entry = ttk.Entry(guessing_frame, width=10)
        self.guess_entry.grid(row=0, column=1, padx=5, pady=5)
        self.guess_entry.bind('<Return>', self.check_guess) # Bind Enter key
        
        self.guess_button = ttk.Button(guessing_frame, text="Guess", command=self.check_guess)
        self.guess_button.grid(row=0, column=2, padx=5, pady=5)

        # --- Feedback Area --- 
        self.feedback_label = ttk.Label(master, text="Select difficulty and start the game!", font=("Helvetica", 10))
        self.feedback_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.number_to_guess = None
        self.attempts = 0
        self.low = 0
        self.high = 0

        # Initial state: disable guessing until game starts
        self.guess_entry.config(state=tk.DISABLED)
        self.guess_button.config(state=tk.DISABLED)

    def start_game(self):
        difficulty = self.difficulty_var.get()
        if difficulty == 1:
            self.low, self.high = 1, 50
        elif difficulty == 2:
            self.low, self.high = 1, 100
        elif difficulty == 3:
            self.low, self.high = 1, 200
        else: # Should not happen with radio buttons, but good practice
            messagebox.showerror("Error", "Invalid difficulty selected.")
            return

        self.number_to_guess = random.randint(self.low, self.high)
        self.attempts = 0
        self.feedback_label.config(text=f"I'm thinking of a number between {self.low} and {self.high}.")
        self.guess_entry.config(state=tk.NORMAL) # Enable entry
        self.guess_button.config(state=tk.NORMAL) # Enable button
        self.guess_entry.delete(0, tk.END) # Clear previous guess
        self.guess_entry.focus() # Set focus to the entry field

    def check_guess(self, event=None):
        # Check if game has started
        if self.number_to_guess is None:
            messagebox.showwarning("Game Not Started", "Please start the game first!")
            return
            
        try:
            guess_str = self.guess_entry.get()
            if not guess_str: # Handle empty input
                 self.feedback_label.config(text="Please enter a number.")
                 return
                 
            guess = int(guess_str)
            self.attempts += 1

            if guess < self.low or guess > self.high:
                 self.feedback_label.config(text=f"Number must be between {self.low} and {self.high}.")
            elif guess < self.number_to_guess:
                self.feedback_label.config(text=f"Too low! (Attempt {self.attempts})")
            elif guess > self.number_to_guess:
                self.feedback_label.config(text=f"Too high! (Attempt {self.attempts})")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} tries.")
                # Reset for a new game potentially
                self.feedback_label.config(text="Select difficulty and start a new game!")
                self.number_to_guess = None # Reset game state
                self.guess_entry.delete(0, tk.END)
                self.guess_entry.config(state=tk.DISABLED)
                self.guess_button.config(state=tk.DISABLED)
                return # Exit after correct guess

        except ValueError:
            self.feedback_label.config(text="Invalid input. Please enter a number.")
            
        # Clear the entry field after each guess
        self.guess_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()