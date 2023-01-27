# **Watch List**

![Am I Responsive Image](/static/media/am-i-responsive.png)

### **Introduction**
Watch List is a list / blog website where the site admin can add TV shows or movies to the list they are planning to watch. Anyone can view the list but to use the recommend box, comment and give a thumbs up to your favouite things to watch you must sign up for an account. 

Watch List is a full stack website, created using HTML, CSS, Bootstrap, Python and Django. The purpose of the project was to create a fully functioning website with CRUD (Create, Read, Update and Delete) functionalities to manipulate the database created. The site owner is able to create, update and delete data managing the lists content and controlling what the user can view. 


## **User Experience**
## **5 Planes of User Experience** 

### **Strategy Plane**
The purpose of the website if for users to follow what TV shows/Movies their friend, loved one or colleague are planning to watch. Registering for an account allows them to join the discussion through comments, thumbs up and the recommendation box. 
#### **Creators Goals:**
- To create a website where users can view, comment and give a thumbs up to the shows on the list.
- Build online community 
- To allow the admin to add, update and delete listings in the front end.
- For the admin to approve comments to ensure no spoilers.
#### **Target Audience:**
- Media Studies Students 
- Film enthusiasts 
- A group of friends 
### **Scope Plane**
#### **Agile Development**
From the initial planning and wireframing to building the front and back end functionalities, Watch List was created using the agile approach. I used a GitHub project to build a Kanban board to help visualise the user stories from ‘Todo’ to ‘In Progress’ to ‘Done’. User stories that could not be completed were put into ‘Out of Scope’.

#### **User Stories**
User & Site Admin:

1. As a user / site admin I can view the watch list so that I can see what shows / films the admin is intending to watch.
2. As a user / site admin I can view comments so that I can read peoples thoughts on the show / film.
3. As a user / site admin I can add comments so that I can be involved in conversations about the show / films.
4. As a user / site admin I can view paginated list of things to watch so that I can easily look through the list.
5. As a user / site admin I can view recommended shows / films so that I can see which shows / films are the most popular.

User only:

6. As a user I can see more details on the show / film so that I can make an informed decision on whether to watch it.
7. As a user I can register and account so that I can comment and use the recommend button.
8. As a user I can click the recommend button so that I can interact with the content and help others find something to watch.
9. As a user I can make a recommendation so that I can share my favourite things to watch.

Site Admin only:

10. As a site admin I can approve comments before they are posted to the website so that I can ensure there are no spoilers
11. As a site admin I can create, read, update and delete content so that I can manage the list.
12. As a site admin I can read through the recommended list so that so I can see what the site users have recommended me to watch
13. As a site admin I can mark shows / films as watched so that I can keep the list current.

### **Structure Plane**
The structure of the page was carefully planned out when designing the website. I wanted to keep it similar to a standard blog site structure ensuring the website is easy to navigate and content is positioned exactly where the user expects it to be. 
#### **Information Architecture**
When planning the media detail page I put myself in the users shoes to understand what information would be most important to the user and how they will view it. I decided with using the image first, below that was the title and thumbs up button. Following from that was the badges displaying the media platform, genre and type of media (TV show or Movie). When deciding on something to watch myself, these three badges are very important in the decision making process. Below that is the media description which was placed last as the user then has the choice to read it if they are interested. 
#### **Content Organisation:**
The media list was created using cards which stacked nicely above each other in a mobile view making it easy to scroll through the list. Pagination was used to organise the list and comments so they are easy to read.

### **Skeleton Plane**
Initial wireframes helped to visualise the website and help with feature placement. The final website did not differ too much from the original wireframes. The choice was made to use landscape images instead of portrait as this improved the card structure and page layout.

![Wireframe List](/static/media/wireframe-list.png)
![Wireframe Detail](/static/media/wireframe-show.png)

### **Surface Plane**
#### **Colours:**
A colour pallet was created using Colour. The main colours used throughout the project are #000000 and #E50914 as these symbolise a cinema chairs which are shown in the background image.

![Colour Palette](/static/media/colour-palette.png)

