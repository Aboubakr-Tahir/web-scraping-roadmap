# Web Scraping Roadmap

This repository contains the scripts and projects I'm building while following a 4-phase roadmap to learn web scraping. The goal is to progress from scraping basic static websites to building robust, scalable crawlers for modern web applications.

## Scraping Roadmap (4 Phases)

This plan is structured to build skills progressively, based on the book "Web Scraping with Python" by Ryan Mitchell, supplemented by other resources.

### Phase 1: The Fundamentals (The "Old Web" - Level 1)

**Objective:** Master scraping static websites using `requests` and `BeautifulSoup`.

- **READ & IMPLEMENT: "Web Scraping with Python"**

  - **Chapter 1: Your First Web Scraper:** Build a basic scraper with `urllib` and `BeautifulSoup`.
  - **Chapter 2: Advanced HTML Parsing:** Learn to navigate HTML structures.
  - **Chapter 3: Starting to Crawl:** Build a crawler that follows links from page to page.
  - **Chapter 5: Storing Data:** Learn to save scraped data to CSV or a database.

- **Mini-Project:**
  - Write a Python script to scrape a static blog.
  - Extract the titles and dates of all articles from the first 5 pages.
  - Save the output to an `articles.csv` file.

### Phase 2: The Modern Web (Levels 2 & 4)

**Objective:** Handle dynamic (JavaScript-rendered) websites and find hidden APIs.

- **READ & IMPLEMENT: "Web Scraping with Python"**

  - **Chapter 10: Crawling Through Forms and Logins:** Manage sessions and cookies for sites requiring login.
  - **Chapter 12: Crawling Through APIs:** Use the browser's "Network" tab to find and scrape data from JSON APIs (Hidden API method).
  - **Chapter 11: Scraping JavaScript:** Use tools like Selenium/Playwright to control a browser and render JavaScript (Bot method).

- **Mini-Project:**
  - Target a Moroccan e-commerce site (e.g., `jumia.ma`).
  - **Attempt 1 (Hidden API):** Use the browser's developer tools (F12) to find a Fetch/XHR call that returns product data as JSON. Use `requests` to scrape it.
  - **Attempt 2 (Bot):** If the API method fails, write a script with Selenium or Playwright to load the page, handle infinite scrolling, and then use `BeautifulSoup` to extract product prices from the fully rendered HTML.

### Phase 3: The "Engineer Mode" (The Framework - Level 3)

**Objective:** Move from disposable scripts to robust scraping projects using the industry-standard framework: **Scrapy**.

- **READ & IMPLEMENT: "Web Scraping with Python"**

  - **Chapter 9: Crawling with Scrapy:** Complete the introductory Scrapy project.

- **KEY RECIPES: "...Cookbook"**

  - **Chapter 8: Scrapy and JavaScript-Rendered Content:** Learn to integrate `scrapy-playwright` to combine the power of a framework and a browser bot.

- **Mini-Project:**
  - Re-do the Phase 2 e-commerce project, but this time build it as a proper Scrapy project, using Spiders, Items, and Pipelines.

### Phase 4: The "Real World" (Ethics, Blocks & Cloud)

**Objective:** Understand how to scrape responsibly, avoid getting blocked, and connect scrapers to a larger data pipeline (e.g., Airflow, S3).

- **READ: "Web Scraping with Python"**

  - **Chapter 13: Avoiding Scraping Traps:** Learn about `robots.txt`, honeypots, and CAPTCHAs.
  - **Chapter 14: Testing Your Website with Scrapers:** Understand the ethical considerations of scraping.

- **KEY RECIPES: "...Cookbook"**
  - **Chapter 11: Scraping Anonymously:** Use proxies to avoid IP bans.
  - **Chapter 9: Scraping in the Cloud with AWS:**
    - Run a scraper on an AWS EC2 instance.
    - Store scraped data in Amazon S3.
    - Schedule scraping tasks (connecting to Airflow).

---

### Scripts in this Repository

- **`wikipedia_web_crawler.py`**: A simple crawler from Phase 1 that traverses Wikipedia articles starting from the Main Page.
- _(More scripts will be added as I progress through the roadmap)_
