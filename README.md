## Recreate charts locally
```bash
pip install -r requirements.txt
python scripts/quick_analysis.py
```

## Push to GitHub
1. Create a new repo on GitHub (no README).
2. Run the following in your terminal **inside this folder**:
```bash
git init
git add .
git commit -m "Initial commit: AI Sales Analysis Project"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## Data dictionary
- `Transaction ID` (int): Unique transaction key
- `Date_x` (date): Original dataset date
- `Customer ID` (str): Customer code
- `Gender` (str): Male/Female
- `Age` (int): Age in years
- `Product Category` (str): Beauty/Clothing/Electronics
- `Quantity` (int): Units bought
- `Price per Unit` (int): Unit price
- `Total Amount` (int): Quantity × Price per Unit
- `Date_y` (datetime): Timestamp from the new dataset
- `Product` (str): Specific product label
- `Sales_Amount` (int): Revenue amount from the new dataset

## Notes
- Master join key: `Transaction ID`
- Dates with suffix `_x` and `_y` come from original vs new dataset respectively.

AUTHOR:
Jagdesh Kumar S
contact me : https://github.com/Jagdesh007.
