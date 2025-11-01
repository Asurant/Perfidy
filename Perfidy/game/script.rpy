# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image i_ace = At('ace1', sprite_highlight('ace'))
image i_ace happy= At('ace_happy', sprite_highlight('ace'))
image i_ace annoyed= At('ace_annoyed', sprite_highlight('ace'))
image i_ace panic= At('ace_panic', sprite_highlight('ace'))
image i_gail = At('gail1', sprite_highlight('gail'))
image i_gail happy= At('gail_happy', sprite_highlight('gail'))
image i_gail mgh= At('gail_mgh', sprite_highlight('gail'))
image i_gail sad= At('gail_sad', sprite_highlight('gail'))
image i_cynthia = At('cynthia1', sprite_highlight('cynthia'))
image i_cynthia happy= At('cynthia_happy', sprite_highlight('cynthia'))
image i_cynthia horror= At('cynthia_horror', sprite_highlight('cynthia'))
image i_vincent = At('vincent1', sprite_highlight('vincent'))
image i_vincent unhinged= At('vincent_unhinged', sprite_highlight('vincent'))
image i_dantes = At('dantes1', sprite_highlight('dantes'))
image i_dantes annoyed = At('dantes_annoyed', sprite_highlight('dantes'))
image i_dantes depressed= At('dantes_depressed', sprite_highlight('dantes'))
image i_dantes smug= At('dantes_smug', sprite_highlight('dantes'))


image butcher = im.Scale("butcher.png", config.screen_width, config.screen_height)
image broke = im.Scale("broke.jpg", config.screen_width, config.screen_height)
image office = im.Scale("office.png", config.screen_width, config.screen_height)

define ace = Character("Ace Wright", image = 'ace1', callback = name_callback, cb_name = 'ace')
define cynthia = Character("Cynthia Carver", image = 'cynthia1', callback = name_callback, cb_name = 'cynthia')
define gail = Character("Gail Mourne", image = 'gail1', callback = name_callback, cb_name = 'gail')
define vincent = Character("Vincent Earl Holmes", image = 'vincent1', callback = name_callback, cb_name = 'vincent')
define dantes = Character("Dantes Medici", image = "dantes1", callback = name_callback, cb_name = 'dantes')
define unknownDantes = Character("...", image = "dantes1", callback = name_callback, cb_name = 'unknownDantes')

default honestyKarma = 0
default ReticenceKarma = 0
default perfidyKarma = 0
default stalkerKarma = 0
default temp = 0
default gailLeaveDantesScene = False

# The game starts here.

label start:
    scene office
    jump karenDeathRevealed

label karenDeathRevealed:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    with None
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show i_gail at left:
        xzoom -1.0

    show i_ace at right

    gail "Karen’s dead."

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
            gail "I meant nothing by it. Just that there were rumors of him harassing women."
            gail "I’ve mentioned this before."
            ace "Apologies. I’m just a bit absentminded right now."
        "Can’t say I disagree":
            $ temp = 0
        "Remain Silent":
            $ temp = 0
    
    gail "Anyways, you're certain that this ‘alleged serial killer’ is the same for all three of these murders?     It feels a bit irresponsible to come to a conclusion so quickly."

    ace "To the contrary, it feels a bit irresponsible to dismiss the idea that Mr. Caller was murder by the same people that murdered Mr. Smith and Mr. Medici."
    ace "After all, they were all killed through the same method: a quick cut using a non-serrated knife across an artery."
    ace "All three deceased have bruises that can be chalked up to there being a quick fight beforehand, so it’s safe to assume that all of our deceased saw their murderers coming."

    gail "Aside from the fact that Mr. Caller’s death is more bloody than the rest."

    ace "Could’ve been a trial run. The first murder tends to not be quite as neat as the others. Our murderer was just figuring out their style."

    gail "It’s death, Ace. Not art. Besides, you’re getting side-tracked."

    menu:
        "I suppose I am.":
            ace "Returning back to what we’re supposed to be doing, any important investigative details I should know?"

            gail "About time you asked. I was questioning how long I was going to need to wait before we’d get to the point. You get distracted too easily."
            gail "Vincent found Karen’s body."

        "And you are changing the subject.":

            gail "I am. Back to the dead body that Vincent found. You know, the one we’re supposed to be investigating?"

    menu:
        "Vincent found the body?":
            $ temp = 0

        "Who?":

            gail "Vincent or Karen?"

            menu:
                "Vincent":

                    gail "Vincent Earl Holmes. He’s a homeless man who lives in the area."
                    gail "Fairly paranoid, but I can hardly blame him. Being homeless is rough."

                    ace "So this Mr. Holmes was the one who found the body."
                "Karen":

                    gail "What do you mean you don’t know Karen- you were the one who mentioned her earlier! Do you have a fever?"
                    
                    ace "I feel fine."

                    gail "If you say so."
                    gail "Karen, or Ms. Medici as your posh ass prefers, was the daughter of Mr. Medici. He’s a well-off banker, so she was financially secure."
                    gail "She was also incredibly rude. Can’t say I ever liked her much."

                    ace "So Ms. Medici’s our deceased."
                "Both. I must confess, I’m already a bit lost.":

                    gail "Well, Karen, or rather Ms. Medici, is the daughter of Dantes, or rather Mr. Medici. He’s a popular banker, so she tends to be a bit privileged."

                    ace "Most people who grew up rich are."

                    gail "Yeah. Vincent, or Vincent Earl Holmes is the one who found the body. He’s homeless. Can’t say I know that much about him aside from hearing that he was paranoid."

                    ace "Any possibility he killed Ms. Medici?"

                    gail "Quit latching onto ideas so early! You always do this- we haven’t even met Mr. Holmes yet!"
                    gail "But I do take this to mean that you are starting to understand my theory of the two deceased being financially motivated?"

                    hide i_ace
                    show i_ace happy at right
                    ace "Thought I wasn’t supposed to jump to conclusions so quickly"
                    
                    hide i_gail
                    show i_gail happy at left:
                        xzoom -1.0
                    gail "Quit being an ass."

                    hide i_gail happy
                    hide i_ace happy

                    show i_gail at left:
                        xzoom -1.0

                    show i_ace at right

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

            gail "That technically is very important."

            ace "So, Ms. technically-not-my-boss, we heading off to investigate our lead?"

            gail "Roger that, Mr. technically-my-boss."

            ace "Well what are we waiting for?"
            jump confrontingVincent1
        "Well what are we waiting for?":
            jump confrontingVincent1
    jump confrontingVincent1

