import pandas as pd
import folium
from folium import plugins

def load_emitters(filename):
    df = pd.read_excel(filename)

    df = df[df["CountryName"] == "Greece"][["Latitude", "Longitude"]]

    return df

def load_storage(filename):
    df = pd.read_excel(filename)

    df = df[["Lat / Y", "Long / X"]].dropna()
    df = df.rename(columns={"Lat / Y": "Latitude", "Long / X": "Longitude"})
    return df

def plot_on_map(dataframe_emitters, dataframe_storage):
    m = folium.Map(location=[(dataframe_emitters["Latitude"].min() + dataframe_emitters["Latitude"].max()) / 2,
                             (dataframe_emitters["Longitude"].min() + dataframe_emitters["Longitude"].max()) / 2], zoom_start=7,
                   control_scale=True)

    for lat, long in zip(dataframe_emitters["Latitude"], dataframe_emitters["Longitude"]):
        folium.CircleMarker(location=(lat, long), radius=5, color='blue', tooltip="Emitter location").add_to(m)

    for lat, long in zip(dataframe_storage["Latitude"], dataframe_storage["Longitude"]):
        folium.CircleMarker(location=(lat, long), radius=5, color='red', tooltip="Storage location").add_to(m)


    minimap = plugins.MiniMap()
    m.add_child(minimap)

    m.save("location - storage_and_emitters.html")

if __name__ == '__main__':
    emitters = load_emitters("../CCUS_NW_SE_Europe-Emitters.xlsx")
    storage = load_storage("../CCUS_NW_SE_Europe-Storage.xlsx")
    plot_on_map(emitters, storage)
