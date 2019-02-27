# Cookbook-MNR
A Cookbook website running in Python-Django, Ricetta.
Content reference/source: https://www.allrecipes.com

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

3. Models:
    - Profile
        - avatar
        - usertype
    - Category
        - name
    - Recipe
        - name
        - description
        - added_by (FK)
        - date_added
        - category
        - picture
        - preparation time
        - cooking time
        - ready time
        - servings
    - Review
        - User (FK)
        - recipe (FK)
        - rating
        - datetime
        - comment
    - Step
        - recipe (FK)
        - date_added (will determine the order of steps)
        - description
    - Ingredient
        - recipe (FK)
        - date_added
        - ingredient (quantity is already included here.)

4. Users:
    - Admin user (Django default)
    - Plain user (Only be able to review/Optional)

# Notes

1. Add users to group programmatically: http://www.re-cycledair.com/programmatically-adding-users-to-groups-in-django
2. Understanding about user permissions and groups: https://micropyramid.com/blog/understanding-django-permissions-and-groups/
3. Django Paginator: https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
4. Django OneToOne: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
5. TimeField: https://stackoverflow.com/questions/33078366/durationfield-format-in-a-modelform