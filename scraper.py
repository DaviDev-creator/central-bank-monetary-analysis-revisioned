import os
from typing import List, Dict
from tavily import TavilyClient
from scrapegraphai import SmartScraper
from instruments import financial_instruments
import requests

class CentralBankScraper:
    def __init__(self, tavily_api_key=None):
        self.tavily = TavilyClient(api_key=tavily_api_key or os.getenv("TAVILY_API_KEY"))
        self.scraper = SmartScraper()

    def get_links(self, instrument: str) -> List[str]:
        return financial_instruments.get(instrument, [])

    def search_news(self, instrument: str, date: str) -> List[str]:
        query = f"monetary policy news {instrument} {date}"
        search_result = self.tavily.search(query=query, search_depth="advanced")
        return [result['url'] for result in search_result['results']]

    def process_links(self, links: List[str], instrument: str) -> str:
        combined_data = []
        for link in links:
            try:
                # Using a simplified prompt for the LLM scraper
                result = self.scraper.run(
                    url=link,
                    prompt=f"Extract key monetary policy decisions and sentiment for {instrument}. Be concise."
                )
                combined_data.append(f"Source {link}: {result}")
            except Exception as e:
                combined_data.append(f"Error scraping {link}: {str(e)}")

        return "\n\n".join(combined_data)

    def execute(self, instrument: str, date: str):
        links = self.get_links(instrument)
        if not links:
            links = self.search_news(instrument, date)
        
        return self.process_links(links, instrument)
