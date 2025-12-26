# -----------------------------
# Import Tkinter main module
# -----------------------------
from tkinter import *

# -----------------------------
# Import ttk for modern widgets like TreeView & ComboBox
# -----------------------------
from tkinter import ttk

# -----------------------------
# Import messagebox for popup messages
# -----------------------------
from tkinter import messagebox

# -----------------------------
# Import pyodbc to connect Python with PostgreSQL
# -----------------------------
import pyodbc


# =====================================================
# Movie Class (Main Application)
# =====================================================
class Movie:

    # -----------------------------
    # Constructor (runs when object is created)
    # -----------------------------
    def __init__(self, root):

        # Store root window reference
        self.root = root

        # Set window title
        self.root.title("Movie Tickets")

        # Get screen width
        self.width = self.root.winfo_screenwidth()

        # Get screen height
        self.height = self.root.winfo_screenheight()

        # Set window to full screen
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        # -----------------------------
        # Title Label (Top Heading)
        # -----------------------------
        self.title = Label(
            self.root,                     # Parent window
            text="Movies Tkicts reservation",  # Heading text
            bd=4,                          # Border width
            relief="raised",               # Border style
            bg="brown",                    # Background color
            fg="white",                    # Text color
            font=("Arial", 50, "bold")     # Font style
        )

        # Place title at top and stretch horizontally
        self.title.pack(side=TOP, fill=X)

        # -----------------------------
        # Main Frame (Container)
        # -----------------------------
        self.frame = Frame(
            self.root,                     # Parent window
            border=5,                      # Border size
            relief="ridge",                # Border style
            bg=self.clr(150, 180, 250)     # Background color
        )

        # Position frame on window
        self.frame.place(
            width=self.width - 300,
            height=self.height - 80,
            x=150,
            y=100
        )

        # -----------------------------
        # Show Selection Label
        # -----------------------------
        self.optionlbl = Label(
            self.frame,
            text="Select_show :",
            bg=self.clr(150, 180, 250),
            font=("Arial", 20, "bold")
        )

        # Place label using grid
        self.optionlbl.grid(row=0, column=0, padx=20, pady=20)

        # -----------------------------
        # Show Selection Dropdown
        # -----------------------------
        self.option = ttk.Combobox(
            self.frame,                    # Parent frame
            width=17,                      # Width of box
            values=("first", "second", "third"),  # Available shows
            state="readonly"               # User cannot type
        )

        # Default value
        self.option.set("select")

        # Place dropdown
        self.option.grid(row=0, column=1, padx=20, pady=20)

        # -----------------------------
        # Name Label
        # -----------------------------
        namelbl = Label(
            self.frame,
            text="your_name :",
            bg=self.clr(150, 180, 250),
            font=("arial", 15, "bold")
        )

        # Place name label
        namelbl.grid(row=0, column=2, padx=20, pady=20)

        # -----------------------------
        # Name Entry Box
        # -----------------------------
        self.name = Entry(
            self.frame,
            bd=2,
            font=("arial", 15)
        )

        # Place entry box
        self.name.grid(row=0, column=3, padx=20, pady=20)

        # -----------------------------
        # Reserve Button
        # -----------------------------
        self.button = Button(
            self.frame,
            text="Reserve",
            font=("arial", 15, "bold"),
            bd=3,
            width=8,
            relief=RAISED,
            command=self.reserveFun   # Call reserveFun on click
        )

        # Place button
        self.button.grid(row=0, column=4, padx=20, pady=20)

        # Call table creation function
        self.tabfram()


    # =====================================================
    # Table Frame (Movie Data Display)
    # =====================================================
    def tabfram(self):

        # Create frame for table
        tabframe = Frame(self.frame, bd=5, relief=SUNKEN, bg="cyan")

        # Position table frame
        tabframe.place(
            width=self.width - 400,
            height=self.height - 380,
            x=50,
            y=90
        )

        # Horizontal scrollbar
        x_scrol = Scrollbar(tabframe, orient=HORIZONTAL)
        x_scrol.pack(side=BOTTOM, fill=X)

        # Vertical scrollbar
        y_scroll = Scrollbar(tabframe, orient=VERTICAL)
        y_scroll.pack(side=RIGHT, fill=Y)

        # -----------------------------
        # TreeView Table
        # -----------------------------
        self.table = ttk.Treeview(
            tabframe,
            columns=("show", "time", "Movie", "price", "seats"),
            xscrollcommand=x_scrol.set,
            yscrollcommand=y_scroll.set
        )

        # Connect scrollbars
        x_scrol.config(command=self.table.xview)
        y_scroll.config(command=self.table.yview)

        # Set column headings
        self.table.heading("show", text="show_no")
        self.table.heading("time", text="Movie_time")
        self.table.heading("Movie", text="Movie_name")
        self.table.heading("price", text="price")
        self.table.heading("seats", text="Seats")

        # Hide default column
        self.table["show"] = "headings"

        # Pack table
        self.table.pack(fill=BOTH, expand=1)

        # Load data from database
        self.showFun()


    # =====================================================
    # Show Data Function (READ from DB)
    # =====================================================
    def showFun(self):
        try:
            # Connect to database
            self.dbFun()

            # Execute SELECT query
            self.cursor.execute("SELECT * FROM movie")

            # Fetch all rows
            rows = self.cursor.fetchall()

            # Clear existing table data
            self.table.delete(*self.table.get_children())

            # Insert rows into table
            for r in rows:
                self.table.insert("", END, values=r)

            # Close database connection
            self.conn.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error : {e}")


    # =====================================================
    # Reserve Seat Function (UPDATE DB)
    # =====================================================
    def reserveFun(self):

        # Get selected show
        opt = self.option.get()

        # Get entered name
        name = self.name.get()

        # Validate input
        if opt == "select" or name == "":
            messagebox.showerror("Error", "please enter a name and select option")
            return

        try:
            # Connect to database
            self.dbFun()

            # Fetch movie data
            self.cursor.execute(
                "SELECT Movie, price, seats FROM movie WHERE show_no=?",
                (opt,)
            )

            # Fetch one record
            row = self.cursor.fetchone()

            # Check invalid show
            if row is None:
                messagebox.showerror("Error", "Invalid show selected")
                self.conn.close()
                return

            # Check seat availability
            if row[2] <= 0:
                messagebox.showerror("Error", f"All seats are reserved Sorry {name}")
                self.conn.close()
                return

            # Update seats
            self.cursor.execute(
                "UPDATE movie SET seats=? WHERE show_no=?",
                (row[2] - 1, opt)
            )

            # Save changes
            self.conn.commit()

            # Success message
            messagebox.showinfo(
                "Success",
                f"Seat reserved for {name}\nNow pay amount {row[1]}"
            )

            # Close connection
            self.conn.close()

            # Refresh table
            self.showFun()

        except Exception as e:
            messagebox.showerror("Error", f"Error : {e}")


    # =====================================================
    # Database Connection Function
    # =====================================================
    def dbFun(self):

        # Create database connection
        self.conn = pyodbc.connect(
            "Driver={PostgreSQL Unicode};"
            "Server=localhost;"
            "Port=5432;"
            "Database=project;"
            "Uid=postgres;"
            "Pwd=password;"
        )

        # Create cursor to execute queries
        self.cursor = self.conn.cursor()


    # =====================================================
    # Color Utility Function
    # =====================================================
    def clr(self, r, g, b):
        # Convert RGB to HEX color
        return f"#{r:02x}{g:02x}{b:02x}"


# =====================================================
# Application Entry Point
# =====================================================

# Create Tkinter root window
root = Tk()

# Create Movie object
obj = Movie(root)

# Start GUI loop
root.mainloop()
