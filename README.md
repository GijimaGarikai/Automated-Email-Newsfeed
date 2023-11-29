
# Automated Email Newsfeed

This Python script sends personalized daily newsfeeds to a list of recipients based on their specified interests. It utilizes the `yagmail` library for email functionality, reads recipient data from an Excel file, and fetches news content using the `NewsFeed` module.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Scheduling](#scheduling)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Make sure you have Python installed on your system. Install the required Python packages:

```bash
pip install yagmail pandas
```

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/Automated-Email-Newsfeed.git
    ```

2. Install the required Python packages:

    ```bash
    pip install yagmail pandas
    ```

## Configuration

1. Open the script and replace the placeholder email and Google App password with your actual email and app password:

    ```python
    email = yagmail.SMTP(user="your-email@example.com", password='your-google-app-password')
    ```

2. Create an Excel file named `people.xlsx` with columns `email` and `interest`.

## How It Works

- The script runs in an infinite loop, checking the current time every minute.
- If the time is 16:06 (in this case), it fetches recipient data from the `people.xlsx` Excel file.
- For each recipient, it fetches news content based on their specified interest using the `NewsFeed` module.
- It sends a personalized email to each recipient with the newsfeed content.

## Scheduling

The script is designed to be run continuously, but it only sends emails once a day at 16:06. Adjust the scheduling logic according to your needs.

## Troubleshooting

If an email address is invalid or there's an issue with fetching the newsfeed, the script prints a message to the console. Check the console output for any error messages.



Feel free to customize the README further based on your preferences or add more details about the script and its features.
