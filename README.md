# Credit Card Fraud Detection

This project is a web-based application designed to detect fraudulent credit card transactions using a machine learning model. It features a Flask backend that serves an XGBoost-based classifier and a modern, responsive frontend for user interaction.

## 🚀 Features

- **Real-time Prediction:** Get instant feedback on whether a transaction is likely fraudulent.
- **Probability Scoring:** View the confidence level (probability) of the fraud detection.
- **Interactive UI:** A clean and intuitive form to input transaction details.
- **Preprocessing Pipeline:** Automatic scaling and encoding of input features.

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Machine Learning:** XGBoost, Scikit-learn, Pandas, Joblib
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Dataset:** Simulated credit card transaction data.

## 📁 Project Structure

```text
credit_card_fraudulent/
├── backend/
│   ├── app.py              # Flask Application
│   ├── model/
│   │   ├── xgb_model.pkl    # Trained XGBoost Model
│   │   ├── scaler.pkl       # Feature Scaler
│   │   └── selected_features.pkl
│   └── notebook/           # Model development (optional)
├── frontend/
│   ├── static/             # CSS and JS files
│   └── templates/          # HTML templates
├── dataset/
│   └── fraudTest.csv       # Dataset used for testing/training
└── requirements.txt        # Python dependencies
```

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd credit_card_fraudulent
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃 Usage

1. **Navigate to the backend directory (or run from root):**
   ```bash
   python backend/app.py
   ```

2. **Open your browser:**
   Go to `http://127.0.0.1:5000`

3. **Input transaction details:**
   Fill in the form with transaction data (Merchant ID, Amount, Category, etc.) and click **Predict Transaction**.

## 📊 Model Information

The model is built using **XGBoost**, an optimized gradient boosting library. It was trained on features including transaction amount, category, location (latitude/longitude), and time-based features (Unix timestamp). Data preprocessing involves scaling numerical values and encoding categorical variables.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- The dataset is based on simulated credit card transactions.
- Inspired by fraud detection research and open-source ML projects.
