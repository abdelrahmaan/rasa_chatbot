# rasa_chatbot
**Making a chatbot with RASA for knowing the capital of a country and the population of it.**

----
## What you can make for run this code?

### 1- Make a python environment:
- By runing this `pip install virtualenv` you can install `virtualenv` for making an environment.

### 2- Setup your environment

- Make a folder `mkdir rasa_app`
- Move to it `cd rasa_app`
- Make an env `virtualenv rasa_env`
- Run it  `source rasa_env/bin/activate`

### 2- Install RASA

- For upgrade rasa `pip3 install --upgrade rasa`
- For create new assistant   `rasa init`
- For train new model for your current assistant  `rasa train`
- For help `rasa -h`
- For to talk with the most recent model of your current assistant `rasa shell`
- if i want to see how things going for getting the proba of every intent appear by the bot `rasa shell nlu`

<!-- - We can make a python file for run custom code as `[actions.py](http://actions.py)` by `rasa run actions` -->
