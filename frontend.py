import streamlit as st
from llm_script import workflow
from fill_form import payload, post


st.title("Provide enough info to extract atleast name, age and profession")
st.write("")
st.write("")
st.write("")
age_name = st.text_input("Give info related to age, name, area of residence like and Vasai and area of work like andheri",
                         placeholder= "Your name is tushar your age is 34 your home is in vasai and you work in andheri")
st.write("")
st.write("")
profession = st.text_input("Give info related to profession",
                           placeholder="you are student")
st.write("")
st.write("")
route = st.text_input("Type info related to travel like how they go from home to work etc",
                      placeholder="You take train to travel from home to work daily")
st.write("")
st.write("")
polictical  = st.text_input("Type info related to political leaning for varaition",
                            placeholder = "you support Rahul Gandhi")
st.write("")
st.write("")
mood = st.text_input("Type info related to pesonality",
                     placeholder="You are generally in happy mood")

enter = st.button("Press after you are done")

if enter :

    prompt = "\n".join([age_name, profession, route, polictical, mood])
    
    if age_name and profession:

        initial_state ={
            "initial_prompt": prompt
        }

        result = workflow.invoke(initial_state)

        
        st.write(str(result))


        form_data = payload(result)

        post(form_data)

        st.success("Success chech google form")

        

    else :

        st.error("Not enough info")