label confrontingVincent1:
    scene broke
    show i_gail:
        xalign 0.75
        yalign 0.97
    show i_ace:
        xalign 1.2
        yalign 0.97
    show i_vincent at left
    gail "Are you Vincent Earl Holmes?"

    vincent "Yeah."

    gail "It’s a pleasure to meet you. I’m detective Mourne, and this is detective Wright. We’re here to ask a few questions."

    vincent "What the hell do you want."

    menu:
        "Just as we said- we’re only here to ask a few questions.":
            vincent "Fine."
        "You better mind your attitude.":
            vincent "..."

    gail "Thank you for your cooperation. Let’s start with something easy. Where did you find Karen’s body?"

    vincent "In the dumpster. By C Carver’s Cuts."

    vincent "Yes. I already said as much! What are you going on about? My answer ain’t gonna change if you don’t like it!"

    gail "..."

    menu:
        "Did you see anything else?":

            vincent "No."

            menu:
                "Why were you in the area?":
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

                            gail "… If you say so. Of course, that would be ignoring how Mr. Holmes here was blatantly insinuating that Cynthia was related to Karen’s murder."

                            ace "I’m not ignoring it, Gail, but it could be a good place to start investigating. Besides, we shouldn’t be ignoring any leads."

                            gail "..."

                            ace "Regardless of what my partner has to say, thank you for your cooperation."
                            ace "Let’s go, Gail. "
                            jump discussionOfLove
                        "Not really.":

                            vincent "‘Course you wouldn’t. You lot never do."

                            ace "Well forgive me for having a few doubts about the validity of your story, because it seems like you’re implying that Cynthia’s to blame for Karen’s murder!"

                            vincent "I didn’t even imply nothing! I was jus’ trying to say what I had experienced!"

                            gail "We will take what you said into consideration. Let’s go."
                            jump discussionOfLove
                "What’s your relationship with Ms. Medici?":

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

                            vincent "Well, yesterday there was an altercation between Karen and Ms. Carver? Guess I stuck around to see what would happen."

                            gail "Altercation? With Cynthia? You’re certain?"

                            vincent "Yeah. Karen was yelling, and she was all profane, saying she’d shut down Ms. Carver’s establishment if it was the last thing she did."

                            gail "And you were still in the area because you were… curious?"

                            vincent "Basically."

                            gail "Yeah right."

                            ace "That’s enough. Thank you for your cooperation."

                            jump discussionOfLove


        "Isn’t it a bit too much of a coincidence that you of all people just so happened to come across the body?":
            vincent "What are you talking about?"

            ace "Bit of a coincidence that it was Karen Medici’s body, specifically."

            vincent "Yes. As you said. Coincidence."

            menu:
                #Stalker Point
                "A coincidence that has nothing to do with your history with Mr. Medici?":
                    $ stalkerKarma += 1

                    vincent "What is this- because Dantes screwed me over, I killed his daughter? That’s bullshit!"

                    ace "It’s reasonable. At this point you have very little to lose. What else could you want aside from revenge?"

                    vincent "Sure I wanted revenge! He ruined my life! That don’t mean I want to kill his daughter!    When I last saw her it was at the triple C."
                    vincent "She was all profane and whatnot, yelling at Ms. Carver, calling her a bastard, saying that she was gonna ruin Ms. Carver’s business if it was the last thing she did."

                    gail "Was anyone else there?"
                    
                    vincent "No. Jus’ me and Karen and Ms. Carver."

                    menu:
                        "Is that the entirety of what happened?":

                            vincent "Yeah it is! What’s the point of asking me anything if you ain’t gonna listen!"

                            ace "I am listening. It’s just very little is helpful to defending your position in regards to your innocence."

                            gail "Ace. Cool it down a bit. "

                            ace "… Fine."
                            ace "In this… recitation of this incident, why were you at Cynthia’s establishment?"

                            vicent "To buy meat. That’s the only reason anyone goes to a butcher’s, ain’t it?"

                            menu:
                                "I suppose as much.":

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
                                    hide i_vincent
                                    show i_vincent unhinged at left
                                    vincent "What’s your goddamn problem? You’re so desperate ta’ know why I was there? Fine!"
                                    vincent "I watched Russel Smith die. He was there in that goddamn hellhole and I heard him scream and watched him bleed to death in that pigsty. I could feel his blood on my hands and it was all over the floor and when I stepped it squelched."
                                    vincent "But’cha can’t tell ‘cause that whole place is soaked in it. All ya’ gotta do is mop up the shit and no one would have a clue. "
                                    vincent "You wan’ta know so badly why I was there, huh? Because I watched a man bleed to death, and I was right in bettin’ that it would happen again. So if anyone has a reason to be here, it would be me. "
                                    hide i_vincent unhinged
                                    show i_vincent at left
                                    menu:
                                        "Are you implying that Cynthia is involved?":

                                            vincent "I dunno. Am I? It’s not like there’s been two bodies by Ms. Carver’s establishment. "

                                            hide i_gail
                                            show i_gail mgh:
                                                xalign 0.75
                                                yalign 0.97
                                            gail "Cynthia is not related to this shit. Keep her name out of your foul mouth, you bastard."
                                            
                                            vincent "Why? She matter to ya’? Maybe you're involved."

                                            menu: 
                                                "Quit throwing baseless accusations. I trust Cynthia far more than I trust you.":
                                                    hide i_ace
                                                    show i_ace annoyed:
                                                        xalign 1.2
                                                        yalign 0.97
                                                    #Cynthia ending
                                                    $ honestyKarma += 1
                                                    vincent "Don’t worry, you’ve made that excruciatingly clear. But you asked your question and I answered so quit accusing me of shit."

                                                    ace "There’s no point in talking to this bastard any further. Let’s go Gail, before he starts accusing us any more."
                                                    jump discussionOfLove
                                                "Your story will be taken into consideration.":

                                                    gail "Will it? He just called us liars, and said that my girlf- Cynthia is a murderer! There’s no point in listening to this horseshit any longer. Let’s go, Ace."

                                                    jump discussionOfLove
                                        "And how are we supposed to trust your account? There’s no evidence to prove this even happened!":
                                            ace "Mr. Smith’s body wasn’t even found near here- it was found in the harbor! Smuggling a body that supposedly died at Cynthia’s would be incredibly difficult and such a hassle."

                                            vincent "So murder’s too inconvenient now, huh?"

                                            ace "It is if you have no evidence that Cynthia’s even the murderer and trying to defend your position by arguing that carrying a body multiple miles just  to dispose of it is ridiculous."
                                            ace "I see little point in continuing this argument who utilizes baseless accusations. Let’s go, Gail."
                                            jump discussionOfLove
                                "With what money?":

                                    gail "Ace! This is getting out of line!"

                                    ace "He’s homeless, isn’t he?"

                                    gail "It’s irrelevant and you’re acting like a classist asshole!"

                                    ace "Butt out of this Gail."

                                    #Vicent Crashout
                                    hide i_vincent
                                    show i_vincent unhinged at left
                                    vincent "You wan’ta know why I was there so badly? Fine!"
                                    vincent "I watched Russel Smith die! And it was there- right there- in that gods forsaken butchers and nobody noticed!"
                                    vincent "He was lying- bleeding out- it was all over and it sunk into the floors  but you’d never find it ‘cause that whole hellhole soaked in it. Bleeding out like every other gutted pig in that place."
                                    vincent "I was next to him- I was tryin’ ta stop the bleeding I think but I knew it was too late he was already unconscious but I could feel his blood in my hand and it soaked into my shoes and my clothes and his body was still so warm and wet and I thought I’d go ‘n vomit cause that whole place smelt of carcass. "
                                    vincent "I went in ‘cause I heard a scream and I didn’t know what was goin’ on. Ms. Carver was always nice and I didn’t want anything to happen to her but it didn’t sound like ‘er, so I wandered in an there he was bleedin’ out on the floor and then-"
                                    vincent "I heard footsteps coming and I bolted."
                                    vincent "Ya’ satisfied with that you bastard?"
                                    hide i_vincent unhinged
                                    show i_vincent at left
                                    menu:
                                        "Why didn’t you tell anyone earlier?":

                                            vincent "You wouldn’t’ve believed me at any point, so why’d it matter when I tell you? It ain’t gonna change a damn thing. You’ve made up your mind before we even had this conversation, huh?"

                                            ace "..."

                                            gail "To the contrary, I doubt you more now."
                                            gail "Two bodies found in a row? And you never reported Russel’s, but you reported Karen’s? How gullible do you assume we are? Honest! "
                                            gail "I see little point in staying. This snake isn’t going to tell us a damn thing. Let’s go, Ace. "
                                            
                                            jump discussionOfLove
                                        "You seriously mean to tell us that you wandered in because you thought you heard someone in danger? You aren’t exactly the self-sacrificing type.":

                                            vincent "And there’s nothing I can do to prove it, huh? Figured as much."
                                            vincent "It’s just as you said though. Nothing else to live for. Why the hell wouldn’t I go?"

                                            ace "Because there’s nothing to prove that you were actually there. Or even that this actually happened. Is there?"

                                            vincent "..."

                                            ace "There’s nothing left to be derived from this conversation. Let’s go, Gail. "

                                            jump discussionOfLove

                                        "Convenient. No one to corroborate your story.":

                                            vincent "What, ‘cause I can’t get an alibi I’m the only at the thought of being at fault? Thought it was innocent ‘til proven guilty, not the other way ‘round!"

                                            ace "Typically, the motivations aren’t laid out so clearly."

                                            vincent "Well get Cynthia! Ask ‘er! I was there!"

                                            gail "Cynthia’s not going to lie for you, Vincent."

                                            vincent "So her word alone s’nough to invalidate mine?"

                                            menu:
                                                "Depends on what she has to say.":

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

                                                            vincent "You know bloody well who! Cynthia!"

                                                        "So is this ‘her’ Ms. Medici? You admit to stalking Karen, then?":

                                                            vincent "No, I don’t bloody admit to stalking Karen because I wasn’t stalking Karen. I was talkin’ about Ms. Carver."

                                                            ace "And why are we supposed to be suspicious of Cynthia now?"

                                                            vincent "Because…"
                                                    hide i_vincent
                                                    show i_vincent unhinged at left
                                                    vincent "You wanna know why so badly, huh? It’s cause’ I watched Russel Smith die. I heard ‘im yell and I rushed in and his blood was drowning that pigsty."
                                                    vincent "I could feel it on my hands. I heard footsteps and I ran out and left his body in that god forsaken place, and I bet that if you got a mop and cleaned up his guts, you’d never even have a clue."
                                                    vincent "She was always nice before but I don’ trust ‘er no more, not after that."

                                                    gail "You mean to tell us that your whole plan to get Cynthia to prove that you were there for this fabled altercation between you and Karen, which would make her look unnecessarily suspicious, all because you allegedly witnessed a murder at Cynthia’s establishment?"

                                                    ace "Not to mention that the body you allegedly found in Cynthia’s establishment was found nowhere near there! It was found in the harbor!"

                                                    vincent "I ain’t lyin’!"

                                                    gail "And I don’t believe a word outta your mouth."
                                                    gail "I can’t be around this asshole for a second longer. Let’s go, Ace."
                                                    jump discussionOfLove

                                                "Sure, when you consider just who’s word she’d be invalidating.":

                                                    vincent "And I can’t change that! You ain’t listening!"

                                                    ace "And what am I supposed to be listening to?"

                                                    vincent "Anything!"

                                                    ace "Why were you at Cynthia's?"

                                                    #Vicent crashout
                                                    hide i_vincent
                                                    show i_vincent unhinged at left
                                                    vincent "You want ‘ta know so desperately? Fine! I saw Russel Smith die"
                                                    vincent "I- I’d heard a scream ‘n I rushed in ‘cause I thought it might’ve been Ms. Carver even though it didn’t really sound like ‘er. And then-"
                                                    vincent "His blood was everywhere and I knelt down and I could feel it, ‘n it was all over my hands and it soaked in my clothes, it was still warm ‘n it was everywhere."
                                                    vincent "I was tryin’ to stop the bleeding I think but I couldn’t do nothing, ‘ne he was already unconscious and it was too late to do nothing anyway, but I tried and thought I was gonna vomit ‘cause that whole pigsty was rank from carcass. "
                                                    vincent "Then I heard footsteps ‘n I ran."
                                                    vincent "You satisfied now?"

                                                    gail "To the contrary, now I’m less satisfied. You can't seriously be trying to accuse my girl-"
                                                    gail "Cynthia, of committing murder? All while mentioning that Cynthia would vouch for you in the event that you have no evidence happened? Attempting to connect Cynthia to one of our deceased who wasn’t even found near the area? Russel was found in the harbor, for Christ’s sake!"
                                                    gail "I can’t listen to this anymore. Let’s go, Ace"

                                                    jump discussionOfLove
                "Describe to us, who was Ms. Medici to you?":

                    vincent " No one now. I only ever really knew her because of Dantes. ‘N you know who that bastard is to me. "

                    gail "Just to reaffirm, you have had no relationship with Karen specifically?"

                    vincent "Yeah."

                    gail "How would you describe your relationship with Dantes?"

                    vincent "Before? It was tense, but fairly amicable. Now? I can’t say I wouldn’t like to deck him."

                    gail "Would you ever consider getting revenge?"

                    vincent "I guess, but only really in the way that everyone ideates beating up someone who screwed them over. "

                    gail "Let’s refocus back to Karen for a little bit. When was the last time you saw her?"

                    vincent "Back at triple C’s."

                    ace "C. Carver’s Cuts? The butchers?"

                    menu:
                        "And why were you there?":
                            
                            vincent "It’s a butcher's shop! There’s only so many reasons a person could be there!"

                            ace "Fewer for you. It’s not like you could afford Cynthia’s cuts anyways."

                            vincent "What, you think I killed ‘er? You stuck on that, huh? Well I didn’t, ‘n I’d bet it’s Cynthia who did!"

                            gail "Cynthia? Leave her out of her damn conspiracy theories you asshole."

                            vincent "Leave her out? She’s the only reason for ‘em at all. Why else was Russel Smith killed in ‘er shop?"

                            gail "Don’t lie like that. We don’t even know you were ever at her shop to begin with."

                            vincent "Lie? Lie about what? I was there ‘n you weren’t! You didn’t hear him yell. You didn’t see him bleed out. You. Weren’t. There."

                            gail "Well why were you ‘there’ then?"

                            vincent "Heard ‘em scream. I went in. He was dead. It’s that simple. You’re the one tryin’ ta make it complicated!"

                            ace "It really isn’t that hard. All we have to do is point out how outrageous your story is, and you do all the work for us."

                            vincent "This is bullshit. You ain’t listening!"

                            gail "Oh, ‘this’ is bullshit? Do you hear yourself? Your story is bull and there’s no point in sticking around a single second longer."

                            jump discussionOfLove
                        "Planning to kill Ms. Medici using knives? It would make sense considering the cause of death of the other victims.":

                            vincent "Of course knives were used, but that don’t mean I used ‘em! It was Cynthia!"

                            gail "What- CYNTHIA? Keep her name out of your foul mouth!"

                            vincent "Thought you wanted ta know why I was there? Or should I lie to soothe your soul?"

                            gail "How about you quit being an asshole and stop blaming my girl-"
                            gail "..."
                            gail "Fine. Why were you there?"

                            vincent "Cause I watched Russel Smith die there."

                            ace "We can’t seriously be listening to this; It’s far too improbable. Russel Smith wasn’t found anywhere near Cynthia’s Cuts, it was found in the harbor!"

                            gail "I think we all know that."

                            vincent "I know, just as  I know you ain’t listening! I saw him bleed out! I heard ‘em yell ‘n I ran in and he was there! It’s as simple as that! "

                            ace "And you what, just left?"

                            vincent "I heard footsteps, and then yeah, I just left."

                            ace "Not interested in continuing your alleged heroicism?"

                            vincent "Not if it meant I was going to be murdered! You can’t act like you’d be much different!"

                            menu: 
                                "What’s the point of telling us this?":

                                    vincent "What do ya’ mean?"

                                    ace "Before telling us this, we had no reason to even suspect you of being related to Mr. Smith’s murder. Now you just confess that you allegedly witnessed it?"

                                    vincent "Why, you planning to frame me?"
                                    vincent "..."
                                    vincent "Are you?"

                                    ace "If we convict you, rest assured, it’ll be entirely because of your own crimes."
                                    ace "I don’t think there’s anything more we can glean from this conversation. Let’s go."

                                    jump discussionOfLove
                                "We would. Though I highly doubt you are ‘heroic’ enough to even ‘run in’ in the first place.":

                                    vincent "What, cause I’m some homeless piece of shit that cares about no one and has no morals?"

                                    ace "..."

                                    vincent " Figures you would. I ain’t got nothing else to say cause it ain’t gonna matter what I say, you ain’t gonna believe me anyway. Classist shit. "

                                    ace "Lets go Gail."

                                    jump discussionOfLove
    jump discussionOfLove

