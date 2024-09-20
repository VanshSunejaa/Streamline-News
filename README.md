# Streamline News

## Project Description
"Streamline News" is a Streamlit application designed to fetch and display news from RSS feeds, specifically from Google News. Users can either view the latest news or search for specific topics of interest. The application utilizes Python libraries such as `requests`, `xmltodict`, and `BeautifulSoup` for effective data processing and extraction.

## Features
- Fetches the latest news articles from Google News RSS feed.
- Allows users to search for news articles by specific queries.
- Displays article titles, descriptions, links, and sources.
- Cleans HTML content from descriptions for better readability.

## Technologies Used
- Python
- Streamlit
- Requests
- xmltodict
- BeautifulSoup

## File Structure
```
/streamline_news
│
├── app.py                  # Main application file
├── requirements.txt        # Dependencies for the project
└── README.md               # Documentation for the project
```

## Installation Instructions
1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd streamline_news
   ```

2. **Install the required packages:**
   You can use pip to install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Start the Streamlit server with the following command:
   ```bash
   streamlit run app.py
   ```
   This will open the application in your web browser.

## Code Explanation
- **fetch_news(url):** This function retrieves the news data from the provided RSS feed URL and parses it from XML format into a Python dictionary using `xmltodict`.
- **extract_news_items(news_data):** This function processes the parsed data to extract relevant news items, including titles, descriptions, links, and sources. It also cleans the description using `BeautifulSoup`.
- **Streamlit UI:** The user interface allows users to select between viewing the latest news or searching for specific news topics. It displays the results in an organized format.

## Disclaimer
This project is created for learning purposes only and is not intended for production use or from a user perspective. It serves as a practical example to understand web scraping and data processing in Python.

## Acknowledgments
- Google News for the RSS feed
- Streamlit for creating a user-friendly web application interface

