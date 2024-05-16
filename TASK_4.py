import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dataset=pd.read_csv("C:\\Users\\SUCHETA P\\Downloads\\twitter_validation.csv")
dataset=dataset.drop(['sentiment'],axis=1)
print(dataset.head(5))
plt.figure(figsize=(6,4))
sns.histplot(x='entity',data=dataset)
plt.xticks(rotation=90,fontsize=5)
plt.show()
sns.histplot(x='comment',data=dataset)
plt.show()
count_ = dataset.groupby(['entity', 'comment']).size().reset_index(name='count')
print(count_.head())
# plot the barplot
plt.figure(figsize=(6,4))
sns.barplot(x='entity', y='count', hue='comment', data=count_)
plt.xticks(rotation=90,fontsize=5)
plt.show()
print(dataset['entity'].value_counts())
