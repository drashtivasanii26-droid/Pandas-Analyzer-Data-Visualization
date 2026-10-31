# 📊 Pandas Analyzer & Data Visualization
### Python-Based Data Analysis and Visualization Project

---

## 👩‍💻 Project Information

| Details | Information |
|---|---|
| **Project Name** | Pandas Analyzer & Data Visualization |
| **Author** | Drashti Vasani |
| **Language** | Python 3 |
| **Libraries** | Pandas, NumPy, Matplotlib, Seaborn |
| **Editor** | Visual Studio Code |
| **Project Type** | Python Practical Assignment |

---

## 📌 1. Project Overview

**Pandas Analyzer & Data Visualization** is a menu-driven Python application developed to perform data analysis and visualization using Python libraries.

This project allows users to load CSV datasets, explore data, perform DataFrame operations, handle missing values, generate statistical summaries, and create different types of visualizations.

It uses Pandas for data manipulation, NumPy for numerical operations, and Matplotlib for graphical representation.

The main purpose of this project is to make data analysis easier, faster, and more understandable.

---

## 🎯 2. Project Objectives

- To understand Pandas DataFrames and Series.
- To load and analyze CSV datasets.
- To perform NumPy array operations.
- To handle missing and null values.
- To perform mathematical and statistical calculations.
- To create Pivot Tables and GroupBy operations.
- To visualize data using different charts.
- To save visualizations as image files.
- To export analyzed data into CSV format.

---

## ✨ 3. Key Features

### 1. Load Dataset
- Load CSV files using Pandas.
- Handle file-not-found errors.
- Handle permission errors.

### 2. Explore Data
- Display the first 5 rows.
- Display the last 5 rows.
- Display column names.
- Display data types.
- Display basic dataset information.

### 3. NumPy Array Operations
- Convert DataFrame columns into NumPy arrays.
- Display array shape and dimensions.
- Perform indexing and slicing.
- Display first and last elements.
- Perform addition, subtraction, multiplication, and division on numeric arrays.

### 4. DataFrame Operations
- Perform mathematical operations.
- Combine datasets using Concatenate, Merge, and Join.
- Split data into groups.
- Search records.
- Sort data in ascending and descending order.
- Filter records.
- Perform aggregate functions.
- Create GroupBy and Transform results.
- Generate Pivot Tables.
- Reset DataFrame indexes.

### 5. Handle Missing Data
- Display rows containing missing values.
- Fill missing numeric values using Mean.
- Remove rows containing missing values.
- Replace missing values with specific values.

### 6. Aggregate Functions
- Sum
- Mean
- Minimum
- Maximum
- Count
- Median

### 7. Statistical Analysis
- Descriptive Statistics.
- Standard Deviation.
- Variance.
- 25th Percentile.
- 50th Percentile.
- 75th Percentile.
- Correlation.

### 8. Data Visualization

The project supports six types of graphical representations:

| Chart Type | Description |
|---|---|
| Bar Plot | Displays comparisons between categories. |
| Line Plot | Shows trends and changes in data. |
| Scatter Plot | Displays relationships between two numeric columns. |
| Pie Chart | Represents data using percentages. |
| Histogram | Displays the frequency distribution of data. |
| Stack Plot | Shows cumulative values of multiple numeric columns. |

### 9. Save Visualization
- Save generated charts as image files.
- Supports PNG, JPG, and JPEG formats.
- Saves images with 300 DPI resolution.

### 10. Export Data
- Export analyzed DataFrame data.
- Save output in CSV format.
- Export data without the DataFrame index.

---

## 🛠️ 4. Technologies & Libraries Used

| Library | Purpose |
|---|---|
| **Pandas** | Data manipulation and analysis. |
| **NumPy** | Numerical calculations and array operations. |
| **Matplotlib** | Creating charts and graphs. |
| **Seaborn** | Imported visualization library. |

---

## 💻 5. Software Requirements

- Python 3.x
- Visual Studio Code
- Pandas
- NumPy
- Matplotlib
- Seaborn
- CSV Dataset

---

## 📥 6. Installation

First, install the required Python libraries using the following commands:

```bash
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
```

---

## ▶️ 7. How to Run the Project

**Step 1:** Open the project folder in Visual Studio Code.

**Step 2:** Save the Python code in a file named:

```text
pandas_analyzer.py
```

