from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.feature_selection import RFE
import numpy as np


def encodeQualitative(variable,name_append,exclude):
    """creates dummy variables for the qualitative features. takes in pandas series and returns a pandas dataframe of the 
    dummy variables. Unlike in my prior HW when I only outputted n-1 columns, I'm going to output n columns to make interpretability easier
    also, this function takes in name_append which is used for creating unique column names since multiple variables have the same qualitative values to encode
    lastly, the exclude variable is a list that has values to exclude from the encoding such as excluding values that are mapped to a NA"""
    unique_values = np.unique(variable)
    #going through and deciding which unique values we want to actually keep
    final_unique = []
    for i in range(len(unique_values)):
        if unique_values[i] not in exclude:
            final_unique.append(unique_values[i])
    unique_values = final_unique
    #creating the column names for the final dataframe
    naming = []
    for j in range(len(unique_values)):
        naming.append(name_append+'_'+str(unique_values[j]))
    #creating the encoded variables
    new_vars = []
    for i in range(len(variable)):
        new_line = []
        for j in range(len(unique_values)):
            if variable[i] == unique_values[j]:
                new_line.append(1)
            else:
                new_line.append(0)
        new_vars.append(new_line)
    #creating the final dataframe to return
    new_vars_df = pd.DataFrame(new_vars,columns=naming)
    return new_vars_df


def getDeathRates3(data,p_variable,t_variable,ax,mapping):
    """This function takes in a dataframe, the name of the predictor variable to group on, and the target variable
    to create the rates on. It returns a list of [0 value rate, 1 value rate]. Also the axis is passed through
    in case of wanting to handle subplots. Lastly, a mapping dictionary variable is passed through which gives the definitions of
    each numerical value in the p_variable"""
    total_death_count = sum(data[t_variable])
    
    unique_p_values = np.unique(data[p_variable])
    
    names = []
    rates = []
    
    for value in unique_p_values:
        value_subset = data[data[p_variable]==value]
        rate = sum(value_subset[t_variable])/len(value_subset[t_variable])
        rates.append(rate)
        names.append(mapping[str(int(value))])
    
    ax.bar(unique_p_values, rates, align='center', alpha=0.5)
    #plt.xticks(y_pos, objects)
    ax.set_xlabel(p_variable)
    ax.set_xticks(unique_p_values)
    ax.set_xticklabels(names)
    ax.set_ylabel('Death Rate')
    ax.set_title('Death Rate by '+p_variable)
    
    return ax



def getMetricSummaries(metrics):
    """This function takes in a list of confusion metric summaries (usually from cross validation over a range of factors) and
    then computes the listing of precision, recall, and accuracy for each factor then returns precision, recall and accuracy in that order."""
    precision = []
    recall = []
    acc = []
    for i in metrics:
        #the max(...,1) is in the case of 0 being in the denominator so precision shows up as 0 instead of error
        precision.append(i[1][1]/max((i[0][1]+i[1][1]),1))
        recall.append(i[1][1]/max(sum(i[1]),1))
        acc.append((i[0][0]+i[1][1])/max(1,(sum(i[0])+sum(i[1]))))
    
    return precision, recall, acc



def performValidations(X,y,variable_sets,folds,model):
    """Function takes in the X and y arrays and also takes in the stepwise models at each step of forward stepwise
    selection. Also takes in how many folds to do with K-fold and which model data should be fitted on"""
    cv = KFold(n_splits=folds, random_state=1, shuffle=True)
    #loop through each set and perform k-fold cross validation for each  model, then report the average classification rate
    #mean_accuracies = []
    #std_accuracies = []
    all_metrics = []
    for sett in variable_sets:
        #scores = cross_val_score(model, X[sett], y, scoring='accuracy', cv=cv, n_jobs=-1)
        predictions = cross_val_predict(model,X[sett],y,cv=cv)
        cm = metrics.confusion_matrix(y,predictions)
        all_metrics.append(cm)
        #mean_accuracies.append(scores.mean())
        #std_accuracies.append(scores.std())
    return all_metrics


def forwardSelection(X,y,model,factor):
    """This function goes and does forward selection using the X and y arrays passed in as well as the model to fit
    the data to. Also takes in which factor to use for model selection. Returns a list containing model from each addition 
    of next most useful feature."""
    predictors = list(X.columns)
    remaining_predictors = list(X.columns)
    factor_values = []
    feature_additions = [[]]

    for i in range(len(predictors)):
        max_factor = -999999999999999
        best_feature = ""
        for feature in remaining_predictors:
            features_to_use = list(feature_additions[-1])
            features_to_use.append(feature)
            model.fit(X[features_to_use],y)
            if factor == 'Deviance':
                #Deviance is -2* log likelihood estimate for model. Sklearn returns the negative of the log likelihood estimate
                #so I would need to multiply by +2. Except since I want to minimize this, but if the wanted comparison is with
                #Rate, then we would want to maximize, I will multiply by -2 so that capturing the maximum of the - vaue
                #will be the minimum of the + value
                f = -2*metrics.log_loss(y, model.predict_proba(X[features_to_use]), normalize=False)
            #if the factor to use is Rate, then that means to use classification accuracy score
            elif factor == 'Rate':
                f = model.score(X[features_to_use],y)
            if f > max_factor:
                max_factor = f
                best_feature = feature
                
        next_model = list(feature_additions[-1])
        next_model.append(best_feature)
        feature_additions.append(next_model)
        factor_values.append(max_factor)
        remaining_predictors.remove(best_feature)
        
    return feature_additions, factor_values