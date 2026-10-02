import tkinter as tk
from tkinter import messagebox as mb


class App:
    def __init__(self, r, n=4):
        self.r, self.n, self.moves, self.run = r, n, 0, False
        r.title("CS456 - Alternating Disks")
        r.resizable(False, False)

        tk.Label(r, text="Alternating Disks: Move all light disks left and dark disks right", font=("Arial", 13, "bold")).pack(pady=(12, 4))
        self.c = tk.Canvas(r, width=760, height=210, bg="white", highlightthickness=0)
        self.c.pack(padx=12)

        ctrl = tk.Frame(r)
        ctrl.pack(pady=8)
        tk.Label(ctrl, text="n =").pack(side="left")
        self.e = tk.Entry(ctrl, width=5)
        self.e.insert(0, str(n))
        self.e.pack(side="left", padx=(3, 12))
        tk.Button(ctrl, text="Reset", command=self.reset).pack(side="left", padx=3)
        tk.Button(ctrl, text="Solve", command=self.start).pack(side="left", padx=3)

        self.st = tk.Label(r, font=("Arial", 11))
        self.st.pack(pady=(0, 10))
        self.disks = [i % 2 for i in range(2 * n)]  # 0: DARK, 1: LIGHT
        self.draw()

    def draw(self, hl=()):
        self.c.delete("all")
        for i, d in enumerate(self.disks):
            x, y = 55 + i * 68, 100
            f, o = ("#222", "#000") if d == 0 else ("#f4f4f4", "#222")
            w = 4 if i in hl else 2
            self.c.create_oval(x - 25, y - 25, x + 25, y + 25, fill=f, outline=o, width=w)
            self.c.create_text(x, y, text=str(i + 1), fill="white" if d == 0 else "black", font=("Arial", 10, "bold"))
        self.st.config(text=f"Moves: {self.moves}    State: {''.join('D' if x == 0 else 'L' for x in self.disks)}")

    def reset(self):
        if self.run: return False
        try:
            n = int(self.e.get())
            if n < 1: raise ValueError
        except ValueError:
            mb.showerror("Invalid n", "Please enter a positive integer.")
            return False
        self.n, self.moves = n, 0
        self.disks = [i % 2 for i in range(2 * n)]
        self.draw()
        return True

    def start(self):
        if self.reset():
            self.run = True
            self.r.after(500, self.step)

    def step(self):
        for i in range(len(self.disks) - 1):
            if self.disks[i] == 0 and self.disks[i + 1] == 1:
                self.disks[i], self.disks[i + 1] = 1, 0
                self.moves += 1
                self.draw((i, i + 1))
                self.r.after(350, self.step)
                return
        self.run = False
        self.draw()
        mb.showinfo("Finished", f"Puzzle solved in {self.moves} adjacent swaps.\nFor n={self.n}, the minimum number of moves is n² = {self.n ** 2}.")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()