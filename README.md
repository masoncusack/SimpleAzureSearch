# Simple Azure Search

The simplest possible front end search box and results rendering for an Azure Cognitive Search app,
utilising [streamlit](https://www.streamlit.io/) and 
[dotenv](https://pypi.org/project/python-dotenv/) to keep it down to a single Python script.

### Usage

Clone the repo.

```
git clone <repo-url> && cd simpleazuresearch
```

In your preferred environment, run:

```bash
pip3 install -r requirements.txt
```

Copy and paste the contents of `.env-dev` into a file named `.env` (which is git ignored).

Fill out `.env` with the details of your project and Azure resources.
Note: these are secrets and you should ensure you do not commit this file to version control.

Run:

```
streamlit run ui.py
```

Then open your browser and search away!