# Python_ETL_Daily

A daily hands-on Python practice repository focused on building practical **Data Engineering and ETL skills**.

## Why This Repository?

I created this repository to strengthen my Python problem-solving and ETL skills through consistent practice.

The idea is to start with simple data-processing tasks and gradually increase the complexity by introducing new data sources, transformations, validation, and eventually real Data Engineering tools.

Each day builds on the previous work instead of starting a completely separate exercise.

The goal is to become comfortable with the complete process of:

**Extract → Transform → Validate → Analyze → Load**

---

## Daily Progress

### Day 1 — Basic CSV ETL

Started with an orders CSV file.

**Data flow:**

```text
CSV
 ↓
Read records
 ↓
Validate data
 ↓
Calculate total amount
 ↓
Filter completed orders
 ↓
Calculate metrics
 ↓
Export cleaned CSV
```

Introduced basic validation, transformations, aggregations, and CSV output.

---

### Day 2 — Data Enrichment

Added customer information from a JSON file.

**Data flow:**

```text
Orders CSV
     ↓
Validation & transformation
     ↓
Customer JSON
     ↓
Customer lookup
     ↓
Enriched orders
     ↓
CSV
```

The pipeline now combines data from two sources and enriches the original records.

---

### Day 3 — Additional Transformation

Added product discount information from another JSON source.

**Data flow:**

```text
Orders CSV
     ↓
Validation
     ↓
Customer enrichment
     ↓
Product discount lookup
     ↓
Discounted prices
     ↓
Final CSV
```

The pipeline now performs multiple transformations and enrichments before producing the final dataset.

---

## Overall Pipeline

The project is gradually evolving from a simple CSV script into a more complete ETL pipeline:

```text
                ┌──────────────┐
                │   Orders CSV │
                └──────┬───────┘
                       ↓
                Data Validation
                       ↓
                Transformations
                       ↓
              ┌────────┴────────┐
              ↓                 ↓
       Customer JSON      Product JSON
              ↓                 ↓
       Customer Lookup    Discount Lookup
              └────────┬────────┘
                       ↓
                Enriched Data
                       ↓
                Final CSV
```

Future days will gradually replace these simplified local data sources with more realistic Data Engineering components such as APIs, databases, larger datasets, and pipeline tools.

---

## Technologies

Currently:

- Python
- CSV
- JSON
- Git
- GitHub

Planned additions include:

- REST APIs
- Postgre
