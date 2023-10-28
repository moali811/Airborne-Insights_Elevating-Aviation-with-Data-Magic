# Import necessary libraries
import pandas as pd
import plotly.express as px
import random
import folium
from folium.plugins import MarkerCluster, HeatMap, MeasureControl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Load the data into a pandas DataFrame
url = "https://raw.githubusercontent.com/moali811/DS_Global-Flight-Report-Sample/main/flight_report2.csv"
df = pd.read_csv(url)

# Data Exploration and Basic Information
print("Basic Data Summary:")
print(df.info())

# To create an "On-Time Percentage" column with imaginary rates and add it to our dataset
# Generate imaginary on-time percentages between 70% and 100%
df['on_time_percentage'] = [random.uniform(70, 100) for _ in range(len(df))]
# Print the first few rows of the updated dataset with the new column
print("Updated Dataset with On-Time Percentage Column:")
print(df.head())

## Temporal Analysis (Assuming date columns are converted to datetime objects)

# Convert date columns to datetime objects
df['date'] = pd.to_datetime(df['date'])
df['departure_scheduled_time'] = pd.to_datetime(df['departure_scheduled_time'])
df['arrival_scheduled_time'] = pd.to_datetime(df['arrival_scheduled_time'])

# Create the 'flight_duration' column by subtracting departure time from arrival time
df['flight_duration'] = (df['arrival_scheduled_time'] - df['departure_scheduled_time']).astype('timedelta64[m]')

# Airline, Airport, and Aircraft Analysis
airline_counts = df['airline_name'].value_counts()
departure_airport_counts = df['departure_airport_icao'].value_counts()
arrival_airport_counts = df['arrival_airport_icao'].value_counts()
aircraft_counts = df['ac_type_icao'].value_counts()

# Flight Duration Analysis
df['flight_duration'] = (df['arrival_scheduled_time'] - df['departure_scheduled_time']).astype('timedelta64[m]')

# Visualization of Data

# Group data by airline and aircraft role and count the number of flights
airline_aircraft_counts = df.groupby(['airline_name', 'aircraft_role']).size().reset_index(name='flight_count')

# 1. Number of Flights by Airline and Aircraft Role (Horizontal Stacked Bar Chart)
fig = px.bar(airline_aircraft_counts, y='airline_name', x='flight_count', color='aircraft_role',
             orientation='h', labels={'flight_count': 'Number of Flights', 'airline_name': 'Airline', 'aircraft_role': 'Aircraft Role'},
             title='Number of Flights by Airline and Aircraft Role', 
             category_orders={'aircraft_role': ['S', 'D', 'T']},
             color_discrete_map={'S': 'blue', 'D': 'orange', 'T': 'green'})
fig.update_layout(paper_bgcolor='white', plot_bgcolor='white')
fig.update_traces(texttemplate='%{x}', textposition='inside')
fig.show()

# 2. Top 10 Departure Airports by Number of Flights (Horizontal Bar Chart with Gradient Color)
fig = px.bar(y=departure_airport_counts.head(10).index[::-1],  # Reversed order here
             x=departure_airport_counts.head(10).values[::-1],  # Reversed order here
             labels={'y':'Departure Airport', 'x':'Number of Flights'},
             color=departure_airport_counts.head(10).values[::-1],  # Reversed order here
             color_continuous_scale='Viridis', orientation='h')
fig.update_layout(title='Top 10 Departure Airports by Number of Flights',
                  paper_bgcolor='white', plot_bgcolor='white')
fig.show()

# 3. Top 10 Arrival Airports by Number of Flights (Horizontal Bar Chart with Gradient Color)
fig = px.bar(y=arrival_airport_counts.head(10).index[::-1],
             x=arrival_airport_counts.head(10).values[::-1],
             labels={'y':'Arrival Airport', 'x':'Number of Flights'},
             color=arrival_airport_counts.head(10).values[::-1],
             color_continuous_scale='Viridis', orientation='h')
fig.update_layout(title='Top 10 Arrival Airports by Number of Flights',
                  paper_bgcolor='white', plot_bgcolor='white')
fig.show()

# 4. Number of Flights by Aircraft Type
fig = px.bar(x=aircraft_counts.index, y=aircraft_counts.values, labels={'x':'Aircraft Type', 'y':'Number of Flights'},
             color=aircraft_counts.values,
             color_continuous_scale='Viridis')
fig.update_xaxes(tickangle=45)
fig.update_layout(title='Number of Flights by Aircraft Type',
                  paper_bgcolor='white', plot_bgcolor='white')
fig.show()

# 5. Distribution of Flight Durations
fig = px.histogram(df, x='flight_duration', nbins=30, labels={'x':'Flight Duration (minutes)', 'y':'Frequency'},
                   color_discrete_sequence=['purple'])
fig.update_layout(title='Distribution of Flight Durations',
                  paper_bgcolor='white', plot_bgcolor='white')
fig.show()

