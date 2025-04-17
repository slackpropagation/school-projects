# Axecellent Guitars

This project was completed as part of the WGU D287 course: *Java Frameworks*. The Performance Assessment (PA) focuses on customizing a Spring Boot Java application with an HTML frontend to meet business requirements, demonstrating real-world development and version control skills.

---

## Project Task C

**Prompt:** Customize the HTML user interface for your customer’s application. The user interface should include the shop name, the product names, and the names of the product parts.

**File Name:** mainscreen.html  
**Line Number:** 14, 19, 21, 53  
**Description of change:**  
- Line 14: Changed the title from “My Bicycle Shop” to “Axecellent Guitars”.  
- Line 19: Updated the heading to “Axecellent Guitars Inventory”.  
- Line 21: Changed the section title from “Parts” to “Guitar Parts”.  
- Line 53: Changed the section title from “Products” to “Custom Guitars”.

---

## Project Task D

**Prompt:** Add an “About” page to the application to describe your chosen customer’s company to web viewers and include navigation to and from the “About” page and the main screen.

**File Name:** about.html  
**Line Number:** All  
**Description of change:**  
- Created a dark mode styled About page using Bootstrap and linear-gradient background.
- Included company description, tonewood details, finishes, and pickup sections.
- Added a “Return Home” button linking back to the mainscreen.

**File Name:** mainscreen.html  
**Line Number:** 13, 16  
**Description of change:**  
- Line 13: Added custom dark mode styling using inline style with a modern font, dark background, and themed Bootstrap overrides.  
- Line 16: Added an “About” button linking to the About page using th:href="@{/about}" and styled it with a Bootstrap info button.

**File Name:** AboutController.java
**Line Number:** All  
**Description of change:**  
- Created controller class to handle GET request for /about route and return the about.html view.

---

## Project Task E

**Prompt:** Add a sample inventory appropriate for your chosen store to the application. You should have five parts and five products in your sample inventory and should not overwrite existing data in the database.

**File Name:** BootStrapData.java  
**Line Number:** All  
**Description of change:**
- Created five InhousePart objects: Roasted Maple Neck, Locking Tuners, CTS 500k Pots, 3-Way Toggle Switch, and Strap Locks.
- Created five OutsourcedPart objects: Vintage Cloth Wiring, GraphTech Nut, Custom Knurled Knobs, Gold Pickup Covers, and Nickel Tremolo Bridge.
- Added logic to insert these into the repository only if partRepository.count() is 0.
- Used helper methods createInhousePart() and createOutsourcedPart() to streamline object creation and reduce repetitive code.

---

## Project Task F

**Prompt:** Add a “Buy Now” button to your product list.  
- The “Buy Now” button must be next to the buttons that update and delete products.  
- The button should decrement the inventory of that product by one. It should not affect the inventory of any of the associated parts.  
- Display a message that indicates the success or failure of a purchase.

**File Name:** mainscreen.html  
**Line Number:** 152-153  
**Description of change:**
- Added a “Buy Now!” button next to the Update and Delete buttons in the product list.
- Made sure it links to /buyProduct and passes the productId.

**File Name:** BuyProductController.java  
**Line Number:** All  
**Description of change:**
- Created a new controller to handle /buyProduct requests.
- Checks if product exists and if inventory is greater than 0.
- If available, decrements inventory and returns purchaseSuccessful.html.
- If not, returns outOfStock.html.

**File Name:** purchaseSuccessful.html  
**Line Number:** All  
**Description of change:**
- Created a confirmation page to let the user know the purchase succeeded.
- Includes a button to return to the main screen.

**File Name:** outOfStock.html  
**Line Number:** All  
**Description of change:**
- Created a page that displays when the selected product is out of stock.
- Includes a button to return to the main screen.


---

## Project Task G

**Prompt:** Modify the parts to track maximum and minimum inventory.  
- Add additional fields to the part entity for maximum and minimum inventory.
- Modify the sample inventory to include the maximum and minimum fields.
- Add to the InhousePartForm and OutsourcedPartForm forms additional text inputs for the inventory so the user can set the maximum and minimum values.
- Rename the file the persistent storage is saved to.
- Modify the code to enforce that the inventory is between or at the minimum and maximum value.

**File Name:** Part.java  
**Line Number:** 114-116, 29-33
**Description of change:**  

- Lines 114-116: Added isInventoryValid() method to verify inventory is between minInventory and maxInventory.
- Lines 29-33: Added validation annotations to minInventory and maxInventory.

**File Name:** InhousePartForm.html  
**Line Number:** 24-25
**Description of change:**
- Added two new input fields: minInventory and maxInventory.

**File Name:** OutsourcedPartForm.html
**Line Number:** 25-26
**Description of change:**
- Added two new input fields: minInventory and maxInventory.

**File Name:** application.properties
**Line Number:** 6
**Description of change:**
- Renamed the database file to AxecellentInventoryDB.

**File Name:** AddInhousePartController.java
**Line Number:** 42-44
**Description of change:**
- Added a condition that checks part.isInventoryValid() and rejects the value with an error message if false.

**File Name:** AddOutsourcedPartController.java
**Line Number:** 43-45
**Description of change:**
- Added a condition that checks part.isInventoryValid() and rejects the value with an error message if false.

---

## Project Task H

**Prompt:** Add validation for between or at the maximum and minimum fields.  
- Display error messages for low inventory when adding and updating parts if the inventory exceeds the minimum number of parts.  
- Display error messages for low inventory when adding and updating products lowers the part inventory below the minimum.  
- Display error messages when adding and updating parts if the inventory exceeds the maximum.

**File Name:** AddInhousePartController.java  
**Line Number:** 38-62  
**Description of change:**
- Added validation logic using isInventoryValid() before saving the part. Rejected form submission with error if inventory was outside allowed range.  

**File Name:** AddOutsourcedPartController.java  
**Line Number:** 39-54  
**Description of change:**
- Added validation logic using isInventoryValid() before saving the outsourced part. Rejected invalid values using rejectValue().

**File Name:** EnufPartsValidator.java  
**Line Number:** 26-42  
**Description of change:**
- Updated validator to reject product inventory updates if any associated part’s inventory would fall below its minimum threshold.

---

## Project Task I

**Prompt:** Add at least two unit tests for the maximum and minimum fields to the PartTest class in the test package.

**File Name:** PartTest.java  
**Line Number:** 159-183  
**Description of change:**
- Added testInventoryValidReturnsTrueWhenWithinRange() to confirm that isInventoryValid() returns true when inventory is between min and max.
- Added testInventoryValidReturnsFalseWhenOutsideRange() to confirm that isInventoryValid() returns false when inventory is outside of allowed range.

---

## Project Task J

**Prompt:** Remove the class files for unused validators to clean your code.

**File Name:** DeletePartValidator.java
**Line Number:** Entire file
**Description of change:** Removed unused and redundant validator. Validation is already handled by ValidDeletePart.

---

## Bug Fixes

**Task E – Sample Inventory Fix:** Initially, only sample parts were being populated, which led to an “Approaching Competence” evaluation. Fixed by adding five realistic Product entries using ProductRepository inside the BootStrapData class. Ensured products are only created if the database is empty to avoid overwriting existing data.

**Task F – Buy Now Button Error:** Clicking the “Buy Now” button resulted in a 400 Bad Request (Whitelabel Error) due to a mismatch between the request parameter name in the HTML (productId) and the controller (productID). Fixed by updating the controller method to accept @RequestParam("productId") and properly returning the purchase confirmation view.