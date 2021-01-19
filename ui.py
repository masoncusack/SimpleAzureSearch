import os

import streamlit as st
from dotenv import load_dotenv

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

load_dotenv()

# constants
search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
search_index = os.getenv(
    "AZURE_SEARCH_INDEX_NAME"
)  # Feel free to use > 1 and switch them out
search_api_key = os.getenv("AZURE_SEARCH_ADMIN_API_KEY")

# UI

title = os.getenv("APPLICATION_NAME")
st.header(title)

q = st.text_input("Search query", "Type your search query here")
st.write("The current search query is:", q)

# Query processing

search_client = SearchClient(
    endpoint=search_endpoint,
    index_name=search_index,
    credential=AzureKeyCredential(search_api_key),
)

results = search_client.search(search_text=q, include_total_count=True)

st.text(f"Total Documents Matching Query: {results.get_count()}")

st.subheader("Results found:")

# print(type(results)) # spoiler: custom Azure Search pagedItem object
for result in results:
    # print(result.keys())  # Inspect what you can display
    st.text(result[str(list(result.keys())[0])])  # Show first available item
