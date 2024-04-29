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

def convert_exp(row):
    # assert  (row['formatted_experience_level'].isna())or(row['formatted_experience_level'] in ['Entry level', 'Mid-Senior level', 'Associate', 'Director', 'Internship', 'Executive']),print("row['formatted_experience_level']:",row['formatted_experience_level'])
    if type(row['formatted_experience_level'])!=str:
        # print("row['formatted_experience_level']:",row['formatted_experience_level'])
        if pd.isna(row['formatted_experience_level']):
            return 0
        else:
            print("Error!")
            print("row['formatted_experience_level']:",row['formatted_experience_level'])
            assert 0
    elif row['formatted_experience_level'] == 'Internship':
        return 0
    elif row['formatted_experience_level'] == 'Entry level':
        return 1 
    elif row['formatted_experience_level'] == 'Associate':
        return 2
    elif row['formatted_experience_level'] == 'Mid-Senior level':
        return 3
    elif row['formatted_experience_level'] == 'Director':
        return 4
    elif row['formatted_experience_level'] == 'Executive':
        return 5
    else:
        print("Error!")
        print("row['formatted_experience_level']:",row['formatted_experience_level'])
        assert 0
def cal_esposed_time(row):
    return(row['expiry']-row['original_listed_date'])
# Load the CSV file
file_path = 'original_data/job_postings.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
print(data.head())
print("before processing, data length:", len(data))

print('currency:', data['currency'].unique())

# Drop trash
data = data.drop(columns=['description','job_posting_url', 'application_url','skills_desc',])
data = data.drop(columns=['original_listed_time','expiry', 'closed_time','listed_time',])
# data = data.drop(columns=['currency']
# check all possible 'work_type' in data
unique_work_type = data['work_type'].unique()
print("possible work_type:", unique_work_type)


# Filter the data for rows where 'formatted_work_type' is 'Full-time'
data = data[data['work_type'] == 'FULL_TIME']
print("after processing1, data length:", len(data))



# check all possible 'pay_period' in data
unique_pay_period = data['pay_period'].unique()
print("possible pay_period:", unique_pay_period)

# Filter the data that 'pay_period' is 'MONTHLY' or 'YEARLY'
data = data[data['pay_period'].isin(['MONTHLY', 'YEARLY'])]
print("after processing2, data length:", len(data))

# Filter the data that 'salary' slot is filled
data = data[~data['max_salary'].isna()| ~data['med_salary'].isna()| ~data['min_salary'].isna()]
print("after processing3, data length:", len(data))


# drop 'med_salary', 'max_salary', 'min_salary' and only keep one number to represent the salary
data['salary'] = data.apply(simplified_salary, axis=1)
data = data.drop(columns=['med_salary', 'max_salary', 'min_salary'])

# convert monthly pay to yearly pay
data['salary'] = data.apply(calculate_salary, axis=1)
data = data.drop(columns=['pay_period'])



# check all possible 'formatted_experience_level' in data
unique_formatted_experience_level = data['formatted_experience_level'].unique()
print("unique_formatted_experience_level:",unique_formatted_experience_level)

# convert 'formatted_experience_level' to a number
data['exp_needed']=data.apply(convert_exp, axis=1)
data = data.drop(columns=['formatted_experience_level'])

# check all possible 'application_type' in data
print("unique_application_type:",data['application_type'].unique())

# data['esposed_time']=data.apply(cal_esposed_time, axis=1)
# data = data.drop(columns=['original_listed_date', 'expiry'])

print(data.head())

# Fill the empties of the columens applies & remote_allowed & views
data['applies'] = data['applies'].fillna(value=0)
data['remote_allowed'] = data['remote_allowed'].fillna(value=0)
data['views'] = data['views'].fillna(value=0)

# Save the filtered data to a new CSV file
filtered_file_path = 'processed_data/job_postings_processed.csv'
data.to_csv(filtered_file_path, index=False)