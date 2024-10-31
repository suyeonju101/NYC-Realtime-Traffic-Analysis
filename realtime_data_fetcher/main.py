import os
import time
from datetime import datetime
from TrafficIncident import TrafficIncidentFetcher
from TrafficFlow import TrafficFlowFetcher

# Directories to save CSV files
incident_output_dir = "TrafficIncidentData"
flow_output_dir = "TrafficFlowData"

# Create directories if they don't exist
os.makedirs(incident_output_dir, exist_ok=True)
os.makedirs(flow_output_dir, exist_ok=True)

## CHANGE VALUES AS YOU WANT #############
# Initialize API key
API_KEY = "N8xhZrbfY7NZEqbqIeEedz4xUBmXARBG"

# Define the Region of Interest (ROI)
bbox = "-74.25,40.50,-73.70,40.95"               # bounding box coordinates for NYC
nyc_lat_min, nyc_lat_max = 40.79830, 40.81826    # Latitude from 103rd to 130th Street
nyc_lon_min, nyc_lon_max = -73.97502, -73.94881  # Longitude from the west edge of Manhattan to Central Park West
lat_step, lon_step = 0.0005, 0.0015

incident_interval = 3600         # an hour in seconds
flow_intervals = {8, 9, 16, 17}  # Peak hours: 8-9 AM, 9-10 AM, 4-5 PM, 5-6 PM
## CHANGE#################################

# Initialize class objects
incident = TrafficIncidentFetcher(API_KEY)
flow = TrafficFlowFetcher(API_KEY)

def main():
    """
    Fetches traffic incidents data every hour and traffic flow data at specific times.
    Saves each data type to its respective CSV file.
    """
    last_incident_fetch = None
    last_flow_fetch_time = None

    try:
        while True:
            # Get the current time and date for checking intervals
            current_time = datetime.now()
            current_hour = current_time.hour
            timestamp = current_time.strftime("%Y%m%d_%H%M%S")

            # Fetch incidents every hour
            if last_incident_fetch is None or (current_time - last_incident_fetch).seconds >= incident_interval:
                incidents_df = incident.get_traffic_incidents(bbox)
                print(f"Traffic incident data fetched at {datetime.now()}")
                if not incidents_df.empty:
                    incident_filename = os.path.join(incident_output_dir, f"traffic_incident_{timestamp}.csv")
                    incident.save_df_to_csv(incidents_df, incident_filename)
                    print(f"Traffic incidents data saved at {incident_filename}")
                else:
                    print("No new incident data available.")
                
                last_incident_fetch = current_time  # Update last fetch time for incidents
            
            # Fetch flow data at specific intervals
            if current_hour in flow_intervals and (last_flow_fetch_time is None or last_flow_fetch_time.hour != current_hour):
                flows_df = flow.get_traffic_flow(nyc_lat_min, nyc_lat_max, nyc_lon_min, nyc_lon_max, lat_step, lon_step)
                print(f"Traffic flow data fetched at {datetime.now()}")
                if not flows_df.empty:
                    flow_filename = os.path.join(flow_output_dir, f"traffic_flow_{timestamp}.csv")
                    flow.save_df_to_csv(flows_df, flow_filename)
                    print(f"Traffic flow data saved at {flow_filename}")
                else:
                    print("No new flow data available.")
                
                last_flow_fetch_time = current_time  # Update last fetch time for flows

    except KeyboardInterrupt:
        print("Real-time data fetching interrupted.")

if __name__ == "__main__":
    main()