label discussionOfLove:
    scene office
    show i_gail at left:
        xzoom -1.0
    show i_ace at right

    ace "You doing alright?"

    gail "I don’t know…"
    gail "It was fine when it was just some unknown killer for money. Now Cynthia’s in it, and I guess it’s just more real now."
    gail "And I know that if anyone else was to figure out that…"

    ace "That you and Cynthia are together?"

    gail "Yeah."

    menu:
        "Don’t worry, I’ll make sure nobody knows. We can try to keep her out of this.":
            gail "Thank you. You don’t know how much this means to me."
            menu:
                "Anytime.":

                    gail "We should probably head out then. Try and see if we can remove her from our list of suspects?"

                    ace "Certainly. "

                    gail "Then what are we waiting for? Let’s go see my girlfriend!"

                    jump interrogatingCynthia1
                "I’d argue I do.":

                    gail "Seriously though, thanks."

                    ace "Anytime."

                    jump interrogatingCynthia1
        "I make no promises regarding Cynthia’s fate, but rest assured I’ll be keeping your relationship secret.":

            gail "Can you at least try to keep her out of this? I know her, and I know she wouldn’t do something like that. She’s the nicest person the both of us know, for Christ’s sake!"

            ace "I said I made no promises."

            gail "Quit acting so damn pragmatic all of a sudden. You know she wouldn’t do something like that. Can’t you just acknowledge that?"

            ace "..."

            gail "Fine. There’s no point in arguing with someone who can’t see reason."
            gail "..."
            gail "We should interview Cynthia. That way, we’ll both be able to see that I’m right."

            ace "If you say so."

            jump interrogatingCynthia1
        #Murder Points +1
        "It’ll happen how it happens. If Cynthia’s guilty, she’d be arrested.":
            $ perfidyKarma += 1
            gail "But she isn’t and I know it!"

            ace "Do you? Happen to know any secret information you’d like to share?"

            gail "I…"
            gail "No, but you know Cynthia almost as well as I do! You were the first person I told when we started dating! Can’t you just be on my side for this?"

            menu:
                "Alright.":

                    gail "Alright… Thanks."
                    gail "We should probably go interview Cynthia."

                    ace "Probably."

                    jump interrogatingCynthia1
                "I’m on the side of the law.":

                    gail "And the law isn’t against Cynthia!"

                    ace "Not if Cynthia can’t prove that she didn’t break the law."

                    gail "What the hell is wrong with you today? It’s innocent until proven guilty, and quit targeting my girlfriend!"

                    ace "You’re too upset at the moment to rationalize. We should-"

                    gail "I’m not being rational right now? Me? Are you even hearing yourself speak or are you just that dumb?"

                    ace "I’m not continuing this discussion. We’re going to be investigating this murder just as we’ve investigated every murder so far. Understand?"

                    gail "..."

                    ace "Good. Let’s go."

                    jump interrogatingCynthia1
    jump interrogatingCynthia1

