""" This is the main script for CLIME applied to the PIMA Indains Diabetes Dataset.
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
import CLEAR_cont
import CLIME_settings, CLIME_Process_Dataset, CLIME_perturbations,CLIME_regression
import time
import sys
Evaluation_type = 'CLIME' #LIME_evaluate
np.random.seed(1)
start_time = time.time()  
for neighbour_seed in range(0,20):
    if Evaluation_type == 'CLIME':
        CLIME_settings.init('CLIME')
        (X_test_sample,explainer,sensitivity_df,feature_list,numeric_features, model)\
         =CLIME_Process_Dataset.Preproccess_Dataset(neighbour_seed,'main_program')
        results_df=CLIME_regression.Run_Regressions(X_test_sample,explainer,feature_list)
        CLIME_perturbations.Calculate_Perturbations(explainer, results_df,sensitivity_df,feature_list,numeric_features, model)
    elif Evaluation_type == 'LIME_evaluate':
        CLIME_settings.init('LIME_evaluate') 
        CLEAR_cont.LIME_CLEAR(neighbour_seed)
    else:
        print('Evaluation type misspecified')
        sys.exit()
        
end_time = time.time()
print("Total execution time: {}".format(end_time - start_time))
    