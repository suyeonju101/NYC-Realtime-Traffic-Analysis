import requests
import pandas as pd

class TrafficFlowFetcher:
    def __init__(self, api_key, 
                 base_url="api.tomtom.com", 
                 version_number=4, 
                 style="absolute", 
                 zoom=22, 
                 form="json", 
                 thickness=1):
        """
        Initializes the TrafficFlowFetcher class with parameters for the TomTom Traffic API.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.version_number = version_number
        self.style = style
        self.zoom = zoom
        self.form = form
        self.thickness = thickness

    def get_traffic_flow(self, location):
        """
        Fetches real-time data on road speeds and travel times from the TomTom Traffic API.
        """
        url = (f"https://{self.base_url}/traffic/services/{self.version_number}/"
               f"flowSegmentData/{self.style}/{self.zoom}/{self.form}?"
               f"key={self.api_key}&point={location}&thickness={self.thickness}")
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to fetch data. Status code: {response.status_code}"}
    
    def json_to_dataframe(self, json_data):
        """
        Converts JSON data from the TomTom Traffic API into a structured DataFrame.
        """
        if 'flowSegmentData' in json_data:
            data = json_data['flowSegmentData']
            df = pd.DataFrame({
                "currentSpeed": [data['currentSpeed']],
                "freeFlowSpeed": [data['freeFlowSpeed']],
                "currentTravelTime": [data['currentTravelTime']],
                "freeFlowTravelTime": [data['freeFlowTravelTime']],
                "coordinates": [[(coord['latitude'], coord['longitude']) for coord in data['coordinates']['coordinate']]]
            })
            return df
        else:
            return pd.DataFrame({"error": [json_data.get("error", "Unknown error")]})

    def save_df_to_csv(self, df, filename):
        """
        Save the DataFrame to a CSV file.
        """
        df.to_csv(filename, index=False)