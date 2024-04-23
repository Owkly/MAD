import pandas as pd
import numpy as np

def simplified_salary(row):
    if pd.notna(row['med_salary']):
        return row['med_salary']
    elif pd.notna(row['max_salary']) and pd.notna(row['min_salary']):
        return (row['max_salary'] + row['min_salary']) / 2
    elif pd.notna(row['max_salary']):
        return row['max_salary']
    elif pd.notna(row['min_salary']):
        return row['min_salary']
    else:
        return None
    
def calculate_salary(row):
    if row['pay_period']=='MONTHLY':
        return row['salary']*12
    else:
        return row['salary']



# Load the CSV file
file_path = 'original_data/job_postings.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
print(data.head())
print("before processing, data length:", len(data))

# check all possible 'work_type' in data
unique_work_type = data['work_type'].unique()
print("possible work_type:", unique_work_type)


# Filter the data for rows where 'formatted_work_type' is 'Full-time'
data = data[data['work_type'] == 'FULL_TIME']
print("after processing1, data length:", len(data))



# check all possible 'pay_period' in data
unique_pay_period = data['pay_period'].unique()
print("possible pay_period:", unique_pay_period)

# Filter the data for rows where 'pay_period' is 'MONTHLY' or 'YEARLY'
data = data[data['pay_period'].isin(['MONTHLY', 'YEARLY'])]
print("after processing2, data length:", len(data))

# Filter the data for 'salary' slot is filled
data = data[~data['max_salary'].isna()| ~data['med_salary'].isna()| ~data['min_salary'].isna()]
print("after processing3, data length:", len(data))


# drop 'med_salary', 'max_salary', 'min_salary' and only keep one number to represent the salary
data['salary'] = data.apply(simplified_salary, axis=1)
data = data.drop(columns=['med_salary', 'max_salary', 'min_salary'])

# convert monthly pay to yearly pay
data['salary'] = data.apply(calculate_salary, axis=1)
data = data.drop(columns=['pay_period'])


print(data.head())

# Save the filtered data to a new CSV file
filtered_file_path = 'processed_data/job_postings_processed.csv'
data.to_csv(filtered_file_path, index=False)