
# Data Science Project Report: Global Flight Analysis and Visualization
<br><br>

## 1. Introduction:
This data science project aims to analyze and visualize global flight data to provide valuable insights for the aviation industry. The analysis encompasses various aspects such as flight counts, on-time performance, airport distribution, and geographical visualization of flight routes. The project utilizes Python and several libraries, including Pandas, Plotly, and Folium, to perform data processing, exploratory analysis, and interactive visualization.
<br><br>

## 2. Data Source:
The flight data used in this analysis was mainly sourced from Spire Aviation. The dataset includes information about flight schedules, airlines, airports, aircraft types, departure/arrival times. However, the IATA/ICAO List data is available from https://github.com/ip2location/ip2location-iata-icao by http://www.ip2location.com (a publicly available dataset on GitHub).
<br><br>

## 3. Data Exploration and Preprocessing:
- Loaded the dataset into a Pandas DataFrame.
- Created an imaginary "On-Time Percentage" column for analysis purposes.
- Converted date columns to datetime objects.
- Calculated flight duration based on departure and arrival times.
<br><br>

## 4. Exploratory Data Analysis (EDA) and Insights:

### Temporal Analysis:
- Explored flight counts and duration trends over the years, providing insights into the industry's growth and operational efficiency.

### Airline, Airport, and Aircraft Analysis:
- **Number of Flights by Airline and Aircraft Role:** Visualized the distribution of flight counts based on airline and aircraft roles, highlighting operational patterns.

  ![newplot-6](https://github.com/moali811/DS_Global-Flight-Report-Sample/assets/59733199/b9d650d1-4b49-4e8f-86b1-b952c80440b8)

- **Top Departure and Arrival Airports:** Identified the busiest departure and arrival airports, aiding in route optimization and resource allocation.

  ![newplot-7](https://github.com/moali811/DS_Global-Flight-Report-Sample/assets/59733199/a0c44acc-c572-4dda-9a8c-4bce4ded6dbb)

  ![newplot-8](https://github.com/moali811/DS_Global-Flight-Report-Sample/assets/59733199/878877cb-5074-447a-a7fd-ef845f0e20cb)

- **Flight Counts by Aircraft Type:** Analyzed the prevalence of different aircraft types in global flights.

  ![newplot-9](https://github.com/moali811/DS_Global-Flight-Report-Sample/assets/59733199/13168990-86ab-4877-851b-43aa96cc3a41)

- **Flight Durations Analysis:** Investigated the distribution of flight durations and their correlation with airline performance and aircraft roles.

  ![newplot-11](https://github.com/moali811/DS_Global-Flight-Report-Sample/assets/59733199/4cc053cc-9d99-4790-9b21-cf06488e56ad)

  ![newplot-12](https://github.com/moali811/DS_Global-Flight-Report-Sample/assets/59733199/b29e94b5-feb1-4802-b2c9-fa47441a1955)

  ![newplot-13](https://github.com/moali811/DS_Global-Flight-Report-Sample/assets/59733199/3bf591f8-a71e-4f16-9bdc-e18ec98b8bbe)

  ![newplot-16](https://github.com/moali811/DS_Global-Flight-Report-Sample/assets/59733199/028cd875-7555-4d6c-928c-755ee2a4eef6)

- **Weekday vs. Weekend Analysis:** Compared flight durations on weekdays and weekends, understanding potential differences in operational efficiency.

  ![newplot-17](https://github.com/moali811/DS_Global-Flight-Report-Sample/assets/59733199/e12f8d36-f62a-4f43-8992-6a83a399a80e)
<br><br>

### On-Time Performance Analysis:
- **Yearly Trend of On-Time Performance:** Examined the yearly trend of on-time percentages for airlines, offering insights into their punctuality and service quality.
<br><br>

### Heatmap for Busiest Time of the Day:
- The heatmap visualizes the busiest times of the day for flights based on departure schedules. It provides insights into the variation of flight counts throughout different hours and days of the week.

  ![newplot-19](https://github.com/moali811/DS_Global-Flight-Report-Sample/assets/59733199/e46b6682-e0e5-4cb9-8e26-327eb00f2ca5)
<br><br>

### Correlation Matrix Heatmap:
- The correlation matrix heatmap illustrates the relationships between different numerical columns in the dataset. It helps identify potential correlations, both positive and negative, between flight-related variables.

  ![newplot-20](https://github.com/moali811/DS_Global-Flight-Report-Sample/assets/59733199/bd9543e5-90a5-4085-af33-eba0f0c635bc)
<br><br>

### Geographical Analysis:
- **Airport Analysis:** Visualized the geographical distribution of airports based on flight counts, on-time percentages, and flight durations, providing insights into regional aviation patterns.
- **Interactive Flight Map:** Developed an interactive map displaying flight routes, on-time percentages, and other flight details, enhancing the understanding of global flight networks.

  <img width="1920" alt="Flight_Map" src="https://github.com/moali811/DS_Global-Flight-Report-Sample/assets/59733199/ba057f18-2b4c-41b2-8f98-0e9909e1d7c7">
<br><br>

## 5. Conclusion and Future Recommendations:
- **Conclusion:** This project successfully analyzed and visualized global flight data, offering valuable insights for the aviation industry. Key findings include trends in on-time performance, busiest airports, and aircraft role distribution.

- **Future Recommendations:**
  - **Real-time Data Integration:** Integrate real-time data sources for up-to-date analysis.
  - **Predictive Analytics:** Implement predictive models for flight delays and optimize routes based on historical and real-time data.
  - **User-Friendly Interface:** Develop a user-friendly dashboard for stakeholders to interact with the data dynamically.
<br><br>

## 6. Project Impact and Value:
This project's comprehensive analysis and interactive visualizations provide significant value to stakeholders in the aviation industry. Employers and industry professionals can gain insights into operational efficiency, enabling data-driven decision-making for airlines, airports, and regulatory authorities.
<br><br>

## 7. Acknowledgments:
We acknowledge the open-source contributors for providing the dataset used in this analysis, enabling valuable insights into the aviation sector.
<br><br>
<br><br>

*Note:* The code presented in this report is a part of the data science project, showcasing the technical skills and proficiency of the author in data analysis and visualization.
