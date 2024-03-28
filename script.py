# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default player_name = "Player"
default choice_black = False
default choice_white = False
default choice_scarlet = False
default choice_mustard = False
default choice_green = False
default choice_peacock = False
default choice_plum = False
default picklistscene1 = []
default picklistscene3 = []
default choice_Library = False
default choice_StudyRoom = False
default choice_BilliardRoom = False
default choice_Bedroom = False
default choice_Conservatory = False
default choice_Kitchen = False
default positive_Point = 0
default negative_Point = 0

define narrator = Character("narrator")
define black = Character("Dr.Black")
define white = Character("Mrs.White")
define scarlet = Character("Miss Scarlet")
define mustard = Character("Colonel Mustard")
define green = Character("Mister Green")
define peacock = Character("Mrs.Peacock")
define plum = Character("Professor Plum")
define center_big = Transform(zoom=2.5, xalign=0.5, yalign=0.6)
define zoom = Transform(zoom=1.2, xalign=0.5, yalign=0.6)
define zooom = Transform(zoom = 0.9, xalign=0.5, yalign=0.6)

# The game starts here.

label start:
    scene escaperoom
    "Welcome to the Dr.Black's Birthday Party"
    black "Welcome everyone! I am glad to see that you all have arrived 
    here safely to my birthday party. It is not everyday that you turn 
    80 years old. As my mother said, “Getting older is like a garage sale - 
    some treasures, a few surprises, and occasionally you find something you 
    just can’t remember where it came from!” So, here’s to all the priceless 
    memories and the occasional mystery in life!"
    narrator "Dr.Black winks playfully, sparking chuckles among the guests"

    "Hey, What is your name?"

    $ player_name = renpy.input("Enter your name: ")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Player"

    "Hello [player_name], it's time to make a choice."

    "You just arrived at the party and saw familiar faces around."
    jump talk_to_characters

label talk_to_characters:
    if choice_white and choice_scarlet and choice_mustard and choice_green and choice_peacock and choice_plum:
        jump continue_story
    menu:
        set picklistscene1
        "Who would you like to talk to?"
        "Mrs.White":
            if (not choice_white):
                $ choice_white = True
                jump white
        "Miss Scarlet":
            if (not choice_scarlet):
                $ choice_scarlet = True
                jump scarlet
        "Colonel Mustard":
            if (not choice_mustard):
                $ choice_mustard = True
                jump mustard
        "Mister Green":
            if (not choice_green):
                $ choice_green = True
                jump green
        "Mrs. Peacock":
            if (not choice_peacock):
                $ choice_peacock = True
                jump peacock
        "Professor Plum":
            if (not choice_plum):
                $ choice_plum = True
                jump plum
    jump check_characters
label check_characters:
    # After talking to a character, check if there are others left to talk to
    if not all([choice_white, choice_scarlet, choice_mustard
    , choice_green, choice_peacock, choice_plum]):
        "You can still talk to other characters."
        jump talk_to_characters

label white:
    "[player_name]""Ah, Mrs. White, could you spare a moment?"
    show mswhite at zooom
    white "Oh, [player_name]! Certainly, what can I do for you?"
    scene escaperoom
    "[player_name]"" I couldn’t help but notice you were preparing tea all 
    by yourself! Would you like any assistance?"
    show mswhite at zooom
    white "Oh, no, thank you. Dr. Black requested tea for everyone to be served 
    promptly at eight. I’m ensuring everything is prepared to his standards."
    scene escaperoom
    "[player_name]""Ah, I didn’t realize Dr. Black had such a penchant for 
    punctuality. I must say, you attention to detail is quite impressive, 
    Mrs. White."
    show mswhite at zooom
    white "Thank you. It’s all part of the job here at the Tudor mansion."
    scene escaperoom
    "[player_name]""Speaking of which, how has the Tudor mansion been lately?"
    show mswhite at zooom
    white "Now that you mention it, there have been some whispers 
    among the staff, but it’s all rumors. Nothing to be concerned about."
    scene escaperoom
    "[player_name]""Curious indeed. Thank you for speaking with me tonight. 
    I will take my leave, there is someone else I need to speak to."
    show mswhite at zooom
    white "Of course, [player_name]. If there's anything else you require, 
    please don't hesitate to ask."
    scene escaperoom
    narrator "Mrs. White resumes her preparations of tea."
    jump talk_to_characters
