# BuggyBlog
**A Beautiful and Functional Persian Weblog**

BuggyBlog is a Django-powered weblog application written in Persian, designed for a captivating user experience. It allows authors to register and contribute articles, while readers can enjoy a well-categorized and visually stunning collection of content.

**Features:**

 - **User Registration and Authorship:** Authors can create accounts and seamlessly publish their articles.
 - **Content Management:** A user-friendly interface empowers authors to manage their articles.
 - **Categorization:** Articles are organized under clear categories, accessible through the intuitive navbar.
 - **Persian Language Support:** The application is fully functional in Persian, providing a smooth experience for your target audience.
 - **Striking Design:** Pre-designed templates ensure a visually appealing user interface. (Note: Further customization is always encouraged!)

## Getting Started

To set up BuggyBlog on your development machine, follow these steps:

- *1- Clone this repository:*

        git clone https://github.com/Aliasghar-Salimi/BuggyBlog.git


- *2- Create a virtual environment:*

        python3 -m venv venv

        source venv/bin/activate  # Linux/macOS
        venv\Scripts\activate.bat  # Windows

- *3- Install dependencies:*

        pip install -r requirements.txt


- *4- Run Migrations:*

        python manage.py makemigrations
        python manage.py migrate

 - *5- Start the Development Server:*

Run the Django development server to access your project in a web browser (default port is usually 8000):

        python manage.py runserver

Now, you should be able to access BuggyBlog at http://127.0.0.1:8000/ in your browser.



**Contributing**

If you'd like to contribute to BuggyBlog's development, feel free to fork the repository and submit pull requests. We appreciate your help in making it even better!


