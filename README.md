# Movie Review Sentiment Analysis

This project demonstrates how to extract, clean, analyze, and model movie reviews from websites such as Letterboxd and Rotten Tomatoes. Each step of the process, including code and explanation, is detailed below.

## Project Structure

- `try/` : Contains different models tested with their associated notebooks.
- `EDA-notebook.ipynb` : Exploratory Data Analysis (EDA).
- `Final-model.ipynb` : Notebook for the final selected model.
- `cleaning.ipynb` : Data preprocessing and cleaning steps.
- `dataset-final-3000.csv` : Final dataset used for training.
- `extraction-letterbox.ipynb` : Extraction of movie reviews from Letterboxd.
- `extraction-rotten-tomato.ipynb` : Extraction of movie reviews from Rotten Tomatoes.
- `rotten_letter.csv` : Combined dataset of reviews from Letterboxd and Rotten Tomatoes.
- `requirements.txt` : List of dependencies required to run the project.
- `streamlit.py` : Streamlit interface to interact with the model and visualize results.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/aichaa28/movie-review-analysis.git
   cd movie-review-analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit interface:
   ```bash
   streamlit run streamlit.py
   ```

## Natural Language Processing (NLP) Approach

This project heavily relies on NLP techniques to preprocess and analyze movie reviews. The following steps were implemented:

- **Tokenization**: Using `nltk.word_tokenize()` to split text into individual words.
- **Stopword Removal**: Filtering out common words using `nltk.corpus.stopwords`.
- **Lemmatization**: Reducing words to their base form with `WordNetLemmatizer`.
- **TF-IDF Vectorization**: Converting text into numerical representations using `TfidfVectorizer` from `sklearn.feature_extraction.text`.
- **Sentiment Prediction**: Training some models on processed textual data to predict sentiment scores.

## Tested Models

Different models have been evaluated in the `try/` folder. Each notebook contains an implementation and performance evaluation.



