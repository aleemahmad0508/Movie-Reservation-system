# 🎬 Movie Ticket Reservation System (Python Tkinter)

A GUI-based Movie Ticket Reservation System developed using Python Tkinter and PostgreSQL.
This desktop application allows users to view movie shows and reserve seats in real time with automatic database updates.

# 📌 Project Features

Full-screen Tkinter GUI

Movie show selection using dropdown (ComboBox)

User name input

Real-time seat reservation

Automatic seat count update

Movie list displayed using TreeView

PostgreSQL database integration

Error & success messages using message boxes

# 🛠️ Technologies Used

Python 3

Tkinter & ttk

pyodbc

PostgreSQL

PostgreSQL Unicode ODBC Driver

# 📂 Project Structure
Movie-Ticket-Reservation-System/
│
├── movie-reservation-system.py
├── README.md

# 🗄️ Database Setup

Create a PostgreSQL database named project and run the following SQL:

CREATE TABLE movie (
    show_no VARCHAR(20) PRIMARY KEY,
    time VARCHAR(50),
    movie VARCHAR(100),
    price INTEGER,
    seats INTEGER
);

# Sample Data
INSERT INTO movie VALUES
('first', '10:00 AM', 'Inception', 500, 20),
('second', '2:00 PM', 'Interstellar', 600, 15),
('third', '6:00 PM', 'Avengers', 700, 10);

# ⚙️ Installation & Requirements
Install Required Python Package
pip install pyodbc

Install PostgreSQL Unicode Driver

Linux (Ubuntu)

sudo apt install odbc-postgresql

# 🔧 Database Configuration

Database connection is handled inside the dbFun() function.

Update your PostgreSQL credentials here:

def dbFun(self):
    self.conn = pyodbc.connect(
        "Driver={PostgreSQL Unicode};"
        "Server=localhost;"
        "Port=5432;"
        "Database=project;"
        "Uid=postgres;"
        "Pwd=password;"
    )
    self.cur = self.conn.cursor()

🔑 What this function does:

Establishes connection with PostgreSQL

Creates a cursor object

Allows execution of SQL queries (SELECT, UPDATE, etc.)

# 🧠 How Database Is Used in This Project
# 1️⃣ Database Connection

The dbFun() function connects the application to PostgreSQL.

This function is usually called:

When the application starts

Before any database operation

# 2️⃣ Fetching Movie Data (READ Operation)

A function (example: fetchMovies() or similar) retrieves movie data:

SELECT * FROM movie;


# 📌 Purpose:

Displays movies in the TreeView table

Loads data into dropdown (show selection)

# 3️⃣ Seat Reservation Logic (UPDATE Operation)

When the Reserve button is clicked:

Selected show is checked

Seat availability is verified

Seat count is decreased by 1

UPDATE movie
SET seats = seats - 1
WHERE show_no = ? AND seats > 0;


# 📌 Purpose:

Prevents overbooking

Updates seats in real time

# 4️⃣ Commit Changes to Database
self.conn.commit()


# 📌 Why commit is important:

Saves changes permanently

Without commit, seat updates will not persist

# 5️⃣ Error Handling with Database

The project handles:

Invalid show selection

No seats available

Database connection failure

Errors are shown using Tkinter message boxes for better user experience.

# ▶️ How to Run the Project
python movie-reservation-system.py

# 🧠 How the Application Works (Step-by-Step)

Application starts

dbFun() connects to PostgreSQL

Movie data loads into table & dropdown

User selects a show

User enters name

Clicks Reserve

Database seat count updates

Table refreshes automatically

# ❗ Error Handling

The system handles:

Empty name field

No show selected

Invalid show number

No seats available

All errors are displayed using popup message boxes.

# 🚀 Future Improvements

Multiple seat booking

Admin panel

Seat layout visualization

Booking history

Payment system integration

# 👤 Author

Aleem Ahmad
Python Developer | Tkinter | PostgreSQL

# 📜 License

This project is open-source and created for educational and learning purposes.