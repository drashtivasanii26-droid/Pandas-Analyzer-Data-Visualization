import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:

    def __init__(self):
        self.data = None
        self.last_plot = None
        print("\nWelcome to Pandas Analyzer & Data Visualization!")

    def __del__(self):
        pass

#=====================
# 1. LOAD DATASET
#=====================

    def load_data(self, file_path):

        try:
            self.data = pd.read_csv(file_path)
            print("\nDataset loaded successfully!")

        except FileNotFoundError:
            print("\nError: CSV file not found!")

        except PermissionError:
            print("\nPermission denied! Close the CSV file and try again.")

        except Exception as e:
            print("\nError:", e)

    def check_data(self):

        if self.data is None:
            print("\nPlease load a dataset first!")
            return False

        return True

    def select_column(self, numeric=False):

        if numeric:
            columns = self.data.select_dtypes(include=np.number).columns.tolist()

        else:
            columns = self.data.columns.tolist()

        if not columns:
            print("\nNo suitable columns found!")
            return None

        print("\nAvailable Columns:", columns)

        col = input("Enter column name: ").strip()

        if col not in columns:
            print("\nInvalid column name!")
            return None

        return col

#=====================
# 2. EXPLORE DATA
#=====================

    def explore_data(self):

        if not self.check_data():
            return

        print("\n========== EXPLORE DATA ==========")
        print("1. Display First 5 Rows")
        print("2. Display Last 5 Rows")
        print("3. Display Column Names")
        print("4. Display Data Types")
        print("5. Display Basic Information")

        ch = input("\nEnter your choice: ")

        if ch == '1':
            print("\nFirst 5 Rows:")
            print(self.data.head().to_string(index=False))

        elif ch == '2':
            print("\nLast 5 Rows:")
            print(self.data.tail().to_string(index=False))

        elif ch == '3':
            print("\nColumn Names:")
            print(self.data.columns.tolist())

        elif ch == '4':
            print("\nData Types:")
            print(self.data.dtypes)

        elif ch == '5':
            print("\nBasic Information:")
            self.data.info()

        else:
            print("\nInvalid Choice!")

#===========================
# 3. NUMPY ARRAY OPERATIONS
#===========================

    def numpy_operations(self):

        if not self.check_data():
            return

        col = self.select_column(numeric=False)

        if col is None:return

        arr = self.data[col].dropna().to_numpy()

        if arr.size == 0:
            print("\nNo values available!")
            return

        print("\nNumPy Array:", arr)
        print("Array Shape:", arr.shape)
        print("Array Dimension:", arr.ndim)
        print("First Element:", arr[0])
        print("Last Element:", arr[-1])
        print("First 5 Elements:", arr[:5])
        print("Last 5 Elements:", arr[-5:])

        if pd.api.types.is_numeric_dtype(self.data[col]):
            print("\nMathematical Operations:")
            print("Addition (+10):", arr + 10)
            print("Subtraction (-10):", arr - 10)
            print("Multiplication (*2):", arr * 2)
            print("Division (/2):", arr / 2)

        else:
            print("\nMathematical Operations:")
            print("Text Column - Mathematical Operations Not Allowed!")