label scarlet:
    "[player_name]""Hey Miss Scarlet, how's it going for you?"
    show scarlett at center_big
    scarlet "Not that great honestly, I am still very tired from the long
    trip. But I would do anything for Dr.Black"
    scene escaperoom
    "[player_name]" "That is very considerate of you."
    show scarlett at center_big
    scarlet "Of course, he's the man who can make my dreams come true!"
    scene escaperoom
    "[player_name]" "He can make all of our dreams come true."
    narrator "Miss scarlet looks at you suspiciously, and walks away"
    jump talk_to_characters
label mustard:
    mustard "I have never seen you here before. Who are you?"
    "[player_name]""I am [player_name], Dr. Brown’s friend. It’s a pleasure to 
    meet you Colonel Mustard, I have heard many great stories about you."
    mustard "Pleasure, you say? You civilians often lack the grit and 
    understanding that comes from facing the horrors of war. Lessons learned
    through bloodshed and sacrifices are not easily grasped by those who have 
    not walked that path. Keep your wits about you, young one. This world has 
    its own set of rules, and it’s best not to stray too far from them."
    narrator "Colonel Mustard gives a dismissive nod and strides away."
    jump talk_to_characters
label green:
    green "Well, well, if it isn't [player_name]. Always a pleasure to see
    familiar face, especially in a crowd like this"
    "[player_name]" "Good to see you too, Mister Green. How have you been?"
    green "Oh, you know, keeping busy. Business never sleeps, as they say. 
    But enough about me, what brings you to this party? Got any interesting 
    stories to share?"
    "[player_name]" "Oh, just the usual. Work, family, you know how it goes."
    green "Is that so? Well, I’ll bet you’ve got more going on beneath the 
    surface that you let on. You always struck me as the mysterious type."
    "[player_name]" "Really? I don't know what you mean"
    green "Come now, [player_name], we both know there’s more to you than meets 
    the eye. Just remember, if you ever need a friend in high places, you know 
    where to find me."
    "[player_name]" "Thanks, Mister Green. I'll keep that in mind."
    jump talk_to_characters
label peacock:
    peacock "Ah, you’ve made it, have you? I suppose even the likes of you 
    can manage to secure an invitation to such an event."
    "[player_name]" "Indeed, Mrs. Peacock. It’s always a pleasure to be 
    part of these gatherings."
    peacock "Pleasure indeed, dear. It’s delightful to see new faces adding 
    to the charm of the evening."
    "[player_name]" "Your grace and elegance truly set the tone for such 
    occasions, Mrs. Peacock."
    peacock "Oh, you flatter me, my dear. It’s simply a matter of upholding the 
    standards one is accustomed to. Now, do enjoy yourself and mingle with the 
    other guests. I shall catch up with you later in the evening."
    jump talk_to_characters
label plum:
    "[player_name]" "Hi Professor! How has school life been treating you?"
    plum "[player_name] ! It is so good to see you again! You were the brightest 
    student I ever had, and I am excited to see how life has shaped you. 
    By the way, have you seen my glasses? I misplaced them somewhere, 
    but I can’t seem to find them."
    "[player_name]" "Professor, your glasses are in your hands."
    plum "Oh...right! Sorry, I forgot. Thank you [player_name], my
    brightest student!"
    jump talk_to_characters
label continue_story:
    #story continues after all the choices has been made

    scene escaperoom
    "[player_name]""Happy Birthday Dr.Black!"
    show drblack at zoom
    black "Thank you so much [player_name]! I am glad you were able to make it
    Last time we spoke...you seemed very anxious. But I hope things are better 
    now. Grab a drink, relax, and enjoy the party!"
    scene escaperoom

    play audio "lights.mp3"

    scene black

    #audio
    #audio

    narrator "You run towards the light switch, flicking it up."

    #audio

    "[player_name]" "Dr.Black!"
    narrator "The other party members rush into the room. Only to discover Dr.Black
    dead on the floor."
    peacock "YOU KILLED HIM"
    "[player_name]""It wasn't me."
    mustard "I know a murderer when I see one. And you [player_name], are one!"
    "[player_name]" "I told you, it wasn't me"
    narrator "Suddenly, you are on the floor with Colonel Mustard restraining your 
    hands behind your back."
    green "Now now, let's not be too hasty in our judgements. Colonel Mustard,
    as military man, you understand the importance of thorough investigation
    and evidence before accusing someone of such a grace act. Let's approach
    this with the precision and logic that you, Colonel, are so familiar with."
    white "I agree with Mr.Green. Lets not jump to conclusions. [player_name]
    can you tell us what happened?"
    "[player_name]" "I don't know. The lights went out and I rushed to turn 
    them back on. I remember hearing the opening and closing of a door. And 
    the next thing I knew, Dr.Black was dead"
    white "We need this murderer to be caught as soon as possible. 
    Everyone, split up and search for clues."

    narrator "The search begins!"




