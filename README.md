# 🎬 Movie Recommender System

This is a **content-based movie recommender system** built using **Python, Pandas, and Streamlit**. It suggests similar movies based on user selection and fetches movie posters from the TMDB API.

## 🚀 Features
- 📌 Recommends similar movies using cosine similarity
- 🖼️ Fetches movie posters from the TMDB API
- 🎭 Supports multiple genres
- 📊 Uses preprocessed datasets for fast recommendations

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ahsananwar102/content-based-movie-recommender.git
cd content-based-movie-recommender
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Key for TMDB
Create a `.streamlit/secrets.toml` file and add your API key:
```toml
API_KEY = "your_tmdb_api_key_here"
```

### 5️⃣ Run the App
```bash
streamlit run app.py
```

## 🔗 Deployment on Streamlit Cloud
1. Push your project to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository and deploy the app.
4. Add the TMDB API key to **Secrets Management** in Streamlit settings.

## 🏗️ Technologies Used
- **Python** 🐍
- **Pandas** 📊
- **NumPy** 🔢
- **Scikit-learn** 🤖
- **Streamlit** ⚡
- **TMDB API** 🎥

## 🤝 Contributing
Pull requests are welcome! If you find a bug or have a feature request, open an issue.

