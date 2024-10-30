import os
import time
from datetime import datetime
from TrafficIncident import TrafficIncidentFetcher
from TrafficFlow import TrafficFlowFetcher


def main():
    # Directories to save CSV files
    incident_output_dir= "TrafficIncidentData"
    flow_output_dir = "TrafficFlowData"
    # Create the directories if they don't exist
    os.makedirs(incident_output_dir, exist_ok=True)
    os.makedirs(flow_output_dir, exist_ok=True)

    # Initialize TrafficIncidentFetcher with API key
    api_key = "N8xhZrbfY7NZEqbqIeEedz4xUBmXARBG"

    # Traffic Incident
    bbox = "-74.25,40.50,-73.70,40.95"  # bounding box coordinates for NYC (minLon,minLat,maxLon,maxLat)

    incident = TrafficIncidentFetcher(api_key)
    flow = TrafficFlowFetcher(api_key)

    try:
        while True:
            # Get the current timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Fetch traffic incidents and directly get DataFrame
            incidents_df = incident.get_traffic_incidents(bbox)

            # Display the DataFrame content for verification
            print("Fetched Incidents DataFrame:")
            print(incidents_df.head())  # show the first few rows for easier inspection
            
            # Check if incidents data is available
            if not incidents_df.empty:
                # Define CSV filename with timestamp
                csv_filename = os.path.join(incident_output_dir, f"traffic_incident_{timestamp}.csv")
                
                # Save the DataFrame to CSV
                incident.save_df_to_csv(incidents_df, csv_filename)
                print(f"Data saved as {csv_filename} at {timestamp}")
            else:
                print(f"No data fetched at {timestamp}. Retrying in 2 minutes.")

            # Wait for 2 minutes (120 seconds) before the next fetch
            time.sleep(120)

    except KeyboardInterrupt:
        print("Real-time data fetching interrupted.")


if __name__ == "__main__":
    main()