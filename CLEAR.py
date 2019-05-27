""" This is the main script for CLEAR applied to the PIMA Indains Diabetes Dataset.
 Last amended 19/12/2018
 
Inputs: PIMA Indian Diabetes Dataset: 'diabetes.csv'
        Results of grid searches on MPL to identify its decision boundaries
                                      'Final_diabetes_sensitivity1.csv'
                                      'Final_diabetes_sensitivity2.csv'
Outputs: File on accuracy of MLP:   'nn_datetime.csv'
         File with local regression statistics: 'LIME_datetime.csv'
         File with all counterfactual perturbations: 'nn_commf_datetime.csv'
         File with all infeasible perturbations: 'missing_log_df_datetime.csv'
"""
 
import numpy as np
import CLEAR_cont, Create_sensitivity_files
import CLEAR_settings, CLEAR_Process_Dataset, CLEAR_perturbations,CLEAR_regression
import time
import sys
start_time = time.time()  
CLEAR_settings.init()
print('Performing grid search - step 1 of CLEAR method')
(X_train,X_test_sample,model,numeric_features,category_prefix,feature_list) \
 =Create_sensitivity_files.Create_sensitivity()
for neighbour_seed in range(0,1):
    if CLEAR_settings.LIME_comparison  == False:    
        (X_test_sample,explainer,sensitivity_df,feature_list,numeric_features, model)\
             = CLEAR_Process_Dataset.Create_Neighbourhoods(X_train,X_test_sample,model,\
                              numeric_features,category_prefix,feature_list,neighbour_seed) 
        results_df=CLEAR_regression.Run_Regressions(X_test_sample,explainer,feature_list)
        CLEAR_perturbations.Calculate_Perturbations(explainer, results_df,sensitivity_df,feature_list,numeric_features, model)
    elif CLEAR_settings.LIME_comparison  == True:
        CLEAR_cont.LIME_CLEAR(neighbour_seed)
    else:
        print('Evaluation type misspecified')
        sys.exit()
        
end_time = time.time()
print("Total execution time: {}".format(end_time - start_time))
    