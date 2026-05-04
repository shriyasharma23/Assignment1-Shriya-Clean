## Assignment 1 | Shriya Sharma | Calsoft Internship 2026

This is my submission for Assignment 1. The assignment was 
originally in Java but I have implemented it in Python using 
FastAPI, keeping all endpoint names and table structures exactly 
as given.

---

## Tech Stack
- Python with FastAPI framework
- SQLAlchemy for database operations
- SQLite as the local database
- Tested using FastAPI Swagger UI at /docs

---

## Q1 - Inventory Report API
- Client needs inventory records between two dates
- Endpoint: GET /getInventoryDetails?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD
- Joins Inventory and InventoryDetails tables
- Filters by date range and returns matching records
- Handles invalid dates and empty results gracefully

---

## Q2 - Device Config Notification API
- Detects when any device has config_changed set to True
- Endpoint: GET /deviceConfigNotification
- Sends a JSON alert for every changed device
- Automatically resets the flag after notifying
- Prevents duplicate alerts for the same change

---

## Q3 - Posts API with Pagination
- Problem: API was timing out due to huge Posts table
- Solution: Pagination - fetch posts page by page instead of all at once
- Endpoint: GET /getPostsUploaded?page=1&per_page=10
- Uses SQL LIMIT and OFFSET for fast and efficient querying
- Returns total pages, has_next and has_previous in response
- Completely eliminates timeout issues on large datasets

---

## How to Run
- pip install -r requirements.txt
- py seed.py
- py -m uvicorn main:app --reload --port 8080
- Visit http://localhost:8080/docs to test all APIs