**Step 3:** Open the terminal in Visual Studio Code.

**Step 4:** Run the following command:

```bash
python pandas_analyzer.py
```

**Step 5:** Select the desired option from the main menu.

**Step 6:** Load a CSV dataset and perform the required operations.

---

## 📋 8. Main Menu

When the program starts, the following menu is displayed:

```text
=======================================================
       PANDAS ANALYZER & DATA VISUALIZATION
=======================================================
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
=======================================================

Enter your choice:
```

---

## 📊 9. Sample Dataset

Example of a Sales Dataset:

| Product | Region | Sales | Quantity |
|---|---|---:|---:|
| Laptop | North | 50000 | 5 |
| Mobile | South | 30000 | 10 |
| Tablet | East | 20000 | 8 |
| Laptop | West | 45000 | 4 |
| Mobile | North | 35000 | 12 |

*Note: This is an example dataset for demonstration purposes.*

---

## 🖥️ 10. Sample Output

### 1. Welcome Screen & Load Dataset

```text
Welcome to Pandas Analyzer & Data Visualization!

=======================================================
       PANDAS ANALYZER & DATA VISUALIZATION
=======================================================
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
=======================================================

Enter your choice: 1

Enter CSV file path: sales_data_analyzer.csv

Dataset loaded successfully!
```

### 2. Explore Data – First 5 Rows

```text
========== EXPLORE DATA ==========

1. Display First 5 Rows
2. Display Last 5 Rows
3. Display Column Names
4. Display Data Types
5. Display Basic Information

Enter your choice: 1

First 5 Rows:

Transaction ID       Date Customer ID Gender  Age Product Category Product  Quantity  Price per Unit  Total Amount Payment Method      City
             1 2026-08-10       C0001   Male   26         Clothing   Jeans         2            1199          2398            UPI Ahmedabad
             2 2026-05-05       C0002 Female   63         Clothing T-Shirt         4             499          1996           Cash Ahmedabad
             3 2026-03-08       C0003   Male   56         Clothing   Jeans         2            1199          2398            UPI  Junagadh
             4 2026-01-16       C0004   Male   65      Electronics   Mouse         2             699          1398            UPI  Vadodara
             5 2026-01-23       C0005   Male   47           Beauty Shampoo         5             399          1995           Card  Vadodara
```

### 3. NumPy Array Operations

**Selected Column: Age**

```text
Enter your choice: 1

Available Columns: ['Transaction ID', 'Date', 'Customer ID',
'Gender', 'Age', 'Product Category', 'Product', 'Quantity',
'Price per Unit', 'Total Amount', 'Payment Method', 'City']

Enter column name: Age

NumPy Array:
[26 63 56 65 47 62 56 52 56 44 61 40 54 55 36 22 49 31
 43 62 22 60 19 57 21 28 30 34 21 32 31 18 62 59 58 27
 26 37 23 24 54 31 49 37 54 65 55 44 49 21 55 28 40 39
 38 35 43 61 30 50 30 41 60 35 41 34 57 63 22 24 19 19
 61 53 44 34 45 48 59 26 26 57 39 64 50 52 32 30 35 32
 60 36 65 48 36 48 26 50 28 43]

Array Shape: (100,)
Array Dimension: 1
First Element: 26
Last Element: 43
First 5 Elements: [26 63 56 65 47]
Last 5 Elements: [48 26 50 28 43]

Mathematical Operations:

Addition (+10)
Subtraction (-10)
Multiplication (*2)
Division (/2)

```

*The mathematical operation results are generated using NumPy on the selected Age column.*

### 4. Handle Missing Data

```text
========== HANDLE MISSING DATA ==========

1. Display Rows with Missing Values
2. Fill Missing Values with Mean
3. Drop Rows with Missing Values
4. Replace Missing Values with a Specific Value

Enter your choice: 1

Missing Values:

Transaction ID      0
Date                0
Customer ID         0
Gender              0
Age                 0
Product Category    0
Product             0
Quantity            0
Price per Unit      0
Total Amount        0
Payment Method      0
City                0
dtype: int64

No missing values found!
```

### 5. Statistical Analysis

