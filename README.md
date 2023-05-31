# Steam Charts and Garry's Mods Scraper

This is a Python script that scrapes data from two websites: [Steam Charts](https://steamcharts.com/) and [Garry's Mods](https://garrysmods.org/). The script retrieves information about the top games on Steam and popular maps on Garry's Mods and saves the data in CSV files. Additionally, it also saves the HTML response for each page scraped in separate HTML files.

## Requirements

To run this script, you need to have the following installed:

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `csv` library

You can install the required libraries using pip:

```
pip install requests beautifulsoup4
```

## Usage

1. Clone the repository or download the script to your local machine.

2. Open the terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

   ```
   python scraper.py
   ```

   The script will start scraping data from the websites and saving it to CSV files. It will also save the HTML responses for each page scraped in separate HTML files.

4. After execution, you will find two CSV files (`steam_charts.csv` and `maps.csv`) and the corresponding HTML files (`steam_pageX.html` and `mods_pageX.html`) in the same directory as the script.

## Configuration

The script is currently set to scrape data for the top 5 pages from both websites. If you want to change the number of pages to scrape, you can modify the following lines of code:

For Steam Charts scraping:

```python
while payload_1['p.'] < 6:
```

Change `6` to the desired number of pages.

For Garry's Mods scraping:

```python
while payload_mods['page']< 6:
```

Change `6` to the desired number of pages.

## Disclaimer

Please note that web scraping may violate the terms of service of the websites being scraped. Make sure to review the terms of service before using this script. Use it responsibly and for educational purposes only.

## License

This script is licensed under the [MIT License](LICENSE). Feel free to modify and use it according to your needs.