#### **Fonts:**
Google Fonts was used to pick the fonts for the website. I chose ‘Oswald’ for the logo as I wanted something punchy in capital letters to grab the viewers attention. I then chose ‘Lato’ for the main font of the page as I wanted something more delicate and not too distracting.

#### **Icons:**
Font Awesome was used for the icons on the page. The add is symbolised by a plus sign, directions symbolised with arrows, the delete button with a trash can and the edit button by an edit icon. The use of these icons ensure the buttons look cleaner and a sale feature was used with the hover effect so users know they can interact with it.

#### **Database Models:**
The Media model was created after building a relationship diagram to better understand and visualise the database. The Comment and RecommendBox was built further along in the project with help from the Media relationship diagram.
![Database Relationship Diagram](/static/media/media-model-db.png)

#### **CRUD Functionalities:**
CRUD functionalities was integral to this project. It was considered throughout the design process and was fulfilled with add, edit and delete buttons and the media list. These are explained in more detail in the features section.

Create: The site admin can create a new media to add to the watch list.

Read: Anyone can read through the watch list and media details.

Update: The site admin can edit existing media listings.

Delete: Only the site admin can delete media listings. 

#### **Features:**
#### Logo:
- The logo is in the top left corner of all pages for consistency.
- Click the logo to return to the landing page (index.html)
![Watch List Logo](/static/media/logo.png)
#### Navigation:
- The navigation links are consistent on all pages.
- Underline hover effect to know which link to click on. 
![Navigation](/static/media/nav.png)
#### Landing Page:
- The landing page has a bootstrap jumbotron welcoming the user to the webiste. 
- A breif description of the purpose of the website and how it can be used.
- A button directing the user to the watch list.
![Landing Page Message](/static/media/landing-message.png)
#### Message Alert:
- Pop up messages appear to guide the user and improve user experience.
- Messages used for tasks such as sign in or out etc.
- The messages will disappear automatically.
![Alert Message](/static/media/alert-message.png)
#### Watch List Page:
- The page uses bootstrap cards to display whats on the watch list.
- Ordered in alphabetical order so the list is easy to browse.
- The list is fully responsive to all screen sizes. 
- Cards display an image, title and a thumbs up button.

Desktop:
![Watch List Desktop](/static/media/list-desktop.png)
Tablet:
![Watch List Tablet](/static/media/list-ipad.png)
Mobile:
![Watch List Mobile](/static/media/list-mobile.png)
#### Site Pagination:
- Site will paginate after 12 entries.
- This ensures the page is full but not overcrowded. 
- Buttons have hover effect making it easy to navigate between pages.
![Pagination Buttons](/static/media/pagination.png)
#### Add Button:
- This is only visable to the site admin. 
- Hover effect on button so user knows its intractable.
![Add Button](/static/media/add-btn.png)
#### Media Detail Page
- Content is ordered by: Image, Title, Thumbs Up Button, Badges, Description.
- The content is organised with the decision making process in mind.
![Media Detail Page](/static/media/media-detail.png)
#### Thumbs Up Button:
- Font Awesome icon used.
- Ouline for unliked and solid icon to display liked.
- Number next to the icon will display how many thumbs up the TV show / movie has.
- Only signed in users can recommend a TV show / movie with a thumbs up.
![Thumbs Up Outline](/static/media/thumbs-up-outline.png)
![Thumbs Up Solid](/static/media/thumbs-up-solid.png)
#### Back Button:
- This is placed above the image for easy navigation back to the list.
![Back Button](/static/media/back-btn.png)
#### Edit and Delete Button:
- This feature is only acessible to the site admin.
- Font Awesome icons and colours were used for familiarity.
![Edit and Delete Button](/static/media/edit-delete-btn.png)
#### Comment Section:
- Only registered users can comment. The 'Leave a Comment' box will not show if a user is not signed in. 
- Comments will be ordered by created on to show most recent comments first.
- Once a comment is left, a message will pop up saying the comment is waiting approval.
![Comment Section](/static/media/comment-section.png)
![Leave a Comment](/static/media/leave-comment.png)
#### Comment Approval:
- This is only accessible to the site admin.
- This acheives the creators goals and user stories to ensure no spoilers are posted.
![Comment approval](/static/media/approve-comments.png)
#### Add Form:
- Only the site admin can access this page.
- This django crispy forms interacts with the Media model in the database.
- Title is a required and unique field.
- Sumbit and Cancel button for navigation.
![Add Form](/static/media/add-form.png)
#### Edit Form:
- Only the site admin can access this page.
- Form has pre populated fields with the media details.
- Sumbit and Cancel button for navigation.
![Edit Form](/static/media/edit-form.png)
#### Delete Form:
- Only the site admin can access this page.
- Defensive programming used so things aren't deleted after one click.
- Site admin has option to cancel using button.
![Delete Form](/static/media/delete-form.png)
#### Recommend Box:
- This interacts with the RecommendBox model.
- Only users who are signed in can use this feature. 
- If user is not signed in a message will display asking them to register or sign in. 
- The data is stored in the admin section for the site admin to see the recomendations.
![Recommend Box](/static/media/recommend-box.png)
![Please Register or Sign In to use Recommend Box](/static/media/recommend-box-noaccess.png)

