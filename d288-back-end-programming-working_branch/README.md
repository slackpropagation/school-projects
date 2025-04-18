# Back End Application Programming

This folder contains my completed project for the **D288 Back-End Programming** course at Western Governors University.  
The project focuses on Spring Boot application development, REST APIs, MySQL database integration, and Docker deployment.

## Completed Tasks

### Task A: Set Up Project Environment

- Cloned project repository and verified all dependencies.
- Confirmed that the Spring Boot application runs locally.

### Task B: Database Configuration

- Verified connection to MySQL database.
- Used `create_and_populate_db.sql` to recreate the schema and populate it with sample data.

### Task C: Entity Mapping

- Created JPA entity classes for:
  - Country
  - Division
  - Customer
  - Cart
  - CartItem
- Mapped all relationships using appropriate annotations:
  - `@ManyToOne`, `@OneToMany`, `@JoinColumn`, etc.
- Ensured all column names matched the MySQL schema exactly.
- Used `@JsonProperty` to align DTO fields with entity fields.

### Task D: Country and Division Endpoint

- Implemented REST endpoint to fetch divisions by country.
- Fixed frontend dropdown issue by ensuring `@JoinColumn(name = "country_id")` matched MySQL column naming.

### Task E: Add Customer Endpoint

- Built logic to add new customers from the Angular frontend to the database.
- Verified proper saving of country and division relationships.

### Task F: Checkout Flow

- Created `CheckoutServiceImpl.java` to handle:
  - Cart creation and customer association.
  - UUID generation for `orderTrackingNumber`.
  - Cart status set to `ORDERED`.
  - Return of purchase response with tracking number.
- Added validation: returns “Cart is empty” if no items present during checkout.

### Task G: Purchase Validation

- Handled edge case where cart is empty:
  - Returned user-friendly message instead of tracking number.
- Updated `PurchaseResponse.java` to support custom error messages.

### Task H: Bootstrapping Sample Customers

- Created `BootStrapData.java` to populate up to 5 sample customers when database is empty.
- Used existing Division entities to avoid foreign key violations.
- Used `customer.addCart(cart)` to establish bidirectional relationship.

## Bug Fixes

- **Customer data not showing on frontend**: Resolved by properly initializing data and verifying DB state.
- **Empty country dropdown**: Fixed by correcting `@JoinColumn` to match actual DB column.
- **Order tracking number missing**: Added `@JsonProperty` to `PurchaseResponse` to ensure proper serialization.
- **"Cart is empty" message not appearing**: Refactored `CheckoutServiceImpl` to check for empty cart items.
- **Unable to delete customers due to FK constraints**: Rebuilt DB using the provided SQL script to reset to a clean state.