label interrogatingCynthia1:
    scene butcher
    show i_gail:
        xalign 0.75
        yalign 0.97
    show i_ace:
        xalign 1.2
        yalign 0.97
    show i_cynthia at left
    cynthia "Hi Gail! Ace. What are the two of you doing here? "

    gail "Hi Cynth. Can you close up early for a bit? We need to talk. "

    cynthia "Of course! What do you need? Wait- does this have to do with our upcoming anniversaire?"

    gail "I… Well, no. It’s more of a professional based inquiry. "

    cynthia "Ah. So this has to do with the body then? "

    gail "Alright. Well, according to Vincent you had an altercation with Karen before she died, but I failed to find any sort of corroborates with this, so feel free to deny-"

    ace "Gail. This is supposed to be an interrogation, not a request for Cynthia to deny any possibilities. At least try to make this seem professional. "

    gail "Well she wouldn’t! Cynthia’s far too nice for something like that!"

    cynthia "As much as I’m incredibly flattered… he wasn’t lying about the argument between Ms. Medici and I. "

    ace "Thank you for your honesty. What led up to this?"

    cynthia "To be honest, I don’t specifically remember. She went in to buy a cut, as this is a barber’s shop, and I sold it. I think she complained about there being too much fat?"
    cynthia "It blended together. I was trying to diffuse it, but she wasn’t listening, and was saying all this horrible stuff. I would be lying if I said I wasn’t a bit relieved."

    gail "Relieved?"

    cynthia "Yeah, relieved. I was half worried she was going to follow through on her threats to shut me down. It’s been hard enough to keep this place running due to sexism. If this place closed, I doubt I could get a job anywhere else, let alone open this place again…" 
    cynthia "Wait- why are you acting surprised, Gail? I could’ve sworn I told you this?"

    menu:
        "Gail, you were keeping information from me?":
            gail "..."

            cynthia "Cynthia: Love? What’s Ace talking about? "

            ace "If I chose to, I could kick you off this investigation"

            gail "… You wouldn’t."
            
            ace "Would I? It’s not like my partner had been obstructing justice by keeping relevant information hidden!"

            gail "For good reason! I didn’t know you’d actually listen to me if I did mention it!"
            
            ace "This is an investigation- regardless of what’s mentioned I’m legally obligated to fully investigate it!"

            gail "Well forgive me if ‘legally obligated’ isn’t reassuring in the slightest."
        "Why didn’t you mention that you already knew that Vincent wasn’t lying?":
            gail "I’d forgotten. "

            ace "You… forgot. Something this important to the investigation? "

            gail "Yes."

            ace "You hardly forget anything! We both know you’re lying to me, so just spit it out!"

            gail "For someone who just insisted on the professionality of the investigation, you should know there’s no way to really prove I apparently remember anything. You can’t prove a negative like that. "

            ace "No, but I can remove you for suspicious behavior."

            gail "..."

    cynthia "What are the two of you even talking about?"
    hide i_gail
    show i_gail mgh:
        xalign 0.75
        yalign 0.97
    #Displeasure
    gail "Probably shouldn’t say. Wouldn’t want to get kicked off the investigation for obstructing it or anything!"

    ace "Gail. Enough. I get your upset, but you still have a job to do. "

    cynthia "And it’ll be fine, love! You yourself said that I’m innocent, so the river of justice will leave us untouched!"

    gail "Alright." 
    hide i_gail mgh
    show i_gail happy:
        xalign 0.75
        yalign 0.97
    gail "You're always so positive. I’ve always loved that about you."
    hide i_cynthia
    show i_cynthia happy at left
    cynthia "I know."
    hide i_gail happy
    show i_gail:
        xalign 0.75
        yalign 0.97
    hide cynthia_happy
    show i_cynthia at left
    ace "Now that we’ve got that sorted, I suppose it’s time to continue on with what we came here to do."

    gail "Probably. Are you sure you’ll be okay, Cynth?"

    cynthia "Don’t worry, I can handle a few questions. Ask away!"

    menu:
        "Did you know Ms. Medici before she died?":
            cynthia "Not really. "

            ace "What about her father, Mr. Medici?"

            cynthia "The banker? Isn’t he rich? I know of him, but we’ve never met."

            gail "What about Karen’s body, what do you know about that?"

            cynthia "Aside from the fact it was found nearby… wasn’t it Vincent who found it? Or found near it? "

            gail "What about Vincent? Is he around often?"

            cynthia "Yeah he’s in the area often. Sometimes if he’s around and it’s cold, I let him stay inside for a while. Not sure why, he’s always such an asshole about it. "

            menu:
                "Was he there during your altercation with Ms. Medici?":
                    cynthia "Yeah."

                    gail "What about afterwards? How long did he stick around for?"

                    cynthia "He left pretty soon afterwards… you don’t think he’s Ms. Medici’s murderer, do you?"

                    menu:
                        "It’s possible. ":
                            gail "Possibly a bit more than possible. "

                            ace "Gail."

                            gail "He is the only person so far that has a motive!"
                        "I’m sorry, but I’m not allowed to say. ":
                            gail "Don't worry, I’ll tell you afterwards."

                            ace "Gail! No you won’t! Have you been flaunting protocol this whole time?"

                            gail "Despite what you claim I am a detective and I do know protocol; as such, I wouldn’t confirm or deny that accusation. "

                            ace "..."
                    
                    cynthia "I don’t know about it being him… I’ve known Vincent for a while and I don’t think he would do that. "

                    ace "We’ll keep it in mind. Thank you for your cooperation."
                    hide i_cynthia
                    show i_cynthia happy at left
                    cynthia "Yeah, of course. See you later, love."
                    hide i_gail
                    show i_gail happy:
                        xalign 0.75
                        yalign 0.97
                    gail "See you!"

                    jump droppingCynthia
                #Prequisite of being mean to Vincent
                "Has he been around more often?" if stalkerKarma > 0:
                    cynthia "Now that you mention it… yeah."

                    gail "How long has he been around more for? "

                    cynthia "I’m not entirely sure. Three months? Why do you ask? "

                    ace "Because it backs up Vincent’s claim. "

                    gail "You can’t be seriously listening to him about this! Nothing about him is trustworthy!"

                    ace "Regardless, you can’t deny the coincidence. And I don’t believe in coincidences. "

                    cynthia "I’m sorry for interrupting, but what are you two talking about? "

                    ace "It’s private information."

                    cynthia "Alright..."

                    menu: 
                        "Was Vincent around during your altercation with Karen?":
                            cynthia "Yeah, he was. Left pretty soon after. He looked nervous- more so than usual, that is. "

                            ace "Thank you for telling us. I believe that concludes this disaster of an interrogation?"

                            gail "Yeah. No kidding about the ‘disaster’ bit, though. "
                            gail "Guess I’ll see you later, love? "
                            hide i_cynthia
                            show i_cynthia happy at left
                            cynthia "Alright. Love you!"
                            hide i_gail
                            show i_gail happy:
                                xalign 0.75
                                yalign 0.97

                            gail "Love you too."
                            jump droppingCynthia
                        "I think we have all we need. Thank you for your cooperation.":
                            gail "Ace what are you talking about? We barely asked Gail shit! Basically the only thing you asked was designed to validate Vincent…"
                            gail "I can’t believe you. You can’t seriously be believing that piece of shit man over my own girlfriend who you’ve known for years! What the hell, Ace! "
                            gail "I need to talk to you. Alone."
                            show i_gail happy:
                                xalign 0.75
                                yalign 0.97
                            gail "See you later, love. "
                            hide i_cynthia
                            show i_cynthia happy at left
                            cynthia "See you later, love. You too, Ace."
                            jump droppingCynthia
        #Mean option
        "Do you know Russel Smith or Christian Caller?":
            $ ReticenceKarma += 1
            $ perfidyKarma += 1
            cynthia "…Why do you ask?"

            gail "Ignore him, he’s just theorizing."

            ace "No, don’t. Cynthia, answer the question."

            cynthia "I…"

            gail "Ace, stop. Cynthia isn’t your theorized serial killer. "

            menu:
                "Is she? I wouldn’t know, considering she hasn’t answered.":
                    gail "Don’t ask dumb questions and she won’t have to! "

                    cynthia "No, it's fine. I did. Know them, that is."

                    ace "Alright. Let’s start with Mr. Smith. How’d you know him?"

                    cynthia "He’s my landlord."

                    ace "He owns the property we’re on now? C. Carver’s Cuts?"

                    cynthia "That’s correct. "

                    ace "When did you last interact with him before he died?"

                    cynthia "He was going to raise my rent. He never really liked me all that much. Thankfully it wasn’t implemented because he died before it was administered. "

                    gail "That guy was such an asshole. "

                    menu:
                        "How so?":
                            cynthia "Sexist. Not that many men are all that much better. Or people in general."

                            gail "Preach."
                        "Keeping this from me too?":
                            gail "Because. It’s. Personal!"

                            ace "Not if it’s related to the deceased, it’s not!"

                            gail "Well my eternal apologies for not telling you every single personal life detail that isn’t even relevant to this investigation! Because Cynthia isn’t the murderer!"

                            ace "You don’t have the right to decide that!"

                            gail "Just because you don’t like it, doesn’t make me not a detective! I can make decisions! I’ve been doing this for years!"

                            ace "You’re too emotionally entwined to deal with this rationally. You don’t get to call the shots on this."

                            gail "Oh now I’m too emotionally involved? You’ve known me for years! You were the first person I told when Cynthia and I started dating! Did that mean nothing to you? "

                            menu:
                                "I need to prioritize my job first. ":
                                    gail "Yeah. Of course you do. Because caring about people would be too much."
                                "...":
                                    $ temp = 0
                            cynthia "Look, it doesn’t matter, okay? I’ll answer whatever questions you need to ask, just let it go. Please. I don’t want to be stuck between the two of you fighting. "

                            ace "Fine. "
                            ace "What about Caller? How’d you know him?"

                            cynthia "I didn’t know him that well. He…"

                            gail "You don’t have to talk about it. "

                            cynthia "Yes, I am, because the two of you will start arguing about it if I don’t. Both of you are such children. "
                            cynthia "He harassed me, to put it simply. Thankfully he died before nothing worse happened, but it was… uncomfortable. "

                            ace "Thank you for your cooperation."

                            gail "Oh so that’s it? All that sounded really incriminating! You know, for someone who apparently hates poor interrogation strategies, you did your best to make that as bad as possible."

                            cynthia "Love, it’s fine. Ace wouldn’t screw us over like that. "

                            gail "Sure he would. "
                            gail "I can’t deal with this right now. See you later, love. Ace, I need to talk to you after this. "

                            ace "Very well. See you soon, Cynthia. "

                            cynthia "See you."
                            jump droppingCynthia
        #Prequisite of being mean to Vincent
        "That’s funny, because I seem to recall Mr. Holmes implying otherwise." if stalkerKarma > 0:
            gail " Oh, so we’re listening to the crackpot now? "

            ace " And out of Vincent and you, which of you lied to me about what they knew? Maybe you were just trying to get me to devalue his argument!"

            gail " You saw how twitchy Vincent was! And what are you talking about? You were being an asshole just fine without my help!"

            ace " Well that doesn’t matter right now! Answer the question Cynthia, did you know them?"

            cynthia "I did! Mr. Smith was my landlord and Caller…  He…"

            gail " You don’t have to talk about it. "

            menu:
                "Oh so you knew something else too, huh? Didn’t think to mention it too?":
                    gail "Because it’s private you asshole! I don’t have to tell you everything that’s ever personally happened to me or someone I know because it’s private!" 

                    ace "Not if it’s relevant to the deceased! "

                    cynthia "Both of you, please, just stop! I said I was happy to answer questions, so please quit acting like I’m a damsel in distress! Comprenez-vous?"

                    gail "Yeah. Sorry, I just hate seeing you in this position. I’m just…tense. "

                    cynthia "It’s alright, love."

                    ace "Now that we’ve got that out of the way, can you continue with how you know Caller?"

                    cynthia "It wasn’t the greatest experience. He… harassed me. Thankfully nothing happened but I would be lying if I said I wasn’t relieved when I heard he died. "
                "Forget Caller, Mr. Holmes saw Mr. Smith die in this very butcher’s. Seems like pretty damning evidence. ":
                            cynthia " I didn’t kill him! I knew him, and I didn’t really like him, but I wouldn’t do that! You know me; you should know this!"

                            ace " Sure, I’ve met you before. But that’s not a valid argument, is it? Or have you not been listening? Have any actual evidence that you’d like to bring to the table? "

                            gail " Ace quit! You didn’t even believe Vincent when we talked to him, quit using his stupid testimony to shit on my girlfriend! "

                            ace " Well I’m reconsidering his testimony now… "

                            menu:
                                "Cynthia, how’d you know Caller?":
                                    cynthia "Not well. He…"

                                    gail "He’s an asshole that harassed my girlfriend. "

                                    cynthia "Thankfully didn’t do much more than that."

                                "Maybe we should be listening to Mr. Holmes afterall. ":
                                    gail " We should be listening to Vincent? Are you even hearing yourself speak right now? He was stalking my girlfriend! As far as I’m concerned, we should prosecute him instead! Who knows what all else he’s done!"

                                    ace " And why would I trust you? What have you done aside from lie to me?"

                                    gail " You’ve known me your whole life! And I haven’t lied to you!"

                                    ace " A lie of omission is still a lie. Now be quiet before I cut you out of the investigation entirely. "

                                    gail " …"

                                    ace " Cynthia, how’d you know Caller?"

                                    gail " Quit pressing, Ace!"

                                    cynthia " No, it’s fine Gail, you don’t have to defend me against Ace. He wouldn’t try and hurt us like that. "
                                    cynthia "Caller… harassed me, to put it likely."

                                    gail " He was a sexist piece of shit that harassed Cynthia because she’s pretty and he’s an asshole. "

                                    cynthia " He didn’t actually do anything, thank god, but it was incredibly… uncomfortable. "
                            menu:
                                "Why didn’t you mention this to me earlier?":
                                    cynthia "Well he died pretty soon after. There wasn’t all that much left that you could do."

                                    gail "Aside from spit on his grave. "

                                    cynthia "That… might be a bit extra. "

                                "I take it this is what you meant when you said that he wouldn’t be missed?":
                                    gail "Yeah."
            ace " Thank you for telling me. Let’s circle back to Mr. Smith. You said he was your landlord?"

            cynthia " Correct. "

            ace " What was your relationship? "

            cynthia " Not the greatest. I don’t think he ever liked me all that much. He’s a bit…"

            gail " Of an asshole. No one is surprised. Maybe this supposed serial killer of yours is doing the world a favor. "

            ace " Don’t talk about the dead like that. "
            ace "What was your last interaction with Mr. Smith before he died?"

            cynthia " It was a few days before he died. It was… tense. He raised my rent by quite a bit, but it was never actually implemented because he died."

            menu:
                "Thank you for your cooperation. ":
                    cynthia "Yeah, of course."

                    gail "Guess we’ve got to go then. See you later, love. Love you lots. "

                    cynthia "Love you too."
                    jump droppingCynthia
                "Convenient":
                    cynthia "Yeah…I know."

                    gail "Coincidence."

                    ace "I don’t believe in coincidences, and I know you don’t either, so keep your bias out of this. "

                    gail "Well maybe Caller’s death was a coincidence, and Karen and Russel Smith were financially motivated? It’s not like Cynthia is the only person either of them have screwed over. Like Vincent. "

                    menu:
                        "We don’t have any proof that Mr. Holmes knew Mr. Smith.":
                            gail " So? Smith is rich. Vincent would have nothing to lose. "
                            
                            ace " So your hypothesis is that he would go after anyone with money? Because he apparently hates the rich? Seems a bit of a reach." 
                            
                            gail " You can’t deny that he’s most likely to have killed Karen, and he openly confessed to witnessing Smith’s death. Seems like more than just a coincidence, there, huh? "
                            
                            ace " …maybe. It could make sense. "
                            
                            gail " We really ought to go before Ace comes up with some other weird line of questioning. Love you Cynth."
                            
                            cynthia  "Love you too. "
                            
                            gail " C’mon Ace. "
                            jump droppingCynthia
                        "Possibly.":
                            gail "Probably. "
                            gail "We should probably head back to base. You done with your bullshit interrogation yet, Ace?"

                            ace "Not bullshit, but fine."

                            gail "Alright. See you later Cynth. Hopefully in better circumstances. "

                            cynthia "See you both later. Love you Gail. "

                            gail "You too. "

                            jump droppingCynthia
                "I take it that Gail also knew this and kept it from me?":
                    gail "Sure! I did! Because it was personal! I’m not obligated to tell you about every little thing that’s happened to me or Cynthia because of your work addiction!"

                    ace "It’s relevant if it involves every single one of our deceased on this investigation! You’ve done this for years, this isn’t new information! And for someone who wants me to trust them, you're doing a poor job explaining why I should. "

                    gail "Because I know you! And I know how obsessive you get with all of this shit and the moment you theorize that it’s Cynthia, you’d never let it go! I’m not just going to stand back and watch you go after my girlfriend!"
                    gail "So yeah, I kept it a secret. Not because she’s guilty, but because you won’t ever listen to anything contrary. "
                    
                    cynthia "Ace… He wouldn’t though, would he? "

                    ace "We’ll wait and see. I have to make sure that she’s actually innocent first. "
                    ace "I’ve got what I need. Let’s go, Gail. "

                    gail "Sorry, love."

                    cynthia "Not your fault. Love you!"
                    jump droppingCynthia

    jump droppingCynthia
    
label droppingCynthia:
    scene office
    show i_gail at left:
        xzoom -1.0

    show i_ace at right

    gail "…"

    ace "It seems like you want to talk, so spit it out. "

    gail "I want you to drop Cynthia from the investigation. "

    ace "…Pardon?"

    gail "Drop Cynthia from the investigation. I know the evidence is stacked up against her but it isn’t her, I can guarantee it. Even though she knew all the deceased…"
    
    menu:
        "Oh, you can guarantee she’s innocent now? I wasn’t aware you became omniscient while I wasn’t looking?":
            gail "Ace, just stop. Please. I know she wouldn’t do that because I know her. It’s that simple. "
            ace "I knew you too, and you still lied."
            gail "By omission! That’s hardly the horrible thing you think it is!"
            gail "Still, just please take her out of this. "
        "So you’ve been keeping that from me too?":
            gail "Because if I told you, this would happen!"
            ace "What would happen? Would I have the ability to do my job well? Or are you just terrified that you could be wrong about her?"
        "What do you mean by ‘all’ the deceased?":
            gail "Caller. Smith too. She knew both of them. "
            ace "In what capacity? "
            gail "I don’t think you’d trust me even if I did say. You certainly aren’t listening to me when I say that Cynthia wouldn’t do this!"
            ace "…"
            gail "As such I want to drop her from the investigation."

    ace "That’s a bold request, even for you, especially now. "

    gail "You and I both know that the courts will be biased against her- she runs her own business for Christ’s sake."
    gail "It’ll only get worse if they learn that she…"
    gail "That she’s bent, and we’re together."

    menu:
        "I’ll do what I can.":
        #Honesty Points
            $ honestyKarma += 1
            gail "Thank you."

            ace "Yeah. Just don’t lie to me in the future. I can’t do anything if you won’t tell me anything."

            gail "Right. Sorry."
            jump dauntingDantes
        "I know how you feel, but I can’t just change the investigation because of your whims.":
            gail "Right. Because of your obsession with ‘proper investigation.’ She’s innocent! And it’s not like I can do all that much to change it."  
            gail "You're busy stopping me from doing anything, and you know what society’s like- people take you far more seriously than they’d take me. If I were to interfere, our relationship could be exposed! Our lives would be just about over!"
            gail "It’s just… you’re my only hope. "

            ace "It’s just any regular investigation- If she’s innocent, then she’ll be dropped. And if you’re so certain that it’s not Cynthia, then she’ll be fine. "

            gail "..."
            gail "I understand. "

            jump dauntingDantes
        "You seem very insistent on Cynthia being dropped. Happen to know something?":
            gail "What are you insinuating?"

            ace "I think you know very well what I’m insinuating. And you still haven’t answered my question. Though I don’t know if I can trust you to tell me anything, with you lying and all. "

            gail "No, I don’t know anything." 
            gail "You know very well why I want Cynthia to be dropped. And you know very well why I care. Why does there have to be more to it!?"

            menu:
                "Sorry. I was a bit too caught up in it. ":
                    gail "If you say so."
                    jump dauntingDantes
                "It all ties together a little too well, doesn’t it. You’d have a motive wouldn’t you? ":
                    gail "In that case, so would you. We’ve been friends for years, and you were the first person I introduced Cynthia to!"

                    ace "So now I’m the murderer?"

                    gail "It’s the same logic you’ve been using for me, isn’t it?"

                    menu:
                        "I suppose.":
                            gail "Glad you’re self-aware enough to realize that at least." 
                            gail "…"
                            gail "I can’t deal with this right now. "
                            jump dauntingDantes
                        "Quit deflecting! Why would I care about your girlfriend anyways?":
                            #Perfidy Points
                            $ perfidyKarma += 1
                            $ gailLeaveDantesScene = True
                            gail "Don’t give me that shit! You’ve known me since we were kids, you don’t get to act like it was all just a farce."
                            gail "Sometimes you really are unbelievable."

                            ace "Why? For asking questions you don’t want to answer? "

                            gail "I can’t deal with all of this. All of your obsessiveness! "
                            gail "I’ll be back later. Don’t follow me, I’m not talking to you. "
                            jump dauntingDantes


    jump dauntingDantes

