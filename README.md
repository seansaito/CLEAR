# Counterfactual Local Explanations via Regression (CLEAR)

This repository has been created to provide access to the code to the version of CLEAR that was used for the Neurips submission
"Measurable Counterfactual Local Explanations for Any Classifier"

CLEAR explains single predictions of machine learning classifiers. It is based on the view that a satisfactory explanation of a single prediction needs to both
explain the value of that prediction and answer ’what-if-things-had-been-different’ questions. In doing this it needs to state the relative importance of the input features and show how they interact. A
satisfactory explanation must also be measurable and state how well it can explain a model. It *must know when it does not know*

### Prerequisites

CLEAR is written in Python 3.7 and Tensorflow 1.13. It runs on Windows 10. CLEAR requires the following Python libraries to be installed:
tkinter, numpy, pandas, sympy, datetime, matplotlib.pyplot, scipy.signal, csv, json, discretize.

### Installation

Download a copy of the CLEAR repository into a new directory on your PC. The file CLIME_settings.py contains the parameter variabler for CLEAR. Open CLIME_settings and change the value of parameter *LIME_path* to the name of the directory you have created for CLEAR e.g. LIME_path='D:/LIME/'

### Running CLEAR

First, CLEAR's parameters for the experiment should be set. 






