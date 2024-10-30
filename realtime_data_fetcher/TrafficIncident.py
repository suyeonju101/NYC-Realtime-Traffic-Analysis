import requests
import pandas as pd

class TrafficIncidentFetcher:
    ICON_MAPPING = {
        0: 'Unknown',
        1: 'Accident',
        2: 'Fog',
        3: 'Dangerous Conditions',
        4: 'Rain',
        5: 'Ice',
        6: 'Jam',
        7: 'Lane Closed',
        8: 'Road Closed',
        9: 'Road Works',
        10: 'Wind',
        11: 'Flooding',
        14: 'Broken Down Vehicle'
    }

    ICON_STYLES = {
        'Accident': {'icon': 'car', 'color': 'red'},
        'Jam': {'icon': 'road', 'color': 'orange'},
        'Road Works': {'icon': 'wrench', 'color': 'blue'},
        'Fog': {'icon': 'cloud', 'color': 'gray'},
        'Rain': {'icon': 'cloud-rain', 'color': 'blue'},
        'Ice': {'icon': 'snowflake', 'color': 'lightblue'},
        'Wind': {'icon': 'wind', 'color': 'lightgreen'},
        'Flooding': {'icon': 'tint', 'color': 'blue'},
        'Broken Down Vehicle': {'icon': 'truck', 'color': 'black'},
        'Lane Closed': {'icon': 'minus-circle', 'color': 'purple'},
        'Dangerous Conditions': {'icon': 'exclamation-triangle', 'color': 'yellow'},
        'Road Closed': {'icon': 'times-circle', 'color': 'darkred'},
        'Unknown': {'icon': 'question-circle', 'color': 'gray'}
    }

    def __init__(self, api_key, base_url="https://api.tomtom.com", version_number=5):
        self.api_key = api_key
        self.base_url = base_url
        self.version_number = version_number

    def get_traffic_incidents(self, bbox):
        """
        Fetch real-time data on traffic incidents and return as a DataFrame.
        """
        url = f"{self.base_url}/traffic/services/{self.version_number}/incidentDetails"
        params = {
            'key': self.api_key,
            'bbox': bbox
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            incidents = response.json().get('incidents', [])
            print(f"\nNumber of Incidents: {len(incidents)}")  # for analysis purposes
            
            # Convert incidents data to DataFrame
            incidents_df = pd.json_normalize(incidents)
            incidents_df['properties.iconCategory'] = incidents_df['properties.iconCategory'].map(self.ICON_MAPPING)
            
            return incidents_df
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return pd.DataFrame()  # return an empty DataFrame if the request fails

    def save_df_to_csv(self, df, filename):
        """
        Save the DataFrame to a CSV file.
        """
        df.to_csv(filename, index=False)