### **Technologies Used** 
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) was used as the building block of the content and structure of the project.
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics) was used to style the web content across the page.
- [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) was used for layout and styling the pages and content.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) was used to auto dismiss the pop up messages.
- [Python](https://www.python.org/) was the core programming language used to write all of the code to make it fully functional.
- [Django](https://www.djangoproject.com/) framework was used to build the project and its apps.
- [Gunicorn](https://gunicorn.org/) was used to run the application.
- [Pyscopg2](https://www.psycopg.org/docs/) was used to perform operations on PostgreSQL using python.
- [Coolors](https://coolors.co/) was used to create the colour palette.
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) was used for account registration.
- [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used for get data from the user.
- [Summernote](https://summernote.org/) was used to create WYSIWYG editors online.
- [Cloudinary](https://cloudinary.com/) was used to store static files and images.
- [Canva]() was used for the wireframes and relationship diagram.
- [Grammerly](https://www.grammarly.com/?utm_term=grammarly&gclid=EAIaIQobChMIpt7_l-i6-QIVme7tCh15kwxvEAAYASAAEgIJrPD_BwE&q=brand&utm_campaign=brand_core_row&utm_medium=cpc&matchtype=e&placement=&gclsrc=aw.ds&network=g&utm_source=google&utm_content=brandcorerow) was used to fix the grammar errors across the project.
- [GitHub](https://github.com/) was used to store the code for the project.
- [GitPod](https://www.gitpod.io/) was used as the development environment.
- [Git](https://git-scm.com/) was used for version control to commit and push to GitHub.
- [DevTools](https://developer.chrome.com/docs/devtools/) was used to fix errors and test responsivness.
- [Heroku](https://id.heroku.com/login) was used to deploy the project.
- [ElephantSQL](https://www.elephantsql.com/) was used to host the database.
- [Pep8](https://peps.python.org/pep-0008/) was used to test my code throughout the project.
- [Google Fonts](https://fonts.google.com/) was used to find the fonts used in the website.
- [Font Awesome](https://fontawesome.com/) was used for icons.
- [Favicon](https://favicon.io/) was used to create a favicon for the website.
- [Am I Responsive](https://ui.dev/amiresponsive) was used to obtain final images of my website across different device sizes.
- [Responsively](https://responsively.app/) was used to test the responsivness of the website across different screen sizes.
- [RawPixel](https://www.rawpixel.com/) was used to get the background image.



## **Testing**
### **User Stories** 
1. As a user / site admin I can view the watch list so that I can see what shows / films the admin is intending to watch.
- The Watch List is displayed to anyone who visits the site.
- Responsive styling makes this easy to view across all screen sizes. 
2. As a user / site admin I can view comments so that I can read peoples thoughts on the show / film.
- Comments are posted in the comment section once approved by the site admin.
- The comment section is accessible to anyone visiting the website.
3. As a user / site admin I can add comments so that I can be involved in conversations about the show / films.
- The leave a comment section allows registered users only to comment.
- The leave a comment box will not show if a user is not logged in.
4. As a user / site admin I can view paginated list of things to watch so that I can easily look through the list.
- The Watch List is easy to scroll through due to the responsiveness of the webiste.
- Arrow buttons direct the user to the next or previous pages.
5. As a user / site admin I can view recommended shows / films so that I can see which shows / films are the most popular.
- The recommended button and number of thumbs up is displayed next to the title on the card. 
- Users can view easily which post has the most thumbs up.
6. As a user I can see more details on the show / film so that I can make an informed decision on whether to watch it.
- The media detail page displays information such as, image, title, number of thumbs up, platform to watch, genre, type of media and description.
- The order of information on this page was created with the decision making process at the forefront.
7. As a user I can register and account so that I can comment and use the recommend button.
- The account registration is a simple design and process.
- Once registered the user has the ability to commennt, use the recommend box and use the thumbs up button to recommend their favourite TV shows / movies.
8. As a user I can click the recommend button so that I can interact with the content and help others find something to watch.
- The user must be registered and logged in to use this feature. 
- The number next to the thumbs up icon will display the most popualr content.
9. As a user I can make a recommendation so that I can share my favourite things to watch
- The recommend box feature allows users to post a recommendation to the site admin.
- This is only accessible for users who are logged in.
10. As a site admin I can approve comments before they are posted to the website so that I can ensure there are no spoilers.
- This is accessed through the admin site.
- It is important to ensure no spoilers are posted.
- Comments will be approved by the admin before posting to the main site. 
11. As a site admin I can create, read, update and delete content so that I can manage the list.
- These features are only acessible to the site admin. 
- The list is maintained through the addition and deletion of listings.
- Non-logged in users and registered users will not be able to see these button.
12. As a site admin I can read through the recommended list so that so I can see what the site users have recommended me to watch.
- This is only accessible through the sit admin.
- The data is stored in a list for which is easy to look through.
- Data will be displayd with title, author and date.
13. As a site admin I can mark shows / films as watched so that I can keep the list current.
- This feature was not implemented as I did not have the time to create it.
- This was placed in the 'Out of Scope' section of the kanban board. 

### **Feature Testing** 
- Logo link: No issues
- Nav link: No issues
- Go to Watch List Button: No issues 
- Recommend Box: No issues
- Messages auto delete: No issues
- Sign In: No issues
- Sign Out: No issues
- Register: No issues
- Recommend Thumbs Up: No issues
- Add Button: No issues
- Edit Button: No issues
- Delete Button: No issues
- Comment: No issues
- Approve Comment: No issues

### **Terminal Errors**
The terminal raised a few issues with my py files. 
- 13 Line too long
- 1 Blank line contains white space
- 1 Blank line at end
- 1 Trailing whitespace  
- 3 No new line at end of file

### **HTML Validator** 
[W3C HTML Validator](https://validator.w3.org/nu/)
Mutiple HTML pages were run through the validator. Multiple warning were raised abount the comments on the HTML pages.
- 2 error: No li element in scope but li end tag seen.
- 11 error: Duplicate ID card-body-border
- 11 error: Duplicate ID title-underline 
- 7 error: The element a must not appear as a decendant of the button element.
- 2 error: The element input must not appear as a decendant of the button element.


### **CSS Validator** 
[W3C CSS Validator](https://validator.w3.org/nu/)
Mutiple pages were tested through the CSS Validator. Warnings were raised again regarding the comments.
- 1 error: The element a must not appear as a decendant of the button element. X

### **Python Linter** 
Python Linter was used to check for erros in my py files. The only erros retuned were on the urls.py file saying the lines were too long. I attempted to shorten the path by spreading it accross multiple lines, however the Python Linter still says its too long.
![Python Linter Errors on urls.py](/static/media/python-linter.png)

### **Responsivness**
The responsiveness of the website was tested throughout the project using devtools. I then used Responsively to test the website on different screen sizes.
Tablet and Desktop:
![](/static/media/responsively-home-desktop.png)
![](/static/media/responsively-list-desktop.png)
Mobile:
![](/static/media/responsively-home-mobile.png)
![](/static/media/responsively-list-mobile.png)
### **Lighthouse**
Desktop:
![Lighthouse Desktop](/static/media/lighthouse-desktop.png)
Mobile:
![Lighthouse Mobile](/static/media/lighthouse-mobile.png)
### **Unfixed Bugs**
1. The element a must not appear as a decendant of the button element.
The buttons are in full working order and the paths are correct.
2. The element input must not appear as a decendant of the button element.
The buttons are in full working order and the paths are correct.
3. Lines too long.
I attempted to shorted the path by spreading it across multiple lines. I did not want to shorten it any more as I did not want to tamper with the readability.

## **Deployment** 
The master branch of this repository is the most current version and was used for deployment.
#### **Code Institute Template**
1. Click 'Use This Template' button.
2. Name your resository and write a despcription (optional).
3. Click the 'Create Repository from Template' to create the repository.
4. Click the 'GitPod' button to create a new workspace.
5. When working on the project, ensure to open the workspace from GitPod, this will open your previous workspace ratehr than creating a new one.
6. Use the following commands to commit your work:
- 'git add' adds all the modified files to a staging area.
- 'git commit -m "Write commit message"' commits the changes to the local repository.
-'git push' pushes all your commited changes to your GitHub repository. 

#### **Django Setup**
1. Create an env.py file. 
2. Add the env variables to the env.py file, and add it to the .gitigrone to avoid disclosing any sensetive information.
3. Install project requirements - 'pip3 install requirements.txt'.
4. Apply database migrations - 'python3 manage.py migrate'.
5. Create superuser - 'python3 manage.py createsuperuser'.
6. The project can be run with - 'python3 manage.py runserver'.
7. Install database package with - 'pip3 install psycopg2'.
8. Intsall gunicorn - 'pip3 install gunicorn'
9. Create a Procfile, and add 'web: gunicorn watchlist.wsgi'.
10. Add host name to settings.py file - ALLOWED_HOSTS = ['<you-app-name>.herokuapp.com', 'localhost'].

#### **ElephantSQL Setup**
1. Open ElephantSQL.
2. Register or Log In.
3. Click 'Create New Instance'.
4. Create name and select region.
5. Confirm new instance by clicking 'Create Instance'.
6. Click the instance you created.
7. Copy URL to clipboard.
8. Paste it into your os.environ["DATABASE_URL"] = "enter url here" in env.py file.

#### **Heroku Deployment**
1. Open Heroku.
2. Register or Log In.
3. Click 'Create New App'.
4. Enter app name and select region.
5. Click 'Create App'.
6. Under the 'Deploy' tab, click the 'Github' icon and click 'Connect to GitHub'.
7. Enter your GitHub credentials.
8. Search for your repository and click 'Connect'.
9. In 'Settings' tab, scroll to 'Reveal Config Vars' and copy the ElephantSQL url from env.py file.
10. In config vars, set PORT to 8000 and add the SECRET_KEY and CLOUDINARY_URL from the env.py file.

### **Development**
#### **Fork**
1. Log into GitHub and click on repositry to download
2.  Click the 'Fork' button in the top right-hand corner 
3. Select a different owner if necessary
4. Click on 'Create Fork' 
5. The repository is now in your account and can be changed (Changes made to a forked repository will not affect the original).

#### **Clone**
1. Navigate to the main repository page.
2. Click on the 'Code' dropdown menu above the list of files.
3. Choose a method to copy the URL for the repository.
4. In the work environment, open Git Bash and change the current directory to target location for cloned repository.
5. Type 'git clone' followed by the copied URL and press 'Enter'.

#### **Download ZIP**
1. Log into GitHub and click on the repository to download.
2. Select 'Code' and click 'Download Zip'.
3. Once download is finished, extract ZIP file and use in local environment.

## **Acknowledgements**
I would like to thank my course mentor Chris Quinn for his support and guidance on this project.