# E-Commerce Manager Admin Dashboard API

This API provides detailed insights into sales, revenue, and inventory status, as well as functionality for new product registration, designed to power a web admin dashboard for e-commerce managers.

## Core Features:

### 1. Sales Status:

- Endpoints to retrieve, filter, and analyze sales data.
- Endpoints to analyze revenue on a daily, weekly, monthly, and annual basis.
- Ability to compare revenue across different periods and categories.
- Provide sales data by date range, product, and category.

### 2. Inventory Management:

- Endpoints to view current inventory status, including low stock alerts.
- Functionality to update inventory levels and track changes over time.

## Technical Stack:

- **Backend Framework:** FastAPI (Python)
- **Database:** MySQL (SQLAlchemy ORM)
- **API Documentation:** Swagger UI (auto-generated by FastAPI)
- **Database Migrations:** Alembic
- **Data Validation:** Pydantic
- **Server Runner:** Uvicorn (for running FastAPI application)

## Getting Started:

### Prerequisites:

- Python 3.6+
- MySQL Database
- pip (for install packages)

### Installation:

1. Clone the repository:

   ```
   git clone https://github.com/AhsanRiaz9/e-commerce-backend
   cd e-commerce-backend
   ```

2. Set virtualenv
   For linux or macOS:

   ```
       python3 -m venv venv
   ```

   For Windows:

   ```
     python -m venv venv
   ```

3. Activate Virtual Environment
   For linux or macOS:

   ```
   source venv/bin/activate
   ```

   For Windows:

   ```
   venv/Scripts/activate
   ```

4. Install dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

5. Configure your database settings by renaming .env.example with .env:

   ```python
   DATABASE_URL = "mysql+mysqlconnector://<username>:<password>@<host>/<database_name>"
   ```

6. Apply database migrations using Alembic:

   ```
   alembic init alembic
   alembic upgrade head
   ```

   Now alembic folder will be created, open env.py and these lines:

   ```
   from app.db.database import Base
   from app.db.models import Product, Sale, Inventory
   target_metadata = Base.metadata
   ```

   Apply migrations:

   ```
   alembic revision --autogenerate -m "message for migration changes"
   alembic upgrade head
   ```

7. Run the FastAPI server:

   ```
    uvicorn app.main:app --reload
   ```

8. Seed data in database:

   ```
     python3 seed_data.py
   ```

Note: you need to rename .env.example with .env and update the value of DATABASE_URL variable according to your database configuration

## API Documentation:

- **Swagger UI:** `http://localhost:8000/docs`

## Endpoints:

#### Products:

- **Create Product Route**

  - **Method:** POST
  - **Endpoint:** `/api/products/`
  - **Description:** Create a new product.

- **Read Products Route**

  - **Method:** GET
  - **Endpoint:** `/api/products/`
  - **Description:** Retrieve a list of all products.

- **Read Product Route**

  - **Method:** GET
  - **Endpoint:** `/api/products/{product_id}/`
  - **Description:** Retrieve details of a specific product by its ID.

- **Update Product Route**
  - **Method:** PUT
  - **Endpoint:** `/api/products/{product_id}/`
  - **Description:** Update details of a specific product by its ID.

#### Inventory:

- **Read All Inventories**

  - **Method:** GET
  - **Endpoint:** `/api/inventory/`
  - **Description:** Retrieve a list of all inventory items.

- **Create Inventory**

  - **Method:** POST
  - **Endpoint:** `/api/inventory/`
  - **Description:** Create a new inventory item.

- **Read Low Stock Inventories**

  - **Method:** GET
  - **Endpoint:** `/api/inventory/low_stock/`
  - **Description:** Retrieve a list of inventory items with low stock.

- **Read Inventory**

  - **Method:** GET
  - **Endpoint:** `/api/inventory/{inventory_id}/`
  - **Description:** Retrieve details of a specific inventory item by its ID.

- **Update Inventory Stock**
  - **Method:** PUT
  - **Endpoint:** `/api/inventory/update_stock/`
  - **Description:** Update stock quantity of a specific inventory item.

#### Sales:

- **Create Sale Record**

  - **Method:** POST
  - **Endpoint:** `/api/sales/`
  - **Description:** Record a new sale.

- **Read Sales**
  - **Method:** GET
  - **Endpoint:** `/api/sales/`
  - **Description:** Retrieve a list of all sales records.

#### Revenue Analytics:

- **Get Daily Revenue**

  - **Method:** GET
  - **Endpoint:** `/api/revenue/daily/{date}`
  - **Description:** Get revenue details for a specific day.

- **Get Weekly Revenue**

  - **Method:** GET
  - **Endpoint:** `/api/revenue/weekly/{start_date}`
  - **Description:** Get revenue details for a specific week.

- **Get Annual Revenue**

  - **Method:** GET
  - **Endpoint:** `/api/revenue/annual/{year}`
  - **Description:** Get revenue details for a specific year.

- **Compare Revenue**
  - **Method:** GET
  - **Endpoint:** `/api/revenue/compare`
  - **Description:** Compare revenue across different periods and categories.

## Examples:

- **Retrieve Daily Revenue:**

  ```
  GET /sales/revenue/daily/2023-10-01
  ```

- **Update Inventory:**
  ```
  POST /inventory
  {
      "product_id": 1,
      "quantity": 50
  }
  ```

## Database Schema:

- **Products:** Table for storing product information.
- **Sales:** Table for storing sales data, linked to Products table via foreign key.
- **Inventory:** Table for managing inventory, linked to Products table via foreign key.

## Contributing:

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -m 'Add a new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Submit a pull request.
