from datetime import datetime
from typing import List

import requests
from bs4 import BeautifulSoup, Tag
from pydantic import BaseModel


class PopulationTableRow(BaseModel):
    country_name: str
    population: int
    date_of_data: datetime


class PopulationTable:
    def __init__(
        self,
        wikipedia_page_url: str,
    ) -> None:
        self.wikipedia_page_url = wikipedia_page_url
        self.sample_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

    def _fetch_page_html(self):
        wikipedia_page = requests.get(
            self.wikipedia_page_url, headers={"User-Agent": self.sample_user_agent}
        )
        return wikipedia_page.text

    @staticmethod
    def _find_table_in_html(page_html: str):
        soup = BeautifulSoup(page_html, "html.parser")

        table_caption = soup.find(
            "caption", text="List of countries and territories by total population\n\n"
        )
        if not table_caption:
            raise Exception("Couldn't find the table with the correct caption.")

        table = table_caption.parent

        if not table:
            raise Exception("Couldn't find the table with the correct caption.")

        return table

    @staticmethod
    def _create_list_of_rows(table: Tag):
        data = []

        if table:
            rows = table.find_all("tr")
            for row in rows:
                cols = row.find_all(["td", "th"])
                cols_text = [ele.get_text(strip=True) for ele in cols]
                data.append([ele for ele in cols_text if ele])

        return data

    @staticmethod
    def _parse_date_of_data(text: str) -> datetime:
        for fmt in ("%d %b %Y", "%Y"):
            try:
                return datetime.strptime(text, fmt)
            except ValueError:
                pass
        raise ValueError(f"No valid date format found for the text '{text}'")

    def _parse_table_rows(self, table_rows: List[List[str]]):
        parsed_rows = []
        for row in table_rows[1:]:
            population_table_row = PopulationTableRow(
                country_name=row[0],
                population=int(row[1].replace(",", "")),
                date_of_data=self._parse_date_of_data(row[3]),
            )
            parsed_rows.append(population_table_row)

        return parsed_rows

    def get_table(self) -> List[PopulationTableRow]:
        wikipedia_page_html = self._fetch_page_html()

        table = self._find_table_in_html(wikipedia_page_html)
        table_rows = self._create_list_of_rows(table)

        return self._parse_table_rows(table_rows)
