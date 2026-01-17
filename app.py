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
    print('3 - Save Data and Exit')
    
    # Get user choice as a string to avoid input errors
    choice = input('\nSelect an option: ')

    # --- Start of Duplicates Handling ---
    if choice == '1':
        print('\n--- Duplicate Options ---')
        print('a - Delete completely duplicated rows')
        print('b - Delete duplicates based on a specific column')
        sub_choice = input('Choose (a) or (b): ').lower()
        
        # Option to delete exact row matches
        if sub_choice == 'a':
            data.drop_duplicates(inplace=True)
            print('All completely duplicated rows have been removed.')
            
        # Option to delete duplicates based on a specific column (e.g., ID)
        elif sub_choice == 'b':
            # Display available columns for the user to choose from
            print("Available columns:", list(data.columns))
            col_name = input('Enter the column name to check for duplicates: ')
            
            # Check if the column exists in the data
            if col_name in data.columns:
                data.drop_duplicates(subset=[col_name], inplace=True)
                print(f'Duplicates removed based on column: {col_name}')
            else:
                print('Error: Column name not found.')

    # --- Start of Missing Values Handling ---
    elif choice == '2':
        # Calculate and display the count of missing values per column
        print('\nCurrent Missing Values Statistics:')
        print(data.isnull().sum())
        print('\n--- Missing Values Options ---')
        print('a - Delete rows containing any empty cells')
        print('b - Delete rows that are completely empty')
        print('c - Replace empty cells with zero (0)')
        sub_choice = input('Choose (a), (b), or (c): ').lower()

        # Drop row if it contains at least one null value
        if sub_choice == 'a':
            data.dropna(how='any', inplace=True)
            print('All rows containing empty cells have been removed.')
            
        # Drop row only if all cells in that row are empty
        elif sub_choice == 'b':
            data.dropna(how='all', inplace=True)
            print('Completely empty rows have been removed.')
            
        # Fill all null values with 0
        elif sub_choice == 'c':
            data.fillna(0, inplace=True)
            print('All empty cells have been replaced with 0.')

    # --- Start of Saving and Exiting ---
    elif choice == '3':
        # Ask for the new filename
        save_name = input('\nEnter the new filename to save (e.g., output.csv): ')
        # Try to save the file
        try:
            # Export data to a new CSV without the index column
            data.to_csv(save_name, index=False)
            print(f'File saved successfully as: {save_name}')
            # Terminate the program
            break
        # In case the file is open elsewhere or permission is denied
        except Exception as e:
            print('Error: Could not save file. Ensure it is not open in another program.')

    # Handle undefined inputs in the main menu
    else:
        print('Invalid selection, please choose 1, 2, or 3.')

# Final closing message
print('\nTool closed. Thank you, Razi!')
