# **Marisol Furniture Website**

The Marisol Furniture website serves as a portfolio and blog platform designed for potential customers interested in bespoke furniture. This project is developed using the Django framework and incorporates various features that facilitate interaction between customers and furniture specialists. Marisol Furniture offers users the ability to request a consultation call with an expert who can provide insights into custom furniture options, pricing, materials, and more.

[Marisol](https://marisol-801c526b3523.herokuapp.com/) - The live site can be viewed here.

![Am I Responsive?](link)

<hr>

## **TABLE OF CONTENTS**

 - [**User Experience (UX)**](#user-experience-ux)
    * [User Stories](#user-stories)
    * [Agile Methodology](#agile-methodology)
    * [The Scope](#the-scope)
 - [**Design**](#design)
    * [Bootstrap Templates Styling](#bootstrap-templates-styling)
    * [Colours](#colours)
    * [Typography](#typography)
    * [Media](#media)
    * [Wireframes](#wireframes)
    * [Database Schema](#database-schema)
 - [**Features**](#features)
   * [Navigation](#navigation)
   * [Footer](#footer)
   * [Home Page](#home-page)
   * [Gallery Page](#gallery)
   * [Blog](#blog)
   * [Homepage Display](#homepage-display)
   * [Article Interaction](#article-interaction)
   * [Call Booking](#call-booking)
   * [Booking Button Block](#booking-button-block)
   * [Booking Page](#booking-page)
   * [Booking Form](#booking-form)
   * [Edit Booking Page](#edit-booking-page)
   * [Delete Booking Page](#delete-booking-page)
   * [Profile Page](#profile-page)
   * [Administrative Panel](#administrative-panel)
   * [Signup Page](#signup-page)
   * [Future Additions](#future-additions)
 - [**Testing**](#testing)
 - [**Technologies Used**](#technology-used)
 - [**Deployment**](#deployment)
 - [**Credits**](#credits)

<hr>

## **USER EXPERIENCE (UX)**

### **User Stories**

Unregistered site user:

- As a user, I can understand the site's purpose as soon as I land on the homepage.
- As a user, I can navigate the site's content without difficulty or confusion.
- As a user, I can view a list of all the blog articles.
- As a user, I can click on and view each blog article so I can view the content.
- As a user, I can view how many likes each blog article has received.
- As a user, I can view approved  comments made on each blog article.
- As a user, I can easily locate and visit social media links.
- As a user, I can sign up and register on the site.

Regsitered site user:

- As a user, I can perform the same actions as an unregistered site user.
- As a user, I can log in and easily make call bookings.
- As a user, I can edit/delete call bookings I have created.
- As a user, I can see my last call booking on the profile page.
- As a user, I can like/unlike blog articles.
- As a user, I can post comments on blog articles.

Site Admin/Superuser:

- As a user, I can perform the same functionalities as unregistered and registered users.
- As a user, I can create, edit and delete blog articles from the admin panel. 
- As a user, I can approve, edit and delete comments to allow control over inappropriate content.
- As a user, I can see a list of booked calls in the admin panel.
- As a user, I can edit and delete booked calls and create new ones if I need this for some reason.

<hr>

### **Agile Methodology**

For planning the development and implementation of the Marisol website, a project kanban board was used as an Agile Tool through Github. This project board utilised issues as 'User Stories', a link can be found [here](https://github.com/users/Julia-cloudname/projects/6).

To help define the functionalities and prioritise key features, these 'User Stories' were broken down into 4 categories of importance; 'Must Have', 'Should Have',  'Could Have' and 'Won't have'.

'Must Have' represents a feature or functionality that is essential to the site, 'Should Have' is a defined requirement needed for the site, 'Could Have' is determined to be optional and 'Won't have' - future functionality that I'm going to do later.

<hr>

### **The Scope**

#### **The Site's Main Goals:**

- Positive User Experience: The primary goal of the Marisol Furniture website is to provide users with an intuitive, efficient, and enjoyable experience. From browsing articles to scheduling consultations, the site aims to create a seamless journey for users.

- Clear Purpose: The site aims to present its purpose and offerings clearly. It allows users to quickly understand that Marisol Furniture is a platform where they can explore custom furniture options, book consultations, and engage with informative content.

- Controlled Functionality: Based on a user's permissions, the website offers controlled functionality. Registered users have access to profile management, consultation booking, and engagement with blog articles, while specialists have the ability to publish articles and manage user interactions.

- User Profile Management: The site emphasizes the importance of user profiles. Users can easily manage their consultation bookings, view details of their reservations, interact with blog posts and engage with other community members.

<hr>

## **DESIGN**

## **Bootstrap Templates Styling**

The project's Bootstrap templates are designed to provide a visually appealing and consistent user experience. They utilize specific fonts and colours to achieve this. 

I used templates:

- [For website structure](https://getbootstrap.com/docs/4.3/examples/jumbotron/)
- [For profile page](https://bbbootstrap.com/snippets/social-profile-container-63944396)
- [For gallery and background](https://codepen.io/sachinchoolur/pen/qNyvGW)

## **Colours**

The templates utilize a cohesive colour scheme to create a visually appealing interface. The primary background colour is a dark shade, #152836, which provides a solid base. This dark background enhances the readability of the content and contrasts well with the text colour.

The secondary background colour, #333, is also utilized in specific elements, contributing to a consistent design. The primary text colour is #eee, providing a high contrast against the dark background, ensuring readability.

## **Typography**

The primary font used in the templates is "Open Sans," which is a modern and clean typeface. This choice ensures readability and a contemporary look. Additionally, the fallback fonts include "Helvetica Neue," "Helvetica," "Arial," and generic sans-serif fonts. These provide compatibility across various devices.

The font size and weight follow the Bootstrap conventions, with variables defined as --bs-body-font-size and --bs-body-font-weight. This consistency ensures a harmonious look throughout the templates.

The chosen fonts and colour scheme create a simple and modern user interface, making it easy for users to navigate and engage with the content. The templates leverage Bootstrap's well-designed components to create a professional and visually appealing website.

### **Media**

- [Balsamiq](https://balsamiq.com/) was used for the design of my wireframes.
- [Canva](https://www.canva.com/) was used for the design of the logo
- [Drawsql.app](https://drawsql.app/) was used for the design of the database schema 

### **Wireframes**

Wireframes for pages are linked here:

Homepage

<img src="https://github.com/Julia-cloudname/marisol/blob/7aa3e04c6791eeee74dae3925339420eb0dd2c72/static/images/home-page-wareframe.png"><br>
 
Booking Page

<img src="https://github.com/Julia-cloudname/marisol/blob/7aa3e04c6791eeee74dae3925339420eb0dd2c72/static/images/booking-page-wareframe.png"><br>

### **Database Schema**

Database Schema

<img src="https://github.com/Julia-cloudname/marisol/blob/7aa3e04c6791eeee74dae3925339420eb0dd2c72/static/images/database-wareframe.png"><br>

<hr>

## **FEATURES**

### **Navigation**

#### **Desktop Navigation**

- The navigation menu on the Marisol Furniture Website is designed for easy access to key sections. It offers links to the 'Home', 'Blog', and 'Gallery' pages, providing a clear pathway for users to explore the primary content areas.
- Registered users are provided with additional options in the menu. They'll find a link to their 'Profile Page' for managing their account details. If the user is already logged in, the menu includes a 'Log Out' button, allowing them to securely sign out from their accounts.

![Registed](docs/read-me/desktop-nav.png)
 
- If a user is not logged in, the navigation menu will feature a link to the 'Registration Page', encouraging new users to create accounts or log in to access more features of the site.

![Not registed](docs/read-me/desktop-nav.png)

- The navigation bar is designed with responsiveness in mind, adapting seamlessly to various screen sizes. On smaller devices, it collapses into a convenient burger menu, ensuring an optimal browsing experience across devices.
- 
This feature enhances the user experience by providing easy navigation to essential sections of the Marisol Furniture Website and enabling registered users to manage their accounts efficiently.


#### **Mobile Navigation**

- The mobile version of the Marisol Furniture Website features a convenient burger menu, ensuring a responsive and user-friendly design for smaller screens.
- When users tap on the burger icon, a dropdown menu unfolds, providing easy access to the same essential page links as mentioned before. This includes the primary pages, such as 'Home', 'Blog', and 'Gallery', along with the user-specific dropdown menu.

![Mobile Nav](docs/read-me/desktop-nav.png)

This mobile navigation approach allows users to navigate the site efficiently on their mobile devices, maintaining consistent access to key sections and user account options through the intuitive dropdown menu.

### **Footer**

- Positioned at the bottom of each page, the footer of the Marisol Furniture Website is dedicated to connecting with our audience on various social media platforms.
- While currently featuring placeholders for social media icons, I will add direct links to official profiles across popular networks such as YouTube, Facebook, Twitter, and Instagram in later versions.
![Footer](docs/read-me/footer.png)

### **Home Page**
The Home Page of the website features the following sections:

- Navigation Menu: A simple and clear menu at the top of the page that helps users navigate to different sections of the website.
- Booking Call-to-Action: Prominently displayed at the top, there's a block encouraging users to book a consultation with experts.
- About Us: A section where users can read about the company, its values, and what sets it apart.
- Blog Articles: A collection of articles from blog, providing insights, tips, and news related to furniture and design.
- Gallery: A visual gallery showcasing images of custom furniture pieces, helping users see the quality of company work.
- Footer: Located at the bottom of the page, the footer includes links to social media platforms (YouTube, Facebook, Twitter, and Instagram).

![Home page](docs/read-me/footer.png)

### **Gallery**

The Gallery is a collection of 4 photos, each showcasing a ready furniture project. 

- Thumbnail Preview: On the main Gallery page, users see a grid of thumbnail images representing each furniture project. These thumbnails provide a quick glance at the projects.
-  Click-to-Enlarge: When a user clicks on a thumbnail, the image opens in a larger view. This allows users to appreciate the details of the project and get a closer look at the craftsmanship.

![Gallery](docs/read-me/footer.png)

-  Project Description: Below each enlarged image, there is a brief description of the project. This description provides insight into the design, materials used, and any special features that make the project unique.
-  Easy Navigation: While viewing an enlarged image, users can navigate between the images using arrow buttons. This allows users to seamlessly move through the entire collection without leaving the fullscreen view.
-  Flexible Interaction: Users have the option to exit the fullscreen view at any time. They can click on the "X" button to close it

![Gallery Full Screen](docs/read-me/footer.png)

The Gallery is designed to showcase the quality and creativity of work, giving users a chance to appreciate the details and learn about the craftsmanship behind each piece of custom furniture.

### **Blog**

Blog is a dynamic collection of insightful articles, with the following features:

### **Homepage Display:**

- The main Blog page features a grid of three articles, each presented with a thumbnail image, article title, author's name, publication date, and the number of likes received.
- As the number of articles exceeds six, a "Next Page" arrow appears, allowing users to explore additional articles.
- When the user clicks "Next Page," the remaining article thumbnails are displayed, along with a "Back" button to return to the previous set of articles.

![Blog](docs/read-me/footer.png)

### **Article Interaction:**

- Clicking on an article's title takes the user to the full version of the article, where they can read the entire content.
- The full article view also displays comments made by other users, allowing for discussion and engagement with the content.

![Article](docs/read-me/footer.png)  

- Registered users have the ability to leave comments in the dedicated comment section below the article.

![Comment form](docs/read-me/footer.png)  

- If a user is not logged in, the comment form is not accessible. 
- When a user submits a comment, it doesn't immediately appear on the site but is instead sent for approval by the administrator. The user is notified with a green message "Your comment is awaiting approval." Upon approval by the admin, the comment is published.

![Comment message to user](docs/read-me/footer.png)

### **Call Booking**

### **Booking Button Block:**

- Users can see a call booking block on every page of the website.
- When the user clicks the "Book Call" button, they are redirected to the booking page.

![Gallery](docs/read-me/footer.png)

### **Booking Page:**

- If the user is logged in, they see the booking form.
- If not, they see a message prompting them to log in or register.

![Not registered booking page](docs/read-me/footer.png)

### **Booking Form:**

- The user sees a booking form where they can provide the name, email, and phone number of the person who needs the consultation. This feature is designed for users who want to book a call for themselves, their close ones or friends.

![Booking form](docs/read-me/footer.png)

- The form includes a message field where users can specify the details of the call - their specific interests, pricing, materials, or other questions. This allows the specialist to prepare for the call and provide comprehensive information.
- Users can select a convenient date using a datepicker calendar and a suitable time interval from a dropdown list.

![Datepicker](docs/read-me/footer.png)

![Timepicker](docs/read-me/footer.png)

- If the user selects a past or today's date, a message appears in red: "The call date cannot be in the past or today!"

![Not valid date booking](docs/read-me/footer.png)

- After clicking the submit button, the user is taken to a page confirming the successful booking. Below the confirmation message, there are buttons to edit or delete the booking.

![Success](docs/read-me/footer.png)

### **Edit Booking Page:**

- When the user clicks the "Edit Booking" button, they are taken to the editing page, where a pre-filled booking form is automatically loaded with the details of their last booking.

![Success page](docs/read-me/footer.png)

- The user can make any necessary changes to the booking information and then save the updates. Upon saving, they are redirected to the success page.
- On the success page, the user receives a confirmation message about the successful changes to the booking, along with two buttons: "Edit Booking" and "Delete Booking."

### **Delete Booking Page:**

- When the user clicks the "Delete Booking" button, they are taken to the deletion page, where they see a warning message: "Are you sure you want to delete this booking?" Below the message, there are two buttons: "Edit Booking" and "Delete Booking."

![Delete Booking](docs/read-me/footer.png)

- If the user confirms the deletion by clicking the "Delete Booking" button, the booking is permanently removed from the user's account and from the administrator panel.
- After successful deletion, the user is redirected to the success page with the message: "Call Booking Successfully Deleted!"

![Delete Success page](docs/read-me/footer.png)

### **Profile Page**

- Registered users have access to the profile page from the navigation menu.
- On this page, the user can see their latest booking, including the details gathered from the booking form: name, email, phone number, call details message, date, and time.
- Below the booking details, there are buttons for "Edit Booking" and "Delete Booking." These buttons allow the user to manage their bookings directly from their profile.

![Profile Page](docs/read-me/footer.png)

### **Administrative Panel**

- The superuser (administrator) has access to the administrative panel with privileges to manage posts, bookings, and comments.
- In the "Posts" section, the administrator can add, edit, and delete articles.
- In the "Comments" section, the administrator can add, edit, approve, and delete comments.
- In the "Bookings" section, the administrator can add, edit, and delete bookings from all users. The administrator can also view comprehensive information about all bookings.

![Administrative Panel Bookings](docs/read-me/footer.png)

### **Signup Page**

If the user is not registered, they can access the "Signup" button from the navigation menu, which leads them to a welcome message and the registration form.

![Register Form](docs/read-me/footer.png)

The registration form includes fields for the following information, along with helpful prompts:
- Username: (Username)
- E-mail (optional): (E-mail address)
- Password: (Password)
- Password (again): (Password)
- The form also includes a registration confirmation button.

### **Log in/Log out Page**

Users, who have an account can log in and log out

![Log in page](docs/read-me/footer.png)

### **Future Additions**

- In the future, we plan to implement account validation to prevent duplicate accounts. If a user attempts to register with a username or email that already exists, they will be prompted to choose a different username or email to complete the registration process if a user with the same credentials already exists. This enhancement will help ensure unique user accounts on the platform.
- One of the upcoming enhancements will be the addition of a customer reviews feature. This feature will allow users, especially customers who have purchased custom furniture from Marisol, to share their feedback and experiences with the community. 

<hr>

## **Testing**

[TESTING DETAILS](TESTING.md)

<hr>

## **TECHNOLOGIES USED**

### Languages used:

- HTML
- CSS3
- Javascript
- Python

### Libraries and Programs Used

- [Gitpod](https://www.gitpod.io/)<br>
   Used for version control alongside GitHub.
- [GitHub](https://github.com/)<br>
   Used to store the project and utilise git version control.
- [Heroku](https://id.heroku.com)<br>
   Used to deploy project.
- [Cloudinary](https://cloudinary.com/)<br>
   Cloud based storage, used for storing any media submitted by users.
- [ElephantSQL](https://www.elephantsql.com/)<br>
   Used to host the PostgreSQL database.
- [W3C - HTML](https://validator.w3.org/)<br>
   Used to validate all HTML code.
- [W3C - CSS](https://jigsaw.w3.org/css-validator/)<br>
   Used to validate all CSS code.
- [CI PEP8 Testing](https://pep8ci.herokuapp.com/)<br>
   Used to validate all Python code.
- [Google Fonts](https://fonts.google.com/)<br>
   Used to provide the font styling.
- [Bootstrap](https://getbootstrap.com/)<br>
   Used to for helping with the HTML design and layout.
- [Fontawesome](https://fontawesome.com/)<br>
   Used to implement effective icons.
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)<br>
   Used during the development to debug and test responsiveness.
- [Balsamiq](https://balsamiq.com/)<br>
   Used to build both the database schema diagram and design wireframes.
  
<hr>

## **DEPLOYMENT**

### ** Create Github Repository **
- Log in to your Github account.
- Navigate to repositories and select 'New'.
- Select the 'Code Institute' template from the 'Repository Template' menu.
- Give your repository a name and select 'Create Repository'.
- When the repository has been created select 'Gitpod' to open a new workspace.

### ** Heroku **
- Log in to your Heroku account [Heroku](https://id.heroku.com).
- From the home page select 'New', then select 'Create New App' from the drop-down.
- Provide a name for your app and selectyour regrion.
- Add 3 new keys along with your relevant value information: 'SECRET_KEY', 'DATABASE_URL' and 'ClOUDINARY_URL'. 
- At the top of the page select the 'Deploy' tab.
- For the preferred deployment method select 'Github'.
- Search for your repository name and connect.
- Additionally, automatic deploys can be enabled for deployment after each push to Github.

### ** Fork this project **
- Sign in to Github and go to my [repository](https://github.com/AndyL86/gt-modellista)
- At the top of the page select 'Fork'.
- The Fork will now be added to your repositories.

### ** Clone this project **
- Sign in to Github and go to my [repository](https://github.com/AndyL86/gt-modellista)
- Select the green 'Code' button.
- Select from one of the cloning options HTTPS, SSH or Github CLI. Click the clipboard icon to copy the URL.
- Open git bash
- Enter ‘git clone’ into the text box and then paste the respository URL and select enter. 

For more information on cloning please read the github documentation [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

<hr>


