# Cryptocurrency Liquidity Prediction for Market Stability ML Project

## Problem statement

Cryptocurrency markets are highly volatile, and liquidity plays a crucial role in market stability. Liquidity refers to
the ease with which assets can be bought or sold without significantly impacting the price. A lack of liquidity
can lead to increased price fluctuations and market instability.


In this project, you are required to build a machine learning model to predict cryptocurrency liquidity levels
based on various market factors such as trading volume, transaction patterns, exchange listings, and social
media activity. The objective is to detect liquidity crises early to help traders and exchange platforms
manage risks effectively.


Your final model should provide insights into market stability by forecasting liquidity variations, allowing
traders and financial institutions to make informed decisions.

## Solution Proposed

Now the question is how to dynamically predict the cluster of the Cryptocurrency Liquidity ?. One of the approaches which we can use of machine learning approach, where we can cluster the Cryptocurrency Liquidity based on the details we have and predict the cluster type based on the domain knowledge and leverage previous Cryptocurrency Liquidity data to predict the cluster.

## Dataset Information
You will use a dataset that includes historical cryptocurrency price and trading volume data from below link.     
The dataset consists of records from 2016 and 2017  

Dataset used
 <html>
<a href="https://drive.google.com/drive/folders/10BRgPip2Zj_56is3DilJCowjfyT6E9AM"> Dataset Link</a>
</html>

## Tech Stack Used

1. Python
2. FastAPI
3. Machine learning algorithms
4. MongoDB

# 📊 Final Report: Cryptocurrency Liquidity Prediction Web Application

This notebook documents the process and key features of the **Cryptocurrency Liquidity Prediction Web Application** built with **FastAPI** and **XGBoost**. The app integrates real-time cryptocurrency data submission, machine learning-based prediction of liquidity clusters, and user-friendly data visualization.

---

## 1️⃣ Project Overview

The **Cryptocurrency Liquidity Prediction Web App** is a FastAPI-powered application that allows users to submit cryptocurrency market data and predict liquidity cluster classifications based on a trained machine learning model. The goal of the project is to predict liquidity risks for cryptocurrencies based on historical market data and real-time statistics.

### Key Features:
- Real-time data submission via a web form.
- Storage of market data in MongoDB.
- Training an **XGBoost model** for classification of liquidity clusters.
- Prediction of liquidity classification based on real-time user input.
- Prediction results rendered on an interactive webpage.

---

## 2️⃣ System Design

### Backend Architecture
- **FastAPI:** Used for creating RESTful APIs that handle form submissions and predictions.
- **XGBoost Classifier:** The machine learning model used to classify liquidity risk based on various market metrics.
- **MongoDB:** NoSQL database used to store user-submitted cryptocurrency data.
- **joblib:** For saving and loading the trained model and scaler.

---

## 3️⃣ Data Flow

1. **Data Submission:**
   - The user submits cryptocurrency market data (e.g., price, market cap, trading volume, etc.) through a form on the `/` route.
   - The form data is stored in MongoDB via the `/submit` route.

2. **Model Training:**
   - The `/train_model` route reads historical clustered data from a CSV, scales the features, and trains an XGBoost model.
   - The trained model and scaler are saved using `joblib`.

3. **Prediction:**
   - On the `/predict` route, users submit new cryptocurrency data (similar to the training data format).
   - The features are scaled using the saved scaler, and the trained model predicts the liquidity cluster.

4. **Prediction Results:**
   - The predicted cluster is returned and rendered with input details in a user-friendly HTML template.

---

