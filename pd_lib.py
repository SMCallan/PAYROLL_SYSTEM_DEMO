import pandas as pd
import os

DATA_SUBFOLDER = 'data'
DATA_FILENAME = 'example.csv'

def get_menu_options():
    return [
        "Get wage by Full Name, Department, Business Unit, or Country",
        "Get Annual Salary List by Pay.",
        "Get Annual Salary cost by Job.",
        "List Employee Numbers and Total outlay in Countries by department.",
        "List Employee Numbers and Total outlay in Countries by Business Unit.",
        "Check for forename palindrome.",
        "Advanced Employee Search",
        "Display Employees by Salary Range",
        "Display Total Salary and Headcount by Department (Sorted)",
        "Display Total Salary and Headcount by Business Unit (Sorted)",
        "Write data to a text file.",
        "Display wage_slip by eeid",
        "Exit."
    ]

def get_data_file_path():
    current_directory = os.getcwd()
    return os.path.join(current_directory, DATA_SUBFOLDER, DATA_FILENAME)

def read_data_frame(file_path):
    """
    Reads a CSV file from the given file path and returns a pandas DataFrame.

    Parameters:
    file_path (str): The full path to the CSV file.

    Returns:
    pandas.DataFrame or None: The DataFrame containing the data from the CSV file, or None if an error occurs.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("No data: The file is empty.")
    except pd.errors.ParserError:
        print("Parse error: Could not parse the CSV file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def get_wage_by_criteria(data_frame, search_value, search_field):
    """
    Retrieves wage information based on given search criteria.

    Parameters:
    data_frame (pandas.DataFrame): DataFrame containing employee information.
    search_value (str): The value to search for (e.g., a name, a department, a business unit, or a country).
    search_field (str): The field/column in the DataFrame to match the search_value against.

    Returns:
    str: A message with the wage information or a not found message.
    """
    if search_field not in data_frame.columns:
        return f"Error: Column '{search_field}' not found in data."

    filtered_df = data_frame[data_frame[search_field] == search_value]

    if len(filtered_df) == 0:
        return f"No data found for {search_field} '{search_value}'."

    if search_field == "Full Name":
        # Assuming each individual has a unique full name
        wage = filtered_df['Annual Salary'].values[0]
        return f"The wage for {search_field} '{search_value}' is £{wage}."

    else:
        total_salary = filtered_df['Annual Salary'].sum()
        employee_count = len(filtered_df)
        return f"Total annual salary for {search_field} '{search_value}' is £{total_salary} across {employee_count} employees."

def write_data_to_file(result, file_name='output.txt'):
    try:
        with open(file_name, 'w') as file:
            file.write(result + '\n')
        print(f"Data written to {file_name}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def get_annual_salary_list_by_pay(data_frame):
    """
    Returns a list of employees sorted by their annual salary.
    """
    sorted_df = data_frame.sort_values(by='Annual Salary', ascending=False)
    return sorted_df[['Full Name', 'Annual Salary']].to_string(index=False)

def get_annual_salary_cost_by_job(data_frame):
    """
    Returns the total annual salary cost for each job title.
    """
    return data_frame.groupby('Job Title')['Annual Salary'].sum().to_string()

def list_employee_numbers_and_total_outlay_by_department(data_frame):
    """
    Lists each department with the number of employees and total salary outlay.
    """
    result = data_frame.groupby('Department').agg({'EEID': 'count', 'Annual Salary': 'sum'})
    result.rename(columns={'EEID': 'Employee Count', 'Annual Salary': 'Total Salary'}, inplace=True)
    return result.to_string()

def list_employee_numbers_and_total_outlay_by_business_unit(data_frame):
    """
    Lists each business unit with the number of employees and total salary outlay.
    """
    result = data_frame.groupby('Business Unit').agg({'EEID': 'count', 'Annual Salary': 'sum'})
    result.rename(columns={'EEID': 'Employee Count', 'Annual Salary': 'Total Salary'}, inplace=True)
    return result.to_string()

def list_employee_numbers_and_total_outlay_by_department_sorted(data_frame):
    result = data_frame.groupby(['Department', 'Country']).agg({'EEID': 'count', 'Annual Salary': 'sum'})
    result.rename(columns={'EEID': 'Employee Count', 'Annual Salary': 'Total Salary'}, inplace=True)
    return result.sort_index(level=['Department', 'Country']).to_string()

def list_employee_numbers_and_total_outlay_by_business_unit_sorted(data_frame):
    result = data_frame.groupby(['Business Unit', 'Country']).agg({'EEID': 'count', 'Annual Salary': 'sum'})
    result.rename(columns={'EEID': 'Employee Count', 'Annual Salary': 'Total Salary'}, inplace=True)
    return result.sort_index(level=['Business Unit', 'Country']).to_string()

def get_employees_by_salary_range(data_frame, min_salary, max_salary):
    filtered_df = data_frame[(data_frame['Annual Salary'] >= min_salary) & (data_frame['Annual Salary'] <= max_salary)]
    sorted_df = filtered_df.sort_values(by=['Country', 'Hire Date'])
    return sorted_df[['Full Name', 'Annual Salary', 'Department', 'City', 'Country']]

def get_advanced_filtered_data(data_frame, department=None, min_salary=None, max_salary=None):
    filtered_df = data_frame
    if department:
        filtered_df = filtered_df[filtered_df['Department'] == department]
    if min_salary is not None:
        filtered_df = filtered_df[filtered_df['Annual Salary'] >= min_salary]
    if max_salary is not None:
        filtered_df = filtered_df[filtered_df['Annual Salary'] <= max_salary]
    return filtered_df

def display_wage_slip_by_eeid(data_frame, eeid):
    # Retrieve the employee's data
    employee_data = data_frame[data_frame['EEID'] == eeid]

    # If the employee doesn't exist in the data, return an error message
    if employee_data.empty:
        return f"No data found for EEID '{eeid}'."

    # Fabricate or calculate the additional financial details
    tax = calculate_tax(employee_data['Annual Salary'].iloc[0])
    national_insurance = calculate_national_insurance(employee_data['Annual Salary'].iloc[0])
    pension_contributions = calculate_pension_contributions(employee_data['Annual Salary'].iloc[0])
    bonus = calculate_bonus(employee_data['Annual Salary'].iloc[0], employee_data['Bonus %'].iloc[0])
    net_pay = employee_data['Annual Salary'].iloc[0] + bonus - tax - national_insurance - pension_contributions

    wage_slip = (
        f"Full Name: {employee_data['Full Name'].iloc[0]}\n"
        f"EEID: {eeid}\n"
        f"Tax Code: TBD\n"
        f"Business Unit: {employee_data['Business Unit'].iloc[0]}\n"
        f"Date: {pd.Timestamp('today').strftime('%d/%m/%Y')}\n"
        f"Location: {employee_data['City'].iloc[0]}, {employee_data['Country'].iloc[0]}\n\n"
        "Earnings:\n"
        f"Gross Salary: £{employee_data['Annual Salary'].iloc[0]:.2f}\n"
        f"Bonus: £{bonus:.2f}\n"
        f"Tax: £{tax:.2f}\n"
        f"National Insurance: £{national_insurance:.2f}\n"
        f"Pension Contributions: £{pension_contributions:.2f}\n\n"
        "Deductions:\n"
        f"Net Pay: £{net_pay:.2f}\n"
    )
    return wage_slip

def calculate_tax(salary):
    # Placeholder for tax calculation logic
    return salary * 0.20  # Example tax rate

def calculate_national_insurance(salary):
    # Placeholder for National Insurance calculation logic
    return salary * 0.12  # Example NI rate

def calculate_pension_contributions(salary):
    # Placeholder for pension contribution calculation logic
    return salary * 0.05  # Example pension rate

def calculate_bonus(salary, bonus_percentage):
    # Convert bonus_percentage to a float if it's a string
    bonus_percentage = float(bonus_percentage.replace('%', '')) if isinstance(bonus_percentage, str) else bonus_percentage
    return salary * (bonus_percentage / 100)

