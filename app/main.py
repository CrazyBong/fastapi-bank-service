from fastapi import FastAPI
from app.database import Base, engine
from app.models import Bank, Branch
import csv
import os

# Create FastAPI app instance
app = FastAPI()

# Import routers
from app.routes import banks, branches

# Include routers
app.include_router(banks.router)
app.include_router(branches.router)


@app.on_event("startup")
def startup_event():
    # Create database tables
    Base.metadata.create_all(bind=engine)
    
    # Load data from CSV file
    load_data_from_csv()


def load_data_from_csv():
    # Create a database session
    from app.database import SessionLocal
    db = SessionLocal()
    
    try:
        # Check if banks table already has data
        if db.query(Bank).first() is not None:
            print("Data already loaded. Skipping data loading.")
            return
        
        # Resolve CSV file path safely using os.path and __file__
        csv_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'bank_branches.csv')
        
        # Read data from CSV file
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            
            # Process each row in the CSV
            for row in reader:
                # Check if bank already exists
                bank = db.query(Bank).filter(Bank.name == row['bank_name']).first()
                
                # If bank doesn't exist, create it
                if not bank:
                    bank = Bank(name=row['bank_name'])
                    db.add(bank)
                    db.flush()  # Get the bank ID without committing
                
                # Check if a branch with the same IFSC already exists
                existing_branch = db.query(Branch).filter(Branch.ifsc == row['ifsc']).first()
                
                # If branch doesn't exist, create it
                if not existing_branch:
                    # Create branch
                    branch = Branch(
                        ifsc=row['ifsc'],
                        branch=row['branch'],
                        address=row['address'],
                        city=row['city'],
                        district=row['district'],
                        state=row['state'],
                        bank_id=bank.id
                    )
                    db.add(branch)
            
            # Commit all changes
            db.commit()
            print("Data loaded successfully.")
    
    except Exception as e:
        # Rollback in case of error
        db.rollback()
        print(f"Error loading data: {e}")
    
    finally:
        # Close the session
        db.close()