```text
========== STATISTICAL ANALYSIS ==========

Descriptive Statistics:

       Transaction ID        Age    Quantity  Price per Unit  Total Amount
count      100.000000  100.00000  100.000000      100.000000    100.000000
mean        50.500000   42.19000    3.160000      630.160000   1892.850000
std         29.011492   14.07964    1.447534      386.490574   1402.471069
min          1.000000   18.00000    1.000000      299.000000    299.000000
25%         25.750000   30.00000    2.000000      386.750000    998.000000
50%         50.500000   42.00000    3.000000      499.000000   1497.000000
75%         75.250000   55.00000    4.000000      699.000000   2422.250000
max        100.000000   65.00000    5.000000     1499.000000   7495.000000
```

**Standard Deviation:**

```text
Transaction ID      29.011492
Age                 14.079640
Quantity             1.447534
Price per Unit     386.490574
Total Amount      1402.471069
dtype: float64
```

**Variance:**

```text
Transaction ID    8.416667e+02
Age               1.982363e+02
Quantity          2.095354e+00
Price per Unit    1.493750e+05
Total Amount      1.966925e+06
dtype: float64
```

**25th Percentile:**

```text
Transaction ID     25.75
Age                30.00
Quantity            2.00
Price per Unit    386.75
Total Amount      998.00
Name: 0.25, dtype: float64
```

**50th Percentile:**

```text
Transaction ID      50.5
Age                 42.0
Quantity             3.0
Price per Unit     499.0
Total Amount      1497.0
Name: 0.5, dtype: float64
```

**75th Percentile:**

```text
Transaction ID      75.25
Age                 55.00
Quantity             4.00
Price per Unit     699.00
Total Amount      2422.25
Name: 0.75, dtype: float64
```

**Correlation:**

```text
                 Transaction ID       Age  Quantity  Price per Unit  Total Amount
Transaction ID        1.000000 -0.077710  0.130607       -0.012841      0.039813
Age                  -0.077710  1.000000 -0.129871       -0.004500     -0.111792
Quantity              0.130607 -0.129871  1.000000       -0.177761      0.489160
Price per Unit       -0.012841 -0.004500 -0.177761        1.000000      0.687742
Total Amount          0.039813 -0.111792  0.489160        0.687742      1.000000
```

### 6. Data Visualization – Scatter Plot

```text
========== DATA VISUALIZATION ==========

1. Bar Plot
2. Line Plot
3. Scatter Plot
4. Pie Chart
5. Histogram
6. Stack Plot

Enter your choice: 3

Available Columns:
['Transaction ID', 'Age', 'Quantity', 'Price per Unit', 'Total Amount']

Enter x-axis column name: Transaction ID
Enter y-axis column name: Total Amount

Generating scatter plot...
Scatter plot displayed successfully!
```

<text color="secondary" size="sm">Visualization: Scatter Plot displaying the relationship between Transaction ID and Total Amount.</text>

### 7. Save Visualization

```text
Enter file name (example: sales_plot.png): Sales.png

Visualization saved as Sales.png
```

### 8. Exit Program

```text
=======================================================
       PANDAS ANALYZER & DATA VISUALIZATION
=======================================================
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
=======================================================

Enter your choice: 8

Thank you for using Pandas Analyzer!
```

---

## 📁 11. Project Structure

```text
Pandas Analyzer & Data Visualization/
│
├── Pandas Analyzer & Data Visualization.py
│
├── sales_data_analyzer.csv
│
├── sales.png
│
└── README.md
```

**File Description:**

- `Pandas Analyzer & Data Visualization.py` – Main Python application.
- `sales.csv` – Input dataset.
- `sales.png` – Saved visualization image.
- `README.md` – Project documentation.

---

## 🚀 12. Future Enhancements

- Add more advanced visualization techniques.
- Add interactive dashboards.
- Support Excel file formats.
- Add advanced data cleaning operations.
- Improve dataset filtering and analysis.
- Add graphical user interface (GUI).

---

## 🎓 13. Learning Outcomes

Through this project, I learned how to:

- Work with Pandas DataFrames.
- Use NumPy arrays and numerical operations.
- Load and manipulate CSV datasets.
- Handle missing values.
- Apply statistical functions.
- Perform GroupBy and Pivot Table operations.
- Create different types of data visualizations.
- Save charts and export datasets.
- Handle errors using Exception Handling.

---
### ⭐ Thank You!

Thank you for exploring my **Pandas Analyzer & Data Visualization** project.

