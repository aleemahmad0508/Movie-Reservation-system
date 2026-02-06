import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
import pyodbc
import os
from datetime import datetime


class Movie:

    def __init__(self, root):

        self.root = root
        self.root.title("Cinema Reservation System")
        

        # ================= MAIN FRAME =================
        main_frame = tb.Frame(root, padding=30)
        main_frame.pack(fill=BOTH, expand=True)

        # ================= TITLE =================
        title = tb.Label(
            main_frame,
            text="🎬 CINEMA RESERVATION SYSTEM",
            font=("Segoe UI", 42, "bold"),
            bootstyle="inverse-primary",
            anchor="center"
        )
        title.pack(fill=X, pady=20)

        # ================= CARD =================
        card = tb.Frame(main_frame, padding=30, bootstyle="dark")
        card.pack(pady=20)

        # Configure grid spacing
        for i in range(6):
            card.columnconfigure(i, weight=1)

        tb.Label(card, text="Select Show",
                 font=("Segoe UI", 16, "bold")).grid(row=0, column=0, padx=15, pady=15)

        self.option = tb.Combobox(
            card,
            values=("first", "second", "third"),
            state="readonly",
            width=18,
            bootstyle="info"
        )
        self.option.set("select")
        self.option.grid(row=0, column=1, padx=15)

        tb.Label(card, text="Your Name",
                 font=("Segoe UI", 16, "bold")).grid(row=0, column=2, padx=15)

        self.name = tb.Entry(card, width=20, bootstyle="secondary")
        self.name.grid(row=0, column=3, padx=15)

        # ================= BUTTONS =================
        tb.Button(
            card,
            text="🎟 Reserve",
            bootstyle="success-outline",
            width=15,
            command=self.reserveFun
        ).grid(row=0, column=4, padx=10)

        tb.Button(
            card,
            text="📜 History",
            bootstyle="warning-outline",
            width=15,
            command=self.showHistory
        ).grid(row=0, column=5, padx=10)

        # ================= MOVIE TABLE =================
        table_frame = tb.Frame(main_frame)
        table_frame.pack(fill=BOTH, expand=True, padx=150, pady=30)

        self.table = tb.Treeview(
            table_frame,
            columns=("show", "time", "movie", "price", "seats"),
            show="headings",
            bootstyle="info"
        )

        headings = ["Show", "Time", "Movie", "Price", "Seats"]

        for col, heading in zip(
                ("show", "time", "movie", "price", "seats"),
                headings):
            self.table.heading(col, text=heading)
            self.table.column(col, anchor=CENTER, width=150)

        self.table.pack(fill=BOTH, expand=True)

        # ================= FOOTER =================
        footer = tb.Label(
            main_frame,
            text="Developed by Aleem Ahmad | Professional Cinema Management System",
            font=("Segoe UI", 12),
            bootstyle="secondary"
        )
        footer.pack(pady=10)

        self.showFun()

    # =====================================================
    # Show Movie Data
    # =====================================================
    def showFun(self):
        try:
            self.dbFun()
            self.cursor.execute("SELECT * FROM movie")
            rows = self.cursor.fetchall()

            self.table.delete(*self.table.get_children())

            for r in rows:
                self.table.insert("", END, values=r)

            self.conn.close()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    # =====================================================
    # Reserve Seat + Save History
    # =====================================================
    def reserveFun(self):

        opt = self.option.get()
        name = self.name.get()

        if opt == "select" or name.strip() == "":
            messagebox.showerror("Error", "Please enter name and select show")
            return

        try:
            self.dbFun()

            self.cursor.execute(
                "SELECT Movie, price, seats FROM movie WHERE show_no=?",
                (opt,)
            )

            row = self.cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid show selected")
                return

            if row[2] <= 0:
                messagebox.showerror("Error", "No seats available")
                return

            # Update seat
            self.cursor.execute(
                "UPDATE movie SET seats=? WHERE show_no=?",
                (row[2] - 1, opt)
            )

            self.conn.commit()
            self.conn.close()

            # Save history with timestamp
            with open("history.txt", "a") as file:
                file.write(
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
                    f"Name: {name} | Show: {opt} | "
                    f"Movie: {row[0]} | Price: {row[1]}\n"
                )

            messagebox.showinfo(
                "Success",
                f"🎉 Seat Reserved Successfully!\n\nName: {name}\nMovie: {row[0]}\nAmount: {row[1]}"
            )

            self.name.delete(0, END)
            self.option.set("select")

            self.showFun()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    # =====================================================
    # Show History Window
    # =====================================================
    def showHistory(self):

        history_window = tb.Toplevel(self.root)
        history_window.title("Reservation History")
        history_window.geometry("800x500")

        header = tb.Label(
            history_window,
            text="📜 BOOKING HISTORY",
            font=("Segoe UI", 24, "bold"),
            bootstyle="inverse-info"
        )
        header.pack(fill=X)

        text_area = tb.Text(history_window, font=("Consolas", 12))
        text_area.pack(fill=BOTH, expand=True, padx=20, pady=20)

        if os.path.exists("history.txt"):
            with open("history.txt", "r") as file:
                text_area.insert(END, file.read())
        else:
            text_area.insert(END, "No booking history found.")

        tb.Button(
            history_window,
            text="🗑 Clear History",
            bootstyle="danger-outline",
            command=lambda: self.clearHistory(text_area)
        ).pack(pady=10)

    def clearHistory(self, text_widget):
        open("history.txt", "w").close()
        text_widget.delete("1.0", END)
        messagebox.showinfo("Success", "History Cleared!")

    # =====================================================
    # Database Connection
    # =====================================================
    def dbFun(self):
        self.conn = pyodbc.connect(
            "Driver={PostgreSQL Unicode};"
            "Server=localhost;"
            "Port=5432;"
            "Database=project;"
            "Uid=postgres;"
            "Pwd=password;"
        )
        self.cursor = self.conn.cursor()


if __name__ == "__main__":
    app = tb.Window(themename="superhero")  # Try: darkly, cyborg, superhero
    Movie(app)
    app.mainloop()
