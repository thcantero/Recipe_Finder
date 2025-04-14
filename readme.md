# Personalized Recipe Finder

**Live Demo**:  
[Recipe Finder on Render](https://recipe-finder-ps1r.onrender.com)

## Table of Contents
- [Personalized Recipe Finder](#personalized-recipe-finder)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Tech Stack](#tech-stack)
  - [Quickstart (Local)](#quickstart-local)
  - [Deployment (Render + Supabase)](#deployment-render--supabase)
  - [Project Structure](#project-structure)
  - [Future Development](#future-development)
  - [Lessons Learned](#lessons-learned)
  - [License](#license)
    - [About the Author](#about-the-author)

---

## Overview
Many people find themselves with a fridge full of ingredients but no inspiration for meals. **Personalized Recipe Finder** solves that problem by allowing users to:
- **Search** for recipes by the ingredients they have on hand  
- **Save** their favorites and view them later  
- **Display** detailed recipe information

This helps reduce food waste and saves time. The project is designed to be a robust full-stack application, demonstrating both front-end and back-end skills.

---

## Features
1. **User Registration & Login**:  
   - Secure registration using **bcrypt** for hashing passwords  
   - Session-based login for personalizing favorite recipes

2. **Ingredient Autocomplete**:  
   - Integrates **Spoonacular** API to suggest possible ingredients as you type

3. **Recipe Search & Details**:  
   - Finds recipes using the ingredients you choose  
   - Shows cooking times, instructions, and images

4. **Favorites**:  
   - Logged-in users can save recipes  
   - View all saved favorites in the user dashboard

5. **Deployed via Render** & **Supabase**:  
   - **Supabase** for scalable PostgreSQL hosting  
   - **Render** for easy, automated app deployment

---

## Tech Stack
- **Front-end**: HTML, CSS, JavaScript  
- **Back-end**: [Flask](https://flask.palletsprojects.com/) (Python)  
- **Database**: [Supabase PostgreSQL](https://supabase.com/)  
- **APIs**:  
  - [Spoonacular API](https://spoonacular.com/food-api) for recipe data and autocomplete  
- **Deployment**:  
  - [Render](https://render.com/) (Web Service hosting)  
  - **Supabase** for PostgreSQL

---

## Quickstart (Local)

1. **Clone the repo**:
   ```bash
   git clone <YOUR_FORK_URL>.git
   cd Recipe-Finder
   ```

2. **Create & activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:  
   Create a `.env` in the root directory:
   ```bash
   SPOONACULAR_API_KEY=<your-spoonacular-api-key>
   SECRET_KEY=<your-flask-secret-key>
   DATABASE_URL=<your-database-connection-string>
   ```
   For Supabase, it might look like:
   ```
   DATABASE_URL=postgresql://postgres:<PASSWORD>@<YOUR_SUPABASE_HOST>:5432/postgres?sslmode=require
   ```

5. **Initialize & run**:
   ```bash
   flask run
   ```
   Then visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

*(Optionally, you can run `python app.py` if you’ve configured your `FLASK_APP` environment variable or placed the right logic in your code. Use whichever method you prefer.)*

---

## Deployment (Render + Supabase)

1. **Supabase Setup**  
   - Create a new project on Supabase.  
   - Retrieve your connection string from **Project Settings → Database**.  
   - Be sure to append `?sslmode=require` to ensure a secure connection.

2. **Render Setup**  
   - Create a new “Web Service” in Render.  
   - Connect your GitHub repo (or push to a Render-connected repo).  
   - In your Render service settings, define the environment variables:
     - `SPOONACULAR_API_KEY`
     - `SECRET_KEY`
     - `DATABASE_URL` (the Supabase string)

3. **Start Command**  
   - Use something like `gunicorn app:app` in Render.  
   - Once deployment is done, you’ll have a public link (e.g., `https://recipe-finder-xxxx.onrender.com`).

---

## Project Structure
```
.
├── app.py                  # Main Flask routes & logic
├── forms.py                # WTForms for user login/registration
├── models.py               # SQLAlchemy models (User & Recipe)
├── requirements.txt        # All Python dependencies
├── static/
│   ├── ingredient-search.js  # Autocomplete logic for ingredients
│   └── style.css             # Basic styles
├── templates/
│   ├── index.html           # Landing page (login/register)
│   ├── register.html        # Registration form
│   ├── homepage.html        # Main user page after login
│   ├── show-recipes.html    # Display list of found recipes
│   ├── display-recipe.html  # Single recipe detail page
│   └── favorites.html       # Displays saved (favorited) recipes
└── README.md
```

---

## Future Development
- **Meal Planning Calendar**: Plan out a week’s worth of recipes and check if you have enough ingredients.  
- **Shopping List Generator**: If ingredients are missing, generate a dynamic shopping list.  
- **Recipe Ratings & Comments**: Let users rate and comment on recipes for community engagement.  
- **Nutritional Analysis**: Integrate with another API (like Edamam or a Spoonacular endpoint) to show macros.
- **Recipe Filtering**: Filter by cuisine, cooking type, cooking time, etc.

---

## Lessons Learned
- **API Rate Limits**: Learned to handle Spoonacular’s quota by caching results and handling exceptions gracefully.  
- **Database Migrations**: Coordinating schema changes locally and on Supabase can be tricky—SQLAlchemy migrations (e.g., Alembic) help.  
- **Session Management**: Ensuring secure session handling in Flask was critical for user authentication.  
- **Deployment Workflow**: Automated CI/CD on Render simplified the process, but taught me the importance of environment variables and logs.

---

## License
For now, this project is licensed under the **MIT License**, making it permissible for anyone to use or modify. You can read more about the MIT License in the [LICENSE](LICENSE) file.

---

### About the Author

I’m Thalia—a **product manager with an MBA** and currently pursuing a **master’s in Computer Science with a focus on AI**. I love bridging **business strategy**, **user-centric design**, and **cutting-edge technology** to tackle real-world challenges—like helping people utilize the ingredients they already have. This project reflects my passion for combining **practical solutions** with **data-driven insights** in a delightful user experience.

You can find more of my work here:
- [**LinkedIn**](https://www.linkedin.com/in/thaliacantero/)
- [**GitHub**](https://github.com/thcantero)

**Feel free to reach out** for feedback, collaboration, or just to chat about AI, product development, and of course—cooking!