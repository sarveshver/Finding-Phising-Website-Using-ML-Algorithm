#import libraries for access and functional purpose
importpandasasp
importnumpyasn
importmatplotlib.pyplotasplt
importseabornass
importwarnings
warnings.filterwarnings('ignore')

#read the given dataset
df=p.read_csv('phishing_data.csv')
df.columns
fromsklearn.preprocessingimportLabelEncoder
var_mod=['Domain','Have_IP','Have_At','URL_Length','URL_Depth',
'Redirection','https_Domain','TinyURL','Prefix/Suffix','DNS_Record',
'Web_Traffic','Domain_Age','Domain_End','iFrame','Mouse_Over',
'Right_Click','Web_Forwards','Label'
]
le=LabelEncoder()
foriinvar_mod:
df[i]=le.fit_transform(df[i]).astype(str)
df.columns
df.head()
fromsklearn.metricsimportconfusion_matrix,classification_report,matthews_corrcoef,cohen_kappa_score,accuracy_score,average_precision_score,roc_auc_score
X=df.drop(labels='Label',axis=1)
#Response variable
y=df.loc[:,'Label']
fromsklearn.model_selectionimporttrain_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1,stratify=y)
print("Number of Training Data:",len(X_train))
print("Number of Testing Data:",len(X_test))
print("Total Dataset:",len(X_test)+len(X_train))
fromsklearn.ensembleimportRandomForestClassifier
rf=RandomForestClassifier()
rf.fit(X_train,y_train)
x=(accuracy_score(y_test,predictrf)*100)
print('Accuracy result is',x)
print("")
c=confusion_matrix(y_test,predictrf)
print(c)
sensitivity1=c[0,0]/(c[0,0]+c[0,1])
print('Sensitivity : ',sensitivity1)
print("")
specificity1=c[1,1]/(c[1,0]+c[1,1])
print('Specificity : ',specificity1)
print("")
TN=c[0][0]
FN=c[1][0]
TP=c[1][1]
FP=c[0][1]
print("True Positive :",TP)
print("True Negative :",TN)
print("False Positive :",FP)
print("False Negative :",FN)
print("")
TPR=TP/(TP+FN)
TNR=TN/(TN+FP)
FPR=FP/(FP+TN)
FNR=FN/(TP+FN)
print("True Positive Rate :",TPR)
print("True Negative Rate :",TNR)
print("False Positive Rate :",FPR)
print("False Negative Rate :",FNR)
print("")
PPV=TP/(TP+FP)
NPV=TN/(TN+FN)
print("Positive Predictive Value :",PPV)
print("Negative predictive value :",NPV)
fromsklearn.svmimportSVC
s=SVC()
s.fit(X_train,y_train)
predictSV=s.predict(X_test)
print(classification_report(y_test,predictSV
))
x=(accuracy_score(y_test,predictSV)*100)
print('Accuracy result is',x)
print("")
cm=confusion_matrix(y_test,predictSV)
sensitivity1=cm[0,0]/(cm[0,0]+cm[0,1])
print('Sensitivity : ',sensitivity1)
print("")
specificity1=cm[1,1]/(cm[1,0]+cm[1,1])
print('Specificity : ',specificity1)
print("")
TN=cm[0][0]
FN=cm[1][0]
TP=cm[1][1]
FP=cm[0][1]
print("True Positive :",TP)
print("True Negative :",TN)
print("False Positive :",FP)
print("False Negative :",FN)
print("")
TPR=TP/(TP+FN)
TNR=TN/(TN+FP)
FPR=FP/(FP+TN)
FNR=FN/(TP+FN)
print("True Positive Rate :",TPR)
print("True Negative Rate :",TNR)
print("False Positive Rate :",FPR)
print("False Negative Rate :",FNR)
print("")
PPV=TP/(TP+FP)
NPV=TN/(TN+FN)
print("Positive Predictive Value :",PPV)