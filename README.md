<!-- [Reference](https://paulabartabajo.substack.com/p/lets-build-a-production-ready-rest?utm_source=substack&publication_id=881497&post_id=149484668&utm_medium=email&utm_content=share&utm_campaign=email-share&triggerShare=true&isFreemail=true&r=24188e&triedRedirect=true) -->

# NYC Taxi Data API

## Overview

This project implements a RESTful API using FastAPI to serve data from the NYC Taxi and Limousine Commission (TLC) Yellow Taxi Trip Records. The API allows users to retrieve trip data within a specified time range.

## Features

- **Efficient Data Retrieval:** Utilizes Parquet files for optimized data storage and retrieval.
- **Caching:** Downloaded Parquet files are cached locally to reduce network requests and improve response times.
- **Pagination:**  The API supports pagination, allowing clients to retrieve data in manageable chunks.
- **Health Check:**  Includes a `/health` endpoint for monitoring the API's status.

## API Endpoints

### `/trips`

**Method:** GET

**Description:** Retrieves a list of taxi trips within a specified time range.

**Query Parameters:**

- `from_ms`: (Required) Unix timestamp in milliseconds representing the start of the time range.
- `n_results`: (Optional) Maximum number of results to return (default: 100).


### `/health`

**Method:** GET

**Description:**  Checks the health of the API.


## Setup and Running

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/nyc-taxi-data-api.git
   cd nyc-taxi-data-api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set the `CACHE_DIR` environment variable (optional):**
   ```bash
   export CACHE_DIR=/path/to/your/cache/directory
   ```

5. **Run the application:**
   ```bash
   uvicorn src.api:app --reload
   ```

The API will be accessible at `http://127.0.0.1:8000`.

