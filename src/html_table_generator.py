from pathlib import Path

from bs4 import BeautifulSoup, Tag

from src.population_table import PopulationTableRow


class HTMLTableGenerator:
    def __init__(self, file_name: Path) -> None:
        self._file_name = file_name

    def _store_html_to_file(self, content: str) -> None:
        with open(self._file_name, "w") as html_file:
            html_file.write(content)

    def _generate_row(
        self, soup: BeautifulSoup, population_row: PopulationTableRow
    ) -> Tag:
        tr = soup.new_tag("tr")

        td = soup.new_tag("td")
        td.string = str(population_row.country_name)
        tr.append(td)

        td = soup.new_tag("td")
        td.string = str(population_row.population)
        tr.append(td)

        td = soup.new_tag("td")
        td.string = str(population_row.date_of_data.strftime("%Y-%m-%d"))
        tr.append(td)

        return tr

    def _generate_header(self, soup: BeautifulSoup) -> Tag:
        columns_names = ["Country Name", "Population", "Date Of Data"]

        header_row = soup.new_tag("tr")
        for header_text in columns_names:
            th = soup.new_tag("th")
            th.string = header_text
            header_row.append(th)

        return header_row

    def generate_table(self, population_table: list[PopulationTableRow]) -> None:
        soup = BeautifulSoup("", "html.parser")
        table = soup.new_tag("table")

        table.append(self._generate_header(soup))

        for row_data in population_table:
            table.append(self._generate_row(soup, row_data))

        soup.append(table)

        self._store_html_to_file(soup.prettify())
