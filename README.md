# Job Postings Visualization

Data Wrangling and Visualization Bonus Assignment (Spring 2025)\
Contributor: Aleliya Turushkina DS-02

## Overview

This project provides interactive visualization of job market data, offering insights into salary distributions, required skills, and work formats across different professions. The dashboard allows users to filter data by profession and explore key trends in the job market.

## Repository Structure

The repository is organized as follows:

- data/ clean_categorized_vacancies.json — Processed job postings data
- templates/ index.html — Frontend part responsible for interactive visualization
- server.py — Flask backend server
- Dockerfile — Container configuration
- docker-compose.yml — Defines services for containerized deployment
- requirements.txt — Python dependencies

## Technologies Used

- Programming Languages: Python, JavaScript, CSS, HTML
- Visualization Libraries: D3js
- Web Frameworks: Flask
- Containerization: Docker

## Sample Visualizations

## Getting Started

To set up and run the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/Aleliya/JobPostingsVisualization.git
   ```

2. Navigate to the project directory:

   ```bash
   cd JobPostingsVisualization
   ```

3. Build and run the containers using Docker Compose:

   ```bash
   docker-compose up --build
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```
   to view the visualizations.

## Project Status

The project is currently under development.  
Future work:

- add geographical distribution map
- include more data sources
- improve usability
