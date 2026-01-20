import requests
import streamlit as st


def payload(result):
    list_data = []


    page = [i for i in result["page_history"][::2]]

    for i in page:
        if i == "0":
            page_0 = {
                "entry.1383535463": result["page_0"].name,
                "entry.883561213": result["page_0"].profession,
                "entry.1076267351": result["page_0"].age,
                "entry.409491525": result["page_0"].frequency_of_travel,
                "entry.1933909750": result["page_0"].mode_of_transport
                }
            list_data.append(page_0)
        elif i == "1":
            page_1 = {
                "entry.258008930": result["page_1"].Train_1,
                "entry.1854439051": result["page_1"].Train_2,
                "entry.1708881375": result["page_1"].Train_3,
                "entry.511514232": result["page_1"].Train_4,
                "entry.1177982515": result["page_1"].Train_5,
                "entry.1478983727": result["page_1"].Train_6,
                "entry.1273969632": result["page_1"].Train_7,
                "entry.1775360457": result["page_1"].Train_8,
                "entry.1772044677": result["page_1"].Train_9,
                "entry.1190733539": result["page_1"].Train_10,
                "entry.1920129645": result["page_1"].Train_11,
                "entry.2034778477": result["page_1"].Train_12,
                "entry.1180857924": result["page_1"].Train_13,
                "entry.763569579": result["page_1"].Train_14,
                "entry.1409256780": result["page_1"].Train_15,
                "entry.995817656": result["page_1"].Train_16,
                "entry.1882945011": result["page_1"].Train_17,
                "entry.266684792": result["page_1"].Train_18,
                "entry.733808597": result["page_1"].Train_19,
                "entry.1141182931": result["page_1"].Train_20,
                "entry.2145201621": result["page_1"].Train_21,
                "entry.411681523": result["page_1"].Train_22
                }
            list_data.append(page_1)
        elif i == "2":
            page_2 ={
                "entry.1635270562": result["page_2"].Metro_1,
                "entry.1639742245": result["page_2"].Metro_2,
                "entry.948642160": result["page_2"].Metro_3,
                "entry.624246007": result["page_2"].Metro_4,
                "entry.1717906847": result["page_2"].Metro_5,
                "entry.2096082113": result["page_2"].Metro_6,
                "entry.999493316": result["page_2"].Metro_7,
                "entry.1793695834": result["page_2"].Metro_8,
                "entry.806735810": result["page_2"].Metro_9,
                "entry.582175216": result["page_2"].Metro_10,
                "entry.2096037595": result["page_2"].Metro_11,
                "entry.1434081813": result["page_2"].Metro_12,
                "entry.1438208972": result["page_2"].Metro_13,
                "entry.1238624243": result["page_2"].Metro_14,
                "entry.1143836105": result["page_2"].Metro_15,
                "entry.1300604235": result["page_2"].Metro_16,
                "entry.1006427203": result["page_2"].Metro_17,
                "entry.1244214906": result["page_2"].Metro_18,
                "entry.147188454": result["page_2"].Metro_19,
                "entry.1870113565": result["page_2"].Metro_20,
                "entry.602383344": result["page_2"].Metro_21,
                "entry.751660305": result["page_2"].Metro_22
                }
            list_data.append(page_2)
        elif i == "3":
            page_3 = {
                "entry.1962406321": result["page_3"].Bus_1,
                "entry.384302933": result["page_3"].Bus_2,
                "entry.1524348528": result["page_3"].Bus_3,
                "entry.1600980005": result["page_3"].Bus_4,
                "entry.876737635": result["page_3"].Bus_5,
                "entry.1159163674": result["page_3"].Bus_6,
                "entry.2096423726": result["page_3"].Bus_7,
                "entry.1557910217": result["page_3"].Bus_8,
                "entry.676732258": result["page_3"].Bus_9,
                "entry.1267573117": result["page_3"].Bus_10,
                "entry.727464336": result["page_3"].Bus_11,
                "entry.1787603987": result["page_3"].Bus_12,
                "entry.670535115": result["page_3"].Bus_13,
                "entry.669340116": result["page_3"].Bus_14,
                "entry.716310364": result["page_3"].Bus_15,
                "entry.1347138457": result["page_3"].Bus_16,
                "entry.1009309754": result["page_3"].Bus_17,
                "entry.1578167306": result["page_3"].Bus_18,
                "entry.1593237737": result["page_3"].Bus_19,
                "entry.1174210339": result["page_3"].Bus_20,
                "entry.2084846103": result["page_3"].Bus_21,
                "entry.1063268850": result["page_3"].Bus_22
                }
            list_data.append(page_3)
        else :
            page_4 ={
                "entry.1267174312": "Nothing particular",
                "entry.1635772738":result["page_4"].sug_1,
                "entry.1738503814": result["page_4"].sug_2,
                "entry.2019461861": result["page_4"].sug_3,
                "entry.345155724": result["page_4"].sug_4,
                "entry.539423936": result["page_4"].sug_5,
                "entry.900890119": result["page_4"].sug_6,
                "entry.778375002": result["page_4"].sug_7,
                "entry.1235403417": result["page_4"].sug_8
                }
            list_data.append(page_4)

    form_data = {}
    for i in list_data:
        form_data.update(i)
    form_data.update({
        "pageHistory": result["page_history"]
        })
    
    return form_data


def post(form_data):
    FORM_ID = "1FAIpQLSd2MgeTBj7EvmbY4ozfE27zuflRgVg7NldipVGm1jx_DhXXyw"

    VIEWFORM_URL = f"https://docs.google.com/forms/d/e/{FORM_ID}/viewform"
    FORMRESPONSE_URL = f"https://docs.google.com/forms/d/e/{FORM_ID}/formResponse"

    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0",
    }


    response = session.post(
        FORMRESPONSE_URL,
        data=form_data,
        headers=headers
    )

    print("Status:", response.status_code)