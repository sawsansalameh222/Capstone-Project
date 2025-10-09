# Capstone-Prject: Recipe Sharing Platform 🍜


## Project Desription
This project is a simple website where users can share their favorite cooking recipes.  
Users can sign up, log in, and add their own recipes with ingredients, steps, and an optional image... etc.
Everyone can also view other users’ recipes and get cooking ideas.  
Each user can edit or delete their own recipes anytime.

## Tech stack
- user registration log in and logout
- CRUD (add, edit, delete ) recipes 
- view all recipes
- in "my recipes" page you can view only your recipes
- Html, css 

## User Stories
1. as a visitor i want to create an account to share my own recipes on the website 
2. user log in and log out to access my own recipes 
3. user add a new recipe and share it with other users
4. user can also edit his own recipes so he can update information or correct mistakes
5. user can delete or remove any of his unwated recipes 
6. visitor view a list of recipes in page in the navbar contains all recipes
7.  visitor view a single recipe with details of that recipe like see ingredients and steps...etc.
8. user can see only his recipes manage and organize them 
9. admin manage all recipes and users to maintain the paltform and remove inappropriate content

## ERD 
![ERD](./images/Untitled.png)
## Relationships
I have 3 models  (User, Reciepes , Cateogry )
- One user can have many recipes 
- Each recipe belongs to one user
- each recipe belongs to one categor
User (1) ----< (many) Recipe (many) >---- (1) Category