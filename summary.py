import pandas as pd
import os
import glob

# Specify the directory containing the files
directory = 'D:\Project\Test_para\Result\excel_result'
file_pattern = os.path.join(directory, '*.xlsx')  # Adjust the pattern if your files have a different extension

# List to hold data for the summary
summary_data = []

# Process each file in the directory
for file_path in glob.glob(file_pattern):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Calculate the average of columns B to E
    average_fitness= df.iloc[:, 1:-3].mean(axis=1).mean()  # Adjust column indices if needed
    
    # Calculate the average of column F
    average_runtime = df.iloc[:, -2].mean()  # Adjust the column index if needed
    
    # Append the results to the summary list
    summary_data.append([os.path.basename(file_path), average_fitness, average_runtime])

# Create a DataFrame for the summary
summary_df = pd.DataFrame(summary_data, columns=['File Name', 'Average Fitness', 'Average Runtime'])

# Write the summary DataFrame to an Excel file
summary_df.to_excel('summary_output.xlsx', index=False)

print("Summary file created successfully.")