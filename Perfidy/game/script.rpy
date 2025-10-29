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
    gail "Not that he’d be missed."

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
    
    gail "Anyways, you're certain that this ‘alleged serial killer’ is the same for all three of these murders?     It feels a bit irresponsible to come to a conclusion so quickly."

    ace "To the contrary, it feels a bit irresponsible to dismiss the idea that Mr. Caller was murder by the same people that murdered Mr. Smith and Mr. Medici."
    ace "After all, they were all killed through the same method: a quick cut using a non-serrated knife across an artery."
    ace "All three deceased have bruises that can be chalked up to there being a quick fight beforehand, so it’s safe to assume that all of our deceased saw their murderers coming."

    gail "Aside from the fact that Mr. Caller’s death is more bloody than the rest."

    ace "Could’ve been a trial run. The first murder tends to not be quite as neat as the others. Our murderer was just figuring out their style."

    gail "It’s death, Ace. Not art. Besides, you’re getting side-tracked."

    menu:
        "I suppose I am.":
            ace "I suppose I am."
            ace "Returning back to what we’re supposed to be doing, any important investigative details I should know?"

            gail "About time you asked. I was questioning how long I was going to need to wait before we’d get to the point. You get distracted too easily."
            gail "Vincent found Karen’s body."

        "And you are changing the subject.":
            ace "And you are changing the subject."

            gail "I am. Back to the dead body that Vincent found. You know, the one we’re supposed to be investigating?"

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
                "Both. I must confess, I’m already a bit lost.":
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
                        "And you say I technically have higher authority. Seems like you’re the one calling the shots.":
                            ace "And you say I technically have higher authority. Seems like you’re the one calling the shots."

                            gail "That technically is very important."

                            ace "So, Ms. technically-not-my-boss, we heading off to investigate our lead?"

                            gail "Roger that, Mr. technically-my-boss."

                            ace "Well what are we waiting for?"

    jump confrontingVincent1

