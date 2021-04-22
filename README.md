## PopularInt
- You can register and log in
    - you don't choose a username, your username will be generated from random consonants (e.g. "knwlhfk might be a username")
        - use consonants only to avoid it making inappropriate words by random
    - or, maybe if you can set up oauth with github, it will be their github username
- You can make "posts"
    - instead of choosing text/image to post, you pick an integer to post
        - make a limit to the number of digits you can use, or else people will start writing things in binary
    - you are supposed to post an integer that you like
    - e.g. you post "21" - your post is "I like the integer 21"
    - someone else can also post "21", and now the number 21 has two upvotes
    - to clarify, people can't like your post, they can just like (post about) the same number that you liked
- there will be a page that shows the most popular integers, based on how many votes they have
- for each integer, there will be a page that lists the people who like that integer
- there is a page for each person, which shows which integers they like
- What is the point of this? None, it's just a test project for Django
### Trying it out
```bash
git clone https://github.com/michaelskyba/PopularInt.git
cd PopularInt
python manage.py runserver
```
### Disclaimer
The commit messages are quite a mess because I'm making this project while
learning the framework, so I don't really know what I'm doing...
