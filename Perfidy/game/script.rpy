# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image i_ace = At('ace1', sprite_highlight('ace'))
image i_ace happy= At('ace_happy', sprite_highlight('ace'))
image i_ace annoyed= At('ace_annoyed', sprite_highlight('ace'))
image i_gail = At('gail1', sprite_highlight('gail'))
image i_gail happy= At('gail_happy', sprite_highlight('gail'))
image i_gail mgh= At('gail_mgh', sprite_highlight('gail'))
image i_cynthia = At('cynthia1', sprite_highlight('cynthia'))
image i_cynthia happy= At('cynthia_happy', sprite_highlight('cynthia'))
image i_cynthia horror= At('cynthia_horror', sprite_highlight('cynthia'))
image i_vincent = At('vincent1', sprite_highlight('vincent'))
image i_vincent unhinged= At('vincent_unhinged', sprite_highlight('vincent'))

define ace = Character("Ace Wright", image = 'ace1', callback = name_callback, cb_name = 'ace')
define cynthia = Character("Cynthia Carver", image = 'cynthia1', callback = name_callback, cb_name = 'cynthia')
define gail = Character("Gail Mourne", image = 'gail1', callback = name_callback, cb_name = 'gail')
define vincent = Character("Vincent Earl Holmes", image = 'vincent1', callback = name_callback, cb_name = 'vincent')
define dantes = Character("Dantes Medici")
define karen = Character("Karen Medici")
define russel = Character("Russel Smith")
define christian = Character("Christian Caller")

# The game starts here.

label start:
    scene bg room
    cynthia "To be honest, I don’t specifically remember. She went in to buy a cut, as this is a barber’s shop, and I sold it. I think she complained about there being too much fat? It blended together. I was trying to diffuse it, but she wasn’t listening, and was saying all this horrible stuff. I would be lying if I said I wasn’t a bit relieved."

    jump karenDeathRevealed

label karenDeathRevealed:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    with None
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show i_gail at left

    gail "Karen’s dead."

    show i_ace at right

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
            scene bg room
        "Remain Silent":
            scene bg room
    
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
            scene bg room

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

                    #Add cheeky to header
                    ace "Thought I wasn’t supposed to jump to conclusions so quickly"
                    
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

                            gail "That technically is very important."

                            ace "So, Ms. technically-not-my-boss, we heading off to investigate our lead?"

                            gail "Roger that, Mr. technically-my-boss."

                            ace "Well what are we waiting for?"
                            jump confrontingVincent1
                        "Well what are we waiting for?":
                            jump confrontingVincent1
    jump confrontingVincent1

