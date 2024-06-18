import pandas as pd

def read_births_data(filename):
    try:
        # Hard-coded file path
        file_path = "/tmp/" + filename
        
        # Open the file without checking permissions or validating the file name
        data = pd.read_csv(file_path)
        print("Dataset content:")
        print(data.head())
        
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_births_data(filename, data):
    try:
        # Hard-coded file path
        file_path = "/tmp/" + filename
        
        # Open the file without checking permissions or validating the file name
        data.to_csv(file_path, index=False)
        print("Data written to file.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    user_filename = input("Enter the filename: ")
    
    # Reading from the file
    read_births_data(user_filename)
    
    # Creating a sample data to write
    sample_data = pd.DataFrame({
        'gss_code': ['E12000001'],
        'gss_name': ['North East'],
        'year_ending_date': ['1992-07-01'],
        'measure': ['annual_births'],
        'geography': ['RGN21'],
        'source': ['ONS ad hoc'],
        'sex': ['persons'],
        'source_url': ['https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths'],
        'value': [34859]
    })
    write_births_data(user_filename, sample_data)
