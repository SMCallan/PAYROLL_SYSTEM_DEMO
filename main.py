import pd_lib

def display_menu(menu_options):
    print("\nPlease select from the following options:\n")
    for idx, option in enumerate(menu_options, start=1):
        print(f"{idx}. {option}")

def get_user_choice(menu_options):
    try:
        choice = int(input("Enter your choice: "))
        if 1 <= choice <= len(menu_options):
            return choice
        print(f"Invalid choice. Please choose a number between 1 and {len(menu_options)}.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return None

def handle_wage_query():
    search_type = input("Choose the search type (1: Full Name, 2: Department, 3: Business Unit, 4: Country): ")
    search_field = ""
    if search_type == "1":
        search_field = "Full Name"
    elif search_type == "2":
        search_field = "Department"
    elif search_type == "3":
        search_field = "Business Unit"
    elif search_type == "4":
        search_field = "Country"

    if search_field:
        search_value = input(f"Enter the {search_field}: ")
        data_frame = pd_lib.read_data_frame(pd_lib.get_data_file_path())
        if data_frame is not None:
            result = pd_lib.get_wage_by_criteria(data_frame, search_value, search_field)
            print(result)
            pd_lib.write_data_to_file(result)
        else:
            print("Failed to read data frame.")
    else:
        print("Invalid search type selected.")

def handle_palindrome_check():
    name = input("Enter the forename to check for palindrome: ")
    if name == name[::-1]:
        print(f"{name} is a palindrome.")
    else:
        print(f"{name} is not a palindrome.")

def handle_data_to_text_file():
    data_frame = pd_lib.read_data_frame(pd_lib.get_data_file_path())
    if data_frame is not None:
        pd_lib.write_data_to_file(str(data_frame))
    else:
        print("Failed to read data frame.")

def handle_annual_salary_list_by_pay():
    data_frame = pd_lib.read_data_frame(pd_lib.get_data_file_path())
    if data_frame is not None:
        result = pd_lib.get_annual_salary_list_by_pay(data_frame)
        print(result)
        pd_lib.write_data_to_file(result)
    else:
        print("Failed to read data frame.")

def handle_annual_salary_cost_by_job():
    data_frame = pd_lib.read_data_frame(pd_lib.get_data_file_path())
    if data_frame is not None:
        result = pd_lib.get_annual_salary_cost_by_job(data_frame)
        print(result)
        pd_lib.write_data_to_file(result)
    else:
        print("Failed to read data frame.")

def handle_employee_numbers_and_outlay_by_department():
    data_frame = pd_lib.read_data_frame(pd_lib.get_data_file_path())
    if data_frame is not None:
        result = pd_lib.list_employee_numbers_and_total_outlay_by_department(data_frame)
        print(result)
        pd_lib.write_data_to_file(result)
    else:
        print("Failed to read data frame.")

def handle_employee_numbers_and_outlay_by_business_unit():
    data_frame = pd_lib.read_data_frame(pd_lib.get_data_file_path())
    if data_frame is not None:
        result = pd_lib.list_employee_numbers_and_total_outlay_by_business_unit(data_frame)
        print(result)
        pd_lib.write_data_to_file(result)
    else:
        print("Failed to read data frame.")
    
def handle_advanced_employee_search():
    department = input("Enter department (or leave blank to ignore): ").strip()
    department = None if department == "" else department

    min_salary_input = input("Enter minimum salary (or leave blank to ignore): ").strip()
    max_salary_input = input("Enter maximum salary (or leave blank to ignore): ").strip()

    try:
        min_salary = float(min_salary_input) if min_salary_input else None
        max_salary = float(max_salary_input) if max_salary_input else None
    except ValueError:
        print("Invalid salary input. Please enter a number.")
        return

    data_frame = pd_lib.read_data_frame(pd_lib.get_data_file_path())
    if data_frame is not None:
        result = pd_lib.get_advanced_filtered_data(data_frame, department, min_salary, max_salary)
        print(result)
        pd_lib.write_data_to_file(str(result))
    else:
        print("Failed to read data frame.")

def handle_display_employees_by_salary_range():
    try:
        min_salary = float(input("Enter minimum salary: "))
        max_salary = float(input("Enter maximum salary: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value for salary.")
        return

    data_frame = pd_lib.read_data_frame(pd_lib.get_data_file_path())
    if data_frame is not None:
        result = pd_lib.get_employees_by_salary_range(data_frame, min_salary, max_salary)
        print(result)
        pd_lib.write_data_to_file(str(result))
    else:
        print("Failed to read data frame.")

def handle_total_salary_and_headcount_department():
    data_frame = pd_lib.read_data_frame(pd_lib.get_data_file_path())
    if data_frame is not None:
        result = pd_lib.list_employee_numbers_and_total_outlay_by_department_sorted(data_frame)
        print(result)
        pd_lib.write_data_to_file(str(result))
    else:
        print("Failed to read data frame.")

def handle_total_salary_and_headcount_business_unit():
    data_frame = pd_lib.read_data_frame(pd_lib.get_data_file_path())
    if data_frame is not None:
        result = pd_lib.list_employee_numbers_and_total_outlay_by_business_unit_sorted(data_frame)
        print(result)
        pd_lib.write_data_to_file(str(result))
    else:
        print("Failed to read data frame.")

def handle_display_wage_slip_by_eeid():
    eeid = input("Enter the EEID to display the wage slip: ").strip()
    if not eeid:
        print("EEID cannot be empty.")
        return
    data_frame = pd_lib.read_data_frame(pd_lib.get_data_file_path())
    if data_frame is not None:
        wage_slip = pd_lib.display_wage_slip_by_eeid(data_frame, eeid)
        print(wage_slip)
        if input("Would you like to write this wage slip to a file? (yes/no): ").strip().lower() == 'yes':
            file_name = input("Enter the file name to write to (default 'wage_slip.txt'): ").strip() or 'wage_slip.txt'
            pd_lib.write_data_to_file(wage_slip, file_name)
    else:
        print("Failed to read data frame.")

def main():
    menu_options = pd_lib.get_menu_options()

    while True:
        display_menu(menu_options)
        choice = get_user_choice(menu_options)

        if choice is None:
            continue

        if choice == 1:
            handle_wage_query()
        elif choice == 2:
            handle_annual_salary_list_by_pay()
        elif choice == 3:
            handle_annual_salary_cost_by_job()
        elif choice == 4:
            handle_employee_numbers_and_outlay_by_department()
        elif choice == 5:
            handle_employee_numbers_and_outlay_by_business_unit()
        elif choice == 6:
            handle_palindrome_check()
        elif choice == 7:
            handle_advanced_employee_search()
        elif choice == 8:
            handle_display_employees_by_salary_range()
        elif choice == 9:
            handle_total_salary_and_headcount_department()
        elif choice == 10:
            handle_total_salary_and_headcount_business_unit()
        elif choice == 11:
            handle_data_to_text_file()
        elif choice == 12:  # New option for Display Wage Slip by EEID
            handle_display_wage_slip_by_eeid()
        elif choice == 13:  # Correct index for Exit
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()