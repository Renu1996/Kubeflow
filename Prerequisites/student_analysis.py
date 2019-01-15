import pandas as pd

data = pd.read_csv('StudentsPerformance.csv')

math_mean = data['math score'].mean()
read_mean = data['reading score'].mean()
write_mean = data['writing score'].mean()

print("Math score mean = "+str(math_mean))
print("Reading score mean = "+str(read_mean))
print("Writing score mean = "+str(write_mean))

grouped_mean = data.groupby('gender').mean()
print("Subject means grouped by genders are as follows: ")
print(grouped_mean)
