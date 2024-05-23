# Web Scraping Project: Game Store Data Scraper

This Python project scrapes game data from multiple online stores, including Steam and Epic Games Store, and outputs the collected data into a CSV file. It aims to provide users with an automated way to gather information about specific games, such as their titles, prices, release dates, and popular tags, from various online platforms.

<br>

<div align="center">
  <!-- Add badges here -->
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/HossamMohamed12/Game-Store-Data-Scraper">
  <img alt="GitHub license" src="https://img.shields.io/github/license/HossamMohamed12/Game-Store-Data-Scraper">
</div>

<br>

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Web scraping is the process of extracting data from websites, and this project utilizes web scraping techniques to gather information about games from Steam and Epic Games Store. By automating this process, users can save time and effort in manually collecting data from these platforms.

## Features

- Scrapes game data from Steam and Epic Games Store.
- Retrieves information such as game titles, prices, release dates, and popular tags.
- Generates a CSV file containing the collected data for further analysis or use.

## Installation

To use this project, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/game-store-scraper.git
    ```

2. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
   ```

## Usage

To run the scraper, execute the main Python script:

```bash
python main.py
```

## Configuration

Before running the scraper, you may need to configure certain parameters, such as the search query and browser settings. Modify the `config.json` file located in the `config` directory to adjust these settings according to your requirements.

## Contributing

Contributions to this project are welcome! If you encounter any issues, have suggestions for improvements, or would like to add new features, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