label dauntingDantes:
    scene office
    show i_ace at left:
        xzoom -1.0
    show i_dantes at right
    
    unknownDantes "Good evening. "

    ace "You as well."

    if gailLeaveDantesScene:
        unknownDantes "Was that your lover who just stormed out? She seemed to be in quite a fit of pique."
    else:
        unknownDantes "Was that your lover who left just now? "

    ace "Was that… what? No, Gail’s my partner. Wait, who are you?"


    unknownDantes "Pity, she seemed like a bit of a catch, though temperamental. "
    unknownDantes "Have I not introduced myself yet? My apologies, I’m not used to needing to do so. I’m Dantes Medici. But please, call me Dantes. "

    ace "You’re Ms. Medici’s father… I’m sorry for your loss. "
    
    hide i_dantes
    show i_dantes depressed at right

    dantes "Thank you. "
    dantes "To be quite honest, it still doesn’t feel real yet. Like I’ll turn and see her standing there, and nothing will have changed at all. That she’ll be admiring outfits through streetview windows, or talking about her day. That she’s just on the precipice of being dead…"
    dantes "Forgive this old man. I’m far too sentimental these days. Especially now considering…"

    menu:
        "Don’t worry, it’s all well. ":
            dantes "Thank you."
        "Considering what?":
            dantes "Considering the horrid fate that befell my lovely daughter."
    dantes "Pardon me, but can I ask your name? I don’t think you’ve introduced yourself yet. "

    ace "Haven’t I? My apologies, I’m Ace Wright. I’m the detective heading your daughter’s case." 
    ace "On such a note, I’d like to ask a few questions regarding your daughter. "

    dantes "Yes, of course. "

    menu:
        "Was your daughter often confrontational? ":
            dantes "She was always assertive, I suppose. Why do you ask?"
            ace "Wished to confirm an altercation between your daughter and another. "
        "Is there any details regarding your daughter that you would like to provide to aid the investigation?":
            dantes "I’m uncertain what I could provide that you don’t already know… have you investigated that lady butcher? I believe Karen was going to visit her establishment before her tragic death… Before her body tossed in a trashcan like a common plebian. She would be ashamed. She deserves far better than that... "
            ace "Certainly."
    dantes "If there’s anything I can do to help, please, let me know. I’d do anything to help. Anything to see my daughter brought to justice. "

    ace "Thank you for your kind offer. I’ll let you know if an opportunity arises. "

    dantes "If you don’t mind me asking, how is the investigation going? I can’t stop thinking about Karen… knowing she’s close to justice truly gives me peace of mind. "

    menu:
        "I’m sorry, but I can’t say.":
            $honestyKarma += 1
            dantes "Oh, well that’s a pity. If you can, you will keep me apprised on how the investigation continues, right? The thought of my daughter’s killer going unpunished makes me sick with worry. "
            ace "Certainly. "
            dantes "Sincerely, thank you. "
            dantes "I suppose it’s best that I take my leave. I’ve been up all night waiting for my daughter to return since she’s never out late, and now that she’s…I’m truly exhausted. "
            dantes "Good night. "
            ace "You as well. "
            jump reconveneAndReview
        "I’d say it’s going fairly well.":
            hide i_dantes depressed
            show i_dantes at right
            dantes "Why, that’s a relief. The thought that my daughter could never be put to rest terrifies me."
            menu:
                "However, I cannot share any more details.":
                    dantes "Are you certain? "
                    ace "Regretfully, yes. I’m already flaunting the rules by telling you this much.  "
                    dantes "Oh. In that case, thank you. And I do truly mean what I said earlier. If there’s anything I can do to help, no matter how small, I would be glad to assist."
                    ace "Your offer is greatly appreciated. "
                    dantes "Of course. "
                    dantes "I suppose it’s best that I take my leave. I’ve been up all night waiting for my daughter to return since she’s never out late, and now that she’s…I’m truly exhausted. "
                    dantes "Good night. "
                    ace "Good night."
                    jump reconveneAndReview
                "In fact, we already have a suspect." if stalkerKarma > 0 or ReticenceKarma > 0:
                    dantes "Do you? Thank God. Who is it? Who killed my daughter?"
                    menu:
                        "Vincent Holmes. He was the first to find your daughter’s body." if stalkerKarma > 0:
                            $ stalkerKarma += 1
                            dantes "Vincent? I knew we’d fallen out over a misunderstanding but I never thought he would…"
                            ace "A misunderstanding? What do you mean?"
                            dantes "I recommended he invest in a railroad company. I swore I thought it was safe! Turns out it was a scam, so I pulled my money out, but I suppose no one ever told Vincent, so he lost big... "
                            ace "He didn’t seem all that friendly when I talked to him. "
                            dantes "I suppose not… but to the extent he would kill my daughter? Despite our falling out I can’t help but feel betrayed. I wish I could talk to him… ask why. It just doesn’t align quite right in my mind… You’re sure it was him?"
                            ace "The investigation has not yet been concluded, so I’m forced to say no, but he admitted to ‘witnessing’ Smith’s murder. I suspect he’s the serial killer I’ve been looking for. "
                            dantes "Truly? That’s a horrifying thought."
                            dantes "I suppose it’s best that I take my leave. I’ve been up all night waiting for my daughter to return since she’s never out late, and now that she’s…I’m truly exhausted. "
                            dantes "Good night. "
                            ace "Good night. "
                            jump reconveneAndReview
                        "Cynthia Carver. She runs the butcher’s near where your daughter was found." if ReticenceKarma > 0:
                            $ ReticenceKarma += 1
                            dantes "That woman? I should’ve thought as much… No respectable woman runs a butchers shop."
                            menu:
                                "That's the part that makes her suspicious to you?":
                                    dantes "Quit with your skepticism. We all know that being a butcher is hardly a woman’s work. "
                                    ace "To the contrary, I always find her cuts to be excellent. "
                                    dantes "I refuse to argue with fools who refuse to see reason. If not for her profession, what’s the reason for your suspicion?"
                                    ace "She confessed to having negative relationships to both Mr. Caller and Mr. Smith along with an altercation with your daughter before she died. Considering the method in which all three died, I fear that she may be the serial killer I’ve been looking for. "
                                    dantes "A serial killer? Why, how serious. If you need any assistance in taking down such a horrid criminal, I would be glad to offer."
                                    ace "I’ll keep it in mind,"
                                    dantes "I suppose it’s best that I take my leave. I’ve been up all night waiting for my daughter to return since she’s never out late, and now that she’s…I’m truly exhausted. "
                                    dantes "Good night. "
                                    ace "Good night. "
                                    jump reconveneAndReview
                                "I suppose.":
                                    dantes "I’d argue it should be more than something you ‘suppose.’ It’s unseemly. "
                                    ace "Right. "
                                    ace "She was recently connected with having an altercation with both your daughter, Mr. Smith, and Mr. Caller, all three of whom were murdered in the same fashion. As such, I have reason to believe that she may be the serial killer I’ve been looking for."
                                    dantes "Why, a serial killer? That’s worse than I thought. If there’s anything I can do to help, please let me know. "
                                    ace "I will. "
                                    dantes "I suppose it’s best that I take my leave. I’ve been up all night waiting for my daughter to return since she’s never out late, and now that she’s…I’m truly exhausted. "
                                    dantes "Good night. "
                                    ace "You as well. "
                                    jump reconveneAndReview

    jump reconveneAndReview

label reconveneAndReview:
    scene office
    show i_gail at left:
        xzoom -1.0
    show i_ace at left
    gail "Good morrow."

    ace "Good morrow."

    gail "I was thinking last night."

    ace "Well that’s never a good sign."

    gail "Oh very funny. What I was saying is that I was thinking, and you might be on to something with the whole serial killer theory. "

    ace "Glad to see you admit I’m right."

    menu: 
        "What caused you to think this?":
            gail "What do you mean?"
            ace "You didn’t seem too adamant about the idea that our murders were done by the same person yesterday. Sans your theory about our serial killer being financially motivated."
        "…Is this just your method of sucking up to me? ":
            ace "So I forgive you immediately for whatever lies you said yesterday?"
            gail "No! It isn’t! And I know I broke your trust yesterday, but I am truly sorry and this is me just trying to be genuine! Apparently that’s too much for your shitty little brain to handle!"
            ace "For someone trying to act sorry, you aren’t doing a good job of it."
            gail "You! You… aren’t wrong, actually."
            ace "I’m often not. You just never choose to acknowledge that."
            gail "I am sorry though. Truly. I’m just frustrated. Frustrated because Cynthia who doesn’t have a mean bone in her body is the suspect in a murder case. Frustrated because you and I aren’t getting along in one of the most terrifying moments of my life. Frustrated because…"
            ace "Because what?"
    gail "Because I’ve been practically barred from being a part of this investigation! There’s not much else I can do, and I know that if I just stick to my theories, you won’t listen to a word I have to say. You’re frustratingly stubborn like that."

    ace "So you are trying to suck up to me?"

    gail "Maybe a bit, but more because I’m trying to keep my job. "
    gail "So really, at this point, there’s not much I can do but theorize. And if you won’t listen to my theories, then I’m just stuck being helpless while Cynthia’s at risk. "

    ace "I suppose that makes sense."
    ace "Wait, why have you been barred?"

    gail "Karen’s good for nothing dad. Apparently this job is too harsh for me, and I can’t be trusted because I’m too ‘delicate.’"

    ace "That’s a lie if I’ve ever heard. You're the least delicate person I know. "

    gail "Tell me about it. It’s complete bullshit."

    ace "Well, now that you’ve been demoted to honorary consultant, have any theories you’d like to share, then?"

    gail "Well I was thinking. If Cynthia knew all of the victims, then the killer was likely centralized in a specific area, and because Cynthia’s also in that area, she gets pulled into it. Smith was found by the harbor, right? And Caller in the sewers? "
    gail "Maybe our suspect has been killing people from the same area, and transporting them to different locations to throw people off their tracks. "

    ace "But why would Ms. Medici’s body be found nearby?"

    gail "Simple. The killer didn’t have time. The body was a lot fresher than any of the others when it was found, so our killer likely dumped it there when they realized that they were going to be caught. "
    
    menu:
        "How is our killer able to move the bodies?":
            gail "Think about it. Caller was found in the sewers. Smith was found in the harbor. They’re using the sewers and waterways!"
            ace "But why leave the body by water then? Wouldn’t people get suspicious? Shouldn’t we have already been suspicious?"
            gail "I’m not sure…"
            ace "Wait. You thought Ms. Medici’s body was so close because the killer feared being caught with the body, right?"
            gail "Yeah. "
            ace "Maybe it’s the same with the other two. Maybe the killer leaves them there because they fear being exposed. Maybe the killer is too paranoid, so they leave the body to make sure they don’t get caught?"
            gail "Could be. "
            ace "Still, I can’t say it’s overly helpful, considering we still don’t have a solid suspect. Any theories on that?"
            gail "Only the first person we interrogated."
            ace "Vincent Holmes?"
            gail "Yeah. But we don’t have anything solid against him at the moment besides circumstantial evidence."
            ace "So you think I should start with him then?"
        "What would our killer’s motivation be, then?":
            gail "I’m not totally sure yet. We’d need to look around more. And by we I mean you."
            ace "Any ideas on where to start? Maybe Mr. Holmes? He was a bit suspicious. Maybe I could start there?"

            gail "No. I vote you go see Cynthia, maybe ask if you’ve seen anyone suspicious around lately. And while you’re there, make sure she’s doing alright. I’m worried about her."

            menu:
                "Will do.":
                    gail "Thank you"
                    jump interrogatingCynthia2
                "Maybe you should keep your biases out of the investigation.":
                    $ perfidyKarma += 1
                    gail "I just asked you to make sure she’s doing okay! Why is not being an asshole such a difficult task for you to comprehend!"
                    gail "I’m not dealing with this right now. Just talk to her."
                    jump interrogatingCynthia2
            


    jump interrogatingCynthia2

