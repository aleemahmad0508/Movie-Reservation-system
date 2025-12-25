🗄️ PostgreSQL Database Utility – Backup & Restore Tool (Python)

A command-line based PostgreSQL Database Utility built with Python that supports database backup, compression, restore, logging, and local storage management.

This tool uses native PostgreSQL utilities (pg_dump, psql) and provides a clean CLI interface for database administrators and learners.
---------------------------------------------------------------------------
📌 Features

✅ PostgreSQL database backup using pg_dump

🗜️ Automatic compression of SQL backups (.gz)

💾 Local backup storage in a dedicated folder

🔄 Database restore from compressed backups

🧾 Logging of all backup & restore operations

⏱️ Timestamp-based backup file naming

🖥️ Command-line interface (CLI) using argparse

---------------------------------------------------------------------------

❗ Error handling with logs

🛠️ Technologies Used

Python 3

PostgreSQL

pg_dump & psql

argparse

subprocess

gzip

logging

File & OS utilities

---------------------------------------------------------------------------

📂 Project Structure
database-utility/
│
├── main.py
├── cli.py
│
├── backup/
│   └── postgres.py
│
├── storage/
│   └── local.py
│
├── utiles/
│   ├── logger.py
│   └── compress.py
│
├── backups/            # Auto-created backup storage folder
├── logs/
│   └── backup.log      # Backup & restore logs
│
└── README.md



---------------------------------------------------------------------------
🧠 How It Works
🔹 Backup Process

CLI command is executed

pg_dump creates a .sql file

SQL file is compressed (.gz)

Compressed file is moved to backups/

Operation is logged

🔹 Restore Process

Compressed backup file is selected

File is decompressed

psql restores the database

Temporary SQL file is deleted

Operation is logged


---------------------------------------------------------------------------
📁 Backup File Naming Format
postgres_backup_YYYYMMDD_HHMMSS.sql.gz


Example:

postgres_backup_20250102_143015.sql.gz


---------------------------------------------------------------------------

⚙️ Requirements

Python 3.8+

PostgreSQL installed

pg_dump and psql available in system PATH

Check PostgreSQL Tools
pg_dump --version
psql --version



---------------------------------------------------------------------------
▶️ How to Run the Project
🔹 Backup Database
python main.py backup --host localhost --port 5432 --user postgres --db project

🔹 Restore Database
python main.py restore --host localhost --port 5432 --user postgres --db project --file backups/postgres_backup_YYYYMMDD_HHMMSS.sql.gz

🧾 Logging System

Logs are stored in:

logs/backup.log


Logged information includes:

Backup start & completion

Restore start & completion

Errors and failures

Timestamps

---------------------------------------------------------------------------

💾 Local Storage

All backups are stored in the backups/ folder

Folder is created automatically if it does not exist

Prevents accidental file overwrites


---------------------------------------------------------------------------

❗ Error Handling

Handles common errors such as:

Invalid database credentials

Missing backup file

Backup or restore failure

File permission issues

All errors are logged for troubleshooting.

---------------------------------------------------------------------------

🔐 Security Notes

PostgreSQL password is requested by pg_dump / psql

Avoid hardcoding credentials

Use environment variables in production environments

---------------------------------------------------------------------------

🚀 Future Enhancements

Support for MySQL & SQLite

Scheduled automatic backups

Encrypted backup files

Cloud storage (AWS / Google Drive)

GUI interface

Multi-database support

---------------------------------------------------------------------------

👤 Author

Aleem Ahmad
Python Developer | Database Utilities | Automation

---------------------------------------------------------------------------

📜 License

This project is open-source and intended for learning, practice, and educational purposes.