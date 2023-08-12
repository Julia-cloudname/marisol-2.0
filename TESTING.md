#### **Marisol Testing Documentation**

## **Table of contents**
 - [**HTML Validation**](#html-validation)
 - [**CSS Validation**](#css-validation)
 - [**Python Validation**](#python-validation)
 - [**Lighthouse**](#lighthouse)
 - [**Manual testing**](#manual-testing)
 - [**Bugs and Issues**](#bugs-and-issues)

<hr>

## **HTML Validation**

* No errors detected when run through the official [W3C HTML Validation Service](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjulia-cloudname.github.io%2FProject_2%2F)

<hr>

## **CSS Validation**

* CSS – no errors were found when passing through the official [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fjulia-cloudname.github.io%2FProject_2%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

<hr>

## **Python Validation**

All Python code has been run through the [CI PEP8 Testing](https://pep8ci.herokuapp.com/) validator and has returned no errors, results can be viewed below:

#### **blog.py**
![admin-py](docs/testing/admin-py.png)

#### **marisol.py**
![admin-py](docs/testing/admin-py.png)

<hr>

## **Lighthouse**
Results from Lighthouse testing:

* Mobile 
![Responsice Mockup](assets/images/lighthouse-mobile.webp)

* Desktop
![Responsice Mockup](assets/images/lighthouse-desktop.webp)

No errors on Javascript validator [jshint.com](https://jshint.com/):

![Responsice Mockup](assets/images/jshint.webp)

<hr>

## **Manual testing** 

#### **Devices:**

- Apple MacBook Pro 2015 | 15.4"
- Acer Aspire 7750Z | 17.3"
- iPhone 8 Plus
- Samsung Galaxy M20

#### **Browsers:**

- Chrome
- Safari
- Brave
- Mozilla Firefox

#### **Feature: Navigation**

#### **Desktop Navigation**

- When I open Navigation links (Home, Blog, Gallery), they are active and functional.
- When I open the site as a Registered user, I see additional options in the menu (Profile Page, Log Out), and these options work as expected.
- When I open the site as a Non-logged-in user, I see a link to the Registration Page.
- The navigation menu is responsive, and the burger menu on smaller screens functions properly.

#### **Mobile Navigation**

- When I open the burger menu icon, opens the dropdown menu as expected.
- The dropdown menu contains the essential links and user-specific options as described.
- Mobile responsiveness has been confirmed on various devices.

#### **Feature: Footer**

- When I open Social media icons they are functional.

#### **Feature: Gallery**

#### **Thumbnail Preview**

- Thumbnail images are displayed correctly on the main Gallery page.
- I can quickly preview each furniture project through the thumbnails.

#### **Click-to-Enlarge**

- When I click on thumbnail images opens them in a larger view, as expected.

#### **Feature: Blog**

- The main Blog page displays articles with thumbnail images, titles, author names, publication dates, and like counts.
- When I add more than 6 articles I see buttons "Next Page" and  "Back" 
- The "Next Page" arrow allows users to explore additional articles, and the "Back" button functions properly.

#### **Article Interaction**

- When I click on article titles it redirects me to the full version of the article.
- Comments made by registered users are displayed below the article, as expected.
- When I try to add comments in the "Comments" section, it works as expected - I see the message about waiting for approval my comment.
- As a Non-logged-in user I cannot access the comment form, as expected.

#### **Feature: Call Booking**

#### **Booking Button Block**

- I can see the "Book Call" button on every page and it successfully redirects me to the booking page.

#### **Booking Page**

- The booking form is displayed for me when I logged in.
- When I'm a Non-logged-in user, I see a message prompting me to log in or register.

#### **Booking Form**

- When I fill out the booking form it's working as expected, including name, email, phone number, message, date, and time.
- When I choose the date in the date picker and time interval selection works correctly.
- A message appears when I select a past or today's date, saying I can't choose past or today's date.

#### **Submission and Confirmation**

- Submitting the booking form redirects me to a page confirming the successful booking.
- Buttons to edit or delete the booking are present on the confirmation page.

#### **Edit Booking Page**

- When I click the "Edit Booking" button it redirects me to the editing page.
- The pre-filled booking form with details of the last booking is loaded correctly.

#### **Delete Booking Page**

- When I click the "Delete Booking" button it redirects me to the deletion page, where a warning message appears.
- The "Edit Booking" and "Delete Booking" buttons appear.

#### **Profile Page**

- When I open the site as a Registered user, I can access my profile page from the navigation menu.
- I see the latest booking details, including name, email, phone number, call details message, date, and time.
- When I click the "Edit Booking" and "Delete Booking" buttons on the profile page they work as expected.

#### **Feature: Administrative Panel**

- When I open the admin panel as a superuser, I can see comments, post and booking sections.
- When I open comments from the admin panel, I can approve, edit and delete them as expected.
-  When I open bookings I can add, edit, and delete bookings.
- As an administrator I can view comprehensive information about all bookings, facilitating management.

#### **Feature: Signup Page**

#### **Registration Form**

- When I open Signup Page the registration form works as expected, prompting me to provide a username, email, password, and password confirmation.
- When I click the registration confirmation button it functions correctly.

<hr>
​
## **Bugs**

1

* Issue - When the user clicks on the button "New round", creates a new round even if the timer doesn't work and displays 0.
* Cause -  there is no checking if the timer starts or not
* Resolution - add if-condition to New round button listener, which returns nothing if the timer doesn't work (the button New round isn't active)

2

* Issue - When the user clicks on the button "New round", rounds start to display from bottom to top and the user doesn't see the value of the last round till scrolls to the bottom
* Cause -  rounds displayed in reverse order
* Resolution - change the method of adding rounds to HTML from .append() to prepend(), now user can see the last round on the top of the list

## **Bugs and Issues**
- One of the main bugs I encountered during development was my CSS file not being loaded upon deployment, only in the local Gitpod terminal. To remedy this, an application called 'whitenoise' was installed to pull the static files. For future applications I am going to research the cause of this issue.
- Additionally, an issue is still visible in devtools for a favicon 404 error. Unfortunately, I was unable to remedy this due to time constraints and lack of knowledge.
![whitenoise](docs/testing/whitenoise.png)

- I ran into a small issue with my delete thread button not working, this was remedied by correctly moving my closing div to fall within the if arguement of the authenticated user.

- Currently the like button icon style is loaded when users are not logged in. However, once a user is logged in the style for the icon disappears. I have tried to remedy this issue, however due to time constraints with the project hand in I was unable to fix this issue.
  
