import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('insurance _csv.csv')

print(data.describe().transpose())


print('\033[95m -------------------------------------- SHAPE OF DATA ----------------------------------------- \033[0m')

print(f'Shape of data : {data.shape}')
print(f'Total {data.shape[0]} rows in the data.')
print(data.sex.value_counts())

print('\033[95m --------------------------------------CHARGES ARE PRETTY HIGHER FOR SMOKERS ----------------------------------------- \033[0m')
print(data.groupby('smoker',)['charges'].max())





# plt.subplot(3,3,3)
# plt.hist(data.charges, color='lightblue', edgecolor = 'black', alpha = 0.7)
# plt.xlabel('charges')

# plt.show()


# plt.figure(figsize  = (4,2))
# plt.subplot(3,1,1)
# sns.boxplot(x= data.bmi, color='lightblue')

# plt.subplot(3,1,2)
# sns.boxplot(x= data.age, color='lightblue')

# plt.show()








plt.figure(figsize=(8,6))
sns.scatterplot(data.age, data.charges,hue=data.smoker,palette= ['red','green'] ,alpha=0.6)
plt.title('Smokers Tends to have more charges then NON smokers')
plt.show()



plt.figure(figsize=(8,6))
sns.lineplot(x = 'age',y = 'charges',data = data,hue = 'smoker')
plt.title('Smokers have wide sepration then non smokers ')
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(data.corr(),annot = True)
plt.title('Age and BMI also have strong positive relation with insurance')
plt.show()

print('\033[95m -------------------------------------SO AS PER THE ABOVE OBSERVATIONS ----------------------------------------- \033[0m \n\n')

print('\033[95m 1. \033[0m \033[4mas per the above observations charges have very strong relation with BMI and AGe \033[0m ... \n ')
print('\033[95m 2. \033[0m \033[4msmokers shows to have upward trend with charges and age as age increases charges increases \033[0m ... \n ')
print('\033[95m 3. \033[0m \033[4mso smokrs and elderly age are 2 major reasons for increasing in charges \033[0m ... \n ')

print('\033[95m 4. \033[0m \033[4mso Even the min of smoker is greater then max of non smoker \033[0m ... \n ')

print('MEAN OF SMOKERS :- \n',data.groupby('smoker')['charges'].mean())

