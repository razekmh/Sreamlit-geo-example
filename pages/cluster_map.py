import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(center=[40, -100], zoom=4)
        cities = "https://github.com/razekmh/Sreamlit-geo-example/blob/a8aa60c5fb144010d4823d74babf8cacd8aec146/data/sample_locations.csv"
        regions = "https://github.com/razekmh/Sreamlit-geo-example/blob/a8aa60c5fb144010d4823d74babf8cacd8aec146/data/sa_regions.geojson"

        m.add_geojson(regions, layer_name="US Regions")
        m.add_points_from_xy(
            cities,
            x="longitude",
            y="latitude",
            color_column="region",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=700)
