import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Couch.settings')

import django
django.setup()
from dice.models import User,Game,Forum,Category

def populate():


    Game =[
         { "Title" : "Magic: The Gathering",
         "Game Type" : "Card",
         "Game Genre": "LGC",
         "Players": "2"},
         { "Title" : "Settlers of Catan",
         "Game Type" : "Board Game",
         "Game Genre" : "Resource Management"},
         { "Title" : "Secret Hitler",
         "Game Type" : "Board Game",
         "Game Genre" : "Party Game",
         "Players" : "8"},
         {"Title" : "Dragon Age: Origins",
         "Game Type" : " Board Game ",
         "Game Genre" : "Role Playing Game",
         "Players" : ""},
         {"Title" : "Ticket To Ride",
         "Game Type" : "Board Game",
         "Game Genre" : "Eurogame",
         "Players" : "5"},
         {"Title" : "Lords of Waterdeep",
         "Game Type" : "Board Game",
         "Game Genre" : "Meeple Management",
         "Players" : "5"},
         {"Title" : "Elder Sign",
         "Game Type" : " Dice ",
         "Game Genre" : "Cooperative",
         "Players" : "4" },
         {"Title" : " Smash Up ",
         "Game Type" : "Card",
         "Game Genre" : "LGC",
         "Players" : "4"}
    ]



    User =[
          {"User Name" : "DIO"},
          {"User Name" : "Dante"},
          {"User Name" : "Nero"},
          {"User Name" : "Virgil"},
          {"User Name" : "V"}
    ]


    Forums = [
          {"Post Title" : "Help me.",
          "Post Type" : "Advice" },
          {"Post Title" : "Stop praying for my grandpa, you're making him too powerful!",
          "Post Type" : " Joke "},
          {"Post Title" : "Miracle child festival 6: Stop me from burying your child, help me bury your child.",
          "Post Type" : "Discussion"},
          {"Post Title" : "Day One Purchase Regret",
          "Post Type" : "Review"},
          {"Post Title" : "Steel Ball Run",
          "Post Type" : "Misc"},
          {"Post Title" : "Gamer Seeking Gamer (GLASGOW)",
          "Post Type" : "Game Search"}
    ]

    cats = {"Game" : {"Game" : Game},
            "User" : {"User" : User},
            "Forums" : {"Forums" : Forums} }






def add_game(cat,title, GameType, GameGenre, players=0, Views=0, Endorsements=0):
    p = Game.objects.get_or_create(category=cat, game_name=title)[0]
    p.game_type=GameType
    p.game_genre=GameGenre
    p.player_number=players
    p.game_views=Views
    p.game_endoresments=Endorsements
    p.save()
    return p

def add_user(cat, UserName, UserEmail, Views=0, Endorsements=0):
    s = User.objects.get_or_create(category=cat, user_name=UserName)[0]
    s.user_email=UserName
    s.user_views=Views
    s.user_endorsements=Endorsements
    s.save()
    return s

def add_forum(cat, PostTitle, PostType, Views=0, Endorsements=0):
    q = Forum.objects.get_or_create(category=cat, post_title=PostTitle)[0]
    q.post_type=PostType
    q.post_views=Views
    q.post_endorsements=Endorsements
    q.save()
    return q

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


if __name__ == '__main__':
    print("Starting pop script..")
    populate()
