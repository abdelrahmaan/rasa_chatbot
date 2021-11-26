# rasa_chatbot
**Making a chatbot with RASA for knowing the capital of a country and the population of it.**

----
## What you can make for run this code?

### 1- make a python environment:
- By runing this `pip install virtualenv` you can install `virtualenv` for making an environment.

### 2- setup your environment

- make a folder `mkdir rasa_app`
- move to it `cd rasa_app`
- make an env `virtualenv rasa_env`
- run it  `source rasa_env/bin/activate`

### 2- Install RASA

- `pip3 install rasa`
- initialized it `rasa init`
- For running it to rest the code by terminal `rasa shell`
- if i want to see how things going for getting the proba of every intent appear by the bot `rasa shell nlu`
- if i add anything in any file, using this command for retrain the data `rasa train`
- we can make a python file for run custom code as `[actions.py](http://actions.py)` by `rasa run actions`
