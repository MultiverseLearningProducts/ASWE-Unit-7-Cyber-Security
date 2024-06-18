import pandas as pd
import os

def read_births_data(filename):
    try:
        # Validate and sanitize the filename
        if not os.path.basename(filename) == filename:
            raise ValueError("Invalid filename")
        
        file_path = os.path.join("/tmp", filename)
        
        # Check if file exists and has read permission
        if not os.access(file_path, os.R_OK):
            raise PermissionError("File is not accessible or does not exist.")
        
        data = pd.read_csv(file_path)
        print("Dataset content:")
        print(data.head())
        
    except (FileNotFoundError, PermissionError, ValueError) as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

def write_births_data(filename, data):
    try:
        # Validate and sanitize the filename
        if not os.path.basename(filename) == filename:
            raise ValueError("Invalid filename")
        
        file_path = os.path.join("/tmp", filename)
        
        # Check if file has write permission
        if not os.access(file_path, os.W_OK):
            raise PermissionError("No write permission for the file.")
        
        data.to_csv(file_path, index=False)
        print("Data written to file.")
        
    except (PermissionError, ValueError) as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    user_filename = input("Enter the filename: ")
    
    # Reading from the file
    read_births_data(user_filename)
    
    # Creating a sample data to write
    sample_data = pd.DataFrame({
        'gss_code': ['E12000001', 'E12000001'],
        'gss_name': ['North East', 'North East'],
        'year_ending_date': ['1992-07-01', '1993-07-01'],
        'measure': ['annual_births', 'annual_births'],
        'geography': ['RGN21', 'RGN21'],
        'source': ['ONS ad hoc', 'ONS ad hoc'],
        'sex': ['persons', 'persons'],
        'source_url': [
            'https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths',
            'https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths'
        ],
        'value': [34859, 32900]
    })
    
    # Writing the sample data to the file
    write_births_data(user_filename, sample_data)
