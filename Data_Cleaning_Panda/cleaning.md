1. Why Data Cleaning Matters
- Ensures accuracy: Dirty data leads to misleading insights.
- Prepares for modeling: Machine learning algorithms require consistent, structured input.
- Saves time later: Clean data reduces debugging and preprocessing overhead.

2. Core Steps in Data Cleaning
- Handle Missing Values : 
Drop rows/columns, fill with mean/median/mode, or use interpolation.
"pandas.DataFrame.dropna(), fillna(), Simplelmputer"

- Remove Duplicates :
Identify and drop duplicate rows.
"pandas.DataFrame.duplicated(), drop_duplicated()"

- Fix Data Types : 
Convert strings to dates, numbers to categorical, etc.
"astype(), to_datetime()"

- Standardize Formats : 
Ensure consistent casing, spacing, units
"str.lower(),regex,custom functions"

- Detect Outliers : 
Use statistical methods (IQR, Z-score)
" NumPy, scipy.stats, visualization with matplotlib "

- Normalize/Scale Data : 
Standardize ranges for ML models
" StandardScaler, MinMaxScaler from sklearn "

