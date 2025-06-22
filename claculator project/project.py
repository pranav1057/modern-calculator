import tkinter as tk
from tkinter import ttk

# --- Calculator App ---
class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#ECECEC")
        self.root.resizable(False, False)

        self.current_input = ""
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        # --- Display ---
        self.display_var = tk.StringVar()
        display = ttk.Entry(self.root, textvariable=self.display_var, font=("Helvetica Neue", 28),
                            justify='right')
        display.place(x=20, y=20, width=360, height=60)

        # --- Buttons Layout ---
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('C', '⌫', 'Hist', '')
        ]

        # --- Button Frame ---
        btn_frame = tk.Frame(self.root, bg="#ECECEC")
        btn_frame.place(x=20, y=100)

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                if char == '':
                    continue
                btn = tk.Button(btn_frame, text=char, font=("Helvetica Neue", 18),
                                bg="#FFFFFF", fg="#000000", width=5, height=2,
                                relief="flat", command=lambda ch=char: self.on_click(ch))
                btn.grid(row=r, column=c, padx=5, pady=5)

        # --- History Box ---
        self.history_box = tk.Text(self.root, height=5, bg="#F0F0F0", font=("Helvetica Neue", 12),
                                   state='disabled')
        self.history_box.place(x=20, y=500, width=360, height=80)

    def on_click(self, char):
        if char == 'C':
            self.current_input = ""
            self.display_var.set("")
        elif char == '⌫':
            self.current_input = self.current_input[:-1]
            self.display_var.set(self.current_input)
        elif char == '=':
            try:
                result = eval(self.current_input)
                full_expr = f"{self.current_input} = {result}"
                self.add_to_history(full_expr)
                self.display_var.set(str(result))
                self.current_input = str(result)
            except:
                self.display_var.set("Error")
                self.current_input = ""
        elif char == 'Hist':
            self.show_history()
        else:
            self.current_input += char
            self.display_var.set(self.current_input)

    def add_to_history(self, entry):
        self.history.append(entry)
        if len(self.history) > 10:
            self.history.pop(0)

    def show_history(self):
        self.history_box.config(state='normal')
        self.history_box.delete(1.0, tk.END)
        for item in reversed(self.history):
            self.history_box.insert(tk.END, item + "\n")
        self.history_box.config(state='disabled')


# --- Run the app ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()
