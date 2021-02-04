'''
@author: Memoona Tahira, MS Student in Computer Science
@institutions: National Universtiy of Sciences and technology

@e-mail: mtahira.mscs17seecs@seecs.edu.pk

@date: August, 2019
'''


import numpy as np
import os
import math


import _list_information_functions as list
import _get_data_functions as get
import _visualize_data_functions as show
import _visual_attention_metrics as metrics
import _compute_statistics as stats



# create output file to store evaluation results:

OUTSEP = '\t'
outputdir= os.path.dirname(os.path.abspath(__file__)) + '/output_txt/'
txtf = open(os.path.join(outputdir + "evaluation_metrics.txt"), 'w')

# get a list of all models
MODELS= list.models()

value_AUCJudd=[]
value_NSS=[]
value_KL=[]
value_CC=[]
value_sim=[]


for model_name in MODELS:

    CATEGORY= list.category()
    for cat in CATEGORY:


        # getting names of all files in the ground truth and results folder for each category

        FIXATION_NAMES= list.fixation_names(cat)

        ORIG_SALIENCY_NAMES = list.orig_saliency_names(cat)

        SALIENCY_NAMES = list.saliency_names(model_name, cat)




        for i in range (len(SALIENCY_NAMES)):

            try:

                # append all map image paths

                fix= FIXATION_NAMES[i]

                orig_sal = ORIG_SALIENCY_NAMES[i]

                sal= SALIENCY_NAMES[i]

                # read all maps as images from the paths collected above

                fix_map=get.fixation_map(cat, fix )

                orig_sal_map= get.orig_saliency_map(cat, orig_sal)

                sal_map = get.saliency_map(model_name, cat, sal)


                # calculate saliency metrics for each image

                value_AUCJudd.append(metrics.AUC_Judd(sal_map, fix_map))
                value_NSS.append(metrics.NSS(sal_map, fix_map))
                value_KL.append(metrics.KLdiv(sal_map, orig_sal_map))
                value_CC.append(metrics.CC(sal_map, orig_sal_map))
                value_sim.append(metrics.sim(sal_map, orig_sal_map))

            except Exception as e:
                print(e)
                continue


        # take average of values of all metrics

        final_value_AUCJudd= np.mean(value_AUCJudd)
        final_value_NSS= np.mean(value_NSS)
        final_value_KL= np.mean(value_KL)
        final_value_CC = np.mean(value_CC)
        final_value_sim = np.mean(value_sim)



        # write a report to a new text file

        txtf.write(OUTSEP.join(['These reuslts are for ', model_name, " with "+ cat]) + '\n')
        txtf.write(OUTSEP.join(['AUC_JUDD', 'NSS', 'KLdiv', 'CC', 'sim']) + '\n')
        txtf.write(OUTSEP.join(map(str, [final_value_AUCJudd, final_value_NSS, final_value_KL, final_value_CC, final_value_sim])))


        txtf.write(OUTSEP.join(['\n']))



txtf.close()