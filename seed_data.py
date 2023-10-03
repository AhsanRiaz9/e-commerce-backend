from app.db.database import SessionLocal
from app.db.models import Product

# Function to seed data for the Product model
def seed_products():
    products = [
        {
            "name": "Product 1",
            "category": "Category 1",
            "price": 29.99,
        },
        {
            "name": "Product 2",
            "category": "Category 2",
            "price": 39.99,
        },
        {
            "name": "Product 3",
            "category": "Category 2",
            "price": 139.99,
        },
        {
            "name": "Product 4",
            "category": "Category 1",
            "price": 139.99,
        },
        {
            "name": "Product 5",
            "category": "Category 4",
            "price": 139.99,
        },
    ]

    # Create session
    db = SessionLocal()

    try:
        for product_data in products:
            product = Product(**product_data)
            db.add(product)

        # Commit the changes to the database
        db.commit()
        print("Data seeding completed successfully!")
    except Exception as e:
        # Rollback the transaction if an error occurs
        db.rollback()
        print(f"Error occurred: {str(e)}")
    finally:
        # Close the session
        db.close()


seed_products()
