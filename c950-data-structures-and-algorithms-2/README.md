# Routing Program

This repository contains my completed performance assessment project for the **DSA2 - Data Structures and Algorithms II** course.

This project simulates a real-world delivery routing problem for the Parcel Service. The objective was to design and implement an optimized delivery system that ensures 40 packages are delivered efficiently across 3 trucks while handling address corrections, strict delivery deadlines, and total mileage constraints (under 140 miles). 

Through this project, students learn essential concepts of **algorithm design**, **greedy strategies**, **data structures** (such as hash tables), and **time simulation techniques**. It serves as a practical application of abstract algorithm theory into tangible problem-solving, emphasizing how efficient data lookup and routing can significantly impact logistical operations. Completing this project builds skills critical for fields like software development, operations research, and logistics optimization.

## Project Summary

- Developed a **Greedy Nearest Neighbor Algorithm** to plan truck delivery routes.
- Built a **custom Hash Table** class from scratch for constant-time package retrieval.
- Simulated **time-based delivery tracking** and dynamic status updates.
- Manually assigned packages across trucks while considering:
  - Tight delivery deadlines
  - Mid-day address corrections (e.g., Package 9's wrong address until 10:20 AM)
  - Special group delivery instructions and notes
- Achieved a total mileage **below 140 miles**, meeting project specifications.
- Passed all checkpoint validations for delivery statuses at 9:00 AM, 10:30 AM, and 12:30 PM.

## Key Components

- **`main.py`**: Orchestrates the loading of data, delivery simulation, and user CLI interface.
- **`package.py`**: Defines the `Package` class, responsible for storing delivery details and handling address corrections.
- **`truck.py`**: Defines the `Truck` class, managing truck properties like departure time, mileage, and inventory.
- **`hash_table.py`**: Implements a custom-built chaining **Hash Table** for fast and efficient package lookup.
- **`/data/` folder**: Includes CSV files containing addresses, distances, and package information.
- **`/screenshots/` folder**: Contains screenshots proving delivery statuses and final mileage for milestone verification.

## Algorithms Used

- **Greedy Nearest Neighbor Algorithm**
  - Chooses the next closest package at each step to minimize travel distance.
  - Provides a simple but effective heuristic for small to medium-sized delivery problems.
  
- **Potential Improvements (for scalability)**
  - **Dijkstra's Algorithm**: For true shortest-path optimization in larger or weighted graphs.
  - **A* Search Algorithm**: For combining greedy and optimal pathfinding approaches using heuristics.

## Task Requirements Covered

- Dynamically updates delivery statuses based on user-specified time input.
- Accurately tracks and sums truck mileage individually and collectively.
- Corrects Package 9's address at exactly 10:20 AM within the simulation.
- Meets all delivery deadlines specified in the project description.

## What I Learned

- How to apply **greedy algorithms** for route optimization.
- Building and testing **custom data structures** like hash tables for real-time lookups.
- Simulating **time-sensitive operations** and dynamic system behavior.
- Combining **manual truck loading** strategies with automated optimization.
- Understanding how small improvements in algorithm design can have large impacts on system performance.
- Strengthening skills in Python development, object-oriented design, and problem decomposition.
