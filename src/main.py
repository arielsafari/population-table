from pathlib import Path
from typing import Literal, Optional

import typer

from src.population_table import PopulationTable

app = typer.Typer()

WIKIPEDIA_PAGE_URL = (
    "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
)


@app.command()
def main(
    sort_by: Literal["asc", "desc"] = "desc",
    min_population: Optional[int] = None,
    output_html_file: Optional[Path] = typer.Option(None),
):
    population_table = PopulationTable(WIKIPEDIA_PAGE_URL).get_table()

    # Sort by population
    population_table.sort(key=lambda row: row.population, reverse=sort_by == "desc")

    for row in population_table:
        print(row)


if __name__ == "__main__":
    app()
