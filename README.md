# Data-science-project-TP4-
Monthly Sales Analysis (NumPy + Pandas + Matplotlib + Seaborn)

# Sales Analysis Project (2025)

## Overview
This project generates, analyzes, and visualizes monthly sales data for four products over one year (January–December 2025).  
The goal is to extract meaningful business insights using **NumPy, Pandas, and Matplotlib**.

The project produces:
- Raw generated dataset (`initial.csv`)
- Enhanced dataset with metrics (`final.csv`)
- Pivot tables, insights, and visualizations
- A complete Jupyter Notebook (`notebook.ipynb`)

---

## 1. Data Generation
The project begins by generating random monthly sales for four products:

| Product | Range (units) |
|--------|----------------|
| Product A | 50–100 |
| Product B | 30–80 |
| Product C | 20–60 |
| Product D | 10–50 |

Steps:
1. A function `generate_random_sales()` creates random integers within defined ranges.
2. `generate_initial_dataframe()` produces 12 months of data.
3. The output is stored as **`initial.csv`** with the following columns:
   - `Date`
   - `Product_A`
   - `Product_B`
   - `Product_C`
   - `Product_D`

---

## 2. Building the Final DataFrame
Using `initial.csv`, additional metrics are computed:

### Added Metrics
- **Total_Sales** → sum of all product sales per month  
- **Average_Sales** → mean of the 4 products  
- **Month_over_Month_Growth** → percentage change vs previous month  
- **Quarter** → Q1/Q2/Q3/Q4  
- **Max_Sales_Product**  
- **Min_Sales_Product**

All results are stored in **`final.csv`**.

---

## 3. Pivot Tables
Two pivot tables are generated:

### 1. Average sales per quarter (per product)
Saved as **`pivot_avg_per_quarter.csv`**

### 2. Total sales per quarter
Saved as **`pivot_total_per_quarter.csv`**

---

## 4. Key Insights
The analysis identifies:

- **Best Month** → highest total sales  
- **Best Product** → based on yearly cumulative sales  
- **Best Quarter** → strongest performance by total sales  

---

## 5. Visualizations
Several charts are created and saved in the `figures/` folder:

| Chart | Description |
|-------|-------------|
| `line_products.png` | Monthly line chart per product |
| `stacked_monthly.png` | Stacked bar chart of total monthly sales |
| `heatmap_products.png` | Heatmap of monthly sales intensity |
| `boxplot_products.png` | Yearly product distribution |

---

## 6. Files Included

### **/data/**
- `initial.csv`
- `final.csv`
- `output.csv`
- `pivot_avg_per_quarter.csv`
- `pivot_total_per_quarter.csv`

### **/figures/**
- All generated images

### Main Project Files
- `utils.py`
- `notebook.ipynb`

---

## 7. How to Run
1. Open `notebook.ipynb` with Jupyter Notebook.
2. Run all cells.
3. Results and graphics will appear inside `/data/` and `/figures/`.

---

## 8. Conclusion
This project provides complete sales data analysis with:
- Automatically generated dataset  
- Enhanced metrics  
- Pivot-based KPIs  
- Visual insights  
- Ready‑to‑use notebook  

It is ideal for learning, teaching, or business analysis modeling.

---