label confrontingVincent1:
    gail "Are you Vincent Earl Holmes?"

    vincent "Yeah."

    gail "It’s a pleasure to meet you. I’m detective Mourne, and this is detective Wright. We’re here to ask a few questions."

    vincent "What the hell do you want."

    menu:
        "Just as we said- we’re only here to ask a few questions.":
            ace "Just as we said- we’re only here to ask a few questions."
            vincent "Fine."
        "You better mind your attitude.":
            ace "You better mind your attitude."
            vincent "..."

    gail "Thank you for your cooperation. Let’s start with something easy. Where did you find Karen’s body?"

    vincent "In the dumpster. By C Carver’s Cuts."

    vincent "Yes. I already said as much! What are you going on about? My answer ain’t gonna change if you don’t like it!"

    gail "..."

    menu:
        "Did you see anything else?":
            ace "Did you see anything else?"

            vincent "No."

            menu:
                "Why were you in the area?":
                    ace "Why were you in the area?"
                    vincent "Curiosity. Bit of boredom."

                    ace "What do you mean?"

                    vincent "Well, a few days ago, I saw Karen ‘n Ms. Carver arguing over somethin’. Not sure what."
                    vincent "All I know is that Karen was real pissed, yellin’ and saying she’d shut down Ms. Carver’s business if it was the las’ thing she did."

                    ace "And you just stuck around to see what would happen next? "

                    vincent "Basically. "

                    gail "You can’t be serious. You’re saying your whole reason for sticking around was because you were nosey?"
                    gail "Because there was allegedly some argument between Karen and Cynthia. Allegedly. We can’t seriously be listening to this shit. "

                    menu:
                        "There’s no harm in listening.":
                            ace "There’s no harm in listening."

                            gail "… If you say so. Of course, that would be ignoring how Mr. Holmes here was blatantly insinuating that Cynthia was related to Karen’s murder."

                            ace "I’m not ignoring it, Gail, but it could be a good place to start investigating. Besides, we shouldn’t be ignoring any leads."

                            gail "..."

                            ace "Regardless of what my partner has to say, thank you for your cooperation."
                            ace "Let’s go, Gail. "
                            jump discussionOfLove
                        "Not really.":
                            ace "Not really."

                            vincent "‘Course you wouldn’t. You lot never do."

                            ace "Well forgive me for having a few doubts about the validity of your story, because it seems like you’re implying that Cynthia’s to blame for Karen’s murder!"

                            vincent "I didn’t even imply nothing! I was jus’ trying to say what I had experienced!"

                            gail "We will take what you said into consideration. Let’s go."
                            jump discussionOfLove
                "What’s your relationship with Ms. Medici?":
                    ace "What’s your relationship with Ms. Medici?"

                    vincent "I know her cause of Dantes, but you probably know that. Never knew ‘er personally, though she always seemed a bit rude. ‘Tended to look down on people who weren’t old money."

                    ace "What was your relationship with Mr. Dantes?"

                    vincent "Then or now?"

                    ace "Both, preferably. "

                    vincent "Fine. Well, before, it was always fairly amicable. Maybe a bit strained? I always got the feeling he didn’t really like either new money all that much. But he was nowhere near as bad as Karen, he only gave a few snide comments every now ‘ n then."

                    ace "And after?"

                    vincent "Haven’t talked to him. Wouldn’t want to, really, unless I can hit ‘em."

                    gail "So would vengeance be on the table?"

                    vincent "I want to punch ‘em, not murder his family!"

                    ace "Our apologies, we didn’t mean to insinuate."

                    vincent "Fine."

                    menu:
                        "How did the two of you break up?":
                            ace "How did the two of you break up?"

                            vincent "Dantes is a banker. I dabbled in stocks a bit. He bought a bunch ‘a stocks of some railroad company, convinced me it was a good investment. Talked ‘ta me about it and whatnot."
                            vincent "I bought a bunch like an idiot, and he sold his, the price dropped, and I lost a bunch. Couldn’t really recover from it, least not financially. "

                            ace "Did Mr. Medici ever talk to you about it afterwards?"

                            vincent "Nah. He didn’t talk to me at all, just ghosted all my attempted correspondence  like the scheming piece of shit he is."

                            ace "Alright. Returning to the more immediate topic at hand, when did you last see Ms. Medici?"

                            vincent "Yesterday. At the triple C."

                            gail "C. Carver’s Cuts? The butchers? You’re sure?"

                            vincent "Yeah, the butchers. Karen was all profane, yelling at Ms. Carver, saying she was gonna ruin her life ‘n whatnot. Not sure what exactly started the fight though. "

                            ace "Alright. Thank you for your cooperation. Let’s go, Gail. "

                            jump discussionOfLove

                        "What about Cynthia? Any reason why you were around her establishment in particular?":
                            ace "What about Cynthia? Any reason why you were around her establishment in particular?"

                            vincent "Well, yesterday there was an altercation between Karen and Ms. Carver? Guess I stuck around to see what would happen."

                            gail "Altercation? With Cynthia? You’re certain?"

                            vincent "Yeah. Karen was yelling, and she was all profane, saying she’d shut down Ms. Carver’s establishment if it was the last thing she did."

                            gail "And you were still in the area because you were… curious?"

                            vincent "Basically."

                            gail "Yeah right."

                            ace "That’s enough. Thank you for your cooperation."

                            jump discussionOfLove


        "Isn’t it a bit too much of a coincidence that you of all people just so happened to come across the body?":
            ace "Isn’t it a bit too much of a coincidence that you of all people just so happened to come across the body?"

            vincent "What are you talking about?"

            ace "Bit of a coincidence that it was Karen Medici’s body, specifically."

            vincent "Yes. As you said. Coincidence."

            menu:
                "A coincidence that has nothing to do with your history with Mr. Medici?":
                    ace "A coincidence that has nothing to do with your history with Mr. Medici?"

                    vincent "What is this- because Dantes screwed me over, I killed his daughter? That’s bullshit!"

                    ace "It’s reasonable. At this point you have very little to lose. What else could you want aside from revenge?"

                    vincent "Sure I wanted revenge! He ruined my life! That don’t mean I want to kill his daughter!	When I last saw her it was at the triple C."
                    vincent "She was all profane and whatnot, yelling at Ms. Carver, calling her a bastard, saying that she was gonna ruin Ms. Carver’s business if it was the last thing she did."

                    gail "Was anyone else there?"
                    
                    vincent "No. Jus’ me and Karen and Ms. Carver."

                    menu:
                        "Is that the entirety of what happened?":
                            ace "Is that the entirety of what happened?"

                            vincent "Yeah it is! What’s the point of asking me anything if you ain’t gonna listen!"

                            ace "I am listening. It’s just very little is helpful to defending your position in regards to your innocence."

                            gail "Ace. Cool it down a bit. "

                            ace "… Fine."
                            ace "In this… recitation of this incident, why were you at Cynthia’s establishment?"

                            vicent "To buy meat. That’s the only reason anyone goes to a butcher’s, ain’t it?"

                            menu:
                                #Cynthia Accuse Path Open
                                "I suppose as much.":
                                    ace "I suppose as much."

                                    vincent "‘Course it is. "

                                    gail "Let me take over from here. "

                                    ace "Go ahead."

                                    gail "Before you lost your fortune, you worked with Mr. Medici, correct?"

                                    vincent "Where are you going with this?"

                                    gail "I just want to make sure we’re on the same page."

                                    vincent "…"
                                    vincent "Yeah that’s correct. "

                                    gail "How would you describe your relationship prior to your financial loss?"

                                    vincent "I dunno’.  It was fairly amicable, but also tense I guess?"

                                    gail "Why would you say that?"

                                    vincent " It’s never really been a secret I ain’t old money. He never really liked me super much ‘cause of that. Tended to be condescending and whatnot."

                                    gail "Alright. What about Karen?"

                                    vincent "Never really talked."

                                    ace "Then why were you by her body?"

                                    gail "Ace! Seriously, for Christ’s sake, just quit."

                                    ace "No, I’m deadly serious. Quit trying to cut me off. Just because we don’t always act like it, doesn’t mean I’m not your superior. Now answer the question Mr. Holmes."
                                    
                                    #Vicent Crashout
                                    vincent "What’s your goddamn problem? You’re so desperate ta’ know why I was there? Fine!"
                                    vincent "I watched Russel Smith die. He was there in that goddamn hellhole and I heard him scream and watched him bleed to death in that pigsty. I could feel his blood on my hands and it was all over the floor and when I stepped it squelched."
                                    vincent "But’cha can’t tell ‘cause that whole place is soaked in it. All ya’ gotta do is mop up the shit and no one would have a clue. "
                                    vincent "You wan’ta know so badly why I was there, huh? Because I watched a man bleed to death, and I was right in bettin’ that it would happen again. So if anyone has a reason to be here, it would be me. "

                                    menu:
                                        "Are you implying that Cynthia is involved?":
                                            ace "Are you implying that Cynthia is involved?"

                                            vincent "I dunno. Am I? It’s not like there’s been two bodies by Ms. Carver’s establishment. "

                                            #Add italics around "not" maybe? IDK
                                            gail "Cynthia is not related to this shit. Keep her name out of your foul mouth, you bastard."
                                            
                                            vincent "Why? She matter to ya’? Maybe you're involved."

                                            menu: 
                                                "Quit throwing baseless accusations. I trust Cynthia far more than I trust you.":
                                                    ace "Quit throwing baseless accusations. I trust Cynthia far more than I trust you."

                                                    vincent "Don’t worry, you’ve made that excruciatingly clear. But you asked your question and I answered so quit accusing me of shit."

                                                    ace "There’s no point in talking to this bastard any further. Let’s go Gail, before he starts accusing us any more."
                                                    jump discussionOfLove
                                                "Your story will be taken into consideration.":
                                                    ace "Your story will be taken into consideration."

                                                    gail "Will it? He just called us liars, and said that my girlf- Cynthia is a murderer! There’s no point in listening to this horseshit any longer. Let’s go, Ace."

                                                    jump discussionOfLove
                                        "And how are we supposed to trust your account? There’s no evidence to prove this even happened!":
                                            ace "And how are we supposed to trust your account? There’s no evidence to prove this even happened!"
                                            ace "Mr. Smith’s body wasn’t even found near here- it was found in the harbor! Smuggling a body that supposedly died at Cynthia’s would be incredibly difficult and such a hassle."

                                            vincent "So murder’s too inconvenient now, huh?"

                                            ace "It is if you have no evidence that Cynthia’s even the murderer and trying to defend your position by arguing that carrying a body multiple miles just  to dispose of it is ridiculous."
                                            ace "I see little point in continuing this argument who utilizes baseless accusations. Let’s go, Gail."
                                            jump discussionOfLove
                                "With what money?":
                                    ace "With what money?"

                                    gail "Ace! This is getting out of line!"

                                    ace "He’s homeless, isn’t he?"

                                    gail "It’s irrelevant and you’re acting like a classist asshole!"

                                    ace "Butt out of this Gail."

                                    #Vicent Crashout
                                    vincent "You wan’ta know why I was there so badly? Fine!"
                                    vincent "I watched Russel Smith die! And it was there- right there- in that gods forsaken butchers and nobody noticed!"
                                    vincent "He was lying- bleeding out- it was all over and it sunk into the floors  but you’d never find it ‘cause that whole hellhole soaked in it. Bleeding out like every other gutted pig in that place."
                                    vincent "I was next to him- I was tryin’ ta stop the bleeding I think but I knew it was too late he was already unconscious but I could feel his blood in my hand and it soaked into my shoes and my clothes and his body was still so warm and wet and I thought I’d go ‘n vomit cause that whole place smelt of carcass. "
                                    vincent "I went in ‘cause I heard a scream and I didn’t know what was goin’ on. Ms. Carver was always nice and I didn’t want anything to happen to her but it didn’t sound like ‘er, so I wandered in an there he was bleedin’ out on the floor and then-"
                                    vincent "I heard footsteps coming and I bolted."
                                    vincent "Ya’ satisfied with that you bastard?"
                                    
                                    menu:
                                        "Why didn’t you tell anyone earlier?":
                                            ace "Why didn’t you tell anyone earlier?"

                                            vincent "You wouldn’t’ve believed me at any point, so why’d it matter when I tell you? It ain’t gonna change a damn thing. You’ve made up your mind before we even had this conversation, huh?"

                                            ace "..."

                                            gail "To the contrary, I doubt you more now."
                                            gail "Two bodies found in a row? And you never reported Russel’s, but you reported Karen’s? How gullible do you assume we are? Honest! "
                                            gail "I see little point in staying. This snake isn’t going to tell us a damn thing. Let’s go, Ace. "
                                            
                                            jump discussionOfLove
                                        "You seriously mean to tell us that you wandered in because you thought you heard someone in danger? You aren’t exactly the self-sacrificing type.":
                                            ace "You seriously mean to tell us that you wandered in because you thought you heard someone in danger? You aren’t exactly the self-sacrificing type."

                                            vincent "And there’s nothing I can do to prove it, huh? Figured as much."
                                            vincent "It’s just as you said though. Nothing else to live for. Why the hell wouldn’t I go?"

                                            ace "Because there’s nothing to prove that you were actually there. Or even that this actually happened. Is there?"

                                            vincent "..."

                                            ace "There’s nothing left to be derived from this conversation. Let’s go, Gail. "

                                            jump discussionOfLove

                                        "Convenient. No one to corroborate your story.":
                                            ace "Convenient. No one to corroborate your story."

                                            vincent "What, ‘cause I can’t get an alibi I’m the only at the thought of being at fault? Thought it was innocent ‘til proven guilty, not the other way ‘round!"

                                            ace "Typically, the motivations aren’t laid out so clearly."

                                            vincent "Well get Cynthia! Ask ‘er! I was there!"

                                            gail "Cynthia’s not going to lie for you, Vincent."

                                            vincent "So her word alone s’nough to invalidate mine?"

                                            menu:
                                                "Depends on what she has to say.":
                                                    ace "Depends on what she has to say."

                                                    vincent "‘Course it is. Bunch a bullshit detectives."

                                                    ace "I suggest you change your tone. It would be best to avoid any unpleasant consequences."

                                                    gail "Tone it down a bit Ace. Figured that you of all people would be able to avoid becoming unprofessional."

                                                    ace "Fine."
                                                    ace "So why were you at Cynthia’s Cuts?"

                                                    vincent "Why’d I go ‘n tell you? You wouldn’t believe a word I have to say anyways!"

                                                    gail "At least try to defend your position. You’re the only person who’s mentioned any possible altercation between Cynthia and Karen at a place you’ve provided no indication as to why you might go to. The hole you’re digging can’t possibly get deeper at this point."

                                                    vincent "Fine! I was there ‘cause I don’t trust ‘er!"

                                                    menu:
                                                        "And who is ‘her’?":
                                                            ace "And who is ‘her’?"

                                                            vincent "You know bloody well who! Cynthia!"

                                                        "So is this ‘her’ Ms. Medici? You admit to stalking Karen, then?":
                                                            ace "So is this ‘her’ Ms. Medici? You admit to stalking Karen, then?"

                                                            vincent "No, I don’t bloody admit to stalking Karen because I wasn’t stalking Karen. I was talkin’ about Ms. Carver."

                                                            ace "And why are we supposed to be suspicious of Cynthia now?"

                                                            vincent "Because…"

                                                            #Ask Elizabeth where to go on from here





    jump discussionOfLove

label discussionOfLove:
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