label interrogatingCynthia2:
    scene butcher
    show i_ace at right
    show i_cynthia at left

    ace "Good morrow, Cynthia."

    cynthia "Good morrow."

    menu:
        "Are you doing alright? ":
            cynthia "A bit rattled, but otherwise fine. I imagine that’s a fairly normal reaction for finding out that you’re connected in a murder. "
        "Gail wants me to check on you.":
            cynthia "Well that’s sweet of her. Tell her I’m doing well and give her my love."
        "...":
            $ temp = 0
    cynthia "Still, you’re back before I thought you’d be. Did something happen?"

    ace "Just testing a theory. Have you noticed any suspicious activity in the area?"

    cynthia "What do you mean?"

    ace "Did you notice anyone acting odd? Suspicious figures?"

    cynthia "I… I think someone’s been following me. "

    ace "Can you elaborate?"

    cynthia "I’ve noticed someone lurking around. Hanging by the edges of the buildings. Scuttling through the shade. They always leave before I get too close, but I know they’re there. "
    
    menu:
        "Did you see who?":
            cynthia " I think it might be Vincent…it looks like him. But he wouldn’t do something like that. He’s not a killer, let alone a serial killer!"
            menu:
                "Gail seems to think otherwise. ":
                    cynthia "Well Gail hasn’t had a proper conversation with him, so I hardly think she’d know what he’s like. "
                    ace "Perhaps. Regardless, if you do find out anything more about the identity of your stalker, please come to me or Gail. It could be paramount to the investigation. "
                    cynthia "I will. "
                "I think otherwise.":
                    cynthia "Well you barely know him! He isn’t like that. I’m sure of it. "
                    ace "Now would be the time that Gail would scold you for your exuberant amounts of optimism. Sometimes, pessimism is a necessity. "
                    cynthia "Well you and Gail are the most pessimistic and pragmatic people I know. Someone has to balance it out. "
                    menu:
                        "Ordinarily, I’d agree with you, but considering just how much Gail is trying to defend you, I’d argue that she’s just as sickeningly optimistic.":
                            cynthia "She’s devoted, no doubt, but I wouldn’t argue that she’s optimistic."
                            ace "Maybe. "
                            ace "Regardless, if you do find out anything more about the identity of your stalker, please come forward to either me or Gail. "
                            cynthia "I will."
                        "I suppose.":
                            ace "Also, if you do find out more about your stalker, please, come forward to either me or Gail."
                            cynthia "I will."
                "Have you ever seen Vincent and this figure in the same place?":
                    cynthia "I… no. "
                    cynthia "Still, I can’t imagine he’d do something like that! He’s a far better person than that!"
                    ace "I need evidence, not ideals. "
                    cynthia "Quit being so pessimistic! "
                    ace "I’m being realistic. We need more solid evidence. "
                    ace "Regardless of our differences on this, if you do find out something more, I need to know. "

        "How long has this been going on for?":
            cynthia "Since I’ve had my stalker? About three weeks."
            ace "And they haven’t done anything since then? "
            cynthia "No… there just watching. It’s incredibly disconcerting. It’s like Caller all over again!"
            ace "What do you mean?"
            cynthia "He also… stalked me. Before he died. "
            cynthia "He was also a lot more verbal then my current stalker. "
            ace "Let me or Gail know the moment you know anything more, or if something happens."
            cynthia "I will. "
            menu: 
                "Do you know the identity of your stalker?":
                    cynthia "I’m not sure. "
                    ace "But if you did have to guess, who would you think it is?"
                    cynthia "I think it might be Vincent. But I don’t think he’d do something like that! He’s not that kind of person!"
                    menu:
                        "Gail and I think otherwise.":
                            cynthia " Oh, and how would you know? You’ve never really talked to him!"
                            ace " You’re being too optimistic. "
                            cynthia " Well you and Gail are the most pessimistic and pragmatic people I know. Someone has to balance it out." 
                            menu:
                                "Ordinarily, I’d agree with you, but considering just how much Gail is trying to defend you, I’d argue that she’s just as sickeningly optimistic.":
                                    cynthia " She’s devoted, no doubt, but I wouldn’t argue that she’s optimistic."
                                    ace " Maybe. "
                                    ace "Regardless, if you do find out anything more about the identity of your stalker, please come forward to either me or Gail. "
                                    cynthia " I will."
                                "I suppose.":
                                    ace "Also, if you do find out more about your stalker, please, come forward to either me or Gail."
                                    cynthia "I will. "
                        "Still, we are required to investigate every lead.":
                            cynthia "I suppose that makes sense. "
                            ace "If you have any further information about this stalker, please, tell either me or Gail. It could be critical to the case we’re solving. "
                            cynthia "Will do. "
                "Have you noticed your stalker stick to specific areas?":
                    cynthia "I don’t know. All I know is that it’s near me. "
                    ace "What about their identity? "
                    cynthia "I’m not sure."
                    ace "If you had to guess, who do you think it would be?"
                    cynthia "It almost looks like Vincent, but it can’t be him, he wouldn’t do something like that! "
                    ace "If you say as much. Still, if you do find out anything, please let me know. "
                    cynthia "I will."
    ace "One more thing: Is there an entrance to the sewers nearby?"

    cynthia "An entrance too… the sewers? Why would you want to go there? "

    ace "I don’t intend to go there. I’d just like to know. "

    cynthia "Yeah. There’s one pretty close by. By the dumpster… that Ms. Medici was found in… "
    ace "Is that connected somehow?"

    ace "I’m not allowed to say. "
    ace "Thank you for your cooperation. Have a nice day. "

    cynthia "You as well."

    jump confrontingVincent2

