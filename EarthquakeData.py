import requests
import matplotlib.pyplot as plt

api_url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson'
response = requests.get(api_url)
data = response.json()

earthquakes = data['features']
magnitudes = []
times = []

for earthquake in earthquakes:
    magnitude = earthquake['properties']['mag']
    time = earthquake['properties']['time']
    magnitudes.append(magnitude)
    times.append(time)

plt.figure("Earthquake Data")
plt.scatter(times, magnitudes)
plt.xlabel("Time of Earthquake")
plt.ylabel("Magnitude")
plt.title("Magnitude of Earthquakes Over Time")
plt.show()

# Data Analysis:
# There appears to be a cluster of earthquakes with magnitudes around 4.6 occurring at similar times during the past week.