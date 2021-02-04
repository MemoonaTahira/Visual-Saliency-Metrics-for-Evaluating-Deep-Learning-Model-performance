# Visual Saliency Metrics for Evaluating Deep-Learning Model Performance
This code allows you to calculate 5 of the most popular saliency metrics to determine how well a model predicted visual saliency by comparing it to a ground truth in python. 

This code is based on [FixTons](https://github.com/dariozanca/FixaTons) and [Salgan](https://github.com/imatge-upc/salgan). Please cite them if you use this code.


# FixaTons
A collection of Human FixationsDatasets and Metrics (AUC-Judd, KLdiv, NSS) for Scanpath Similarity

Here I used my own dataset [CrowdFix](https://github.com/MemoonaTahira/CrowdFix) and evaluated it over different saliency prediction Models. You can see the results [here](https://ieeexplore.ieee.org/document/8918032). 
 
# Edit:

Added two new saliency metrics (CC and Sim) and added a main file demonstarting how to use the saliency metrics.

The ground truths are for the CrowdFix dataset which has three classees representing three categories of crowds: Sparse, Dense Free-Flowing and Dense Congested. If you have a dataset with different classes, you can use a similiar file structure to hold each class and its corresponding ground truth.

The code stores the results of the saliency metrics in a .txt file. A sample is added to the repository. 

## Structure of FixaTons - sample folder added for better understanding
________________________________________________________________________________

- For the input, you need to place the following folders:

    - DATASET_NAME
        
        -GroundTruths:  contains a folder for each cateogry with the same structure below. You can skip folders you won't need, e.g. scanpaths if you are only working with saliency. 
  
        

         - STIMULI : contains original images.
                  They can have different file format (jpg, jpeg, png,...). Needed for scanpaths. Can skip for saliency metric calculations
                  
         - FIXATION_MAPS : contains a fixation map of each original image
            they are matrices of zeros (NON-fixated pixels) and 255's (fixated
            pixels). They can have different file format (jpg, jpeg, png,...)
            Needed for AUC-Judd, KLdiv, NSS and Sim calculation

         - GND_SALIENCY_MAPS : A gnd_saliency map is only a fixation_map blurred with a gaussian of a sigma of 1 degree visual angle. 
            They can have different file format (jpg, jpeg, png,...). Needed for CC calculations. 
            
            Alternatively,
            code can be added here to generate the gnd_saliency_map from the fixation_map within the code. However,
            if this evaluation code is run many time, it is better to generate the gnd_saliency maps once and place them in the folder here.
            Also useful if the dataset you are working with already provides the gnd_saliency maps.
            
            
            Please note that fixation and ground saliency maps are both generated from human observation data, e.g. an eyetracking experiment.

       
     - Results: Results from any model that predicts the saliency. These are the results you want to evaluate to determine how good your model is.
     
         
          - Model_name
            
              -SALIENCY MAPS: for each category
            
            
- Output
    - A .txt containing values of each saliency metrics. The output file is overwritten each time you run the code again. 
          

_______________________________________________________________________________

More saliency metrics can be added by adding their code in the visual_attention.py file. [Pysaliency] (https://github.com/matthias-k/pysaliency) is a python package that has code for many diffferent metrics. Unfortunately the package works with a limited number of datasets and Models. 

You can also check out the latest commit of [FixaTons](https://github.com/dariozanca/FixaTons) for AUC_Shuffled and Infogain Metrics. 

## Citations
If you intend to use this collection of datasets on your research, please cite the technical report

- FixaTons technical report: https://arxiv.org/abs/1802.02534


 
