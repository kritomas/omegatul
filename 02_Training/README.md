# Training

Trainer for the ML model.

# Installation

Install dependencies: `python3`

Install Python libraries: `pandas`, `scikit-learn`

# Usage

First, place the whole SQLite3 DB created by the crawler inside `data`.

Then run `python3 main.py`. The trainer will use the whole CPU (if possible). The resulting models will be pickled and placed inside `models`.