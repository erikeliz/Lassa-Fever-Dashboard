#Erik Elizarraras
#Dr. Akwafuo Sampson URE 2024
#Project Raise 

import streamlit as st
import pandas as pd

#Lassa Fever CSV file converted to Pandas Dataframe  
dataFrame = pd.read_csv("LassaSpatialdataset201219separateyearsLabconfirmed - LassaConfirmed.csv")

#Containers for top row 
row1 = st.columns([1,1,1,1,1], vertical_alignment="bottom")

# Container for page title 
row2 = st.columns([1], vertical_alignment= "center")

#Title for bar chart, bar chart
st.subheader("Increase in Lassa fever Cases")
st.bar_chart(dataFrame, x = "Year", y = "Cases", x_label="Year", y_label="Cases")

#Title for information about Lassa Fever and container for text 
st.subheader(f"About Lassa Fever")
row3 = st.columns([1], vertical_alignment= 'center')

#Title for information about Lassa Fever and container for text 
st.subheader("Signs and Symptoms")
row4 = st.columns([1], vertical_alignment= 'center')

#Title for information about Lassa Fever and container for text 
st.subheader("Treatment")
row5 = st.columns([1], vertical_alignment= 'center')

# Formatting for containers 
tile1 = row1[0].container(height = 165, border= False)
tile2 = row1[1].container(height = 100, border= False)
tile3 = row1[2].container(height = 100, border= False)
tile4 = row1[3].container(height = 100, border= False)
tile5 = row1[4].container(height = 165, border= False)
tile6 = row2[0].container(height = 100, border=False)
tile7 = row3[0].container(height = 100, border=False)
tile8 = row4[0].container(height = 325, border=False)
tile9 = row5[0].container(height = 200, border=False)\

#Top left CSUF Logo
tile1.image("CSUF_logo.png")

#Dashobard link button 
tile2.link_button("Dashboard", "https://public.tableau.com/shared/7Z8WMQ92W?:display_count=n&:origin=viz_share_link")

#Form link button 
tile3.link_button("Go to Form","https://forms.gle/meW35UtVFEsWJdWg9" )

#Predictions link button placeholder 
tile4.button("Predictions")

#Top right CEDDI logo 
tile5.image("CEDDI_CircularLogo.png")

#Text - Page Title Section
tile6.title("Lassa Fever Dashboard and Form")

#Text - About Lassa Fever Section 
tile7.markdown ("Lassa fever is an animal-borne, or zoonotic, acute viral illness spread by the common African rat. It is endemic in parts of West Africa including Sierra Leone, Liberia, Guinea and Nigeria. Neighboring countries are also at risk because the animal vector lives throughout the region.")

#Text - Signs and Symptoms Section
tile8.markdown(
"Signs and symptoms of Lassa fever typically occur 1-3 weeks after the patient comes into contact with the virus. For the majority of Lassa fever virus infections (approximately 80%), symptoms are mild and are undiagnosed. Mild symptoms include slight fever, general malaise and weakness, and headache. Approximately 15%-20% of patients hospitalized for Lassa fever die from the illness. However, only 1% of all Lassa virus infections result in death. The death rates for women in the third trimester of pregnancy are particularly high. Spontaneous abortion is a serious complication of infection with an estimated 95% mortality in fetuses of infected pregnant mothers. Because the symptoms of Lassa fever are so varied and nonspecific, clinical diagnosis is often difficult. Lassa fever is also associated with occasional epidemics, during which the case-fatality rate can reach 50% in hospitalized patients.\n"
"In 20% of infected individuals, however, disease may progress to more serious symptoms including hemorrhaging (in gums, eyes, or nose, as examples), respiratory distress, repeated vomiting, facial swelling, pain in the chest, back, and abdomen, and shock."
)

#Text - Treatment Section 
tile9.markdown(
"Ribavirin, an antiviral drug, has been used with success in Lassa fever patients. It has been shown to be most effective when given early in the course of the illness. Patients should also receive supportive care consisting of maintenance of appropriate fluid and electrolyte balance, oxygenation and blood pressure, as well as treatment of any other complicating infections."
)

#Text - Treatment Section - Source 
tile9.markdown("Source: Center for Disease Control and Prevention")

#Scatterplot map 
st.map(dataFrame, latitude ="y", longitude="x", size=25 )

