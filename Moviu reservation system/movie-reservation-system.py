from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyodbc


class Movie:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Tickets")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        self.title = Label(
            self.root,
            text="Movies Tkicts reservation",
            bd=4,
            relief="raised",
            bg="brown",
            fg="white",
            font=("Arial", 50, "bold")
        )
        self.title.pack(side=TOP, fill=X)

        # global variables
        self.row = 4
        self.seats = 5

        self.frame = Frame(
            self.root,
            border=5,
            relief="ridge",
            bg=self.clr(150, 180, 250)
        )
        self.frame.place(
            width=self.width - 300,
            height=self.height - 80,
            x=150,
            y=100
        )

        self.optionlbl = Label(
            self.frame,
            text="Select_show :",
            bg=self.clr(150, 180, 250),
            font=("Arial", 20, "bold")
        )
        self.optionlbl.grid(row=0, column=0, padx=20, pady=20)

        self.option = ttk.Combobox(
            self.frame,
            width=17,
            values=("first", "second", "third"),
            state="readonly"
        )
        self.option.set("select")
        self.option.grid(row=0, column=1, padx=20, pady=20)

        namelbl = Label(
            self.frame,
            text="your_name :",
            bg=self.clr(150, 180, 250),
            font=("arial", 15, "bold")
        )
        namelbl.grid(row=0, column=2, padx=20, pady=20)

        self.name = Entry(self.frame, bd=2, font=("arial", 15))
        self.name.grid(row=0, column=3, padx=20, pady=20)

        self.button = Button(
            self.frame,
            text="Reserve",
            font=("arial", 15, "bold"),
            bd=3,
            width=8,
            relief=RAISED,
            command=self.reserveFun
        )
        self.button.grid(row=0, column=4, padx=20, pady=20)

        self.tabfram()

    # ---------------- TABLE FRAME ----------------
    def tabfram(self):
        tabframe = Frame(self.frame, bd=5, relief=SUNKEN, bg="cyan")
        tabframe.place(
            width=self.width - 400,
            height=self.height - 380,
            x=50,
            y=90
        )

        x_scrol = Scrollbar(tabframe, orient=HORIZONTAL)
        x_scrol.pack(side=BOTTOM, fill=X)

        y_scroll = Scrollbar(tabframe, orient=VERTICAL)
        y_scroll.pack(side=RIGHT, fill=Y)

        self.table = ttk.Treeview(
            tabframe,
            columns=("show", "time", "Movie", "price", "seats"),
            xscrollcommand=x_scrol.set,
            yscrollcommand=y_scroll.set
        )

        x_scrol.config(command=self.table.xview)
        y_scroll.config(command=self.table.yview)

        self.table.heading("show", text="show_no")
        self.table.heading("time", text="Movie_time")
        self.table.heading("Movie", text="Movie_name")
        self.table.heading("price", text="price")
        self.table.heading("seats", text="Seats")

        self.table["show"] = "headings"

        self.table.column("show", width=150)
        self.table.column("time", width=200)
        self.table.column("Movie", width=200)
        self.table.column("price", width=100)
        self.table.column("seats", width=100)

        self.table.pack(fill=BOTH, expand=1)
        self.showFun()

    # ---------------- SHOW DATA ----------------
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
            messagebox.showerror("Error", f"Error : {e}")

    # ---------------- RESERVE SEAT ----------------
    def reserveFun(self):
        opt = self.option.get()
        name = self.name.get()

        if opt == "select" or name == "":
            messagebox.showerror("Error", "please enter a name and select option")
            return

        try:
            self.dbFun()
            self.cursor.execute(
                "SELECT Movie, price, seats FROM movie WHERE show_no=?",
                (opt,)
            )
            
            row = self.cursor.fetchone()
            print(row)

            if row is None:
                messagebox.showerror("Error", "Invalid show selected")
                self.conn.close()
                return

            if row[2] <= 0:
                messagebox.showerror("Error", f"All seats are reserved Sorry {name}")
                self.conn.close()
                return

            upd = row[2] - 1
            self.cursor.execute(
                "UPDATE movie SET seats=? WHERE show_no=?",
                (upd, opt)
            )
            self.conn.commit()

            messagebox.showinfo(
                "Success",
                f"Seat reserved for {name}\nNow pay amount {row[1]}"
            )

            self.conn.close()
            self.showFun()

        except Exception as e:
            messagebox.showerror("Error", f"Error : {e}")

    # ---------------- DATABASE ----------------
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

    # ---------------- COLOR ----------------
    def clr(self, r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"


root = Tk()
obj = Movie(root)
root.mainloop()
