import folium

def plot_path_on_map(locations, path, save_path='ucsd_map_path.html'):
    m = folium.Map(location=[32.8801, -117.2375], zoom_start=16)
    for idx in range(len(path)):
        i = path[idx]
        j = path[(idx + 1) % len(path)]
        start = locations[i][::-1]
        end = locations[j][::-1]
        folium.Marker(start, tooltip=f'{i}').add_to(m)
        folium.PolyLine([start, end], color='blue', weight=3).add_to(m)
    m.save(save_path)
