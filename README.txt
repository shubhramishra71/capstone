#README
Title: This project contains the IBM Data Science Professional Certification Capstone Project code
Author: Shubhra Mishra
Date: 26-JUN-2023

Overview of Project:
The commercial space age is here, companies are making space travel affordable for everyone. Virgin Galactic is providing suborbital spaceflights. 
Rocket Lab is a small satellite provider. Blue Origin manufactures sub-orbital and orbital reusable rockets. 
Perhaps the most successful is SpaceX. SpaceX’s accomplishments include: Sending spacecraft to the International Space Station. 
Starlink, a satellite internet constellation providing satellite Internet access. Sending manned missions to Space. 
One reason SpaceX can do this is the rocket launches are relatively inexpensive. SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; 
other providers cost upwards of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. 
Therefore, if we can determine if the first stage will land, we can determine the cost of a launch. Spaces X’s Falcon 9 launch like regular rockets. 

Project Description:
The project contains all the code required for Data Collection, Data Analysis and Visualisation, and Model predictions.
This is split into components listed below and each jupyterlite file is the code representing these.
1. data collection using Request to the SpaceX APIs, and then cleaning of this data
2. web scraping to collect Falcon 9 historical launch records from a Wikipedia page titled List of Falcon 9 and Falcon Heavy launches
3. Exploratory Data Analysis (EDA) to find some patterns in the data and determine what would be the label for training supervised models
4. Load the dataset into the corresponding table in a Db2 database and Execute SQL queries to answer assignment questions
5. Exploratory Data Analysis and Feature Engineering using Pandas and Matplotlib with Visualisations
6. Launch Sites Locations Analysis with Folium
7. Create a dashboard application with findings of Data Analysis
8. Space X Falcon 9 First Stage Landing Prediction using ML Algorithms