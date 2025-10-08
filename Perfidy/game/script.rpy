# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ace = Character("Ace Wright")
define cynthia = Character("Cynthia Carver")
define gail = Character("Gail Mourne")
define vincent = Character("Vincent Earl Holmes")
define dantes = Character("Dantes Medici")
define karen = Character("Karen Medici")
define russel = Character("Russel Smith")
define christian = Character("Christian Caller")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    gail "Ace where are you???"

    hide eileen happy

    with dissolve

    show bush

    ace "Look Gail. I'm a bush now"

    # These display lines of dialogue.

    ace "Test"

    cynthia "Test"

    gail "Test"

    vincent "Test"

    dantes "Test"

    karen "Test"

    russel "Test"

    christian "Test"

    jump end




label end:
    return