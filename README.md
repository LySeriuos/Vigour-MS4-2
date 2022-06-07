# Vigour page

![Vigour page Mockup Images]()

[View the live project here](https://github.com/LySeriuos/MS-3-book-review)

## Table of contents
1. [`Introduction`](#introduction)
2. [`UX`](#ux)    
    1. [`Design`](#design)
3. [`Features`](#features)
4. [`Issues and Bugs`](#issues-and-bugs)
5. [`Technologies Used`](#technologies-Used)
     1. [`Main Languages Used`](#main-languages-used)    
     2. [`Frameworks, Libraries & Programs Used`](#frameworks,-libraries-&-programs-Used)
6. [`Testing`](#automated-testing)
7. [`Further testing`](#further-testing)    
8. [`Deployment`](#deployment)    
9. [`Credits`](#credits)
     1. [`Audio`](#audio)
10. [`Acknowledgements`](#acknowledgements)
[`Back to top ⇧`](#vigour-page)

***
## Introduction
---
* **Vigour page** page is for active life lovers who is looking the better version of themselves. The name "Vigour" is a perfect match for active people and in Oxford dictionary gives us these meanings: 
1. Active bodily or mental strength or force. 
2. Active healthy well-balanced growth especially of plants. 
3. Intensity of action or effect : force.

[`Back to top ⇧`](#vigour-page)

### Requirements
---
1. HTML, CSS, JavaScript, Python-Django, Heroku and Amazon AWS servise as cloud for static files.
2. Design, develop and implement a full stack web application, with a relational database,
using the Django/Python full stack MVC framework and related contemporary technologies.
3. Design and implement a relational data model, application features and business logic to
manage, query and manipulate relational data to meet given needs in a particular
real-world domain.
4. Identify and apply authorisation, authentication and permission features in a full stack web
web application solution.
5. Design, develop and integrate an e-commerce payment system in a cloud-hosted full stack
web application.
6. Deployment: Deploy the final version of your code to a hosting platform such as GitHub Pages.
7. Document the development process through a git based version control system and deploy
the full application to a cloud hosting platform.

[`Back to top ⇧`](#vigour-page)

### UX
---

The potential user of this Vigour page:
* Active People.
* People who wants to inspire.
* People who'slooking for change.
* People who is pushing thru teh limits.

### User Stories:

1. User would like to see easy understandible web page with fuctionality.
2. User would like to have easy purchase of products.
3. User would like to have posibility to pay by card.
4. User would like to be able to see all the orders.
5. User would like to create profile and save information to make easier purchase.
6. User would like to have variaty of products.
7. User would like to share their goals and achievements with other users.
8. User would like to get reciept for their purchase by email.
9. User would like to be able to edit,delete their texts-blogs.
 


[`Back to top ⇧`](#vigour-page)

## Skeleton 
---
Wireframe mockups were created in a [Figma Workspace](https://www.figma.com/file/Xx5l1l6FwudhJC4zu5vnuF/vigour-ms4?node-id=52%3A1418) for the positive expierence:

Index Page:
![Index Page Wireframe](assets/read.me/Vigour page MS2.png"Index Page Wireframe")

### Design
---
* The main idea was to create a stylish page with simple design to be easy understanble and not crowded with functions that users do not need. Website has fixed container width because is much more easier to surf thru it on bigger screens. The main colours is Black and White. By the time I was looking ideas I noticed that the Black colour looks most clean colour off all. The Black colour follows White. It is just clasic colours which never get bored. But! The whole page was missing something to give these classic colours 
a fresh accent. It Became Green colour (#4AE290) and fulfils modern look weebsite. The main font is ["Inter"](https://fonts.google.com/specimen/Inter). As a back up font going to be "Sans Serif". 
* Vigour page meets user with the image wich tells directly what about this page is. 
* Buttons has slightly different colours: black and white. to bee easy readible. * 
* The index page ('home) is looks like one-page website just to introduce User with what can he find here.
"Tiny-Slider" did the job for all screen sizes, easy to control easy to set and nice for user eyes. We have 5 main sections to introduse ourself. We can find:
* Main nav and Hero section.
* Short text about owners, what is so crazy about them.
* Third "row" is the most common trainings with the explanation about each when button is pressed. The user can get all the inportant information in one click. These trianing cards can be suitable for everybody. From active walking to professional sportsman. It just give every user opportunitie to be better than yesterday with activelife.
* One row lower follows aswell "tiny-slider" but it activates only on medium and small screens just to keep image sizes and qoulity and not overload page with moving pictures.
* Later we can find training plans for every user. It is aswell "tiny-slider" and as abowe it works only on smaller screens and it is not loaded automatically. Swiping to sides do the work. Subscriptions for training plans comming later. Now it is underconstruction.
* One step lower is section for customers reviews. It is very important to show live updates about the page and in mane page. It gives future users more trust. It should be possibilities to click on the (comment-oppinion) to see that person blog or goals in the future. 
* Later Stylish section for Most commons questions from the users. It is very important to give abilitie to find answers for themselves. It will make them feel more that we care.
[`Back to top ⇧`](#vigour-page)

### Features
---
* The Vigour page developed as responsive. It can be shown on mobile phones, tablet computers and on big screens.
* User can register, log in and logout.
* User can leave their achieved goals in user blog separatly.
* All Vigours and user information is saved in the Amazon AWS cloud database.
* User is able to see his created blogs and member profile page.
* User can add, delete or edit their blog. 
* User can search for the products in shop.


  [`Back to top ⇧`](#vigour-page)  

## Further Testing 
## Code


* The Vigour page was tested on Google Chrome, Opera, Mozilla Firefox, Microsoft Edge and Safari, mobile Safari, mobile Chrome browsers.
* The Vigour page was viewed on a variety of devices such as Desktop, Laptop, Android phones, iPhone7, iPhone 8 & iPhone13.
* Friends and family members were asked to review the Website and documentation to point out any bugs and/or user experience issues.
* Some bugs left to fix.

[`Back to top ⇧`](#vigour-page)


### Issues-and-Bugs
---
1. Problem: 
"fixed issue with reverse. Had to change {url 'shop'} in main-nav menu to {url 'products'}"
 !!!local variable 'query' referenced before assignment !!! """ fixed with query=None. 
2. Problem: 
Local variable 'categories' referenced before assignment. 
Solution: 
Needed to create variable category=None before assigment.
3. Problem: 
Method Not Allowed (GET): /checkout/
[09/May/2022 10:38:57] "GET /checkout/ HTTP/1.1" 405 0
Solution:
Moved @require_POST at the begining of all function in the views.py.
4. Problem:
"POST /checkout/wh/ HTTP/1.1" 400 63.
Solution:
Couldn't set the secret_wh_key so instead of writing "set wh" in terminal used "export wh".
5. Problem:
ProgrammingError at /admin/login/
relation "profiles_userprofile" does not exist
LINE 1: ...e", "profiles_userprofile"."default_country" FROM "profiles_...
Solution:
1.Make sure your manage.py file is connected to your mysql database
2.Use this command to backup your current database and load it into a db.json file:
python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
3.Connect your manage.py file to your postgres database
4.Then use this command to load your data from the db.json file into postgres:
python3 manage.py loaddata db.json

[`Back to top ⇧`](#vigour-page)

## Automated Testing

### Code Validation
The [FreeFormatter Validator](https://www.freeformatter.com/html-validator.html) service was used to validate the `HTML` code used.
The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) service was used to validate the `CSS` coded used.


**Results:**

- Not added at the moment.




[`Back to top ⇧`](#vigour-page)

## Deployment

Information coming soon!

[`Back to top ⇧`](#vigour-page)

## Credits 

* All the credits is in the Html code on the side of every image.

# Technologies Used
### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")
- [Java Script](https://en.wikipedia.org/wiki/JavaScript "Link to JS Wiki")
- [Python](https://www.python.org/ "Link to Python Original")
- [Django](https://www.djangoproject.com/ "Link to Django Original")

[`Back to top ⇧`](#vigour-page)

### Frameworks, Libraries & Programs Used
- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/ "Link to Bootstrap page")
     - Bootstrap was used to implement the responsiveness of the site, using bootstrap classes.
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
    - Google fonts was used to import the fonts "Lora" into the style.css file.
- [JQuery](https://jquery.com/ "Link to Jquery")
    - JQuery was used to simplify Java Script code.
- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
     - Font Awesome was used to import icons mute/unmute.
- [Git](https://git-scm.com/ "Link to Git homepage")
     - Git was used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project after pushing
- [Figma](https://www.figma.com/ "Link to Figma homepage")
     - Figma was used to create the wireframes during the design phase of the project.
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used in order to see responsive design throughout the process and to generate mockup imagery to be used.


[`Back to top ⇧`](#vigour-page)

## Acknowledgements

- I would like to thank my friends and family for their valued opinions and critic during the process of design and development.
- I would like to thank my mentor, Seun, for her invaluable help and guidance throughout the process.
- I would like to thank tutor support for showing me the way with my issues.

[`Back to top ⇧`](#vigour-page)