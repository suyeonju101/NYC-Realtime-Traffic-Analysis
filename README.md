# NYC Realtime Traffic Analysis

*Note: This application builds on top of the sample application provided by TomTom API. You can find the original tutorial here: [TomTom Traffic Tutorial](https://developer.tomtom.com/maps-sdk-web-js-v5/tutorials-use-cases/traffic-tutorial).*

This repository offers a detailed analysis of real-time traffic data in New York City, combining both **traffic flow** and **incident** data to deliver actionable insights. The project is designed to provide users with comprehensive visualizations of current traffic conditions, helping optimize travel routes and identify congestion points.

For a live view of the traffic analysis, check out the interactive map: [NYC Real-time Traffic Map](https://suyeonju101.github.io/NYC-Realtime-Traffic-Analysis/traffic.html).

### Key Features
- **Real-time data extraction**: Leverages the TomTom API to fetch both live **traffic flow** and **incidents** data for NYC.
- **Interactive visualizations**: Clear and dynamic visualizations of traffic patterns across NYC, enabling better decision-making for commuters and analysts.

### Key Differences from the Sample Application
- The map is centered around New York City for localized analysis.
- The map updates automatically every hour to ensure up-to-date traffic information.
- The traffic flow style uses `absolute` speed values (in km/h) instead of the default `relative` flow style for clearer interpretation of traffic conditions.

## Limitation
- It focuses solely on visualizing traffic patterns (flows and incidents), but it does not fetch or store the data locally for further analysis. It is a black box. This restricts the ability to (1) explore/analyze historical and realtime traffic patterns and (2) perform predictive modeling directly within the application.

## Beyond Visualization: Fetching and Analyzing Data 
To overcome this limitation and extend the project's capabilities, I have implemented an approach that fetches real-time traffic data, enabling deeper analysis beyond just visualization:
- **Data extraction:** Using the TomTom Traffic API, real-time traffic flow and incident data are collected and stored for further analysis.
- **Jupyter Notebook for in-depth analysis:** The repository includes a Jupyter Notebook where the fetched data is processed and visualized in python. This setup allows for traffic flow and incident trend analysis, making it possible to develop predictive models to forecast future traffic conditions or identify potential congestion hotspots.