label confrontingVincent2:
    scene broke
    show i_ace at right
    show i_vincent at left

    ace "Mr. Holmes. Quite a coincidence, seeing you so close. "

    vincent "I live here. "

    ace "I can’t say it’s entirely unwelcome, though. I need to talk to you. "
    vincent "Well that makes one of us. ‘Cause I don’t need ‘ta talk to you."

    ace "I suggest you cooperate to avoid being subjected to the full force of the law. "

    vincent "Fine. What do ya need."

    menu:
        "Why are you here?":
            vincent "‘Cause I live here. Like I said. You deaf or just a moron?"
            ace "Is it because Cynthia’s here? "
            ace "Why have you been stalking Cynthia?"
            vincent "I don’t know what the hell you're talking about. "
            ace "Don’t play dumb with me. Cynthia’s been giving you the benefit of the doubt, but I’m not so nice. "
            vincent "Don’t worry I know. You and your partner have made watch’ya think of me perfectly clear. "
            ace "Well you are stalking her. "
            vincent "Yeah! I am! Because she’s a criminal and none of you realized nothing! "
            menu:
                "What makes you think that?":
                    vincent "Because she killed Russel Smith! "
                    ace "What are you talking about? "
                    vincent "I was there. I saw her kill Russel Smith. It was in her butcher’s. "
                    vincent "I heard a yell. I was curious. I wandered in ‘n I saw him bleeding out all over that pigsty. I’ve been watchin’ that hell hole ever since, seein’ if she would kill someone else. And she did! "
                    menu:
                        "What proof do you have that it was Cynthia?":
                            vincent "Cause I saw it!"
                            ace "Not proof enough. You aren’t going to be considered a reliable source."
                            vincent "I’ve got proof enough! Ms. Carver ‘n your partner are gay!"
                            menu:
                                "How long have you known?":
                                    vincent "A while. I never really cared at first ‘cause she was always nice, and there’s only so many times a police woman can sneak in’ta another woman’s place before someone gets suspicious. "
                                    vicent "I wasn’t plannin’ on sayin’ nothing, but if it’s what it takes to put ‘er away, I’ll do it ."

                                    menu:
                                        "Resourceful. ":
                                            vincent "Yeah. I know. There’s a reason I’ve survived this long, ‘n it ain’t cause of society bein’ nice to me. If that’s what it takes, then that’s what it takes. "
                                        "Coward. That’s not even the crime, you’re just using the worst of society to further your own ends!":
                                            vincent "I know, I’m sick ‘n I don’t need any of you to tell me that, but I can’t just let her run around ‘n kill more people! Sometimes it’s worth it. "
                                "How is that proof that she killed someone?":
                                    vincent "It ain’t. But she did kill someone ‘n we could arrest her for it. "
                                    ace "You suggest that ‘we’ arrest her on the grounds that she’s gay, as a front, because she apparently actually killed someone?"
                                    vincent "Cause she did kill someone! It ain’t great but sometimes there ain’t that much of a choice. "
                        "So she’s the murderer… because you stalked around because you apparently saw she killed someone?":
                            vincent "She’s a murderer ‘cause she murdered someone. It ain’t that hard to remember. "
                            ace "You still were stalking someone. This information would be obtained illegally, and therefore would be unable to be used. "
                            vincent "Good thing that ain’t the only information I have. ‘Cause I know she and Gail are gay. "
                            menu:
                                "How long have you known?":
                                    vincent "A while. I never really cared at first ‘cause she was always nice, and there’s only so many times a police woman can sneak in’ta another woman’s place before someone gets suspicious. "
                                    vincent "I wasn’t plannin’ on sayin’ nothing, but if it’s what it takes to put ‘er away, I’ll do it ."
                                    menu:
                                        "Resourceful. ":
                                            vincent "Yeah. I know. There’s a reason I’ve survived this long, ‘n it ain’t cause of society bein’ nice to me. If that’s what it takes, then that’s what it takes."
                                        "Coward. That’s not even the crime, you’re just using the worst of society to further your own ends!":
                                            vincent "I know, I’m sick ‘n I don’t need any of you to tell me that, but I can’t just let her run around ‘n kill more people! Sometimes it’s worth it. "
                                "How is that proof that she killed someone?":
                                    vincent "It ain’t. But she did kill someone ‘n we could arrest her for it. "
                                    ace "You suggest that ‘we’ arrest her on the grounds that she’s gay, as a front, because she apparently actually killed someone?"
                                    vincent "Cause she did kill someone! It ain’t great but sometimes there ain’t that much of a choice. "
                "Cynthia’s the criminal? Remind me who was stalking who?":
                    vincent "I didn’t kill no one! Unlike her! "
                    ace "What are you talking about?"
                    vincent "She killed Russel Smith in that god forsaken pigsty of hers, I saw it! I heard ‘em yell so I ran in ‘n I saw him dying! I know it happened! ‘N it’s gotta be her, cause no one else was there!"
                    ace "Do you have any proof that it happened?"
                    vincent "Cause I saw it happen! Why can’t you listen to that?"
                    ace "Then make me. "
                    vincent "You want proof so badly? Fine! I ain’t got none but I know she and your partner are gay ‘n I’ll release it!"
                    menu:
                        "To who? Who would believe you?":
                            vincent "I think you’d go ‘n be surprised just how many people who jump to hatred. I’d know. I was there. I’m still there. "
                            ace "So if you can’t get proof for your theory that Cynthia murdered someone, then you’ll ruin their lives? Have you no shame? "
                            vincent "Thought you thought I had nothing to lose? ‘Least this way I can take down a murderer.  So are you going ‘ta arrest her or should I? "
                            ace "I’ll handle it, and I’ll handle it right. "
                        "So your big plan is to out her in front of everyone… for what purpose?":
                            vincent "If I can’t get you to arrest her then I’ll expose her for everyone ‘ta hear. Least that way I can ruin her life."
                "Still sticking with the story where she murdered someone?" if stalkerKarma > 0:
                    vincent "Cause she did! And you ain’t listening!"
                    ace "Then make me. "
                    vincent "You want proof so badly? Fine! I ain’t got none but I know she and your partner are gay ‘n I’ll release it!"
                    menu:
                        "To who? Who would believe you?":
                            vincent "I think you’d go ‘n be surprised just how many people who jump to hatred. I’d know. I was there. I’m still there. "
                            ace "So if you can’t get proof for your theory that Cynthia murdered someone, then you’ll ruin their lives? Have you no shame?" 
                            vincent "Thought you thought I had nothing to lose? ‘Least this way I can take down a murderer.  So are you going ‘ta arrest her or should I? "
                            ace "I’ll handle it, and I’ll handle it right. "
                        "So your big plan is to out her in front of everyone… for what purpose?":
                            vincent "If I can’t get you to arrest her then I’ll expose her for everyone ‘ta hear. Least that way I can ruin her life."
        "Why have you been stalking Cynthia?":
            vincent "I don’t know what the hell you're talking about. "
            ace "Don’t play dumb with me. Cynthia’s been giving you the benefit of the doubt, but I’m not so nice. "
            vincent "Don’t worry I know. You and your partner have made watch’ya think of me perfectly clear. "
            ace "Well you are stalking her. "
            vincent "Yeah! I am! Because she’s a criminal and none of you realized nothing! "
            menu:
                "What makes you think that?":
                    vincent "Because she killed Russel Smith! "
                    ace "What are you talking about? "
                    vincent "I was there. I saw her kill Russel Smith. It was in her butcher’s. "
                    vincent "I heard a yell. I was curious. I wandered in ‘n I saw him bleeding out all over that pigsty. I’ve been watchin’ that hell hole ever since, seein’ if she would kill someone else. And she did! "
                    menu:
                        "What proof do you have that it was Cynthia?":
                            vincent "Cause I saw it!"
                            ace "Not proof enough. You aren’t going to be considered a reliable source."
                            vincent "I’ve got proof enough! Ms. Carver ‘n your partner are gay!"
                            menu:
                                "How long have you known?":
                                    vincent "A while. I never really cared at first ‘cause she was always nice, and there’s only so many times a police woman can sneak in’ta another woman’s place before someone gets suspicious. "
                                    vicent "I wasn’t plannin’ on sayin’ nothing, but if it’s what it takes to put ‘er away, I’ll do it ."

                                    menu:
                                        "Resourceful. ":
                                            vincent "Yeah. I know. There’s a reason I’ve survived this long, ‘n it ain’t cause of society bein’ nice to me. If that’s what it takes, then that’s what it takes. "
                                        "Coward. That’s not even the crime, you’re just using the worst of society to further your own ends!":
                                            vincent "I know, I’m sick ‘n I don’t need any of you to tell me that, but I can’t just let her run around ‘n kill more people! Sometimes it’s worth it. "
                                "How is that proof that she killed someone?":
                                    vincent "It ain’t. But she did kill someone ‘n we could arrest her for it. "
                                    ace "You suggest that ‘we’ arrest her on the grounds that she’s gay, as a front, because she apparently actually killed someone?"
                                    vincent "Cause she did kill someone! It ain’t great but sometimes there ain’t that much of a choice. "
                        "So she’s the murderer… because you stalked around because you apparently saw she killed someone?":
                            vincent "She’s a murderer ‘cause she murdered someone. It ain’t that hard to remember. "
                            ace "You still were stalking someone. This information would be obtained illegally, and therefore would be unable to be used. "
                            vincent "Good thing that ain’t the only information I have. ‘Cause I know she and Gail are gay. "
                            menu:
                                "How long have you known?":
                                    vincent "A while. I never really cared at first ‘cause she was always nice, and there’s only so many times a police woman can sneak in’ta another woman’s place before someone gets suspicious. "
                                    vincent "I wasn’t plannin’ on sayin’ nothing, but if it’s what it takes to put ‘er away, I’ll do it ."
                                    menu:
                                        "Resourceful. ":
                                            vincent "Yeah. I know. There’s a reason I’ve survived this long, ‘n it ain’t cause of society bein’ nice to me. If that’s what it takes, then that’s what it takes."
                                        "Coward. That’s not even the crime, you’re just using the worst of society to further your own ends!":
                                            vincent "I know, I’m sick ‘n I don’t need any of you to tell me that, but I can’t just let her run around ‘n kill more people! Sometimes it’s worth it. "
                                "How is that proof that she killed someone?":
                                    vincent "It ain’t. But she did kill someone ‘n we could arrest her for it. "
                                    ace "You suggest that ‘we’ arrest her on the grounds that she’s gay, as a front, because she apparently actually killed someone?"
                                    vincent "Cause she did kill someone! It ain’t great but sometimes there ain’t that much of a choice. "
                "Cynthia’s the criminal? Remind me who was stalking who?":
                    vincent "I didn’t kill no one! Unlike her! "
                    ace "What are you talking about?"
                    vincent "She killed Russel Smith in that god forsaken pigsty of hers, I saw it! I heard ‘em yell so I ran in ‘n I saw him dying! I know it happened! ‘N it’s gotta be her, cause no one else was there!"
                    ace "Do you have any proof that it happened?"
                    vincent "Cause I saw it happen! Why can’t you listen to that?"
                    ace "Then make me. "
                    vincent "You want proof so badly? Fine! I ain’t got none but I know she and your partner are gay ‘n I’ll release it!"
                    menu:
                        "To who? Who would believe you?":
                            vincent "I think you’d go ‘n be surprised just how many people who jump to hatred. I’d know. I was there. I’m still there. "
                            ace "So if you can’t get proof for your theory that Cynthia murdered someone, then you’ll ruin their lives? Have you no shame? "
                            vincent "Thought you thought I had nothing to lose? ‘Least this way I can take down a murderer.  So are you going ‘ta arrest her or should I? "
                            ace "I’ll handle it, and I’ll handle it right. "
                        "So your big plan is to out her in front of everyone… for what purpose?":
                            vincent "If I can’t get you to arrest her then I’ll expose her for everyone ‘ta hear. Least that way I can ruin her life."
                "Still sticking with the story where she murdered someone?" if stalkerKarma > 0:
                    vincent "Cause she did! And you ain’t listening!"
                    ace "Then make me. "
                    vincent "You want proof so badly? Fine! I ain’t got none but I know she and your partner are gay ‘n I’ll release it!"
                    menu:
                        "To who? Who would believe you?":
                            vincent "I think you’d go ‘n be surprised just how many people who jump to hatred. I’d know. I was there. I’m still there. "
                            ace "So if you can’t get proof for your theory that Cynthia murdered someone, then you’ll ruin their lives? Have you no shame?" 
                            vincent "Thought you thought I had nothing to lose? ‘Least this way I can take down a murderer.  So are you going ‘ta arrest her or should I? "
                            ace "I’ll handle it, and I’ll handle it right. "
                        "So your big plan is to out her in front of everyone… for what purpose?":
                            vincent "If I can’t get you to arrest her then I’ll expose her for everyone ‘ta hear. Least that way I can ruin her life."
    ace "Why should I think that you aren’t the murderer? Why should I trust you?"

    vincent "‘Sides the fact I don’t have a bloody reason to kill no one so?"

    ace "Sans Ms. Medici. "

    vincent "Fine. Sans her. Not that I’d kill no one either way, but I ain’t got no reason to kill no one else."

    menu:
        "No one would be suspicious if you were wandering the sewers.":
            vincent "What, cause I’m homeless? What do sewers have ‘ta do with nothing?"
            ace "Defensive. Suspicious. "
            vincent "You’re randomly accusing me! ‘Cause you think I can be found in a sewer! How am I s’posed to react?"
        "And you think that Cynthia does?":
            vincent "Yeah she does. I looked around ‘n she didn’t like all of the people who died, and right before they died, she all fought with ‘em!"
            vincent "Carver was an asshole, he sorta had it coming, but all Smith did was raise ‘er rent! Tell me that ain’t a’least a bit suspicious?"
    ace "…"
    ace "Thank you for your cooperation. I’ll keep what you said in mind."

    vincent "You are gonna expose her though, right? Cause with the shit she did, she shouldn’t go ‘n walk free. "

    ace "I’ll consider." 
    ace "Just one more question. Why didn’t you mention all this earlier? It feels like it should be paramount to the investigation. "

    vincent "‘Cause her girlfriend was there. Why'd I tell everything to her? She’d probably go on an’ spill everythin’ to Ms. Carver. Probably been using each other as a go-between for ages. Maybe your partner’s been wrapped up in all it, ‘n just said nothing to ya. I couldn’t risk it. "
    vincent "Besides, why’d I threaten your partner with revealing her own relationship with ‘er there?  I ain’t that bloody stupid. "

    ace "Maybe…"
    ace "I best return. Have a good evening. "

    vincent "Yeah. Remember what I said. "

    jump dauntingDantes2

