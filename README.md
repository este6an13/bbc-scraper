# BBC Scraper

This is a Python program that scrapes news articles from the BBC website using Selenium. It visits different categories on the website, extracts the article links, and then processes each article to retrieve the title and body content. The program saves the article data in JSON format.

## Prerequisites

- Python 3.6 or higher
- Selenium
- Chrome WebDriver

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/bbc-scraper.git
   ```

2. Install the dependencies:

    ```bash
    pip install selenium
    ```

3. If needed, download the Chrome WebDriver and place it in your system's PATH.

## Usage

1. Run the script:

    ```bash
    python bbc_scraper.py
    ```
2. The program will launch a Chrome browser and visit the BBC News website.

3. It will scrape articles from the "Business" and "Tech" categories.

4. The article data will be saved as JSON files in the articles directory.

5. If an article has already been processed (based on the sequence of numbers in the article link), it will be skipped to avoid duplication.

6. After processing all articles, the set of visited links will be printed.

## Customization
* You can modify the categories to scrape by editing the get_category_links function in the code.

* If you want to change the output directory for the JSON files, you can update the file_path variable in the process_articles function.

* Feel free to customize the program further to suit your needs.

## License

This project is licensed under the MIT License.

You can copy and save this content as a `README.md` file in your project directory. Feel free to modify it according to your specific requirements and add any additional information or instructions.