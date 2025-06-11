# PandemicGraphCluster

This project is an application developed as part of the "**Data Mining and Data Extraction**" course in the MSc program "**Information Systems and Services**" of the Department of Digital Systems at the University of Piraeus.

The application focuses on the **analysis and clustering of pandemic COVID-19 data** using graphs. The user can select a specific week, year, and number of clusters, and visually view the results.

---

## Installation & Execution

The application has been tested with:
- Python **3.8**
- Windows

### Step 1: Create Virtual Environment (recommended)
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3.8-venv

python3.8 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Start the Server
```bash
python3 server.py
```
The server will remain running in the terminal.

## Access the UI
Open the following file in a web browser:
```bash
frontend/index.html
```

## Authors
- Panagiotis Karamolegkos
- Kyriakos Kyriakou