🎬 Movie Ticket Reservation System (Python Tkinter)

A GUI-based Movie Ticket Reservation System developed using Python Tkinter and PostgreSQL.
This desktop application allows users to view movie shows and reserve seats in real time.

--------------------------------------------------------------------
📌 Project Features

Full-screen Tkinter GUI

Movie show selection using dropdown

User name input

Seat reservation system

Automatic seat count update

Movie list displayed using TreeView table

PostgreSQL database integration

Error and success messages using message boxes



--------------------------------------------------------------------

🛠️ Technologies Used

Python 3

Tkinter & ttk

pyodbc

PostgreSQL

PostgreSQL Unicode ODBC Driver


--------------------------------------------------------------------
📂 Project Structure
Movie-Ticket-Reservation-System/
│
├── movie-reservation-system.py
├── README.md


--------------------------------------------------------------------
🗄️ Database Setup

Create a PostgreSQL database named project and run the following SQL:

CREATE TABLE movie (
    show_no VARCHAR(20) PRIMARY KEY,
    time VARCHAR(50),
    Movie VARCHAR(100),
    price INTEGER,
    seats INTEGER
);

--------------------------------------------------------------------

Sample Data
INSERT INTO movie VALUES
('first', '10:00 AM', 'Inception', 500, 20),
('second', '2:00 PM', 'Interstellar', 600, 15),
('third', '6:00 PM', 'Avengers', 700, 10);


--------------------------------------------------------------------

⚙️ Installation & Requirements
Install Required Python Package
pip install pyodbc



Install PostgreSQL Unicode Driver

Linux (Ubuntu)

sudo apt install odbc-postgresql



--------------------------------------------------------------------
🔧 Database Configuration

Update database credentials in the dbFun() function:

self.conn = pyodbc.connect(
    "Driver={PostgreSQL Unicode};"
    "Server=localhost;"
    "Port=5432;"
    "Database=project;"
    "Uid=postgres;"
    "Pwd=password;"
)



--------------------------------------------------------------------
▶️ How to Run the Project
python main.py

🧠 How the Application Works

Select a movie show from the dropdown

Enter your name

Click Reserve

Seat count decreases by one

Updated data appears in the table

❗ Error Handling

Empty name or show selection

Invalid show selection

No seats available

Errors are shown using popup message boxes.


--------------------------------------------------------------------

🚀 Future Improvements

Multiple seat booking

Admin panel

Seat layout visualization

Booking history

Payment system integration



--------------------------------------------------------------------

👤 Author

Aleem Ahmad
Python Developer | Tkinter | PostgreSQL


--------------------------------------------------------------------

📜 License

This project is open-source and created for educational and learning purposes.