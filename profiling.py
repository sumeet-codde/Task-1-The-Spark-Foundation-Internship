import pandas as pd
from pandas_profiling import ProfileReport

#reading the data
df=pd.read_csv('student_scores - student_scores.csv')
profile=ProfileReport(df,title="The Spark Foundation-Intern")

# data will be generated in html file
profile.to_file(output_file="GRIP.html")
