import pandas as pd

# Load the CSV file into a pandas dataframe
df = pd.read_csv('chinese_to_yale.csv')

# Ask the user to enter a Chinese character or multiple characters
user_input = input("Enter a Chinese character or multiple characters: ")

# Iterate through each Chinese character in the user-submitted string
for char in user_input:
    # Find the corresponding Yale romanization in the dataframe
    yale_romanization = df.loc[df['Chinese Characters'] == char, 'Yale Tone Marks'].values[0]
    
    # Print the Yale romanization in the terminal
    print(f"{char} = {yale_romanization}")