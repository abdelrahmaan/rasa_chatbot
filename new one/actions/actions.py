# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"


import arrow
from typing import Text, Any, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

# db = {
#     "USA"       : ["Washington", "331,002,651"],
#     "Greece"    : ["Athens", "10,423,054"],
#     "Sweden"    : ["Stockholm", "10,099,265"], 
#     "Australia" : ["Canberra", "25,499,884"], 
#     "Finland"   : ["Helsinki", "5,540,720"], 
#     "Japan"     : ["Tokyo", "126,476,461"], 
#     "Russia"    : ["Moscow", "145,934,462"], 
#     "India"     : ["New Delhi", "1,380,004,385"], 
#     "Egypt"     : ["Cairo", "102,334,404"], 
    
# }
db_country = {
    "USA"       : "Washington",
    "Greece"    : "Athens",
    "Sweden"    : "Stockholm", 
    "Australia" : "Canberra", 
    "Finland"   : "Helsinki",
    "Japan"     : "Tokyo",  
    "Russia"    : "Moscow",  
    "India"     : "New Delhi", 
    "Egypt"     : "Cairo",  
    }
    
db_population = {
    "USA"       : "331,002,651",
    "Greece"    : "10,423,054",
    "Sweden"    : "10,099,265", 
    "Australia" : "25,499,884", 
    "Finland"   : "5,540,720", 
    "Japan"     : "126,476,461", 
    "Russia"    : "145,934,462", 
    "India"     : "1,380,004,385",
    "Egypt"     : "102,334,404", 
    }


        # - action_population_place
        # - action_country_place

    # curr_capital = db.get(current_place, None)[0]
    # curr_populatoin = db.get(current_place, None)[1]
    # mes = f"The capital of {current_place} is {curr_capital}, and the population of it is {curr_populatoin}"
    
class ActionCountryPlace(Action):
    
    def name(self) -> Text:
        return "action_country_place"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_place = next(tracker.get_latest_entity_values("place"), None)
        
        curr_capital = db_country.get(current_place, None)
        
        if not curr_capital:
            mes = f"It did't found {current_place} in our database!"
            dispatcher.utter_message(text= mes)
            return []
        
        mes = f"The capital of {current_place} is {curr_capital}"
        
        dispatcher.utter_message(text=mes)

        return []




class ActionPopulationPlace(Action):
    
    def name(self) -> Text:
        return "action_population_place"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_place = next(tracker.get_latest_entity_values("place"), None)
        
        curr_capital = db_population.get(current_place, None)
        
        if not curr_capital:
            mes = f"It did't found {current_place} in our database!"
            dispatcher.utter_message(text= mes)
            return []
        
        mes = f"The population of {current_place} is {curr_capital}"
        
        dispatcher.utter_message(text=mes)

        return []






