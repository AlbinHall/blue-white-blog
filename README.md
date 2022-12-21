# Blue White FanBlog

Blue White FanBlog is a website for fans of the fotball club IFK Gothenburg. The site is simple but yet effective and design to give the fans quick and easy information written by admin and or the website crew. The Site Contains one main page that will display news and articles about whats going on in and outside the Club. The side gives the user an ability to login, read and comment the posts/news 

The site is built via github/django

![responsive site view](media/responsive.png)

## Features 

### Main page
- The main page contains of navbar with the ability to log in and a overview of the posts available
    - The site user can log in via google and github for smooth and easy login
- The blog posts are clickable and redirects the user to the post details.
    - The post details is the place where fans of the fotball club can read and commit the post
    - The comments are deleteable and editable for the creater of the comment
        - The comment section is a place for fans to express their feeling about the post
- The site user can send email to the owner of the page via a link in the foter
    - The site user may have some useful informationn about improvement of the site etc
    - the site user may want to be a writer of posts  
    - The email is only connected to mailtrap for testing as I dont want any mail to my adress

### Existing Features

- __The starting page nav__

  - The navbar is made with bootstrap class and contains links so the user can login/logout/register
    - For logged in users there will be an option to reach out to page owner via mail
    - The loggedin user will be able to se their name under the navbar

![Navbar](media/The-navbar.png)

- __The scrollable post page__

  - The site user can scroll through all the different post that is available
    - Only loggedin users will be able to click in to the posts and comment/like

![starting page](media/starting-page.png)

- __The Footer__

  - The footer will contain content for the logged in user
  - The footer will exand in height as the page content decreases to give the page more styling

![the footer](media/footer.png)

- __Inside the post view__

  - This page will let authenticated users to comment/read/like the post. 

![post detail view](media/post-detail.png)

- __The comments__

  - Users will be able to create,delete,edit and view their comments for every post

![comment section](media/comment-section.png)

- __The Login__

  - User will be able to create their own user with username and password
    - The user can choose to login via their github account

![The login section](media/login.png)

- __The email form__

  - User will be able to send email directly from the site

![The send email section](media/email.png)

### Features Left to Implement

- Comment thread page
  - The site user can start a comment thread to discuss their opinions on certain matters

- More social account login providers

- User who is authenticated and got the right permission can create posts 
  - give some users the ability to create posts without entering the admin panel

- Javascript function instead of page refresh for comments and like etc

## Testing 

The testing has been done manually both under the development process but also after the product was finnished developed

- __Manually testing that has been done__
  - Check so that users can't create accounts/send email without adding the correct information
  - Check so that the site users that is not authenticated can visist the blog posts
    - This has been made so that the un autherised site user can visit the first page but a modal will apear when clicking the posts
  - Check so that authenticated users can't change or delete comments they havent made them self
  - Check so that all the colors works well togheter and does not disturb the user
  - Check so that messages appear to the user when something has been deleted/created or when the user login/logout etc
  - Check so that the send email function works and dont allow harmful content or whitespace for name
  - Check so that the mobile version of the site works well and look good

- __Bugs__
  - Whitespace allowed for send email name (Fixed)
  

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


### Validator Testing 

- HTML
    - No errors were returned when passing through the official except for marks on using of '{}' [W3C validator](https://validator.w3.org/)
- CSS
    - No errors were found when passing through the official [(Jigsaw) validator](http://jigsaw.w3.org/css-validator/validator$link)
- JavaScript
    - No self written Javascript code exist to be tested

### Unfixed Bugs


## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to Heroku. The steps to deploy are as follows: 
  - First the project was started in gitpod
    - In gitpod I installed the absolute necissery packages and made an env.py file and a requirements.txt
  - In herkoku I created a new app and added The neccessary config vars such as:
    - the secret key, Database_url and the cloudinary_url (storage of image)
  - The Database was obtained from elephantsql and is hosted from Amazon server in Sweden
  - After the config vars where setup the site was now ready for deployment through heroku

The live link can be found here - https://code-institute-org.github.io/love-maths/


## Credits 

### Content 

- The text for the one available post was taken from [expressens news site](https://www.expressen.se/sport/fotboll/allsvenskan/erik-sorga-lamnar-ifk-goteborg-for-bulgarien/)
- Instructions on how to implement email function was taken from [Codie with stein](https://www.youtube.com/watch?v=dnhEnF7_RyM&ab_channel=CodeWithStein)
- Whitespace validation for the email form was taken from[stackoverflow](https://stackoverflow.com/questions/332102/what-is-the-best-way-to-catch-and-show-an-error-if-user-enters-only-whitespace-i)
- Update comment and delete comment view was inspired from[geeksforgeeks](https://www.geeksforgeeks.org/updateview-class-based-views-django/)
- overall help was taken from Tutors at code institute
- The icons where taken from [Font Awesome](https://fontawesome.com/)
- The fonts where taken from [Google Fonts](https://fonts.google.com/about)
- Styling of page is made with [bootstrap](https://getbootstrap.com/)

### Media

- The placeholder image is taken from [picsum](https://picsum.photos/200)
- picture from blogpost is taken from [fotboll direkt](https://fotbolldirekt.se/2022/05/29/erik-sorga-om-att-ha-blivit-publikfavorit-i-ifk-goteborg-trots-att-han-knappt-spelat)
