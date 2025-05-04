import pytest
from pages.Other.page_scraper import PageScraper
from ..urls import URLS

def test_scrape_links_from_page(page_handler):
    scraper = PageScraper(page_handler, URLS)

    try:
        links = scraper.scrape_all_links()
        assert len(links) > 0, "No links found on the page"

    except Exception as e:
        pytest.fail(f"Error: {str(e)}")

    finally:
        print('Test execution completed.')