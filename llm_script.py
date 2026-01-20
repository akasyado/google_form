from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field
from typing import Literal, TypedDict, Annotated, List
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
import operator

load_dotenv()

class Demographic(BaseModel):
    name : str = Field(description = "Name of the individual")
    profession : Literal["Student", "Working Professional"] = Field(description= "Profession of the individual")
    age : Literal["Under 18", "18–24", "25–34", "35–44", "45 and above"] = Field(description = "What is your age?")
    frequency_of_travel : Literal["Daily", "Several times a week", "Once a week", "Less than once a week", "Rarely/Never"] = Field(description = "How often do you use the public transport")
    mode_of_transport : Literal["Train", "Metro", "Bus"] = Field(description = "Which modes of transport do you use?")


class Train_(BaseModel):
    Train_1 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Train coaches and platforms are clean.")
    Train_2 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "There is enough space in the train, even during busy hours.")
    Train_3 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Fans and ventilation inside the train work well.")
    Train_4 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Railway staff are polite and helpful.")
    Train_5 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Staff give correct information about train timings and platforms.")
    Train_6 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Trains usually run on time.")
    Train_7 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The frequency of train, especially during peak hours, is satisfactory.")
    Train_8 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The train journey is fast compared to other modes.")
    Train_9 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The ticket purchasing process (online, physical ticket) is easy and efficient.")
    Train_10 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The fares are reasonable and offer good value for money.")
    Train_11: Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The train network covers the places I need to travel to.")
    Train_12 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The information provided at stops/stations (maps, timetables) is clear and up-to-date.")
    Train_13 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "I feel safe while travelling in trains and at stations.")
    Train_14 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Stations and trains have features that help elderly and disabled passengers.")
    Train_15 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Crowd control at big stations is managed well.")
    Train_16 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Ladies’ coaches are easily available and safe.")
    Train_17 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Platform connectivity (FOBs, escalators, lifts) is sufficient.")
    Train_18 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Digital indicators show correct arrival and departure information.")
    Train_19 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Station facilities (toilets, seating, drinking water) work properly.")
    Train_20 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Getting on and off the train is safe and easy.")
    Train_21: int = Field(description= "How satisfied are you with your train journey?", ge = 1, le =5)
    Train_22: Literal["Bus", "Metro", "No, I don't."] = Field(description= "Do you use any other modes of transport ?")


class Metro_(BaseModel):
    Metro_1 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Metro trains and stations are clean and well maintained.")
    Metro_2 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Metros have enough space, and they are not too crowded.")
    Metro_3 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Metro AC works properly and keeps the train comfortable.")
    Metro_4 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Metro staff (station assistants, security) are polite and helpful.")
    Metro_5 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Staff give clear information about routes and tickets.")
    Metro_6 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Metros run on time.")
    Metro_7 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "There are enough metro trains, even during rush hours.")
    Metro_8 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Metro travel is fast and convenient.")
    Metro_9 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Buying tickets (QR, token, smart card) is easy.")
    Metro_10 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Metro fares are reasonable for the service provided.")
    Metro_11: Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Metro routes cover the destinations I need.")
    Metro_12 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Station signs, maps, and announcements are clear and up to date.")
    Metro_13 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "I feel safe while travelling by metro")
    Metro_14 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Metro stations and trains are easy to use for elderly and disabled passengers.")
    Metro_15 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Lifts and escalators in stations work properly.")
    Metro_16 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "It is easy to move around inside the metro station.")
    Metro_17 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Mobile network/Wi-Fi works well inside the station.")
    Metro_18 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Changing lines (interchange) is easy and properly marked.")
    Metro_19 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Station facilities (toilets, seating, drinking water) work properly.")
    Metro_20 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Audio and visual announcements inside the train are clear.")
    Metro_21: int = Field(description= "How satisfied are you with your metro journey?", ge = 1, le =5)
    Metro_22: Literal["Bus", "Train", "No, I don't."] = Field(description= "Do you use any other modes of transport ?")


