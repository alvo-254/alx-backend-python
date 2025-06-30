# 🌀 Python Generators with MySQL: Streaming Large Datasets

## 📚 About the Project

This project demonstrates the use of **Python generators** to efficiently stream and process large datasets from a **MySQL** database. It simulates a real-world data pipeline where records are processed one at a time without loading everything into memory — enabling performance, scalability, and low memory usage.

## 🎯 Learning Objectives

- ✅ Master Python’s `yield` and generator functions
- ✅ Stream data row-by-row from SQL tables
- ✅ Integrate Python with MySQL for efficient querying
- ✅ Handle large datasets in a memory-safe manner
- ✅ Use batch processing and simulate real-time data updates

## 🧰 Technologies Used

- Python 3.x
- MySQL (with `mysql-connector-python`)
- SQL (MySQL-compatible)
- CSV (for data seeding)

---

## 📁 Project Structure

.
├── seed.py # Handles database connection, creation, seeding, and streaming
├── user_data.csv # CSV with sample user records
├── 0-main.py # Entry point to run the setup and test streaming
└── README.md # Project documentation

markdown
Copy
Edit

---

## ⚙️ Features Implemented

### ✅ Database Setup
- Creates MySQL database `ALX_prodev` if it doesn't exist
- Creates a `user_data` table with:
  - `user_id` (UUID, primary key)
  - `name` (VARCHAR)
  - `email` (VARCHAR)
  - `age` (DECIMAL)

### ✅ Data Seeding
- Populates the table from `user_data.csv` only if data does not already exist

### ✅ Generator Function
- `stream_users(connection)` yields one row at a time using `cursor.fetchone()` — enabling memory-efficient iteration

---

## 🚀 How to Run

1. **Ensure MySQL is running** and accessible
2. **Install dependencies** (if needed):
   ```bash
   pip install mysql-connector-python
Run the script:

bash
Copy
Edit
chmod +x 0-main.py
./0-main.py