label dauntingDantes2:
    scene office
    show i_gail:
        xalign 0.75
        yalign 0.97
    show i_ace:
        xalign 1.2
        yalign 0.97
    show i_dantes at left

    dantes "Good evening. Do you have anything for me? "

    ace "As a matter of fact, I do. We have a confirmed suspect. "

    gail "We do? You didn’t mention this to me. Good to know just how little of a sway I hold in your mind. "

    ace "Gail, not now. "

    dantes "Trouble in paradise, hm? "

    gail "There is no paradise. We are not together."

    dantes "If you say so! Regardless, you do have something for me- someone to be precise. "
    dantes "So? Who is it? Who killed my daughter?"

    menu:
        "Cynthia Carver." if ReticenceKarma > 0: 
            gail "You shitty liar! It isn’t her!"
            hide i_dantes
            show i_dantes smug at left
            dantes "It isn’t? She’s always been the most obvious suspect. What self-respecting woman owns a butchers? Let alone work there? It’s disgusting how the state of the world deteriorates."
            gail "You disgust me. She works her ass off in her job, while your prissy ass doesn’t do shit but count cash. Don’t talk to me about how the world ‘deteriorates’ if you’re the worst of it. "
            dantes "Do you hear her, Ace? All her profanity and disrespect. How could you let her work here?"
            menu:
                "Because she’s the best detective here.":
                    dantes "...If you say so. "
                    $ honestyKarma +=1
                "I’m not totally sure how I let her stay so long.":
                    $ perfidyKarma += 1
                    gail "Really, Ace? I’ve worked here for years, don’t act like I’m the issue! Do you not hear what he’s saying?"
            dantes "Regardless, it’s time you should arrest that witch. She doesn’t deserve to breathe now my daughter is dead. "
            dantes "And don’t let this… woman come with you. "
            gail "This woman can make her own choices. And this woman is coming with you."
            menu:
                "It’s fine, she can come. She needs to see this. ":
                    $ honestyKarma += 1
                    gail "Thank you. "
                    dantes "You’re certain? You never know with women. They become hysterical very easily."
                    ace "I have faith that she won’t. "
                    dantes "If you say as much. "
                    dantes "Ace, can I trust you to be able to handle Carver’s arrest, bring my lovely daughter to rest? "
                    ace "You can."
                    dantes "Good."
                    if perfidyKarma >= honestyKarma:
                        jump perfidy
                    else:
                        jump honesty
                "I think you overestimate your own authority. You aren’t coming.":
                    $ perfidyKarma +=1
                    gail "You- you can’t be serious! "
                    dantes "I’m afraid what Ace says goes. "
                    gail "I… Fine."
                    gail "I need some fresh air. "
                    dantes "Women. Always so frail."
                    dantes "Ace, can I trust you to be able to handle Carver’s arrest, bring my lovely daughter to rest? "
                    ace "You can."
                    dantes "Good."
                    if perfidyKarma >= honestyKarma:
                        jump perfidy
                    else:
                        jump honesty
                "I don’t trust you, now that you’ve been lying to me, infringing on the integrity of the investigation. ":
                    gail " Oh you shitty little- you can’t cut me out of this!"
                    dantes "I’m afraid we can. Harming the integrity of the investigation in which my own daughter died? That’s rather serious. "
                    gail "Is this about me not telling you about Cynthia’s private life? Is that what this is? You can’t be serious! "
                    dantes "You’re acting rather hysterical. I’ll arrange for the police to take care of you. After all, I’d hate for anything to happen to a gorgeous woman like you. "
                    dantes "Ace, I trust for you to be able to handle Carver’s arrest, bring my lovely daughter to rest? "
                    ace "Of course sir. "
                    gail "No- no- you can’t! You can’t do this! Ace! "
                    dantes "Oh really? And why would that be? Care to share?"
                    gail "You piece of shit! "
                    menu:
                        "Dantes, this is going too far. It truly is too personal, and it wouldn’t be professional to share. ":
                            dantes "I suppose. "
                            dantes "Regardless, I’ve got this woman handled. Bring my daughter to justice. "
                            gail "It’s not her! Ace it’s not her! Don’t do this!"
                            ace "I will, Dantes. "
                            jump reticence
                        "I’d be delighted to share. The two of them are dating.":
                            dantes "Your profane little partner? And that witch who killed my daughter? It’s a match made in hell. God is disgusted by you. Did the two of you delight in my daughter’s suffering?"
                            gail "No! Cynthia wasn’t even involved, it wasn’t her! She’s innocent! "
                            dantes "Don’t listen to a word out of her mouth, you can’t trust any of her kind. "
                            dantes "Ace, can I trust you to bring my daughter to justice? "
                            ace "Yes sir. "
                            dantes "Then get her. "
                            jump reticence
        "Vincent Holmes." if stalkerKarma > 0:
            dantes "Vincent? How disappointing. And yet, I feel betrayed. To think he would be the one to murder my dear daughter…"
            ace "My condolences. "
            dantes "Thank you. "
            dantes "On such a note, it’s best you seize that traitor. "
            gail "Can I go with you for his arrest? I’ve been benched for most of this investigation, and it would be refreshing to be able to do something again."
            dantes "A woman? Going to arrest someone? It’s best not to offend your delicate sensibilities. "
            ace "To the contrary, she’s done most of the investigation work. It’s only fair she gets to see the reward for it. "
            dantes "I… suppose I will not try and stop you. "
            gail "Thank god. I was going to lose my mind if I were to stay here any longer. Especially with him. "
            dantes "I suggest you show some more decorum. My daughter is dead and you’re complaining about being bored. "
            gail "Like your daughter was ever any good a-"
            ace "It’s best we leave. We’ll be back shortly with your daughter’s killer brought to justice. "
            dantes "Good."
            jump stalker

label reticence:
    scene butcher
    show i_ace at right
    show i_cynthia at left

    ace "Good evening. "

    cynthia "Good evening! You’re back sooner than I thought you’d be. Did something happen? Is Gail alright?"

    ace "No, but she’ll be better once she’s had time to move on. "

    cynthia "Move on? What are you talking about? Je ne comprends pas. "

    menu:
        "I imagine it can be hard to remain faithful if you find out your girlfriend’s a murderer.":
            cynthia "What are you talking about? I didn’t kill anyone. "
            ace "You can deny all you want, but it won’t change what you’ve done. "
            cynthia "I didn’t do anything. What’s going on? Where’s Gail?"
            ace "I, Ace Wright, place you, Cynthia Carver, under arrest. You’re charged with the murders of Karen Medici, Russel Smith, and Christian Caller. "
            cynthia "I didn’t do it! You’ve got the wrong person! "
        "I, Ace Wright, place you, Cynthia Carver, under arrest.":
            cynthia "I… I don’t understand. "
            ace "You’re charged with the murders of Karen Medici, Russel Smith, and Christian Caller. "
            cynthia "It’s not me! I’m innocent! "

    scene black with fade
    "Ending: Reticence"
    jump end

label honesty:
    scene butcher
    show i_gail sad:
        xalign 1.2
        yalign 0.97
    show i_ace:
        xalign 1.2
        yalign 0.97
    show i_cynthia at left
    ace "Good evening."

    cynthia "Good evening! You’re both back sooner than I thought you’d be. "
    cynthia "Is everything alright, love? You look positively sick. "

    gail "…"

    ace "I, Ace Wright, place you, Cynthia Carver, under arrest. "

    cynthia "Wha- what? I didn’t do anything! "

    ace "You’re charged with the murders of Karen Medici, Russel Smith, and-"

    gail "WAIT! "
    gail "Just stop. Please. I can’t watch this. "
    gail "I can't watch her get arrested…"
    gail "Not for me… "

    cynthia "Y-You? "

    gail "Yeah. I’m the serial killer. I was the one who killed them; Caller for his catcalling, Smith for his eviction attempts, Karen for her threats. I couldn’t watch it any more. I couldn’t talk to them- I know it’d never work, they’d never listen to us, so I did the only thing I could. "

    ace "I don’t understand. Why would you do this? Why would you throw away your life for-for petty revenge! "

    gail "You wouldn’t understand!"
    gail "You didn’t have to watch her get hurt. You didn’t watch her cry. You didn’t see her when they stalked her and threatened everything she’s ever worked toward. I can’t watch everyone keep taking from me. Not again and again and again. I can’t keep watching this happen. "
    gail "Life isn’t kind. And I can’t fix it. But I can’t let it happen. Not if I can stop it. "
    gail "I can’t let her be hurt. "

    cynthia "You can’t let me? I’m not a child. I thought we were in this together. But you lied. "
    cynthia "Well you’re wrong. Because this hurt me far more than anyone else ever did. "

    gail "I know. I’m sorry. "

    ace "Do you confess?"

    gail "I do."
    gail "I, Gail Mourne, confess to the murders of Karen Medici, Russel Smith, and Christian Caller. "
    gail "As such, I therefore place myself under arrest, and await the full subjugation of the law." 

    scene black fade
    "Ending: Honesty"
    jump end

label perfidy:
    scene butcher
    show i_ace:
        xalign 0.75
        yalign 0.97
    show i_gail sad:
        xalign 1.2
        yalign 0.97
    show i_cynthia at left
    ace "Good evening. "

    cynthia "Good evening! You’re both back sooner than I thought you’d be. "
    cynthia "Is everything alright, love? You look positively sick. "

    gail "It’s just… I feel like I’m on the precipice of something awful. Like I’m about to make the worst decision in my life. "

    cynthia "What do you mean?"

    ace "I’ll summarize. I, Ace Wright, place you, Cynthia Carver under a- urgh. "

    hide i_ace
    show i_ace panic:
        xalign 0.75
        yalign 0.97

    hide i_gail sad
    show i_gail:
        xalign 1.2
        yalign 0.97

    hide cynthia
    show i_cynthia horror at left

    ace "Y-you… how could you…"
    cynthia "Oh my god Gail. What did you do! You stabbed him! Oh-ohmy god. We need to get help. "

    ace "You…k-killed them… didn't you…"
    ace "You be…tray…"

    gail "No. All we have to do is wait. "

    ace "You…"

    gail "And no one will ever know."

    scene black fade
    "Ending: Perfidy"
    jump end

label stalker:
    scene broke
    show i_gail:
        xalign 0.75
        yalign 0.97
    show i_ace:
        xalign 1.2
        yalign 0.97
    show i_vincent at left
    ace "Good evening."

    vincent "Good… evening…"
    vincent "What is she doing here?"


    gail "I’m here to do my job. "

    vincent "And what job would that be?"

    gail "I think you can guess. Care to do the honors, Ace?"

    menu:
        "I’d be delighted too.":
            ace "I, Ace Wright, place you, Vincent Holmes, under arrest. You’re charged with stalking Cynthia Carver, and the murders of Karen Medici, Russel Smith, and Christian Caller."
        "To the contrary, I’d gladly give you the opportunity.":
            gail "Why thank you. It delights me to have this piece of shit put away and my worries abated." 
            gail "I, Gail Mourne, place you, Vincent Holmes, under arrest. You’re charged with the stalking of Cynthia Carver, and the murders of Karen Medici, Russel Smith, and Christian Caller. "
    vincent "It ain’t me who killed ‘em, it’s her bloody girlfriend! ‘N if you try ‘nd arrest me I’ll tell everyone just what the two of you are! "

    gail "Oh please. And who would believe you? The only thing that would happen is that I could sue you for defamation. Not that it would matter. You don’t have any money, and therefore, you don’t have any respect. "
    gail "Hey Ace, can I have a word alone with our accused? "

    ace "Keep it snappy. "

    gail "Oh, don’t worry, I will."
    
    hide i_ace

    gail "See, this is where you made one very important mistake. You fucked with my girlfriend, accused her, stalked her, because you thought you were some sort of hero. Well you aren’t. In fact you aren’t even right about your little accusation."
    gail "Because it isn’t Cynthia. It’s me. And you and I know fully well that if you accuse me, no one would ever believe you, so I suggest you keep your mouth shut. "
    gail "Do you understand me?"

    vincent "Yeah."

    gail "Good. "

    scene black fade
    "Ending: Stalker"

    jump end


label end:
    return