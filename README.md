# ai-asset-deprecation-calculator-agent

Welcome to the **AI-Powered Asset Depreciation Calculator**! This application simplifies asset depreciation calculations using AI-powered algorithms and stores data in a PostgreSQL database.

---

## Getting Started

### Prerequisites
Ensure the following are installed on your system:
- Python 3.12
- Node.js and npm (for the frontend)  
- PostgreSQL (for the database)  

---

## Installation Guide

Follow these steps to set up and run the project:

1. **Clone the Repository**
   Obtain the project files from the provided source and extract them to your local machine.  

2. **Create a Virtual Environment with Conda**
    Before installing dependencies, it's a good practice to create a virtual environment with Conda:
    ```bash
    conda create -n your_env_name python=3.12
    conda activate your_env_name
    ```

3. **Set Up PostgreSQL**
   - Install PostgreSQL if it\u2019s not already installed.  
   - Create a new PostgreSQL database:
     ```sql
     CREATE DATABASE depreciation_db;
     ```
   - Note the database credentials (e.g., username, password, database name, host, port).

4. **Install Backend Dependencies**
   Navigate to the root directory and install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Database Migration**
    To create the `assets` table in the database, navigate to the `database` folder and run the `migrate.py` file:
    ```bash
    python -m backend.database.migrate.py
    ```

6. **Set Up Environment Variables**  
   Create a `.env` file in the root directory of the project. Define the variables by looking at `.example.env`.

## Run the Backend
Once the dependencies are installed and environment variables are set, run the FastAPI server:

  1.  **For macOS or Linux:**
  ```bash
  python3 main.py
  ```


  2. **For Windows:**
  ```bash
  python main.py
  ```

## Run the Frontend
Navigate to the frontend directory, install the necessary dependencies, and start the frontend server:
```bash
npm install
npm start
```

## Access the Application

- Backend should be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Frontend should be accessible at [http://127.0.0.1:3000](http://127.0.0.1:3000)
- Asset report will be available at [http://127.0.0.1:3000/assets/\<asset_uuid\>](http://127.0.0.1:3000/assets/\<asset_uuid\>)

## Usage

### Add an Asset
Use the frontend to fill the asset form by entering the Asset Name, Purchase Cost, Purchase Date and Category.

### View Depreciation Results
The AI-powered system will generate a depreciation report for the asset, including details providing annual depreciation values, accumulated depreciation, and book value.
