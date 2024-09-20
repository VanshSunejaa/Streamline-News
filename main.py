import json
import requests
import xmltodict
from bs4 import BeautifulSoup
import streamlit as st

# Function to fetch and process news from RSS feed
def fetch_news(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    xml_data = xmltodict.parse(response.content)
    return xml_data

# Function to extract news items from the parsed data
def extract_news_items(news_data):
    items = news_data['rss']['channel']['item']
    news_list = []
    for item in items:
        title = item.get('title', 'No Title')
        description = item.get('description', 'No Description')
        link = item.get('link', 'No Link')
        source = item.get('source', {}).get('#text', 'No Source')

        # Parse HTML description using BeautifulSoup
        soup = BeautifulSoup(description, 'html.parser')
        clean_description = soup.get_text()

        news_list.append({'title': title, 'description': clean_description, 'link': link, 'source': source})
    return news_list

# Streamlit UI
st.title('Streamline News')

# Selection option
option = st.selectbox('Select News Type:', ['Latest News', 'Search News'])

if option == 'Latest News':
    url = "https://news.google.com/rss"
else:
    query = st.text_input('Enter search query:')
    if query:
        url = f"https://news.google.com/rss/search?q={query}"
    else:
        st.warning('Please enter a search query.')
        url = None

if url:
    try:
        # Fetch and process news
        news_data = fetch_news(url)
        news_items = extract_news_items(news_data)

        # Display news
        for item in news_items:
            st.subheader(item['title'])
            st.write(item['description'])
            st.write(f"[Read more]({item['link']})")
            st.write(f"Source: {item['source']}")
            st.markdown("---")
    except requests.RequestException as e:
        st.error(f"Error fetching news: {e}")