label confrontingVincent1:
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
                "A coincidence that has nothing to do with your history with Mr. Medici?":

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
                                #Cynthia Accuse Path Open
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
                                    vincent "What’s your goddamn problem? You’re so desperate ta’ know why I was there? Fine!"
                                    vincent "I watched Russel Smith die. He was there in that goddamn hellhole and I heard him scream and watched him bleed to death in that pigsty. I could feel his blood on my hands and it was all over the floor and when I stepped it squelched."
                                    vincent "But’cha can’t tell ‘cause that whole place is soaked in it. All ya’ gotta do is mop up the shit and no one would have a clue. "
                                    vincent "You wan’ta know so badly why I was there, huh? Because I watched a man bleed to death, and I was right in bettin’ that it would happen again. So if anyone has a reason to be here, it would be me. "

                                    menu:
                                        "Are you implying that Cynthia is involved?":

                                            vincent "I dunno. Am I? It’s not like there’s been two bodies by Ms. Carver’s establishment. "

                                            #Add italics around "not" maybe? IDK
                                            gail "Cynthia is not related to this shit. Keep her name out of your foul mouth, you bastard."
                                            
                                            vincent "Why? She matter to ya’? Maybe you're involved."

                                            menu: 
                                                "Quit throwing baseless accusations. I trust Cynthia far more than I trust you.":

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
                                    vincent "You wan’ta know why I was there so badly? Fine!"
                                    vincent "I watched Russel Smith die! And it was there- right there- in that gods forsaken butchers and nobody noticed!"
                                    vincent "He was lying- bleeding out- it was all over and it sunk into the floors  but you’d never find it ‘cause that whole hellhole soaked in it. Bleeding out like every other gutted pig in that place."
                                    vincent "I was next to him- I was tryin’ ta stop the bleeding I think but I knew it was too late he was already unconscious but I could feel his blood in my hand and it soaked into my shoes and my clothes and his body was still so warm and wet and I thought I’d go ‘n vomit cause that whole place smelt of carcass. "
                                    vincent "I went in ‘cause I heard a scream and I didn’t know what was goin’ on. Ms. Carver was always nice and I didn’t want anything to happen to her but it didn’t sound like ‘er, so I wandered in an there he was bleedin’ out on the floor and then-"
                                    vincent "I heard footsteps coming and I bolted."
                                    vincent "Ya’ satisfied with that you bastard?"
                                    
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
    ace "You doing alright?"

    gail "I don’t know…"
    gail "It was fine when it was just some unknown killer for money. Now Cynthia’s in it, and I guess it’s just more real now."
    gail "And I know that if anyone else was to figure out that…"

    ace "That you and Cynthia are together?"

    gail "Yeah."

    menu:
        "Don’t worry, I’ll make sure nobody knows. We can try to keep her out of this.":
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

    #Displeasure
    gail "Probably shouldn’t say. Wouldn’t want to get kicked off the investigation for obstructing it or anything!"

    ace "Gail. Enough. I get your upset, but you still have a job to do. "

    cynthia "And it’ll be fine, love! You yourself said that I’m innocent, so the river of justice will leave us untouched!"

    gail "Alright." 
    #smile
    gail "You're always so positive. I’ve always loved that about you."

    cynthia "I know."

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

                    cynthia "Yeah, of course. See you later, love."

                    gail "See you!"

                    jump droppingCynthia
                #Prequisite of being mean to Vincent
                "Has he been around more often?":
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

                            cynthia "Alright. Love you!"

                            gail "Love you too."
                            jump droppingCynthia
                        "I think we have all we need. Thank you for your cooperation.":
                            gail "Ace what are you talking about? We barely asked Gail shit! Basically the only thing you asked was designed to validate Vincent…"
                            gail "I can’t believe you. You can’t seriously be believing that piece of shit man over my own girlfriend who you’ve known for years! What the hell, Ace! "
                            gail "I need to talk to you. Alone."
                            gail "See you later, love. "

                            cynthia "See you later, love. You too, Ace."
                            jump droppingCynthia
        #Mean option
        "Do you know Russel Smith or Christian Caller?":
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
                                    scene bg room
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
        "That’s funny, because I seem to recall Mr. Holmes implying otherwise.":
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
    gail "…"

    ace "It seems like you want to talk, so spit it out. "

    gail "I want you to drop Cynthia from the investigation. "

    ace "…Pardon?"

    gail "Drop Cynthia from the investigation."
 
    ace "That’s a bold request, even for you, especially now. "

    gail "You and I both know that the courts will be biased against her- she runs her own business for Christ’s sake."
    gail "It’ll only get worse if they learn that she…"
    gail "That she’s bent, and we’re together."

    menu:
        "I’ll do what I can.":
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
                            gail "Don’t give me that shit! You’ve known me since we were kids, you don’t get to act like it was all just a farce."
                            gail "Sometimes you really are unbelievable."

                            ace "Why? For asking questions you don’t want to answer? "

                            gail "I can’t deal with all of this. All of your obsessiveness! "
                            gail "I’ll be back later. Don’t follow me, I’m not talking to you. "
                            jump dauntingDantes


    jump dauntingDantes

label dauntingDantes:
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