## Folder Structure (Backend + ML Focused)
```
smart-expense-categorizer/
│
├── app/                     # Backend (FastAPI later)
│   ├── main.py              # FastAPI app entry
│   ├── config.py            # env, settings
│   │
│   ├── api/                 # API routes
│   │   └── categorize.py
│   │
│   ├── services/            # Business logic
│   │   └── categorizer_service.py
│   │
│   ├── schemas/             # Request / response models
│   │   └── expense.py
│   │
│   └── utils/               # Helpers
│       └── logger.py
│
├── ml/                      # AI / ML logic (core)
│   ├── train.py             # Training script
│   ├── predict.py           # Load model + predict
│   ├── category_model.pkl   # Trained ML model
│   └── vectorizer.pkl       # TF-IDF vectorizer
│
├── data/                    # Dataset
│   └── expenses.csv
│
├── notebooks/               # Optional (experiments)
│   └── exploration.ipynb
│
├── tests/
│   └── test_prediction.py
│
├── README.md                
├── requirements.txt
└── .gitignore
```