# 6. Flight Duration Distribution by Airline (Violin Plot)
fig = px.violin(df, x='airline_name', y='flight_duration', labels={'x':'Airline', 'y':'Flight Duration (minutes)'},
                box=True, points="all")
fig.update_xaxes(tickangle=45)
fig.update_layout(title='Flight Duration Distribution by Airline',
                  paper_bgcolor='white', plot_bgcolor='white')
fig.show()

# 7. Flight Duration by Aircraft Role (Swarm Plot with Stripplot)
fig = px.strip(df, x='aircraft_role', y='flight_duration', labels={'x':'Aircraft Role', 'y':'Flight Duration (minutes)'},
               category_orders={'aircraft_role': ['S', 'D', 'T']},
               color_discrete_sequence=['green'])
fig.update_xaxes(tickangle=45)
fig.update_layout(title='Flight Duration by Aircraft Role',
                  paper_bgcolor='white', plot_bgcolor='white')
fig.show()

# Extract year, month, and day of the week for analysis
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['day_of_week'] = df['date'].dt.dayofweek
# Calculate average flight duration for each airline and year
average_durations = df.groupby(['year', 'airline_name'])['flight_duration'].mean().reset_index()

# 8. Animated Bar Chart for Number of Flights over the Years for Each Airline
animated_fig = px.bar(average_durations, x='year', y='flight_duration', color='airline_name',
                     labels={'x': 'Year', 'y': 'Average Flight Duration'},
                     title='Change in Average Flight Duration Over the Years',
                     animation_frame='year', range_y=[0, df['flight_duration'].max()])
animated_fig.show()

# 9. Yearly Trend of On-Time Performance by Airline (assuming 'on_time_percentage' column exists)
'''
This visualization allows for a quick comparison of different airlines' punctuality trends over time,
providing valuable insights into their operational efficiency.
'''
fig = px.line(df, x='year', y='on_time_percentage', color='airline_name',
              labels={'x': 'Year', 'y': 'On-Time Performance (%)', 'color': 'Airline'})
fig.update_layout(title='Yearly Trend of On-Time Performance by Airline',
                  paper_bgcolor='white', plot_bgcolor='white')
fig.show()

# 10. Monthly Distribution with Box Plot
fig = px.box(df, x='month', y='flight_duration', labels={'x': 'Month', 'y': 'Flight Duration (minutes)'},
             color_discrete_sequence=['brown'])
fig.update_layout(title='Monthly Distribution of Flight Durations',
                  paper_bgcolor='white', plot_bgcolor='white')
fig.show()

# 11. Weekday vs. Weekend Analysis
df['is_weekend'] = df['day_of_week'].isin([5, 6])  # 5 and 6 represent Saturday and Sunday (weekends)
fig = px.box(df, x='is_weekend', y='flight_duration', labels={'x': 'Weekend', 'y': 'Flight Duration (minutes)'},
             color='is_weekend',
             color_discrete_map={False: 'lightblue', True: 'orange'})
fig.update_layout(title='Flight Durations: Weekdays vs. Weekends',
                  paper_bgcolor='white', plot_bgcolor='white')
fig.update_xaxes(tickvals=[0, 1], ticktext=['Weekdays', 'Weekends'])
fig.show()

# 12. Interactive Heatmap for Flight Counts
heatmap_data = df.groupby(['month', 'day_of_week']).size().reset_index(name='flight_count')
fig = px.imshow(heatmap_data.pivot(index='month', columns='day_of_week', values='flight_count'),
                x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                y=heatmap_data['month'].unique(),
                labels={'x': 'Day of Week', 'y': 'Month', 'color': 'Number of Flights'},
                color_continuous_scale='Viridis')
fig.update_layout(title='Flight Counts by Month and Day of the Week')
fig.show()

# 13. Heatmap for Busiest Time of the Day
heatmap_data = df.groupby(['departure_scheduled_time', 'day_of_week']).size().reset_index(name='flight_count')
fig = px.imshow(heatmap_data.pivot(index='departure_scheduled_time', columns='day_of_week', values='flight_count'),
                x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                y=heatmap_data['departure_scheduled_time'].unique(),
                labels={'x': 'Day of Week', 'y': 'Time of Day', 'color': 'Number of Flights'},
                color_continuous_scale='Viridis')
fig.update_layout(title='Busiest Time of the Day for Flights',
                  paper_bgcolor='white', plot_bgcolor='white')
fig.show()

# 14. Correlation Matrix Heatmap
fig = px.imshow(df.corr(), labels={'x':'Columns', 'y':'Columns'},
                color_continuous_scale='Viridis')
fig.update_layout(title='Correlation Matrix Heatmap')
fig.show()


## Geographical Analysis using Folium

# Load the latitude and longitude dataset
# Source of data: ""
url_iata_icao = "https://raw.githubusercontent.com/moali811/DS_Global-Flight-Report-Sample/main/iata-icao.csv"
df_iata_icao = pd.read_csv(url_iata_icao)

