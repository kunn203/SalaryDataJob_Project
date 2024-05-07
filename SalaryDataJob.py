import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



df=pd.read_csv('D:\Python\MiniProject - 2111894\ds_salaries.csv')

df['company_size'] = df['company_size'].replace({
    'S': 'Small',
    'M': 'Medium',
    'L' : 'Large',
})

df['remote_ratio'] = df['remote_ratio'].astype(str)
df['remote_ratio'] = df['remote_ratio'].replace({
    '0': 'On-Site',
    '50': 'Half-Remote',
    '100' : 'Full-Remote',
})

#Tổng công việc trong ngành Data
result_job = df[['job_title']].value_counts()
#Tổng số lượng hình thức công việc
result_type = df[['employment_type']].value_counts()
#Tổng số lượng các cấp bậc công việc
result_level=df[['experience_level']].value_counts(ascending=False)
#Tổng số lượng các kích thước các công ty
result_company_size=df[['company_size']].value_counts()
#Top 10 công việc phổ biến
top10_job=df[['job_title']].value_counts(ascending=True).iloc[-10:]
#Tỉ lệ làm việc từ xa
remote = df[['remote_ratio']].value_counts()
#Lương của từng cấp bậc cao nhất
level_salary=df.groupby('experience_level')['salary_in_usd'].max().sort_values(ascending=False)
#Trung bình lương của từng công việc
avg_salary = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)


font = {'family':'serif','weight':'bold','size': 7}
plt.rc('font',**font)




#Biểu đồ tỉ lệ của hình thức làm việc
plt.figure('Biểu đồ tỉ lệ của hình thức làm việc',figsize=(10,6))
type = np.array(['Full Time','Part Time','Contract','Freelance'])
result = result_type
colors = ['#8250C4','#5ECBC8','#438FFF','#FF977E']
plt.title('Tỉ lệ giữa các hình thức công việc',fontsize=13)
plt.pie(result,labels=type,colors=colors)
plt.legend(title='Type',loc='upper right',fontsize=8)
plt.show()

#Biểu đồ số lượng cấp bậc công việc
plt.figure('Biểu đồ số lượng cấp bậc công việc',figsize=(10,6))
level = df['experience_level'].unique()
result = result_level
plt.xlabel('Cấp bậc',fontsize=9)
plt.ylabel('Số lượng',fontsize=9)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.bar(level,result_level,color=["#8250C4",'#5ECBC8','#438FFF','#FF977E'])
plt.title('Số lượng nhân viên theo từng cấp bậc công việc',fontsize=13)
for i in range (len(level)):
    plt.text(i,result[i]+2,result[i],ha='center',va='center')
plt.show()

#Biểu đồ top10 các công việc phổ biến
plt.figure('Biểu đồ Top10 các công việc phổ biến',figsize=(15,6))
job_title = np.array(['Director of Data Science','Machine Learning Scientist','Big Data Engineer','Data Architect','Data Science Manager','Research Scientist','Machine Learning Engineer','Data Analyst','Data Engineer','Data Scientist'])
top10 = top10_job
plt.xlabel('Số lượng',fontsize=9)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.barh(job_title,top10,color="#8250C4")
plt.title('Top 10 công việc phổ biến',fontsize=13)
for i in range(len(top10)):
    plt.text(top10[i]+2.5,i,top10[i],ha='center',va='center')
plt.show()

#Biểu đồ tỉ lệ làm việc từ xa
plt.figure('Biểu đồ tỉ lệ làm việc từ xa',figsize=(10,6))
labels = np.array(['Full-Remote','On-Site','Half-Remote'])
plt.pie(remote,labels=labels,autopct='%1.1f%%',colors=['#8250C4','#5ECBC8','#438FFF'])
plt.legend(title='Tỉ lệ làm từ xa')
plt.title('Tỷ lệ làm việc từ xa',fontsize=13)
my_circle=plt.Circle( (0,0), 0.3, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.show()

#Biểu đồ tổng các loại hình công ty
plt.figure('Biểu đồ tổng các loại hình công ty',figsize=(10,6))
size = np.array(['Medium','Large','Small'])
result = result_company_size
plt.xlabel('Kích Thước',fontsize=9)
plt.ylabel('Số lượng',fontsize=9)
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.bar(size,result_company_size,color="#8250C4")
plt.title('Số lượng các loại hình công ty',fontsize=13)
for i in range (len(size)):
    plt.text(i,result[i]+2,result[i],ha='center',va='center')
plt.show()

#Biểu đồ mức lương cao nhất theo từng cấp bậc
plt.figure('Biểu đồ mức lương cao nhất theo từng cấp bậc',figsize=(10,6))
level = np.array(['Executive','Intermediate','Senior','Junior'])
plt.bar(level, level_salary, color="#8250C4")
plt.xlabel("Mức Lương")
plt.ylabel("Cấp bậc")
plt.title('Mức lương cao nhất theo từng bậc công việc',fontsize=13)
for i in range(len(level_salary)):
    plt.text(i,level_salary[i],level_salary[i],ha='center')
plt.show()
