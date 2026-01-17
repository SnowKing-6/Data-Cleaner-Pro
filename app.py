# Import pandas library for data manipulation
import pandas as pd
# Import os library to handle file paths and existence
import os

# Welcome message
print("Hello my friend!", "\nThis tool is provided for free for the sake of Allah.")

# Loop until a file is successfully loaded
while True:
    # Ask the user for the file path
    file_path = input('\nEnter the data file path (e.g., data.csv): ')
    
    # Try to read the file to ensure the path is correct
    try:
        # Load the CSV file into a DataFrame
        data = pd.read_csv(file_path)
        # Inform the user of success
        print('--- Data loaded successfully ---')
        # Break the loop and proceed
        break
    # In case of any error during reading
    except Exception as e:
        # Alert the user about the error
        print(f'Error! Please ensure the path is correct and the file is in CSV format.')

# Main loop to display program options continuously
while True:
    # Display available options to the user
    print('\n================ MAIN MENU ================')
    print('1 - Handle Duplicates (General)')
    print('2 - Handle Missing Values (General)')
    print('3 - Handle Outliers (Replace with Mean)') # الميزة الجديدة
    print('4 - Save Data and Exit')
    
    # Get user choice as a string to avoid input errors
    choice = input('\nSelect an option: ')

    # --- Start of Duplicates Handling ---
    if choice == '1':
        print('\n--- Duplicate Options ---')
        print('a - Delete completely duplicated rows')
        print('b - Delete duplicates based on a specific column')
        sub_choice = input('Choose (a) or (b): ').lower()
        
        if sub_choice == 'a':
            data.drop_duplicates(inplace=True)
            print('All completely duplicated rows have been removed.')
            
        elif sub_choice == 'b':
            print("Available columns:", list(data.columns))
            col_name = input('Enter the column name to check for duplicates: ')
            if col_name in data.columns:
                data.drop_duplicates(subset=[col_name], inplace=True)
                print(f'Duplicates removed based on column: {col_name}')
            else:
                print('Error: Column name not found.')

    # --- Start of Missing Values Handling ---
    elif choice == '2':
        print('\nCurrent Missing Values Statistics:')
        print(data.isnull().sum())
        print('\n--- Missing Values Options ---')
        print('a - Delete rows containing any empty cells')
        print('b - Delete rows that are completely empty')
        print('c - Replace empty cells with zero (0)')
        sub_choice = input('Choose (a), (b), or (c): ').lower()

        if sub_choice == 'a':
            data.dropna(how='any', inplace=True)
            print('All rows containing empty cells have been removed.')
            
        elif sub_choice == 'b':
            data.dropna(how='all', inplace=True)
            print('Completely empty rows have been removed.')
            
        elif sub_choice == 'c':
            data.fillna(0, inplace=True)
            print('All empty cells have been replaced with 0.')

    # --- Start of Outlier Handling (The New Feature) ---
    elif choice == '3':
        print("\nAvailable columns:", list(data.columns))
        col_name = input('Enter the numeric column name to fix outliers: ')
        
        # Check if the column exists
        if col_name in data.columns:
            try:
                # Ensure the column is numeric
                data[col_name] = pd.to_numeric(data[col_name])
                
                # Calculate the Mean of the column
                column_mean = data[col_name].mean()
                print(f"Current average for {col_name} is: {column_mean:.2f}")

                # Ask user for logical boundaries
                low_limit = float(input('Enter the minimum logical value: '))
                high_limit = float(input('Enter the maximum logical value: '))

                # Logic: Replace any value outside limits with the Mean
                data.loc[(data[col_name] < low_limit) | (data[col_name] > high_limit), col_name] = column_mean
                
                print(f'Done! Outliers in "{col_name}" have been replaced with the mean value ({column_mean:.2f}).')
            except Exception as e:
                print("Error: Please make sure the column contains only numbers.")
        else:
            print("Error: Column name not found.")

    # --- Start of Saving and Exiting ---
    elif choice == '4':
        save_name = input('\nEnter the new filename to save (e.g., output.csv): ')
        try:
            data.to_csv(save_name, index=False)
            print(f'File saved successfully as: {save_name}')
            break
        except Exception as e:
            print('Error: Could not save file. Ensure it is not open in another program.')

    else:
        print('Invalid selection, please choose 1, 2, 3, or 4.')

# Final closing message
print('\nTool closed. Thank you, Razi!')
