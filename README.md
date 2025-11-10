# Car Data Lab

### Explanation Lab

This project was developed as part of a university assignment in Data Mining and Performance Analysis with Docker.

The goal is to demonstrate how data from an Excel file can be transformed into useful information stored in MySQL, visualized with Grafana, and monitored with Prometheus and cAdvisor within a fully containerized environment.

---

This project is a small **Data Mining & Monitoring Lab** built using **Python**, **MySQL**, **Grafana**, and **Prometheus** — all running inside Docker containers.

It demonstrates how to:
- Extract and clean data from an Excel file using Python.
- Store the dataset in a MySQL database running in Docker.
- Visualize analytics and performance dashboards with Grafana.
- Monitor container resource usage (CPU, RAM, disk, I/O) using Prometheus and cAdvisor.

---

## Architecture

```text
Excel (carros_v2-2.xlsx)
        │
        ▼
Python (pandas + SQLAlchemy)
        │
        ▼
MySQL (Docker)  ─────────────┐
        │                    │
        ▼                    ▼
Grafana (Docker)        Prometheus + cAdvisor (Docker)
        │                    │
        └──────────── Real-time metrics

## **Technologies Used**
 - Python 3.12+
 - Pandas, SQLAlchemy, PyMySQL, OpenPyXL
 - MySQL 8 (Docker)
 - Grafana
 - Prometheus
 - cAdvisor
 - Docker Compose
#########

## Data Loading Process

- Run the Python script to upload the Excel data to MySQL:
- python script.py


##This process:

- Reads the Excel sheet into a Pandas DataFrame.
- Detects and classifies data types per column.
- Loads the dataset into MySQL as a table named carros_v2.
- Optionally exports a metadata table containing column data types.

To verify the upload:

- mysql -h 127.0.0.1 -P 3307 -u root -p

Then:

USE carros_db;
SHOW TABLES;
SELECT COUNT(*) FROM carros_v2;

## Data Mining Process.

- The project follows the phases of the Knowledge Discovery in Databases (KDD) process:
- Data selection: a dataset of automobiles with 9 variables is used.
- Preprocessing: cleaning and classifying data types using Pandas.
- Transformation: converting the Excel file into an SQL structure.
- Data mining: statistical analysis and exploration using Grafana.
- Evaluation and visualization: observing results and environment performance using Prometheus and cAdvisor.
- This workflow allows for the integration of real-world tools from the Data Engineering ecosystem with theoretical data mining concepts.

## Example Queries
SQL Example (Grafana or MySQL)
SELECT Marca, AVG(Precio) AS avg_price
FROM carros_v2
GROUP BY Marca
ORDER BY avg_price DESC;

Prometheus Query Example
rate(container_cpu_usage_seconds_total{name=~".*mysql-carros.*"}[1m])

## Example Dashboard Ideas

 - Panel 1: Average car price per brand (from MySQL data).
 - Panel 2: Container CPU and memory usage (from Prometheus).
 - Panel 3: Query execution performance trend over time.

## Each dashboard combines business-level data with real-time system performance.

 ## Project Structure
carros-lab/
├─ script.py
├─ carros_v2-2.xlsx
├─ docker-compose.yml
├─ prometheus/
│  └─ prometheus.yml
├─ README.md
└─ .gitignore

## Author

Arturo Esteva Castillo
- Englewood, Colorado, USA
- Master’s Student – Big Data & Data Science
- Year 2025
- Focus areas: Data Engineering, Cloud, and Network Automation.

## Future Improvements

- Integration with AWS RDS or Amazon QuickSight.
- Alert rules and anomaly detection using Prometheus Alertmanager.
- Automation pipeline via Apache Airflow or Prefect.
- Add Docker health metrics dashboards inside Grafana.