class Bus_(BaseModel):
    Bus_1 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The bus is clean and well looked after.")
    Bus_2 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The bus has enough space, and it is not too crowded.")
    Bus_3 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The bus AC/fans work properly and keep the bus comfortable.")
    Bus_4 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The driver and conductor behave politely and help passengers.")
    Bus_5 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The bus staff know the routes and give correct information.")
    Bus_6 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Buses usually come on time.")
    Bus_7 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "There are enough buses, even during rush hours.")
    Bus_8 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The bus does not take too long compared to other travel options.")
    Bus_9 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Buying a bus ticket (cash or digital) is easy.")
    Bus_10 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Bus fares are reasonable.")
    Bus_11: Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Bus routes cover the places I need to travel to.")
    Bus_12 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Information at bus stops is clear and updated.")
    Bus_13 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "I feel safe while travelling by bus.")
    Bus_14 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The bus is easy to use for elderly people and people with disabilities.")
    Bus_15 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Bus stops have enough shade and seating.")
    Bus_16 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "Real-time bus arrival information (if available) is correct.")
    Bus_17 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The bus ride feels smooth and comfortable.")
    Bus_18 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "There are enough eco-friendly or electric buses.")
    Bus_19 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The bus stop is not too far from where I live or work.")
    Bus_20 : Literal["Strongly Disagree", "Disagree", "Neutral",	"Agree", "Strongly Agree"] = Field(description= "The overall bus journey is comfortable.")
    Bus_21: int = Field(description= "How satisfied are you with your bus journey?", ge = 1, le =5)
    Bus_22: Literal["Train", "Metro", "No, I don't."] = Field(description= "Do you use any other modes of transport ?")


class Suggestion(BaseModel):
    sug_1 : int = Field(description = "Affordability: It is the most cost-effective option.",ge =1, le =5)
    sug_2 : int = Field(description = "Speed: It is the fastest way to reach my destination.",ge =1, le =5)
    sug_3 : int = Field(description = "Reliability: It is punctual and arrives on time.",ge =1, le =5)
    sug_4 : int = Field(description = "Frequency: The services run often, so I don't have to wait long.",ge =1, le =5)
    sug_5 : int = Field(description = "Connectivity: The station/stop is close to my home or workplace.",ge =1, le =5)
    sug_6 : int = Field(description = "Comfort: It is less crowded or has better seating/AC.",ge =1, le =5)
    sug_7 : int = Field(description = "Safety: I feel safer using this mode compared to others.",ge =1, le =5)
    sug_8 : int = Field(description = "Traffic Avoidance: To avoid road congestion/traffic jams.",ge =1, le =5)


class FormState(TypedDict):
    initial_prompt : str
    refined_prompt : str
    page_0 :dict
    page_1 : dict
    page_2 : dict
    page_3 : dict
    page_4 : dict
    page_history : str
    page_visited : Annotated[List[str], operator.add]


llm = ChatGroq(model = "openai/gpt-oss-120b", temperature = 0)
llm_dem = llm.with_structured_output(Demographic)
llm_train = llm.with_structured_output(Train_)
llm_metro = llm.with_structured_output(Metro_)
llm_bus = llm.with_structured_output(Bus_)
llm_sugg= llm.with_structured_output(Suggestion)


def page_0(state : FormState):
    role = state["initial_prompt"]
    system_prompt = """
You are role-playing as a real human survey participant.
Do NOT explain your answers.
Do NOT mention that you are an AI.
""" 
    role = llm.invoke(f"The system prompt is {system_prompt} and human message is {role} refram the human message so as to not confuse the model for structured output").content
    message = [SystemMessage(content = system_prompt), HumanMessage(content = role)]
    result = llm_dem.invoke(message)
    page_update = "0"
    return {"page_0" : result, "refined_prompt" : role, "page_history" : page_update, "page_visited" : ["page_0"]}


def page_1(state : FormState):
    if "Train" not in state["page_visited"]:
        add_page = ["Train"]
    else :
        add_page = ["No, I don't."]
        return {"page_visited" : add_page}
    role = state["refined_prompt"]
    system_prompt = """
You are role-playing as a real human survey participant.
Do NOT explain your answers.
Do NOT mention that you are an AI.
Answer naturally and consistently based on the given profile.
\nRate your agreement.
"""
    message = [SystemMessage(content = system_prompt), HumanMessage(content = role)]
    result = llm_train.invoke(message)
    if result.Train_22 in state["page_history"]:
        result = result.model_copy(update={"Train_22": "No, I don't."})
    page_update = state["page_history"]+",1"
    return {"page_1" : result, "page_history" : page_update, "page_visited" : add_page}


