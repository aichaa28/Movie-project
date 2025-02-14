# Movie Review Sentiment Analysis

This project demonstrates how to extract, clean, analyze, and model movie reviews from websites such as Letterboxd and Rotten Tomatoes. Each step of the process, including code and explanation, is detailed below.

## Project Structure

- `Movie_critics_report.pdf` : a detailed report of each step of the project
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

## Tested Models

Different models have been evaluated in the `try/` folder. Each notebook contains an implementation and performance evaluation.



