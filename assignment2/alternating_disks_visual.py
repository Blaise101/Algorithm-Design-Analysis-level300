import tkinter as tk
from tkinter import messagebox

LIGHT = "light"
DARK = "dark"

class AlternatingDisksApp:
    def __init__(self, root, n=4):
        self.root = root
        self.root.title("CS456 - Alternating Disks")
        self.root.resizable(False, False)

        self.n = n
        self.disks = [DARK if i % 2 == 0 else LIGHT for i in range(2 * n)]
        self.move_count = 0
        self.running = False

        self.canvas_width = 760
        self.canvas_height = 210
        self.disk_radius = 25
        self.gap = 18
        self.start_x = 55
        self.center_y = 100

        title = tk.Label(
            root,
            text="Alternating Disks: Move all light disks left and dark disks right",
            font=("Arial", 13, "bold")
        )
        title.pack(pady=(12, 4))

        self.canvas = tk.Canvas(
            root, width=self.canvas_width, height=self.canvas_height,
            bg="white", highlightthickness=0
        )
        self.canvas.pack(padx=12)

        controls = tk.Frame(root)
        controls.pack(pady=8)

        tk.Label(controls, text="n =").pack(side=tk.LEFT)
        self.n_entry = tk.Entry(controls, width=5)
        self.n_entry.insert(0, str(n))
        self.n_entry.pack(side=tk.LEFT, padx=(3, 12))

        tk.Button(controls, text="Reset", command=self.reset).pack(side=tk.LEFT, padx=3)
        tk.Button(controls, text="Solve", command=self.start_solution).pack(side=tk.LEFT, padx=3)

        self.status = tk.Label(root, text="", font=("Arial", 11))
        self.status.pack(pady=(0, 10))

        self.draw()

    def disk_x(self, index):
        return self.start_x + index * (2 * self.disk_radius + self.gap)

    def draw(self, highlight=None):
        self.canvas.delete("all")

        for i, color in enumerate(self.disks):
            x = self.disk_x(i)
            y = self.center_y

            if color == DARK:
                fill = "#222222"
                outline = "#000000"
            else:
                fill = "#f4f4f4"
                outline = "#222222"

            width = 4 if highlight is not None and i in highlight else 2

            self.canvas.create_oval(
                x - self.disk_radius, y - self.disk_radius,
                x + self.disk_radius, y + self.disk_radius,
                fill=fill, outline=outline, width=width
            )

            self.canvas.create_text(
                x, y, text=str(i + 1),
                fill="white" if color == DARK else "black",
                font=("Arial", 10, "bold")
            )

        self.status.config(
            text=f"Moves: {self.move_count}    "
                 f"State: {''.join('D' if x == DARK else 'L' for x in self.disks)}"
        )

    def reset(self):
        if self.running:
            return
        try:
            n = int(self.n_entry.get())
            if n < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid n", "Please enter a positive integer.")
            return

        self.n = n
        self.disks = [DARK if i % 2 == 0 else LIGHT for i in range(2 * n)]
        self.move_count = 0
        self.draw()

    def start_solution(self):
        if self.running:
            return
        self.reset()
        self.running = True
        self.root.after(500, self.solve_step)

    def solve_step(self):
        # Adjacent swaps, moving every LIGHT disk to the left of every DARK disk.
        # This is equivalent to bubble sorting L before D.
        for i in range(len(self.disks) - 1):
            if self.disks[i] == DARK and self.disks[i + 1] == LIGHT:
                self.disks[i], self.disks[i + 1] = self.disks[i + 1], self.disks[i]
                self.move_count += 1
                self.draw(highlight=(i, i + 1))
                self.root.after(350, self.solve_step)
                return

        self.running = False
        self.draw()
        messagebox.showinfo(
            "Finished",
            f"Puzzle solved in {self.move_count} adjacent swaps.\n"
            f"For n={self.n}, the minimum number of moves is n² = {self.n ** 2}."
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = AlternatingDisksApp(root, n=4)
    root.mainloop()