#=========================
# 4. DATAFRAME OPERATIONS
#=========================

    def dataframe_operations(self):

        if not self.check_data():
            return

        print("\n========== DATAFRAME OPERATIONS ==========")
        print("1. NumPy Array (index and slice)")
        print("2. Mathematical Operations")
        print("3. Combine Data")
        print("4. Split Data by region")
        print("5. Search/Sort/Filter")
        print("6. Aggregate Functions")
        print("7. Pivot Table")
        print("8. groupby/transform/rename")

        ch = input("\nEnter your choice: ")

        if ch == '1':
            self.numpy_operations()

        elif ch == '2':
            col = self.select_column(numeric=True)

            if col:
                try:
                    num = float(input("Enter number: "))

                    print("\nAddition:")
                    print(self.data[col] + num)

                    print("\nSubtraction:")
                    print(self.data[col] - num)

                    print("\nMultiplication:")
                    print(self.data[col] * num)

                    if num != 0:
                        print("\nDivision:")
                        print(self.data[col] / num)

                    else:
                        print("Division by zero is not allowed!")

                except ValueError:
                    print("\nPlease enter a valid number!")

        elif ch == '3':
            try:
                path = input("Enter second CSV file path: ").strip().strip('"').strip("'")
                df2 = pd.read_csv(path)
                print("\n1. Concatenate")
                print("2. Merge")
                print("3. Join")
                op = input("Enter choice: ")
                if op == '1':
                    self.data = pd.concat( [self.data, df2], ignore_index=True)

                elif op == '2':
                    key = input("Enter common column: ").strip()

                    self.data = pd.merge(self.data,df2,on=key, how='inner')

                elif op == '3':
                    self.data = self.data.join(df2,rsuffix='_second')

                else:
                    print("\nInvalid Choice!")
                    return

                print("\nCombined DataFrame:")
                print(self.data.head().to_string(index=False))

            except Exception as e:
                print("\nError:", e)

        elif ch == '4':
            col = self.select_column()

            if col:
                groups = {name: group.copy()for name, group in self.data.groupby( col, dropna=False)}
                print("\nTotal Groups:", len(groups))

                for name, group in groups.items():
                    print("\nGroup:", name)
                    print(group.head().to_string(index=False))

        elif ch == '5':
            col = self.select_column()

            if col:
                value = input("Enter search value: ")

                result = self.data[ self.data[col].astype(str).str.contains(value,case=False,na=False,regex=False)]

                print("\nSearch Result:")
                print(result.to_string(index=False))

        elif ch == '6':
            col = self.select_column()

            if col:
                result = self.data.sort_values( by=col, ascending=True)

                print("\nAscending Sorting:")
                print(result.to_string(index=False))

        elif ch == '7':
            col = self.select_column()

            if col:
                result = self.data.sort_values( by=col, ascending=False)
                print("\nDescending Sorting:")
                print(result.to_string(index=False))

        elif ch == '8':
            col = self.select_column()

            if col:
                value = input("Enter filter value: ")

                result = self.data[self.data[col].astype(str) == value ]

                print("\nFiltered Data:")
                print(result.to_string(index=False))

        elif ch == '9':
            self.aggregate_functions()

        elif ch == '10':
            col = self.select_column()

            if col:
                num = self.select_column(numeric=True)

                if num:
                    result = self.data.groupby(col)[num].agg(['sum', 'mean', 'min', 'max', 'count'])

                    print("\nGroupBy Result:")
                    print(result.to_string())

        elif ch == '11':
            col = self.select_column()

            if col:
                num = self.select_column(numeric=True)

                if num:
                    new_col = num + '_group_avg'

                    self.data[new_col] = (self.data.groupby(col)[num].transform('mean'))

                    print("\nTransform Result:")
                    print(self.data.head().to_string(index=False))

        elif ch == '12':
            self.create_pivot_table()

        elif ch == '13':
            try:
                self.data = self.data.reset_index(drop=True)

                print("\nIndex reset successfully!")
                print(self.data.head().to_string(index=False))

            except Exception as e:
                print("\nError:", e)

        else:
            print("\nInvalid Choice!")

#========================   
# 5. HANDLE MISSING DATA
#========================

    def clean_data(self):

        if not self.check_data():
            return

        print("\n========== HANDLE MISSING DATA ==========")
        print("1. Display Rows with Missing Values")
        print("2. Fill Missing Values with Mean")
        print("3. Drop Rows with Missing Values")
        print("4. Replace Missing Values with a Specific Value")

        ch = input("\nEnter your choice: ")

        if ch == '1':
            print("\nMissing Values:")
            print(self.data.isnull().sum())

            missing = self.data[
                self.data.isnull().any(axis=1)
            ]

            if missing.empty:
                print("\nNo missing values found!")

            else:
                print(missing.to_string(index=False))

        elif ch == '2':
            cols = self.data.select_dtypes(include=np.number ).columns

            self.data[cols] = self.data[cols].fillna(self.data[cols].mean())

            print("\nNumeric missing values filled with mean!")

        elif ch == '3':
            self.data.dropna(inplace=True)
            print("\nMissing rows removed!")

        elif ch == '4':
            col = self.select_column()

            if col:
                value = input("Enter replacement value: ")

                if pd.api.types.is_numeric_dtype(self.data[col]):
                    try:
                        value = float(value)

                    except ValueError:
                        print("\nNumeric replacement required!")
                        return

                self.data[col] = self.data[col].fillna(value)
                print("\nMissing values replaced!")

        else:
            print("\nInvalid Choice!")

