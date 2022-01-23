#!/bin/bash

#echo '#### Create Virtual Environment ####'
#VIRTUAL_ENV_NAME='auto-test'
#virtualenv $VIRTUAL_ENV_NAME


#echo '#### Activate Virtual Environment ####'
#source $VIRTUAL_ENV_NAME/bin/activate


echo '#### Install requirements ####'
pip3 install -r ./gui_automation/requirements.txt


echo '#### Run tests ####'
python3 ./gui_automation/predict_price_scenario.py  

 
#echo ### deactivate virtual environment ###
#deactivate
