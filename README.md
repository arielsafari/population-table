# Population Table

Display list of countries and territories by total population all around the world.

## What this project is about?

The project is based on the Wikipedia page [List of countries and dependencies by population](https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population).

With the following features:

1. Parsing the table on the page and extracting for each country:
   - Country name
   - Population
   - Date of data (as listed in the table)
2. Output the results sorted by population in descending order (if a country appears more than once, list all occurrences)
3. Output the results to an HTML file with a table format.
4. Add an option to filter results by a minimum population threshold.

## How to run locally?

### Requirements

- Python 3.8+
- `virtualenv` or `venv`

---

### Installation

1. **Clone the repository**:

```bash
git clone https://github.com/arielsafari/population-table.git
cd population-table
```

2. **Create and activate a virtual environment**:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

---

### Usage

Run the `main.py` file:

```bash
python -m src.main
```

To sort the file, use the flag `--sort-by` (asc|desc):

```bash
python -m src.main --sort-by asc
```

To set a minimum limit of population, use the flag `--min-population`:

```bash
python -m src.main --min-population 500
```

To output the table into a HTML file, use the flag `--output-html-file`:

```bash
python -m src.main --output-html-file "population_data.html"
```
