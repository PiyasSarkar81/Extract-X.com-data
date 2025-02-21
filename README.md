# x.com API Tweet Scraper

This project is a simple Python script that uses the **x.com API v2** to fetch recent tweets based on a search query and save them as a JSON file. The script is designed to run in a local Python environment.

## Features
- Fetch recent tweets using the x.com API v2
- Save extracted tweets into a structured JSON file
- Handles API authentication via a Bearer Token stored in `config.py`
- Organizes data storage in a `data/` directory

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/PiyasSarkar81/Extract-X.com-data.git
   cd Extract-X.com-data
   ```

2. **Set up a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your x.com API credentials**
   - Create a `config.py` file in the project directory.
   - Add your **Bearer Token**:
     ```python
     bearer_token = "YOUR_X_BEARER_TOKEN"
     ```

## Usage

Run the script to fetch tweets for a specific keyword and store it into JSON file in `data/` directory.
```bash
python extract_tweets_to_json.py
```

You can modify the search keyword by updating the `keyword` variable in the script:
```python
keyword = "AI"
```

## Output
- The script fetches tweets and saves them in the `data/` directory.
- Example filename: `data/stream_AI.json`
- The JSON file will contain tweets with fields like `created_at`, `author_id`, and `text`.

## Requirements
Ensure you have Python 3 installed and install dependencies using:
```bash
pip install -r requirements.txt
```
The `requirements.txt` file includes:
```
requests
```

## License
This project is licensed under the MIT License.
