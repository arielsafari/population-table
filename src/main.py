from pathlib import Path
from typing import Optional

import typer

from src.population_table import PopulationTable

app = typer.Typer()

WIKIPEDIA_PAGE_URL = (
    "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
)


@app.command()
def main(
    min_population: Optional[int] = None,
    output_html_file: Optional[Path] = typer.Option(None),
):
    population_table = PopulationTable(WIKIPEDIA_PAGE_URL).get_table()

    # TODO: Sort by population

    # TODO: Output to stdout
    pass


if __name__ == "__main__":
    app()