# Merge latitude and longitude data into the original dataset based on departure airport
merged_df = pd.merge(df, df_iata_icao, left_on='departure_airport_icao', right_on='icao', how='inner')
merged_df.rename(columns={'latitude': 'departure_latitude', 'longitude': 'departure_longitude'}, inplace=True)

# Merge latitude and longitude data into the merged dataset based on arrival airport
merged_df = pd.merge(merged_df, df_iata_icao, left_on='arrival_airport_icao', right_on='icao', how='inner')
merged_df.rename(columns={'latitude': 'arrival_latitude', 'longitude': 'arrival_longitude'}, inplace=True)

# Drop rows with missing latitude or longitude values for departure or arrival airports
merged_df = merged_df.dropna(subset=['departure_latitude', 'departure_longitude', 'arrival_latitude', 'arrival_longitude'])

# Save the merged data to a CSV file
merged_df.to_csv('merged_data.csv', index=False)

# Calculate flight count for each airport
departure_flight_counts = merged_df.groupby('departure_airport_icao').size().reset_index(name='flight_count')

# Merge flight counts back to the merged_df DataFrame
merged_df = pd.merge(merged_df, departure_flight_counts, on='departure_airport_icao', how='left')

# 16. Create an interactive Flight Map

# Define the function to create the interactive flight map
def create_interactive_flight_map(merged_df):
    try:
        # Determine the busiest airport (departure or arrival) based on flight count
        busiest_airport = merged_df.groupby(['departure_airport_icao', 'arrival_airport_icao']).size().idxmax()
        busiest_airport_icao = busiest_airport[0] if busiest_airport[0] != busiest_airport[1] else busiest_airport[1]

        # Calculate the center latitude and longitude based on the average of departure and arrival coordinates
        center_lat = merged_df[['departure_latitude', 'arrival_latitude']].mean().mean()
        center_lng = merged_df[['departure_longitude', 'arrival_longitude']].mean().mean() + 20  # Adjusting to the right
        zoom_level = 3

        # Create an Interactive Flight Map
        flight_map = folium.Map(location=[center_lat, center_lng], zoom_start=zoom_level)

        # Create feature groups for departures and arrivals
        departures = folium.FeatureGroup(name='Departures')
        arrivals = folium.FeatureGroup(name='Arrivals')

        # Iterate through merged_df and add flight routes and markers to the appropriate feature group
        for _, row in merged_df.iterrows():
            # Add flight route as a blue line to departures group
            folium.PolyLine([(row['departure_latitude'], row['departure_longitude']),
                             (row['arrival_latitude'], row['arrival_longitude'])],
                            color='blue', weight=1, opacity=1).add_to(departures)

            # Determine color based on flight duration (blue to red gradient)
            color = f'#{int(255 * (row["flight_duration"] / merged_df["flight_duration"].max())):02x}0000'

            # Determine marker radius based on flight count (proportional sizes)
            radius = int(row['flight_count'] / merged_df['flight_count'].max() * 10) + 5

            # Add marker for departure airport with popup information to departures group
            folium.CircleMarker([row['departure_latitude'], row['departure_longitude']],
                                color=color, fill=True, fill_color=color, radius=radius,
                                popup=folium.Popup(f"<b>Departure Airport</b>: {row['departure_airport_icao']}<br>"
                                                   f"<b>Date</b>: {row['departure_scheduled_time']}<br>"
                                                   f"<b>Flight Count</b>: {row['flight_count']}<br>"
                                                   f"<b>On-Time Percentage</b>: {row['on_time_percentage']:.1f}%<br>"
                                                   f"<b>Flight Duration</b>: {row['flight_duration']} minutes",
                                                   max_width=300)).add_to(departures)

            # Add marker for arrival airport with popup information to arrivals group
            folium.CircleMarker([row['arrival_latitude'], row['arrival_longitude']],
                                color=color, fill=True, fill_color=color, radius=radius,
                                popup=folium.Popup(f"<b>Arrival Airport</b>: {row['arrival_airport_icao']}<br>"
                                                   f"<b>Date</b>: {row['arrival_scheduled_time']}<br>"
                                                   f"<b>Flight Count</b>: {row['flight_count']}<br>"
                                                   f"<b>On-Time Percentage</b>: {row['on_time_percentage']:.1f}%<br>"
                                                   f"<b>Flight Duration</b>: {row['flight_duration']} minutes",
                                                   max_width=300)).add_to(arrivals)

        # Add feature groups to the map
        flight_map.add_child(departures)
        flight_map.add_child(arrivals)

        # Add Layer Control to choose between Departures and Arrivals
        folium.LayerControl(collapsed=False).add_to(flight_map)

        # Save the interactive map as an HTML file
        file_path = 'interactive_flight_route_map.html'
        flight_map.save(file_path)
        print(f"Interactive map generated and saved successfully as '{file_path}'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Load your DataFrame 'merged_df' from your data source
    # merged_df = pd.read_csv('your_data.csv')
    create_interactive_flight_map(merged_df)
