DATA VALIDATION PROCESS
Importpandasasp
data=p.read_csv("phishing_data.csv")
data.head()
data.tail()
data.columns
data.shape
df=data.dropna()
df.shape
df.dtypes
df.isnull().sum()
df['Label'].value_counts()
df['URL_Depth'].value_counts()
df['Web_Traffic'].value_counts()
df['Domain_Age'].value_counts()
df.describe()
df.corr()
df.columns
p.Categorical(df['URL_Length']).describe()

