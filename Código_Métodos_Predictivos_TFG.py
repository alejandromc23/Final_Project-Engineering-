
# coding: utf-8

# In[73]:


import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm


# In[34]:


data=pd.read_excel("/home/alejandro/Escritorio/Datos Académicos ETSEIB/Notas(TFG)_binario.xls")


# In[35]:


X=[]
lista_var_respuesta=['ELECTROMAG','METODOS','MATERIALES','EDOS','INFO','MEC']
for e in data.columns.values.tolist()[:-3]:
    if e not in lista_var_respuesta:
        X.append(e)
X=X[6:]
X=data[X]


# # Regresión Logística

# In[38]:


for e in ['ELECTROMAG','METODOS','MATERIALES','EDOS','INFO','MEC']:
    print(e)
    l=['ALGEBRA','CALCULO1','MECFON','QUIMICA1','FONINFO','GEOMETRIA','CALCULO2','TERMO','QUIMICA2','EXPRE','Intentos ALGEBRA','Intentos CALCULO1','Intentos MECFON','Intentos QUIMICA1','Intentos FONINFO','Intentos GEOMETRIA','Intentos CALCULO2','Intentos TERMO','Intentos QUIMICA2','Intentos EXPRE','NOTA_ACCES']
    y=data[e]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=17, shuffle=True)
    model=LogisticRegression(C=10000000000)
    model.fit(X_train,y_train)
    predictions=model.predict(X_test)
    print( "Accuracy Score = " + str(accuracy_score(y_test, predictions)) + "\n")
    string = e + " = " + str(model.intercept_[0])
    for i in range(len(model.coef_[0])):
        string=string+ " + " + str(model.coef_[0][i]) + "*" +l[i]
    print(string + "\n")
    confm=confusion_matrix(y_test, predictions)
    print(confm)
    print(classification_report(y_test, predictions))
    # SI INTERESA SABER COMO CALCULA CADA UNO DE LOS TÉRMINOS ELIMINAR "#"
    #print("0 precision = " + str(confm[0][0]) + " / (" + str(confm[1][0]) + " + "+str(confm[0][0])+")")
    #print("1 precision = " + str(confm[1][1]) + " / (" + str(confm[1][0]) + " + "+str(confm[1][1])+")")
    #print("0 recall = " + str(confm[0][0]) + " / (" + str(confm[0][1]) + " + "+str(confm[0][0])+")")
    #print("1 recall = " + str(confm[1][1]) + " / (" + str(confm[1][0]) + " + "+str(confm[0][0])+")")
    #print("0 support = " + str(confm[0][0]) + " + "+str(confm[0][1]))
    #print("1 support = " + str(confm[1][0]) + " + "+str(confm[1][1]))


# # Árboles de Decisión

# In[47]:


l=[]
for a in ['ELECTROMAG','METODOS','MATERIALES','EDOS','INFO','MEC']:
    Y=data[a]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=17,shuffle=True)
    l1=[]
    for i in [1,2,3,5,7,10,15,20,25,30,35,40,45,50]:
        l2=[]
        for e in [1,2,3,5,7,10,15,20,25,30,35,40,45,50]:
            tree=DecisionTreeClassifier(criterion="entropy",max_depth=i,min_samples_leaf=e)
            tree.fit(X_train,y_train)
            prediction=tree.predict(X_test)
            confm=confusion_matrix(y_test,prediction)
            print( a + " : Prof =" + str(i)+", Min Elem = " + str(e) )
            print(confm)
            l2.append(tree.score(X_test,y_test))
        l1.append(l2)
    l.append(l1)
l


# In[55]:


l_asig=['ELECTROMAG','METODOS','MATERIALES','EDOS','INFO','MEC']
for e in range(len(l_asig)):
    dataframe=pd.DataFrame(
        {
            "Elementos por Nodo":[1,2,3,5,7,10,15,20,25,30,35,40,45,50],
            "1":l[e][0],
            "2":l[e][1],
            "3":l[e][2],
            "5":l[e][3],
            "7":l[e][4],
            "10":l[e][5],
            "15":l[e][6],
            "20":l[e][7],
            "25":l[e][8],
            "30":l[e][9],
            "35":l[e][10],
            "40":l[e][11],
            "45":l[e][12],
            "50":l[e][13]
        }

    )

    # ACTIVAR PARA CREAR EL ARCHIVO CON LA MATRIZ DE SCORES
    #dataframe[["Elementos por Nodo","1","2","3","5","7","10","15","20","25","30","35","40","45","50"]].to_excel("Dirección dónde guardarlo" + l_asig[e]+"Scores_ÁrbolesDecisionBUENOS.xls")


# In[60]:


l_0=[]
l_1=[]
for a in ['ELECTROMAG','METODOS','MATERIALES','EDOS','INFO','MEC']:
    Y=data[a]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=17,shuffle=True)
    l1_0=[]
    l1_1=[]
    for i in [1,2,3,5,7,10,15,20,25,30,35,40,45,50]:
        l2_0=[]
        l2_1=[]
        for e in [1,2,3,5,7,10,15,20,25,30,35,40,45,50]:
            tree=DecisionTreeClassifier(criterion="entropy",max_depth=i,min_samples_leaf=e)
            tree.fit(X_train,y_train)
            prediction=tree.predict(X_test)
            confm=confusion_matrix(y_test,prediction)
            print( a + " : Prof =" + str(i)+", Min Elem = " + str(e) )
            print(confm)
            recall0=confm[0][0]/(confm[0][1]+confm[0][0])
            print(str(recall0))
            recall1=confm[1][1]/(confm[1][0]+confm[1][1])
            #PARA MOSTRAR COMO SE CALCULAN LOS RECALLS DESACTIVAR #
            #print("0 recall = " + str(confm[0][0]) + " / (" + str(confm[0][1]) + " + "+str(confm[0][0])+")")
            #print("1 recall = " + str(confm[1][1]) + " / (" + str(confm[1][0]) + " + "+str(confm[1][1])+")")
            #print("Score testing = " + str(tree.score(X_test,y_test)))
            #print("Score para i = ",str(i)," es de ", score, "Std_deviation = ",std_score)
            l2_0.append(recall0)
            l2_1.append(recall1)
        l1_0.append(l2_0)
        l1_1.append(l2_1)
    l_0.append(l1_0)
    l_1.append(l1_1)


