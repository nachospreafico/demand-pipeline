# 🛠️ Demand Pipeline (Pure Python Project)

A lightweight, fully modular data cleaning and analysis pipeline built in pure Python.  
This project simulates a real-world demand planning workflow using a mock dataset of monthly product demand across regions and categories.

---

## 📌 Overview

This project showcases:
- Reading and parsing `.csv` files using Python’s built-in `csv` module
- Data cleaning (handling missing values, type conversion)
- Computing basic statistics (e.g., average demand, top products)
- Writing cleaned data to a new `.csv`
- Writing modular, readable code with docstrings and comments

> ⚠️ No external libraries like `pandas` were used — logic is implemented from scratch to demonstrate programming fundamentals.

---

## 📁 Project Structure

demand_pipeline/
│
├── data/
│   ├── raw/
│   │   └── mock_demand_planning_data.csv   ← Put your CSV here
│   └── clean/
│       └── cleaned_data.csv                ← Output will go here
│
├── src/
│   ├── reader.py       ← For reading raw CSV manually
│   ├── cleaner.py      ← For handling missing values, type checks
│   ├── analyzer.py     ← For calculating summaries
│   └── writer.py       ← For writing output CSV
│
├── pipeline.py         ← Main script that calls the above in order
└── README.md

---

## 🧪 Key Features

- **Custom CSV reader** using `csv.DictReader`
- **Data cleaning logic** that validates and standardizes numerical fields
- **Statistical functions** to compute average demand and top products by shipped units
- **Clear output** with printed summaries and structured writing to file

---

## 📊 Example Output

📊 Average Actual Demand: 2745

🏆 Top Products by Units Shipped:
P012 → 48750 units
P007 → 47990 units
P018 → 47123 units
P005 → 46982 units
P003 → 46880 units

---

## 📂 Dataset Info

A mock dataset was generated with:
- 1,000 rows
- 20 unique product IDs
- 4 regions and 3 categories
- Fields: `Product_ID`, `Category`, `Region`, `Month`, `Planned_Demand`, `Actual_Demand`, `Units_Shipped`
- Includes missing values to simulate real-world imperfections

---

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/nachospreafico/demand-pipeline.git
   cd demand-pipeline

👩‍💻 Author
Ignacio Spreafico
MD | Demand Planner | Aspiring Data Scientist
LinkedIn Profile — (https://www.linkedin.com/in/ignacio-spreafico)

📝 License
This project is licensed under the MIT License.