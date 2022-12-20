# Blue White FanBlog

Blue White FanBlog is a website for fans of the fotball club IFK Gothenburg. The site is simple but yet effective and design to give the fans quick and easy information written by admin and or the website crew. The Site Contains one main page that will display news and articles about whats going on in and outside the Club. The side gives the user an ability to login, read and comment the posts/news 

The site is built via github/django

![Picture of Ifk Gothenburgs club emblem](media/love_maths_mockup.png)

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

![Logo](media/love_maths_logo.png)

- __The scrollable post page__

  - The site user can scroll through all the different post that is available
    - Only loggedin users will be able to click in to the posts and comment/like

![Game](me)

- __The Footer__

  - The footer will contain content for the logged in user
  - The footer will exand in height as the page content decreases to give the page more styling

![Question](media/love_maths_question.png)

- __Inside the post view__

  - This page will let authenticated users to comment/read/like the post. 

![score](media/love_maths_answer.png)

- __The comments__

  - Users will be able to create,delete,edit and view their comments for every post

- __The Login__

  - User will be able to create their own user with username and password
    - The user can choose to login via their github account


### Features Left to Implement

- Comment thread page
  - The site user can start a comment thread to discuss their opinions on certain matters

- More social account login providers

- User who is authenticated and got the right permission can create posts 
  - give some users the ability to create posts without entering the admin panel

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
  - The message for completed editing of comment does not work propperly
  - Whitespace allowed for send email name (Fixed)
  

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


### Validator Testing 

- HTML
    - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-maths%2F)
- CSS
    - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-maths%252F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
- JavaScript
    - No errors were found when passing through the official [Jshint validator](https://jshint.com/)
      - The following metrics were returned: 
      - There are 11 functions in this file.
      - Function with the largest signature takes 2 arguments, while the median is 0.
      - Largest function has 10 statements in it, while the median is 3.
      - The most complex function has a cyclomatic complexity value of 4 while the median is 2.

### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to Heroku. The steps to deploy are as follows: 
  - In the Heroku app, navigate to the create new app 
  - The app was created 
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-maths/


## Credits 

In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 