#=========================
# 6. AGGREGATE FUNCTIONS
#=========================

    def aggregate_functions(self):

        if not self.check_data():
            return

        col = self.select_column(numeric=True)

        if col is None:
            return

        data = self.data[col]

        print("\n========== AGGREGATE FUNCTIONS ==========")
        print("Sum:", data.sum())
        print("Mean:", data.mean())
        print("Minimum:", data.min())
        print("Maximum:", data.max())
        print("Count:", data.count())
        print("Median:", data.median())

#=========================
# 7. STATISTICAL ANALYSIS
#=========================

    def statistical_analysis(self):

        if not self.check_data():
            return

        print("\n========== STATISTICAL ANALYSIS ==========")

        numeric = self.data.select_dtypes(include=np.number)

        if numeric.empty:
            print("\nNo numeric columns available!")
            return

        print("\nDescriptive Statistics:")
        print(numeric.describe().to_string())

        print("\nStandard Deviation:")
        print(numeric.std())

        print("\nVariance:")
        print(numeric.var())

        print("\n25th Percentile:")
        print(numeric.quantile(0.25))

        print("\n50th Percentile:")
        print(numeric.quantile(0.50))

        print("\n75th Percentile:")
        print(numeric.quantile(0.75))

        print("\nCorrelation:")
        print(numeric.corr().to_string())

#=====================
# 8. PIVOT TABLE
#=====================

    def create_pivot_table(self):

        if not self.check_data():
            return

        print("\n========== CREATE PIVOT TABLE ==========")

        index = self.select_column()

        if index is None:
            return

        column = self.select_column()

        if column is None:
            return

        value = self.select_column(numeric=True)

        if value is None:
            return

        print("\n1. Sum")
        print("2. Mean")
        print("3. Count")
        print("4. Maximum")
        print("5. Minimum")

        choice = input("Enter choice: ")

        functions = {'1': 'sum','2': 'mean','3': 'count','4': 'max','5': 'min'}

        if choice not in functions:
            print("\nInvalid Choice!")
            return

        try:
            pivot = self.data.pivot_table(index=index,columns=column,values=value,aggfunc=functions[choice],observed=True)

            print("\nPivot Table:")
            print(pivot.to_string())

        except Exception as e:
            print("\nError:", e)

