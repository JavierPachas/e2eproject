# End-to-End ML Project: Student Exam Performance

Predict student math scores from demographic and academic inputs using a trained model and a simple Flask web UI.

## What is in this repository
- A Flask app that serves a prediction form and result page.
- A trained model and preprocessor in `artifacts/` used for inference.
- Modular pipeline code in `src/` for data processing and prediction.
- Notebooks for EDA and model training in `notebook/`.

## Project structure
- `application.py` - Flask app entry point (default port 5000).
- `app.py` - Flask app entry point with debug on port 8000.
- `templates/` - HTML templates for the UI.
- `src/` - Pipeline, components, utilities, and exception handling.
- `artifacts/` - Model, preprocessor, and sample datasets.
- `notebook/` - EDA and training notebooks.

## Quickstart
1. Create and activate a virtual environment (optional).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the web app:
   ```bash
   python application.py
   ```
   Then open `http://localhost:5000` in your browser.

If you prefer debug mode and port 8000:
```bash
python app.py
```

## Prediction inputs
The app expects the following fields:
- Gender
- Race or ethnicity
- Parental level of education
- Lunch type
- Test preparation course
- Reading score (0-100)
- Writing score (0-100)

## Notes
- Prediction uses `artifacts/model.pkl` and `artifacts/preprocessor.pkl` via `src/pipeline/predict_pipeline.py`.
- If you retrain or replace artifacts, keep the filenames the same or update the pipeline accordingly.

## Notebooks
The notebooks in `notebook/` cover exploratory data analysis and model training. They can be used to reproduce or refine the model.


https://github.com/JavierPachas/e2eproject/blob/main/img/home.png