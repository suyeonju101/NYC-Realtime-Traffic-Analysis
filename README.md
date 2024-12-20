# NYC Realtime Traffic Analysis

*Note: This application builds upon the sample application provided by TomTom Traffic API. You can explore the original tutorial here: [TomTom Traffic Tutorial](https://developer.tomtom.com/maps-sdk-web-js-v5/tutorials-use-cases/traffic-tutorial).*

This repository presents a comprehensive analysis of real-time traffic data in New York City, integrating both traffic flow and incident data to generate actionable insights. The project aims to:
- Provide users with interactive visualizations of current traffic conditions.
- Assist in optimizing travel routes.
- Identify and highlight congestion hotspots.
For a live view of the traffic analysis, explore the interactive map here: [NYC Real-time Traffic Map](https://suyeonju101.github.io/NYC-Realtime-Traffic-Analysis/traffic.html).

Additionally, this repository includes modules for fetching real-time traffic flow and incident data, making it a valuable tool for urban traffic analysis and prediction.


## Repository Structure

    ├── realtime_data_fetcher 
    
        ├── README.txt  # README file for how to use real-time traffic data fetcher module
    
        ├── main.py
    
        ├── TrafficFlow.py
        
        └── TrafficIncidents.py
    
    ├── LICENSE

    ├── README.md

    ├── Traffic Flows Fetch and Visualization.ipynb

    ├── Traffic Incidents Visualization.ipynb

    ├── img             # a directory contained all images used in the dashboard
    
    ├── package.json    # a file needed to build dashboard
    
    ├── styles.css      # a file needed to build dashboard
    
    ├── traffic.js      # a file needed to build dashboard
        
    └── traffic.html    # a main html file for dashboard


## Key Features
- **Real-time data extraction**: Leverages the TomTom API to fetch both live **traffic flow** and **incidents** data for NYC.
- **Interactive visualizations**: Clear and dynamic visualizations of traffic patterns across NYC, enabling better decision-making for commuters and analysts.

## Key Differences from the Sample Application
- The map is centered around New York City for localized analysis.
- The map updates automatically every hour to ensure up-to-date traffic information.
- The traffic flow style uses `absolute` speed values (in km/h) instead of the default `relative` flow style for clearer interpretation of traffic conditions.

## Limitation
- It focuses solely on visualizing traffic patterns (flows and incidents), but it does not fetch or store the data locally for further analysis. It is a black box. This restricts the ability to (1) explore/analyze historical and realtime traffic patterns and (2) perform predictive modeling directly within the application.

## Beyond Visualization: Fetching and Analyzing Data 
To overcome this limitation and extend the project's capabilities, I have implemented an approach that fetches real-time traffic data, enabling deeper analysis beyond just visualization:
- **Data extraction:** Using the TomTom Traffic API, real-time traffic flow and incident data are collected and stored for further analysis.
- **Jupyter Notebook for in-depth analysis:** The repository includes a Jupyter Notebook where the fetched data is processed and visualized in python. This setup allows for traffic flow and incident trend analysis, making it possible to develop predictive models to forecast future traffic conditions or identify potential congestion hotspots.
