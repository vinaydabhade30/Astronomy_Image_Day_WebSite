import streamlit as st
import requests
# prepare API key and API url
NASA_APP_KEY = "dIBJjdbXLMCoRQRnfAlDTQbgPJOL9o898dEck35L"

web_request = "https://api.nasa.gov/planetary/apod?" \
              "api_key=dIBJjdbXLMCoRQRnfAlDTQbgPJOL9o898dEck35L"

# get the request data as a dictionary

call_url = requests.get(web_request)
content = call_url.json()

# extract the image, title, url and explanation
art_date = content['date']
art_info = content['explanation']
art_title = content['title']
art_type = content['media_type']
art_url = content["url"]

st.title(art_title)

# download the image
if art_type == 'image':
    get_img = requests.get(art_url)
    with open("image.jpg", "wb") as file:
        file.write(get_img.content)
    st.image("image.jpg")
# if video then show link
else:
    link = f'[{art_title}- a short film link]({art_url})'
    st.markdown(link, unsafe_allow_html=True)

# show on webpage by streamlit


st.write(art_info)
st.write(f'Today Date: {art_date}')
