# Hotel Localization

This repository contains my completed project for the D387 Advanced Java course at Western Governors University.
In this project, I enhanced an existing hotel management application built with Spring Boot (backend) and Angular (frontend) by adding key enterprise features like internationalization (i18n), multithreading, time zone conversion, and containerization with Docker. The purpose of the project is to simulate real-world software engineering practices where global user needs, time differences, and scalable deployments must be addressed. Through completing this project, students gain hands-on experience with resource bundles for localization, thread management for concurrent operations, ZonedDateTime classes for accurate time zone handling, currency formatting for different markets, and Docker for cloud-ready deployment. It also strengthens skills in version control with Git, backend RESTful service development, frontend UI modifications, and understanding how modern applications are deployed in cloud environments like Azure.

## Completed Tasks

### Task A – Project Setup

- Cloned the starter repository from WGU GitLab.
- Set up `working_branch` using Git in IntelliJ IDEA Ultimate.
- Verified backend and frontend startup processes.
- Followed required commit and push milestones after each major task.

## Task B – Application Modifications

### B1 – Multithreaded Welcome Message

- Created two resource bundle files:
  - `translation_en_US.properties`
  - `translation_fr_CA.properties`
- Populated each file with a welcome message in English and French.
- Built `MultilingualGreeter.java` to load each message in a separate thread.
- Used `GreetingController.java` to expose messages via the `/welcome` endpoint.

**Sample Output:**
```
Welcome to the Landon Hotel.
Bienvenue a l’hotel Landon.
```

### B2 – Currency Display on Frontend

- Modified `app.component.ts` and `app.component.html` in the Angular frontend.
- Displayed room prices in:
  - U.S. Dollars (USD)
  - Canadian Dollars (CAD)
  - Euros (EUR)
- Each price appears on a separate line for clarity.
- Prices are calculated using static conversion rates.

### B3 – Time Zone Conversion

- Created `TimeConversionService.java` using `ZonedDateTime`.
- Converted a hardcoded event time from **ET** to **MT** and **UTC**.
- Built `TimeController.java` to expose results via `/presentation`.

**Sample Output:**
```json
{
  "ET": "18:00",
  "MT": "16:00",
  "UTC": "22:00"
}
```

## Task C – Docker and Cloud

### C1 – Dockerfile Creation

- Created a `Dockerfile` in the root directory.
- Used `openjdk:17-jdk-slim` as the base image.
- Packaged the Spring Boot app into a `.jar` and copied it into the image.
- Exposed port 8080.

**Build Command:**
```bash
docker build -t d387-app .
```

### C2 – Run Container

- Ran the image in a container named with student ID:
```bash
docker run -d -p 8080:8080 --name D387_studentID d387-app
```

- Verified container was running via `docker ps`.
- Confirmed both `/welcome` and `/presentation` endpoints worked in the container.
- Accessed the frontend via `http://localhost:4200`.

### C3 – Cloud Deployment Description

Deployment plan using **Microsoft Azure**:

- Uploaded Docker image to Docker Hub.
- Created a **Resource Group** and **Web App for Containers** on Azure.
- Configured the web app to pull and run the image.
- Exposed port 8080 to allow public access.
