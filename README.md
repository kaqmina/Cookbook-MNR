# Cookbook-MNR
A Cookbook website running in Python-Django.

# Plan

1. Functions:
    - Add, edit, delete (status/archive), view recipe.
    - Able to review recipes. (Rate and review?)
    - Account pages. (Register and Login)
    - Average rating per recipe.

2. Templates:
    - Home page
    - Login page
    - List page (By category).
    - Detail page
    - Account page
    - Category addition page (?)

3. Models:
    - Category
        - name
    - Recipe
        - name
        - description
        - steps (?)
        - category
    - Review
        - User (FK)
        - recipe (FK)
        - rating
        - datetime
        - comment

4. Users:
    - Admin user (Django default)
    - Plain user (Only be able to review)

# Clarifications

1. Should the name of the reviewer be displayed?
2. Do we have to make a `User` model? if yes, how to integrate that with Django's built-in login system without redundancy?

# Notes

1. Add users to group programmatically: http://www.re-cycledair.com/programmatically-adding-users-to-groups-in-django
2. Understanding about user permissions and groups: https://micropyramid.com/blog/understanding-django-permissions-and-groups/