def page_2(state : FormState):
    if "Metro" not in state["page_visited"]:
        add_page = ["Metro"]
    else :
        add_page = ["No, I don't."]
        return {"page_visited" : add_page}
    role = state["refined_prompt"]
    system_prompt = """
You are role-playing as a real human survey participant.
Do NOT explain your answers.
Do NOT mention that you are an AI.
Answer naturally and consistently based on the given profile.
\nRate your agreement.
"""
    message = [SystemMessage(content = system_prompt), HumanMessage(content = role)]
    result = llm_metro.invoke(message)
    if result.Metro_22 in state["page_history"]:
        result = result.model_copy(update={"Metro_22": "No, I don't."})
    page_update = state["page_history"]+",2"
    return {"page_2" : result, "page_history" : page_update, "page_visited" : add_page}


def page_3(state : FormState):
    if "Bus" not in state["page_visited"]:
        add_page = ["Bus"]
    else :
        add_page = ["No, I don't."]
        return {"page_visited" : add_page}
    role = state["refined_prompt"]
    system_prompt = """
You are role-playing as a real human survey participant.
Do NOT explain your answers.
Do NOT mention that you are an AI.
Answer naturally and consistently based on the given profile.
\nRate your agreement.
"""
    message = [SystemMessage(content = system_prompt), HumanMessage(content = role)]
    result = llm_bus.invoke(message)
    if result.Bus_22 in state["page_history"]:
        result = result.model_copy(update={"Bus_22": "No, I don't."})
    page_update = state["page_history"]+",3"
    return {"page_3" : result,  "page_history" : page_update, "page_visited" : add_page}


def page_4(state : FormState):
    role = state["refined_prompt"]
    system_prompt = f"""
You are role-playing as a real human survey participant.
Do NOT explain your answers.
Do NOT mention that you are an AI.
\nrate out of 5 the based on what influences your choice to use the {state["page_0"].mode_of_transport}""" 

    message = [SystemMessage(content = system_prompt), HumanMessage(content = state["refined_prompt"])]
    result = llm_sugg.invoke(message)
    page_update = state["page_history"]+",4"
    return {"page_4" : result, "page_history" : page_update, "page_visited" : ["page_4"]}


def conditional_route(state : FormState):
    if state["page_0"].mode_of_transport == "Train":
        return "page_1"
    elif state["page_0"].mode_of_transport == "Metro":
        return "page_2"
    else :
        return "page_3"
    
def route_1(state : FormState):
    if "No, I don't." not in state["page_visited"]: #state["page_1"].Train_22 not in state["page_visited"] and 
        if state["page_1"].Train_22=="Metro":
            return "page_2"
        else :
            return "page_3"
    else :
        return "page_4"
    
def route_2(state : FormState):
    if "No, I don't." not in state["page_visited"]: #state["page_2"].Metro_22 not in state["page_visited"] and 
        if state["page_2"].Metro_22=="Train":
            return "page_1"
        else :
            return "page_3"
    else :
        return "page_4"
    
def route_3(state : FormState):
    if "No, I don't." not in state["page_visited"]: #state["page_3"].Bus_22 not in state["page_visited"] and 
        if state["page_3"].Bus_22=="Metro":
            return "page_2"
        else :
            return "page_1"
    else :
        return "page_4"
    


graph = StateGraph(FormState)

graph.add_node("page_0", page_0)
graph.add_node("page_1", page_1)
graph.add_node("page_2", page_2)
graph.add_node("page_3", page_3)
graph.add_node("page_4", page_4)

graph.add_edge(START, "page_0")
graph.add_conditional_edges("page_0", conditional_route)
graph.add_conditional_edges("page_1", route_1)
graph.add_conditional_edges("page_2", route_2)
graph.add_conditional_edges("page_3", route_3)
graph.add_edge("page_4", END)

workflow=graph.compile()