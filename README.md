# COVID-Death-Rates
This repository uses classification methods to predict whether a patient with COVID will die given their underlying health measures.
# How do your underlying health conditions impact the chances of COVID killing you if infected?
---
## Summary
---
Logistic Regression and Decision Tree Machine Learning algorithms were applied to the data set, with the binary feature "Died" being the target variable. All risk factors were included in the analysis as well as the Mexican state of residence of that person. The final selected model was <b>Final Model!!!</b>. When applied to a test data set, the model yielded a precision, recall, and accuracy of <b> Insert Here</b> respectively. The features used in predicting the life outcome of a COVID positive patient were <b> Insert features here </b>.
For the Logistic Regression model, Forward Stepwise and Backward Stepwise feature selection were considered in this project, as well as full feature selection using L2 Regularization. All considered models were tested first using 10-fold cross validation. <The Final model was ...</b>. 
All features were considered in the Decision Tree model, but the number of leaf nodes was controlled at various 
## Data
---
This project uses data from a Mexican Government [website](https://www.gob.mx/salud/documentos/datos-abiertos-152127). I found a link to this dataset in a [kaggle](https://www.kaggle.com/tanmoyx/covid19-patient-precondition-dataset) project that somebody has done. I thought that finding COVID data would be easier than this, but it turns out that HIPPA laws do not allow data on the individual patient level to be made available to the public even if their names are left out. Therefore, only summary level data sets (like by county, or by age group) are able to be viewed by the public. This data set from the Mexican Government is at the individual patient level and doesn't provide any patient identification information.
After cleaning, the data contains 696,781 observations of people testing positive for COVID as well as information such as where they live, where they were born, their age, sex, and underlying health conditions. The risk factors presented in this data set include the presence of Pneumonia, Diabetes, COPD, Asthma, Immunosuppression, Hypertension, Cardiovascular Disease, Obesity, Kidney Failure, Pregnancy, Smoker, and an umbrella term of Other Diseases. For each observation, we are shown whether or not the patient died.
## Repository Contents
---
<pre>
Code        : <a href=https://github.com/harperd17/COVID-Death-Rates/blob/master/Notebooks/Data_Cleanup.ipynb>Data Cleaning Notebook </a>
            : <a href=https://github.com/harperd17/COVID-Death-Rates/blob/master/Notebooks/Data_Visualizations.ipynb>Data Visualization Notebook </a>
            : <a href=https://github.com/harperd17/COVID-Death-Rates/blob/master/Notebooks/Modelling_code.ipynb>Classification Modelling Notebook </a>
Report      : <a href=https://github.com/harperd17/COVID-Death-Rates/blob/master/Report/Report_Notebook.ipynb>Report Notebook</a>
Presentation: <a href=https://github.com/harperd17/COVID-Death-Rates/blob/master/Presentation/Presentation_Slides.html>Report Notebook</a>
</pre>
