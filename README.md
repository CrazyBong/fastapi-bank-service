# Bank Branch API

This project is a REST API built with FastAPI that exposes bank and branch data from a CSV dataset. It provides endpoints to retrieve information about banks and their respective branches.

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- pytest

## How to Run

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Start the server:
   ```
   uvicorn app.main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

- `GET /banks/` - Retrieve all banks
- `GET /banks/{bank_id}/branches` - Retrieve all branches for a specific bank
- `GET /branches/{ifsc}` - Retrieve a specific branch by IFSC code

## Time Taken

Approximately 45mins to complete the assignment.
