# **Watch List**

### **Introduction**

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

Site Admin only:

9. As a site admin I can approve comments before they are posted to the website so that I can ensure there are no spoilers
10. As a site admin I can create, read, update and delete content so that I can manage the list.
11. As a site admin I can mark shows / films as watched so that I can keep the list current.

### **Structure Plane**
The structure of the page was carefully planned out when designing the website. I wanted to keep it similar to a standard blog site structure ensuring the website is easy to navigate and content is positioned exactly where the user expects it to be. 
#### **Information Architecture**
When planning the media detail page I put myself in the users shoes to understand what information would be most important to the user and how they will view it. I decided with using the image first, below that was the title and thumbs up button. Following from that was the badges displaying the media platform, genre and type of media (TV show or Movie). When deciding on something to watch myself, these three badges are very important in the decision making process. Below that is the media description which was placed last as the user then has the choice to read it if they are interested. 
#### **Content Organisation:**
The media list was created using cards which stacked nicely above each other in a mobile view making it easy to scroll through the list. Pagination was used to organise the list and comments so they are easy to read.

### **Skeleton Plane**
Initial wireframes helped to visualise the website and help with feature placement. The final website did not differ too much from the original wireframes. The choice was made to use landscape images instead of portrait as this improved the card structure and page layout.
### **Surface Plane**
#### **Colours:**
A colour pallet was created using Colour. The main colours used throughout the project are #000000 and #E50914 as these symbolise a cinema chairs which are shown in the background image.

#### **Fonts::**
Google Fonts was used to pick the fonts for the website. I chose ‘Oswald’ for the logo as I wanted something punchy in capital letters to grab the viewers attention. I then chose ‘Lato’ for the main font of the page as I wanted something more delicate and not too distracting.

#### **Icons:**
Font Awesome was used for the icons on the page. The add is symbolised by a plus sign, directions symbolised with arrows, the delete button with a trash can and the edit button by an edit icon. The use of these icons ensure the buttons look cleaner and a sale feature was used with the hover effect so users know they can interact with it.

#### **Database Models:**
The Media model was created after building a relationship diagram to better understand and visualise the database. The Comment and RecommendBox was built further along in the project with help from the Media relationship diagram.
#### **CRUD Functionalities:**
CRUD functionalities was integral to this project. It was considered throughout the design process and was fulfilled with add, edit and delete buttons and the media list. These are explained in more detail in the features section.

Create: The site admin can create a new media to add to the watch list.

Read: Anyone can read through the watch list and media details.

Update: The site admin can edit existing media listings.

Delete: Only the site admin can delete media listings. 

#### **Features:**


### **Technologies Used** 
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) was used as the building block of the content and structure of the project.
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics) was used to style the web content across the page.
- [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) was used for layout and styling the pages and content.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) was used to auto dismiss the pop up messages.
- [Python](https://www.python.org/) was the core programming language used to write all of the code to make it fully functional.
- [Django](https://www.djangoproject.com/) framework was used to build the project and its apps.
- [Gunicorn](https://gunicorn.org/) was used to run the application.
- [Pyscopg2]()
- [Coolors](https://coolors.co/) was used to create the colour palette.
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) was used for account registration.
- [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used for get data from the user.
- [Summernote](https://summernote.org/) was used to create WYSIWYG editors online.
- [Cloudinary](https://cloudinary.com/) was used to store static files and images.
- [Wireframes]()
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
### **Feature Testing** 
### **HTML Validator** 
### **CSS Validator** 
### **Python Lint** 
### **Responsivness**
### **Lighthouse**
### **Unfixed Bugs**

## **Deployment** 
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