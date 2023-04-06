7.2.1 DATA VISUALIZATION PROCESS:

importpandasaspd
importnumpyasnp
importmatplotlib.pyplotasplt
importseabornassb
#read the given dataset
df
df.columns
g=df['URL_Depth'].value_counts()
g.plot(kind='bar',color='b')

plt.title('URL Depth ',fontsize=18)
plt.xlabel('URL_Depth',fontsize=18)
plt.ylabel('Count',fontsize=18)
df
importpandasasp
importnumpyasn
importmatplotlib.pyplotasplt
importseabornass

defPropByVar(df,variable):

dataframe_pie=df[variable].value_counts()
ax=dataframe_pie.plot.pie(figsize=(10,10),autopct='%1.2f%%',fontsize=12);
ax.set_title(variable+' \n',fontsize=15);
returnn.round(dataframe_pie/df.shape[0]*100,2)

PropByVar(df,'URL_Depth')
importpandasasp
importnumpyasn
importmatplotlib.pyplotasplt
importseabornass

defPropByVar(df,variable):
myexplode=[0.2,0.2]
mycolors=["red","yellow"]
dataframe_pie=df[variable].value_counts()
ax=dataframe_pie.plot.pie(figsize=(10,10),autopct='%1.2f%%',fontsize=12,explode=myexplode,shadow=True,colors=mycolors);
ax.set_title(variable+' \n',fontsize=15);
returnn.round(dataframe_pie/df.shape[0]*100,2)


PropByVar(df,'DNS_Record')
importpandasasp
importnumpyasn
importmatplotlib.pyplotasplt
importseabornass

defPropByVar(df,variable):
myexplode=[0.2,0.2]
dataframe_pie=df[variable].value_counts()
ax=dataframe_pie.plot.pie(figsize=(10,10),autopct='%1.2f%%',fontsize=12,explode=myexplode,shadow=True);
ax.set_title(variable+' \n',fontsize=15);
returnn.round(dataframe_pie/df.shape[0]*100,2)


PropByVar(df,'Web_Forwards')
crosstab1=pd.crosstab(df["URL_Depth"],df["Label"])
crosstab1.plot(kind="bar",stacked=False,grid=False)

7.2.2 RandomForest Algorithm:
Application of Algorithm on dataset
