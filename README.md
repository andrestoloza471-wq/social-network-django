# Social Network Django

## Overview
This repository contains a Django-based social network application that allows users to create, share, and connect with each other in a modern social media environment.

## Features
- User registration and authentication
- Profile management
- Posting updates and multimedia sharing
- Friend connections and messaging
- Notifications for user activities
- An intuitive user interface for seamless navigation

## Installation
To set up the development environment, follow these steps:
1. Clone the repository
   ```bash
   git clone https://github.com/andrestoloza471-wq/social-network-django.git
   ```
2. Navigate to the project directory
   ```bash
   cd social-network-django
   ```
3. Create a virtual environment
   ```bash
   python -m venv env
   ```
4. Activate the virtual environment
   ```bash
   # On Windows:
   .\env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```
5. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```
6. Run migrations
   ```bash
   python manage.py migrate
   ```
7. Start the development server
   ```bash
   python manage.py runserver
   ```

## Usage
After running the development server, navigate to `http://127.0.0.1:8000/` in your web browser to access the application. Create an account and start interacting with the social network!

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.