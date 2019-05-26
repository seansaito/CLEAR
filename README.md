# Counterfactual Local Explanations via Regression (CLEAR)

This repository has been created to provide access to the code to the version of CLEAR that was used for the Neuips submission
"Measurable Counterfactual Local Explanations for Any Classifier"

CLEAR explains single predictions of machine learning classifiers. It is based on the view that a satisfactory explanation of a single prediction needs to both
explain the value of that prediction and answer ’what-if-things-had-been-different’ questions. In doing this it needs to state the relative importance of the input features and show how they interact. A
satisfactory explanation must also be measurable and state how well it can explain a model. It *must know when it does not know*

### Prerequisites

CLEAR is written in Python 3.7 and Tensorflow 1.13. It runs on Windows 10. CLEAR requires the following Python libraries to be installed:
tkinter, numpy, pandas, sympy, datetime, matplotlib.pyplot, scipy.signal, csv, json, discretize.

### Installation

The user needs to create a directory on their PC in which to download the following files:

CLIME_settings.py
CLIME_regression.py
CLEAR_cont.py
lime_tabular.py
CLIME_perturbations.py
LIME_CLEAR_ comp.py
CLIME_Process_Dataset.py




