
# Personal Portfolio Website

## Overview
This is my responsive personal portfolio website, built using Django, HTML, and Bootstrap. It showcases my professional experiences, projects, and skills. The site comprehensively views my professional profile across four distinct pages. I have included features to make the site simple and dynamic. Feel free to play around with the different modal and button elements.

## 🚀 Features

### Home Page
- Personal introduction
- Quick links to social media profiles
- Navigation to key sections of the portfolio

### Projects Section
- Comprehensive display of personal projects
- Direct links to GitHub repositories
- Live demo links for each project
- Showcase of technical skills and practical applications

### Resume Page
- Professional experience section that highlights key roles over one year long, with additional experiences lasting less than a year accessible through an expandable dropdown menu.
- Educational background with extra information available over a modal window.
- List of my languages and technologies
- Structured and easy-to-read layout

### Contact Page
- User-friendly contact form
- Fields for:
  - Full Name
  - Email Address
  - Message submission

## 🛠️ Technologies Used
- Backend: Django
- Frontend: HTML5
- Styling: Bootstrap
- Responsive Design

## 🌟 Key Highlights
- Clean, modern, and professional design
- Fully responsive across devices
- Easy navigation
- Comprehensive professional presentation

## 🔧 Setup and Installation
1. Clone the repository
2. Run `pip install -r requirements.txt` to install all dependencies needed for the project.
   > Remember to seed the database before running the server, But you can also run the server without making the migrations to see how the site reacts when there is no data in the DB. 
3. Seed the db using the following commands:
  i. `py manage.py seed_resume_data` and `py manage.py seed_projects`
4. Perform `py manage.py makemigrations`
5. commit migrations by running `py manage.py migrate`
6. Run Django development server using `py manage.py runserver`
   > Note: I used the default db provided by django for this project. You are however, not limited to using this default db. Make your own changes as you please.

## 📝 Prerequisites
Make sure to use the latest versions of:
- Python
- Django
- Bootstrap

## 🤝 Contributions
I am open to any suggestions or improvements you might have. Please feel free to contact me through my socials and direct links.

## 📄 License
MIT