#=======================
# 9. DATA VISUALIZATION
#=======================

    def visualize_data(self):

        if not self.check_data():
            return

        print("\n========== DATA VISUALIZATION ==========")
        print("1. Bar Plot")
        print("2. Line Plot")
        print("3. Scatter Plot")
        print("4. Pie Chart")
        print("5. Histogram")
        print("6. Stack Plot")

        ch = input("\nEnter your choice: ")

        try:
            plt.figure(figsize=(9, 5))

            if ch == '1':
                x = self.select_column()
                y = self.select_column(numeric=True)

                if not x or not y:
                    plt.close()
                    return

                result = self.data.groupby(x)[y].sum()

                plt.bar(result.index.astype(str), result.values)

                plt.xlabel(x)
                plt.ylabel(y)
                plt.title("Bar Plot")

            elif ch == '2':
                x = self.select_column()
                y = self.select_column(numeric=True)

                if not x or not y:
                    plt.close()
                    return

                result = self.data.groupby(x,sort=True)[y].sum()

                plt.plot(result.index.astype(str),result.values,marker='o',linewidth=2,label=y)
                plt.xlabel(x)
                plt.ylabel(y)
                plt.title("Line Plot")
                plt.legend()
                plt.grid(True)

            elif ch == '3':
                numeric_columns = self.data.select_dtypes(include=np.number).columns.tolist()
                print("\nAvailable Columns:", numeric_columns)

                x_col = input("Enter x-axis column name: ").strip()
                y_col = input("Enter y-axis column name: ").strip()

                if x_col not in numeric_columns or y_col not in numeric_columns:
                    print("\nPlease enter valid numeric column names!")
                    plt.close()
                    return

                plt.scatter(self.data[x_col],self.data[y_col])

                plt.xlabel(x_col)
                plt.ylabel(y_col)
                plt.title("Scatter Plot")

            elif ch == '4':
                col = self.select_column()

                if not col:
                    plt.close()
                    return

                counts = self.data[col].value_counts()

                plt.pie(counts.values,labels=counts.index.astype(str),autopct='%1.1f%%')

                plt.title("Pie Chart")

            elif ch == '5':
                col = self.select_column(numeric=True)

                if not col:
                    plt.close()
                    return

                plt.hist(self.data[col].dropna(),bins=10,edgecolor='black')
                plt.xlabel(col)
                plt.ylabel("Frequency")
                plt.title("Histogram")

            elif ch == '6':
                numeric = self.data.select_dtypes(include=np.number)

                if numeric.shape[1] < 2:
                    print("\nAt least 2 numeric columns required!")
                    plt.close()
                    return

                numeric = numeric.fillna(0)
                plt.stackplot(
                np.arange(len(numeric)),
                *[numeric[c].values for c in numeric.columns],
                labels=numeric.columns)

                plt.title("Stack Plot")
                plt.xlabel("Row Index")
                plt.ylabel("Values")
                plt.legend()
                plt.show()

            else:
                print("\nInvalid Choice!")
                plt.close()
                return

            plt.xticks(rotation=30)
            plt.tight_layout()

            self.last_plot = plt.gcf()

            plt.show()

            print("\nGenerating scatter plot...")
            print("Scatter plot displayed successfully!")

        except Exception as e:
            print("\nVisualization Error:", e)
            plt.close()

#========================
# 10. SAVE VISUALIZATION
#========================

    def save_visualization(self):

        if self.last_plot is None:
            print("\nPlease create a visualization first!")
            return

        filename = input(
            "Enter file name (example: sales_plot.png): "
        ).strip()

        if not filename:
            filename = "sales_plot.png"

        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filename += '.png'

        try:
            self.last_plot.savefig(filename,dpi=300,bbox_inches='tight')

            print("\nVisualization saved as", filename)

        except PermissionError:
            print("\nPermission denied! Close the image file first.")

        except Exception as e:
            print("\nError:", e)

#=====================
# 11. EXPORT DATA
#=====================

    def export_data(self):

        if not self.check_data():
            return

        filename = input(
            "Enter CSV filename (example: sales_data_analysis .csv): "
        ).strip()

        if not filename:
            filename = "filtered_sales.csv"

        if not filename.lower().endswith('.csv'):
            filename += '.csv'

        try:
            self.data.to_csv(filename,index=False)

            print("\nCSV exported successfully:", filename)

        except PermissionError:
            print("\nPermission Error! Close the CSV file and retry.")

        except Exception as e:
            print("\nError:", e)

#==================
# 12. MAIN MENU
#==================

    def menu(self):

        while True:
            print("\n" + "=" * 55)
            print("       PANDAS ANALYZER & DATA VISUALIZATION")
            print("=" * 55)

            print("1. Load Dataset")
            print("2. Explore Data")
            print("3. Perform DataFrame Operations")
            print("4. Handle Missing Data")
            print("5. Generate Descriptive Statistics")
            print("6. Data Visualization")
            print("7. Save Visualization")
            print("8. Exit")
            print("=" * 55)

            ch = input("\nEnter your choice: ")

            if ch == '1':
                path = input("Enter CSV file path: ").strip().strip('"').strip("'")
                self.load_data(path)

            elif ch == '2':
                self.explore_data()

            elif ch == '3':
                self.dataframe_operations()

            elif ch == '4':
                self.clean_data()

            elif ch == '5':
                self.statistical_analysis()

            elif ch == '6':
                self.visualize_data()

            elif ch == '7':
                self.save_visualization()

            elif ch == '8':
                print("\nThank you for using Pandas Analyzer!")
                break

            else:
                print("\nInvalid Choice! Please try again.")


# PROGRAM EXECUTION

if __name__ == "__main__":
    analyzer = SalesDataAnalyzer()
    analyzer.menu()