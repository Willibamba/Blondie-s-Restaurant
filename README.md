# Blondie's Restaurant
#### Video Demo: <https://youtu.be/dVbRJhrB1So>
#### Decription:
This a Restaurant Web App created for my friend's restaurant to enable internet users to make oline orders of dishes, booking table resservations and birthday celebrations with an e-mail notifiaction to the restaurant for each online order activities made and other informations about the restaurant. The reason behind choosing this project is to help my friend have to have a website as his business relies on Facebook postings to communicate and relay information to customers and internet users alike. I believe having a web app for a restaurant is a very essential part of the business to relay information about the dish menus, online orders and the services offered like musical entertainments, birthday celebrations, etc.

This project helps me to implement and bring together the knowledge acquired during my studies and also, I have learnt a lot during making this project in the form of how to think as a programmer to face challenges to solve problems with steps and the importance of reading documentation of languages, frameworks and database.

The main files in the project:

#### **App.py**

- **home function**: The route to the home page which return index.html template.
    
- **menu function**: The route to the menu page of dishes which return menu.html template.
    
- **order function**: The route to online order page with methods of both "GET" and POST" requests. This function store order information to the databse.db, sends email notification of a new order to the restaurant and renders succesful_order.html template to the user when the conditions to make orders are met, or displays error massages on the page and return order.html template. 
    
- **orders function**: This route require a login, fetch information about orders made from the database and return orders.html template.
 
- **login_required function**: Decorates the route to require login.
    
- **login function**: The route to the login page, checks if the login requirements  are met, establish session and return a redirect to orders.html template, or displays error message and return login.html template.
    
- **log_out function**: The route to log out of seesion and return a redirect to the root (index.html).
    
- **about function**: The route to the about page which return about.html template.

#### **databae.db**
- It has two tables for storing information of the online order and bookings made by customers and also the login account.

#### ***Templates***

- **layout.html**: The base for all other templates containing navigation bar with brand logo, brand name and menu links, and footer, which contains the inforamion about the address and contact deatils.
    
- **index.html**: This page includes the main information about the Resaturant, opening hours and it's services.
    
- **menu.html**: The page displays the information about the food menu and their prices.
    
- **order.html**: A page with a form to make online orders and bookings with a submit button.
    
- **successful_order.html**: The page shows information to confirm that the order is made successfully.
    
- **orders.html**: A page that requires login to view the information of online orders and bookings made by customers with time and date from the database.
    
- **login.html**: The login page to fill in the username and password to view the information of the online orders and bookings made. 
    
- **about.html**: This page shows information the summary of description of the restaurant.

#### ***Static Files***

- **images folder**: Contains the photos of used for the project like dish, logo, etc.

- **Videos folder**: Contains the video for musical entertain.

- **styling.css**: A file that contains the custom css settings for the web-pages with desing techniques like the box-sizing, flex, text-align, font-size, color, border, padding, etc.

#### **requirement.txt**
The followings are the rquired packeges needed for this app to run:
    
- **Python3**

- **Flask** 

- **Flask_Session**

- **quick-mailer**

- **requests**

- **sqlite3**

- **bootstrap 5.0.2 for CSS and Javascript**

#### **.gitignore**
For git to ignore files 
