'''
@author: Dario Zanca, Ph.D. Student in Smart Computing
@institutions: University of Florence, University of Siena

@e-mail: dario.zanca@unifi.it
@tel: (+39) 333 82 78 072

@date: September, 2017
'''

#########################################################################################

# IMPORT EXTERNAL LIBRARIES

import os

#########################################################################################

# to get inside the input folder:

COLLECTION_PATH= os.path.dirname(os.path.abspath(__file__)) + '/input_data'

#########################################################################################
def category():

    ''' This functions lists the names of the category specified dataset '''

    return sorted(os.listdir(COLLECTION_PATH+'/Dataset/'))

#########################################################################################


def models():

    ''' This functions lists the names of the models over which the dataset was evaluated '''


    return sorted(os.listdir(COLLECTION_PATH + '/Model_Results/'))


#########################################################################################

def stimuli(CATEGORY):

    ''' This functions lists the names of the stimuli (original images, or video frames) of a specified dataset '''

    return sorted(os.listdir(COLLECTION_PATH+'/Dataset/'+CATEGORY+'/STIMULI'))

#########################################################################################

def fixation_names(CATEGORY):

    ''' This functions lists the names of the fixation_maps of a specified dataset '''

    return sorted(os.listdir(COLLECTION_PATH+'/Dataset/'+CATEGORY+'/FIXATION_MAPS'))


#########################################################################################

def orig_saliency_names(CATEGORY):

    ''' This functions lists the names of the ground truth saliency_maps of a specified dataset '''

    return sorted(os.listdir(COLLECTION_PATH+'/Dataset/'+CATEGORY+'/GND_SALIENCY_MAPS'))

#########################################################################################


def saliency_names(MODEL_NAME, CATEGORY):

    ''' This functions lists the names of the saliency_maps produced by a specified model '''

    return sorted(os.listdir(COLLECTION_PATH + '/Model_Results/' + MODEL_NAME + '/' + CATEGORY + '/SALIENCY_MAPS'))

#########################################################################################


def subjects(DATASET_NAME, CATEGORY, STIMULUS_NAME):

    ''' This functions lists the names of the subjects which have been watching a
        specified stimuli of a dataset '''

    file_name, _ = os.path.splitext(STIMULUS_NAME)

    return sorted(os.listdir(COLLECTION_PATH+'/'+DATASET_NAME+'/'+CATEGORY+'/SCANPATHS/'+file_name))