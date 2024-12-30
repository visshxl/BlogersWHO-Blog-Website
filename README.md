# BlogersWHO! - Blog Website: A Dynamic Blogging Platform Built with Django

This project is a dynamic and interactive **Blog Website** developed using **Django**, designed to provide a seamless experience for both content creators and readers. The platform comes with several key features that enhance functionality, usability, and engagement.

## Features

- **Home Page with Recent Posts**  
  Displays the latest blog posts prominently on the homepage for quick access.
  

- **"Save for Later" Functionality**  
  Users can save blog posts for future reading and access them via a dedicated "Stored Posts" page.

- **All Posts Page**  
  Lists all available blog posts in a well-organized format for easy exploration.

- **Post Detail Page with Comments**  
  Displays the full content of a selected post with a **comment section** for interactive discussions.

- **Tagging System**  
  Organizes posts with tags, allowing users to discover related content easily.

- **Author Management**  
  Displays author details with posts and links posts to their respective authors.

- **Admin Panel Customization**  
  Simplifies content management with easy creation, updating, and deletion of posts, tags, authors, and comments.

## Core Models

- **Post Model**: Represents a blog post with fields for title, content, publication date, featured image, and author, with relationships to tags and comments.
- **Author Model**: Stores author details and links posts to their authors.
- **Tag Model**: Defines categories/topics for posts and allows filtering by tags.
- **Comment Model**: Enables user comments on posts, storing commenter details and text.

## Technologies Used

- **Backend**: Django (Python Framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (Django’s default database)
- **Version Control**: Git and GitHub

## How to Run the Project

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/blog-website.git
   cd blog-website

2. Set up a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt

3. Run database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate

4. Start the development server:

    ```bash
    python manage.py runserver

5. Access the website in your browser at:
    ```bash
    http://127.0.0.1:8000/

## Future Enhancements
- User authentication system for personalized features like user-specific saved posts.
- Search functionality to locate posts by keywords, tags, or authors.
- Pagination for improved navigation of the "All Posts" and "Stored Posts" pages.

This project showcases the power of Django in creating a scalable and feature-rich blogging platform. Feel free to explore the code, raise issues, or contribute to its development! 😊
