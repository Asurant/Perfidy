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
    jump karenDeathRevealed

label karenDeathRevealed:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with None
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show gailConcept at left

    gail "Karen’s dead."

    show bush at right

    ace "Karen? Karen Medici? Daughter of Mr. Medici?"
    ace "That’s a bit bold, isn’t it, Gail."

    gail "I suppose."

    ace "After Mr. Smith was murdered, I reckoned our killer was becoming more… conspicuous, but this is a whole new level. "

    gail "Yeah."
    gail "So you reckon our killer might be financially motivated then?"

    ace "Perhaps. But that wouldn’t explain the death of Mr. Caller. He was neither financially stable nor well liked."

    #OI. Future me. Figure out how to make it so she's saying it quietly
    gail "Not that he’d be missed. (OI. Future me. Figure out how to make it so she's saying it quietly)"

    menu:
        "Pardon?":
            ace "Pardon?"
            gail "I meant nothing by it. Just that there were rumors of him harassing women."
            gail "I’ve mentioned this before."
            ace "Apologies. I’m just a bit absentminded right now."
        "Can’t say I disagree":
            ace "Can’t say I disagree"
        "Remain Silent":
            ace "..."
    
    gail "Anyways, you're certain that this ‘alleged serial killer’ is the same for all three of these murders?
    It feels a bit irresponsible to come to a conclusion so quickly."

    ace "To the contrary, it feels a bit irresponsible to dismiss the idea that Mr. Caller was murder by the same people that murdered Mr. Smith and Mr. Medici."
    ace "After all, they were all killed through the same method: a quick cut using a non-serrated knife across an artery."
    ace "All three deceased have bruises that can be chalked up to there being a quick fight beforehand, so it’s safe to assume that all of our deceased saw their murderers coming."

    gail "Aside from the fact that Mr. Caller’s death is more bloody than the rest."

    ace "Could’ve been a trial run. The first murder tends to not be quite as neat as the others. Our murderer was just figuring out their style."

    gail "It’s death, Ace. Not art. Besides, you’re getting side-tracked."

    menu:
        "I suppose I am.":
            ace "I suppose I am."

    menu:
        "Vincent found the body?":
            ace "Vincent found the body?"
        "Who?":
            ace "Who?"
            gail "Vincent or Karen?"
            menu:
                "Vincent":
                    ace "Vincent"

                    gail "Vincent Earl Holmes. He’s a homeless man who lives in the area."
                    gail "Fairly paranoid, but I can hardly blame him. Being homeless is rough."

                    ace "So this Mr. Holmes was the one who found the body."
                "Karen":
                    ace "Karen"

                    gail "What do you mean you don’t know Karen- you were the one who mentioned her earlier! Do you have a fever?"
                    
                    ace "I feel fine."

                    gail "If you say so."
                    gail "Karen, or Ms. Medici as your posh ass prefers, was the daughter of Mr. Medici. He’s a well-off banker, so she was financially secure."
                    gail "She was also incredibly rude. Can’t say I ever liked her much."

                    ace "So Ms. Medici’s our deceased."
                "Both. I must confess, I’m already a bit lost."
                    ace "Both. I must confess, I’m already a bit lost."

                    gail "Well, Karen, or rather Ms. Medici, is the daughter of Dantes, or rather Mr. Medici. He’s a popular banker, so she tends to be a bit privileged."

                    ace "Most people who grew up rich are."

                    gail "Yeah. Vincent, or Vincent Earl Holmes is the one who found the body. He’s homeless. Can’t say I know that much about him aside from hearing that he was paranoid."

                    ace "Any possibility he killed Ms. Medici?"

                    gail "Quit latching onto ideas so early! You always do this- we haven’t even met Mr. Holmes yet!"
                    gail "But I do take this to mean that you are starting to understand my theory of the two deceased being financially motivated?"

                    #Add cheeky to header
                    ace "Thought I wasn’t supposed to jump to conclusions so quickly. (But cheeky)"
                    
                    #Add amused to header
                    gail "Quit being an ass."

                    ace "So just to clarify, Ms. Medici’s our deceased, and was discovered by Mr. Holmes?"

                    gail "Yeah. Found in a dumpster. The body was still fairly fresh, so it couldn’t have been there for long. I’d guess about 24 hours, if that."

                    ace "Any other important details I should note?"

                    gail "Not that I know of. I’m not exactly omniscient."

                    ace "So I suppose now we have to investigate."

                    gail "That is typically what happens in an investigation. Besides, what are you asking me for? You technically have higher authority than I do."

                    ace "Technically."

                    gail "Anyways, our main and only lead at this moment would be Vincent."

                    menu:
                        "And you say I technically have higher authority. Seems like you’re the one calling the shots."
                            ace: "And you say I technically have higher authority. Seems like you’re the one calling the shots."

                            gail: "That technically is very important."

                            ace "So, Ms. technically-not-my-boss, we heading off to investigate our lead?"

                            gail "Roger that, Mr. technically-my-boss."


    jump confrontingVincent1

label confrontingVincent1:
    jump test


label test:
    show bush
    with dissolve

    ace "Look Gail. I'm a bush now"

    jump menuTest

label menuTest:
    menu:
        "Right":
            jump rightTest
        "Left":
            jump leftTest
        "Leave":
            jump end

label rightTest:
    show bush at right
    ace "Look Gail. I'm on the right now"
    jump menuTest

label leftTest:
    show bush at left
    ace "Look Gail. I'm on the left now"
    jump menuTest

label end:
    return