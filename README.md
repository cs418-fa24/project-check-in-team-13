[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QOtgW9iu)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16397669&assignment_repo_type=AssignmentRepo)

# Stock Market Analysis 

This project presents a comprehensive analysis of stock performance across various sectors and indices, visualizes trends around significant events, and detects anomalies in stock volatility. The deliverables are the final report and a streamlit dashboard (see below). Completed during the UIC Fall '24 course CS 418 under Prof. Sathya Ravi. 

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Contributors](#contributors)
- [License](#license)

## Introduction

The Stock Market Analysis Dashboard is designed to provide insights into the performance of different sectors, including Defense, Tech, Healthcare, Energy, and major Indices. It allows users to visualize normalized stock prices, analyze correlations, and detect anomalies in stock volatility using machine learning techniques.

## Features

- **Sector Performance Visualization**: Compare normalized stock prices within a selected sector over a specified time period.
- **Correlation Heatmap**: Display the correlation matrix of stocks within a sector to understand interdependencies.
- **Volatility Analysis and Anomaly Detection**: Analyze stock volatility and detect anomalies using the Isolation Forest algorithm.

## Run Dashboard

View the Deployed dashboard [Here](https://dashboardfinalpy-dsproject.streamlit.app/)

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/cs418-fa24/project-check-in-team-13.git
   cd project-check-in-team-13
   
2. **Create a virtual environment (optional but recommended)**:
     python -m venv venv
     source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install the required dependencies**:
   pip install -r requirements.txt

4. Run DataScienceProject_FinalReport.ipynb for Report notebook
                 OR
   Run Dashboard_Final.py to open it on a localhosted streamlit dashboard

## Data

The project utilizes stock data fetched using the [yfinance](https://github.com/ranaroussi/yfinance) library. Users can specify the date range and sector of interest in the dashboard. The data is normalized to facilitate comparison across different stocks.

## Contributors

1. Prajwal Vishwanath - [ParzivalDV](https://github.com/ParzivalDV)
2. Apoorva Vutukur - [avutuUIC ](https://github.com/avutuUIC)
3. Devarshi Dhola - [DevarshiDhola07](https://github.com/DevarshiDhola07)
4. Sanjana Uppalike - [suppa17](https://github.com/suppa17)
5. Shriraksha B Srinivas - [sbyra](https://github.com/sbyra)
6. Varun P Srivathsa - [varunpuic](https://github.com/varunpuic)
