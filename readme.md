# Personalized Recipe Finder

## Description
Many people find themselves with a fridge full of ingredients but lack the inspiration to create meals. This often leads to food waste and unnecessary grocery expenses. **The Personalized Recipe Finder** is a web application designed to help users input their available ingredients and dietary preferences to generate meal ideas. The app provides nutritional information and cooking instructions to help users make informed decisions and reduce waste.

---

## Tech Stack

- **Front-end**: HTML, CSS
- **Back-end**: Python, Flask
- **Database**: PostgreSQL
- **External APIs**:
  - [Spoonacular API](https://spoonacular.com/food-api) for recipe suggestions
  - [Edamam Nutrition API](https://developer.edamam.com/) for nutritional analysis

This project aims to deliver a **full-stack** experience, emphasizing both user interface (front-end) and data handling/API integrations (back-end).

---

## Project Structure

    personalized-recipe-finder/
    ├── app.py                    # Main Flask application
    ├── requirements.txt          # Python dependencies
    ├── static/                   # CSS, images, and other static files
    ├── templates/                # HTML templates
    ├── config.py                 # Configuration settings (e.g., database URL, API keys)
    ├── models/                   # Database models
    │   ├── user.py
    │   ├── recipes.py
    │   └── ...
    ├── utils/                    # Helper functions (e.g., API calls, data processing)
    └── README.md                 # Project readme

---
