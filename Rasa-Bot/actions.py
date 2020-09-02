# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3

class ActionHelpReply(Action):

    def name(self) -> Text:
        return "custom_help_reply"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="What happened, tell me? I will surely try to help you😊")
        return []

class ActionShowMessage(Action):

    def name(self) -> Text:
        return "show_message"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        curr_intent = tracker.latest_message['intent'].get('name')
        # curr_intent = ''
        msg = ''
        if curr_intent == 'user_having_office_issue':
            msg = 'Listen, There are many people right now who are facing this issue'
            msg += '\nRight now just focus on your future'
            msg += "\nTalk to your family, friends\nJust don't focus on this type of things\n"
            dispatcher.utter_message(text=msg)
        elif curr_intent == 'user_having_breakup':
            msg = 'Listen here, Don\'t be sad because of one person.'
            msg += '\nThere are many people i your life. They love you'
            msg += '\nThere is many more things going to happen in the future. Don\'t step back.'
            msg += '\nTalk to your parents. Go out for walk, and Important thing, Keep smiling'
            dispatcher.utter_message(text=msg)
        elif curr_intent == 'user_having_education_issue':
            msg = 'Listen to me, There are many more doors for you. Don\'t feel sad.'
            msg += '\nThere are many more students like you.'
            msg += '\nThere were many students in the past like you, that are very successful in life'
            msg += '\nTalk to your parents. Keep smiling'
            dispatcher.utter_message(text=msg)
        else:
            dispatcher.utter_message(text='Unable to load some messages')
        return []


class ActionGiveRecommandation(Action):

    def name(self) -> Text:
        return "give_recommendation"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        messages = []
        for event in (list(tracker.events))[:15]:
            if event.get("event") == "user":
                messages.append(event.get("text"))

        if "yes" in str(tracker.latest_message['text']).lower():
            city = ""
            for message in messages:
                if 'ahmedabad' in message.lower():
                    city = 'Ahmedabad'
                elif 'mumbai' in message.lower():
                    city = 'Mumbai'
                elif 'delhi' in message.lower():
                    city = 'Delhi'
                elif 'bangalore' in message.lower():
                    city = 'Bangalore'

            exe_str = f'Select doctor_name, email from doctors where city is "{city}"'
            conn = sqlite3.connect('docs.db')
            contents = conn.execute(exe_str)
            reply = "Here are Some professional recommandations from your city\n"
            for content in contents:
                reply += f"Name : {content[0]} \t Email : {content[1]}\n"

            dispatcher.utter_message(text=reply+"I hope this help you😊\n")
            return []
        else:
            dispatcher.utter_message(text="It's ok, I am here for you whenever you need me!")
            return []


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