label search_rooms:
    if choice_Library and choice_StudyRoom and choice_BilliardRoom and choice_Bedroom and choice_Conservatory and choice_Kitchen:
        jump more_story
    menu:
        set picklistscene3
        "Which Room would you like to search first"
        "Library":
            if (not choice_Library):
                $ choice_Library = True
                jump Library
        "StudyRoom":
            if (not choice_StudyRoom):
                $ choice_StudyRoom = True
                jump StudyRoom
        "BilliardRoom":
            if (not choice_BilliardRoom):
                $ choice_BilliardRoom = True
                jump BilliardRoom
        "Bedroom":
            if (not choice_Bedroom):
                $ choice_Bedroom = True
                jump Bedroom
        "Conservatory":
            if (not choice_Conservatory):
                $ choice_Conservatory = True
                jump Conservatory
        "Kitchen":
            if (not choice_Kitchen):
                $ choice_Kitchen = True
                jump Kitchen
    jump check_rooms

label check_rooms:
    # After talking to a character, check if there are others left to talk to
    if not all([choice_Library, choice_StudyRoom, choice_BilliardRoom
    , choice_Bedroom, choice_Conservatory, choice_Kitchen]):
        "You have more rooms to search"
        jump search_rooms
label Library:
    narrator "You see Miss Scarlet pick up an ancient-looking book and start to skim
    through it."
    scarlet "...chronoflora..."
    "[player_name]" "What was that Miss Scarlet?"
    scarlet "[player_name] You scared me! Ignore what I said, it's just
    the name of a french perfume I recently bought"
    "Pick the response that would make them think
    you're not the murderer"
    menu:
        "It smells really delightful on you":
            $ positive_Point += 1
            scarlet "Thank you! Maybe after all of this is over, 
            we can go perfume shopping together."
        "What is the book you are reading?":
            $ negative_Point += 1
            scarlet "Nothing important, just a book about perfumery."
            "[player_name] A book that happens to be named Chronoflora. Why 
            are you so obsessed with it?"
            scarlet "Why are you so fixated on prying into my interests?
            Can't you see we have more pressing matters at hand? Instead of 
            pestering me with your questions, perhaps you should focus on aiding
            our investigation. The sooner we uncover the truth behind this 
            heinous crime, the sooner we can bring justice to our
            host and ensure the safety of everyone else."
    narrator "Miss Scarlet puts the book into her handbag."

label StudyRoom:
    mustard "It's you again."
    "Pick the response that would make them think
    you're not the murderer"
    menu:
        "positiveresponse filler":
            $ positive_Point += 1
        "negativeresponse filler":
            $ negative_Point += 1
    jump search_rooms
label BilliardRoom: 
    "Pick the response that would make them think
    you're not the murderer"
    menu:
        "positiveresponse filler":
            $ positive_Point += 1
        "negativeresponse filler":
            $ negative_Point += 1
    jump search_rooms   
label Bedroom:
    "Pick the response that would make them think
    you're not the murderer"
    menu:
        "positiveresponse filler":
            $ positive_Point += 1
        "negativeresponse filler":
            $ negative_Point += 1
    jump search_rooms
label Conservatory:
    "Pick the response that would make them think
    you're not the murderer"
    menu:
        "positiveresponse filler":
            $ positive_Point += 1
        "negativeresponse filler":
            $ negative_Point += 1
    jump search_rooms
label Kitchen:
    "Pick the response that would make them think
    you're not the murderer"
    menu:
        "positiveresponse filler":
            $ positive_Point += 1
        "negativeresponse filler":
            $ negative_Point += 1
    jump search_rooms
label more_story:
    "hello"
