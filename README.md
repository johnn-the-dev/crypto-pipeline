# 📈 Crypto Data Pipeline & Dashboard

**An End-to-End Data Engineering pipeline fetching real-time cryptocurrency market data and visualizing it in a cloud-connected dashboard.**

## 🏗️ Architecture
1. **Data Extraction:** Python script fetches live prices and 24h volumes from the **CoinGecko API**.
2. **Containerization:** The extraction script is fully dockerized for consistent, environment-agnostic execution.
3. **Cloud Storage:** Data is securely pushed to a remote **Neon PostgreSQL** database.
4. **Visualization:** A **Streamlit** dashboard connects directly to the cloud DB to display historical trends using Pandas.
5. **Automation (WIP):** Scheduled to run autonomously via GitHub Actions.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Database:** PostgreSQL (Neon Serverless Cloud)
* **Infrastructure:** Docker, GitHub Actions (CI/CD)
* **Libraries:** `requests`, `psycopg2`, `pandas`, `streamlit`, `python-dotenv`

## 🚀 How to Run Locally

### Prerequisites
* Docker Desktop installed
* Python 3.11 installed
* A Neon PostgreSQL database (with Connection String)

### Setup
1. Clone the repository...
2. Create a `.env` file... (ZDE DOPLŇ, CO TAM MÁ UŽIVATEL NAPSAT)
3. ...

### Running the Extractor (Docker)
1. Build the Docker image:
   `docker build -t crypto-extractor .`
2. Run the container with your environment variables:
   `docker run --env-file .env crypto-extractor`

### Running the Dashboard
streamlit run dashboard.py