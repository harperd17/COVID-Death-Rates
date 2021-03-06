# COVID-Death-Rates
This repository uses classification methods to predict whether a patient with COVID will die given their underlying health measures.
# Could COVID Kill You?
---
## Summary
---
Logistic Regression and Decision Tree Machine Learning algorithms were applied to the data set, with the binary feature "Died" being the target variable. All risk factors were included in the analysis as well as the Mexican state of residence of that person. The final model selected was a Logistic Regression model. The final selected Logistic Regression model uses the features pneumonia, kidney failure, age, and sex, which were selected using backward stepwise feature selection. It acheived an accuracy, precision, and recall of 90.59%, 59.66%, and 36.24% when applied to test data. The features found to raise the probability of death the most for a COVID positive patient were found to be whether or not the patient has pneumonia, kidney failure, and their age.
## Data
---
This project uses data from a Mexican Government [website](https://www.gob.mx/salud/documentos/datos-abiertos-152127). I found a link to this dataset in a [kaggle](https://www.kaggle.com/tanmoyx/covid19-patient-precondition-dataset) project that somebody has done. I thought that finding COVID data would be easier than this, but it turns out that HIPPA laws do not allow data on the individual patient level to be made available to the public even if their names are left out. Therefore, only summary level data sets (like by county, or by age group) are able to be viewed by the public. This data set from the Mexican Government is at the individual patient level and doesn't provide any patient identification information.
After cleaning, the data contains 696,781 observations of people testing positive for COVID as well as information such as where they live, where they were born, their age, sex, and underlying health conditions. The risk factors presented in this data set include the presence of Pneumonia, Diabetes, COPD, Asthma, Immunosuppression, Hypertension, Cardiovascular Disease, Obesity, Kidney Failure, Pregnancy, Smoker, and an umbrella term of Other Diseases. For each observation, we are shown whether or not the patient died.
## Repository Contents
---
<pre>
Data            : <a href=https://github.com/harperd17/COVID-Death-Rates/blob/master/Data>Data Files </a>
                 Raw data file found in 'Raw Data.zip' and data files used for visualization and modelling found in 'Manipulated Data.zip'

Code            : <a href=https://github.com/harperd17/COVID-Death-Rates/blob/master/Notebooks/Data_Cleanup.ipynb>Data Cleaning Notebook </a>
                : <a href=https://github.com/harperd17/COVID-Death-Rates/blob/master/Notebooks/Data_Visualizations.ipynb>Data Visualization Notebook </a>
                : <a href=https://github.com/harperd17/COVID-Death-Rates/blob/master/Notebooks/Final_Classification_Modelling.ipynb>Classification Modelling Notebook </a>
                
Report          : <a href=https://github.com/harperd17/COVID-Death-Rates/blob/main/Report/Final%20Report_Notebook.ipynb>Report Notebook</a>

Presentation    : <a href=https://github.com/harperd17/COVID-Death-Rates/blob/main/Presentation/Project_Presentation.pdf>Presentation Slides</a>
                : <a href=https://youtu.be/fXX6ErDWHBc>Presentation Video</a>
</pre>