# In[65]:


l_asig=['ELECTROMAG','METODOS','MATERIALES','EDOS','INFO','MEC']
for e in range(len(l_asig)):
    dataframe=pd.DataFrame(
        {
            "Elementos por Nodo":[1,2,3,5,7,10,15,20,25,30,35,40,45,50],
            "1":l_0[e][0],
            "2":l_0[e][1],
            "3":l_0[e][2],
            "5":l_0[e][3],
            "7":l_0[e][4],
            "10":l_0[e][5],
            "15":l_0[e][6],
            "20":l_0[e][7],
            "25":l_0[e][8],
            "30":l_0[e][9],
            "35":l_0[e][10],
            "40":l_0[e][11],
            "45":l_0[e][12],
            "50":l_0[e][13]

            }

        )
        # ACTIVAR PARA CREAR EL ARCHIVO CON LA MATRIZ DE RECALLS PARA LA CLASE 0
        #dataframe[["Elementos por Nodo","1","2","3","5","7","10","15","20","25","30","35","40","45","50"]].to_excel("dirección" + l_asig[e]+"Recall0.xls")


# In[68]:


l_asig=['ELECTROMAG','METODOS','MATERIALES','EDOS','INFO','MEC']
for e in range(len(l_asig)):
    dataframe=pd.DataFrame(
        {
            "Elementos por Nodo":[1,2,3,5,7,10,15,20,25,30,35,40,45,50],
            "1":l_1[e][0],
            "2":l_1[e][1],
            "3":l_1[e][2],
            "5":l_1[e][3],
            "7":l_1[e][4],
            "10":l_1[e][5],
            "15":l_1[e][6],
            "20":l_1[e][7],
            "25":l_1[e][8],
            "30":l_1[e][9],
            "35":l_1[e][10],
            "40":l_1[e][11],
            "45":l_1[e][12],
            "50":l_1[e][13]

            }

        )
        # ACTIVAR PARA CREAR EL ARCHIVO CON LA MATRIZ DE RECALLS PARA LA CLASE 0
        #dataframe[["Elementos por Nodo","1","2","3","5","7","10","15","20","25","30","35","40","45","50"]].to_excel("/Users/aleja/Desktop/Datos TFG/" + l_asig[e]+"Recall1.xls")


# In[70]:


dataframe[["Elementos por Nodo","1","2","3","5","7","10","15","20","25","30","35","40","45","50"]]


# # SVM (Kernel Lineal)

# In[ ]:


lista=['ALGEBRA','CALCULO1','MECFON','QUIMICA1','FONINFO','GEOMETRIA','CALCULO2','TERMO','QUIMICA2','EXPRE','Intentos ALGEBRA','Intentos CALCULO1','Intentos MECFON','Intentos QUIMICA1','Intentos FONINFO','Intentos GEOMETRIA','Intentos CALCULO2','Intentos TERMO','Intentos QUIMICA2','Intentos EXPRE','NOTA_ACCES']
X=data[lista]
for a in ['ELECTROMAG','METODOS','MATERIALES','EDOS','INFO','MEC']:
    print(a)
    target=data[a]
    X_train, X_test, target_train, target_test = train_test_split(X, target, test_size=0.3, random_state=17, shuffle=True)
    l=[0.001,0.01,0.1,1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]
    for i in range(len(l)):
        classifier= svm.SVC(kernel="linear",C=l[i])
        classifier.fit(X_train, target_train)
        prediction=classifier.predict(X_test)
        print("C = " + str(l[i]) + ", Score = " + str(classifier.score(X_test,target_test)) + ", Number of Support Vectors = "+str(len(classifier.support_vectors_)))
        confm=confusion_matrix(target_test,prediction)
        print(confm)
        print(classification_report(target_test, prediction))
        # ELIMINAR "#" PARA MOSTRAR EL CÁLCULO DE CADA UNO DE LOS TÉRMINOS DE INTERÉS
        #print("0 precision = " + str(confm[0][0]) + " / (" + str(confm[1][0]) + " + "+str(confm[0][0])+")")
        #print("1 precision = " + str(confm[1][1]) + " / (" + str(confm[1][0]) + " + "+str(confm[1][1])+")")
        #print("0 recall = " + str(confm[0][0]) + " / (" + str(confm[0][1]) + " + "+str(confm[0][0])+")")
        #print("1 recall = " + str(confm[1][1]) + " / (" + str(confm[1][0]) + " + "+str(confm[1][1])+")")
        #print("0 support = " + str(confm[0][0]) + " + "+str(confm[0][1]))
        #print("1 support = " + str(confm[1][0]) + " + "+str(confm[1][1]) + "\n")
        string="Ecuación Plano : 0 = " + str(classifier.intercept_[0])
        for e in range(len(classifier.coef_[0])):
            string=string+ " + " + str(classifier.coef_[0][e]) + "*" +lista[e]
        print(string)

