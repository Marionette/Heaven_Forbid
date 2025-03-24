#define narrator = nvl_narrator

label start:

  $headpiece_halo = False
  $headpiece_helm = False
  $headpiece_coronet = False
  $wings_feather = False
  $wings_flaming = False
  $wings_gold = False
  $accessory_bow = False
  $accessory_sword = False
  $accessory_trumpet = False
  $condition_god = False
  $points_dexterity = 0
  $points_strength = 0
  $points_charisma = 0
  $points_victory = 0
  $points_surrender = 0

  jump part_001

label part_001:

  play music music_tension fadein 2.0

  show bg bg_arena_empty with slow_dissolve

  show asta asta_sad at center behind lilis with dissolve

  Cherub "Oh, you poor things."

  Cherub "You're finally here in paradise."

  Cherub "This is the culmination of your empty, lonely lives."

  Cherub "You didn't think heaven would be like this, did you?"

  Cherub "You imagined fanfare. Trumpets and trilling voices."

  Cherub "Instead, you've ended up in this arena."

  show bg bg_arena with slow_dissolve

  show lilis lilis_anxious #as side image

  show eva eva_anxious at right behind lilis with dissolve

  "We, the last two humans in a sea of angels, say nothing."

  "We're staring steadily, sizing each other up."

  show asta asta_smile at center behind lilis

  Cherub "Pray, what are your names?"

  show asta asta_default at center behind lilis

  "No answer is forthcoming from her. I doubt she's even heard."

  show lilis lilis_default #as side image

  "I suppose I should say something, just to be polite."

  "True, this cherub speaking to us seems sympathetic enough."

  show lilis lilis_anxious #as side image

  "But who knows what the rest of the cherubim will make us do?"

  show eva eva_default at right behind lilis

  show lilis lilis_default #as side image

  Lilis "My name in the living world was Lilis."

  show asta asta_smile at center behind lilis

  Cherub "Lilis. That's a lovely name."

  Cherub "You must be named after one of mankind's very eldest."

  Cherub "Is that accurate?"

  show asta asta_default at center behind lilis

  show lilis lilis_anxious #as side image

  "When I only furrow my brows, the cherub swiftly backtracks."

  show asta asta_anxious at center behind lilis

  Cherub "Never mind that."

  Cherub "I didn't mean to suggest anything untoward."

  show lilis lilis_default #as side image

  show asta asta_smile at center behind lilis

  Cherub "Hello, Lilis. You can call me Asta."

  show asta asta_default at center behind lilis

  "The cherub called Asta now addresses the other human being."

  show asta asta_smile at center behind lilis

  Asta "And how would you prefer us to refer to you?"

  show asta asta_default at center behind lilis

  "There's a beat of silence before she responds."

  Eva "My friends call me Eva."

  show lilis lilis_anxious #as side image

  "Her phrasing just now is particular."

  "{i}Her friends{/i} call her Eva, she tells us."

  "But we're not {i}her friends,{/i} are we?"

  show lilis lilis_sad #as side image

  "Presently, she sees me as an enemy more than anything."

  "However, it wasn't always that way."

  show lilis lilis_anxious #as side image

  show eva eva_anxious at right behind lilis

  "She's eyeing me now as if weighing her chances of winning."

  "In the arena, a charged silence reigns once more."

  show asta asta_smile at center behind lilis

  Asta "Have you two been enjoying the weather in heaven?"

  Asta "Do you know the weather is forever fair up here?"

  show asta asta_default at center behind lilis

  "Neither Eva nor I respond."

  show asta asta_sad at center behind lilis

  "The cherub called Asta blows out a delicate sigh."

  Asta "I can't expect small talk in this situation, I suppose."

  Asta "It's no wonder you humans are acting this way."

  show asta asta_anxious at center behind lilis

  Asta "You're teeming with distrust, hardened with hostility."

  Asta "You're picturing tricks and traps around every corner."

  show asta asta_sad at center behind lilis

  Asta "It's understandable in the context of how you've come."

  Asta "From ninth to second of heaven's tiers, you've climbed."

  Asta "With every tier, hope has increasingly deserted you."

  Asta "Here you are in the second tier, ruled by the cherubim."

  Asta "How far you've come since arriving at the pearly gates."

  hide eva

  hide asta

  show bg bg_dark with slow_dissolve

  show lilis lilis_sad #as side image

  "Indeed, much has transpired since we set foot in paradise."

  stop music fadeout 1.0

  "In the beginning, there were more of us. Ten, to be exact."

  play music music_default fadein 2.0

  show bg bg_gates with slow_dissolve

  show lilis lilis_shock #as side image

  "Upon my arrival, I gazed up at the pearly gates."

  "Never had I ever witnessed such a wondrous sight."

  "I couldn't believe I was finally here."

  "Paradise at last."

  show lilis lilis_smile #as side image

  "Already, heaven was promising to be such a glorious place."

  "I'd evidently done enough in my lifetime to merit a spot."

  "The mere thought filled my heart with peace."

  show lilis lilis_default #as side image

  "As I was admiring the gates, I heard footsteps approaching."

  show eva eva_shock at center behind lilis with dissolve

  show lilis lilis_shock #as side image

  "Before me was a beautiful woman I'd never seen before."

  "Where did she come from?"

  show lilis lilis_default #as side image

  show eva eva_smile at center behind lilis

  Eva "Hey, this is heaven, isn't it?"

  show eva eva_default at center behind lilis

  show lilis lilis_smile #as side image

  Lilis "That's right. I got here just before you did."

  Lilis "I've been waiting for these gates to open."

  show lilis lilis_default #as side image

  show eva eva_smile at center behind lilis

  Eva "I'll wait with you, then."

  Eva "I'm Eva, by the way."

  show eva eva_default at center behind lilis

  show lilis lilis_smile #as side image

  Lilis "And I'm Lilis."

  show lilis lilis_default #as side image

  Eva "Do you think anyone else is coming?"

  Lilis "I'm not sure. Perhaps."

  show eva eva_smile at center behind lilis

  Eva "Well, either way, I'm happy we're both here."

  show eva eva_default at center behind lilis

  show lilis lilis_smile #as side image

  Lilis "Yes, it's nice to know I won't have to enter alone."

  show lilis lilis_default #as side image

  "Eva's dark gaze wandered up the gates."

  Eva "I wonder when we can expect these gates to open?"

  Lilis "I have no clue."

  show lilis lilis_anxious #as side image

  Lilis "Sorry, while we're waiting, can I ask you something?"

  Lilis "It's something very personal."

  show lilis lilis_default #as side image

  show eva eva_shock at center behind lilis

  Eva "Oh! Ask me anything!"

  show eva eva_smile at center behind lilis

  Eva "I don't mind. It'll help pass the time."

  show eva eva_default at center behind lilis

  show lilis lilis_smile #as side image

  Lilis "All right. If it's really okay with you."

  show lilis lilis_default #as side image

  show eva eva_smile at center behind lilis

  Eva "It's a hundred percent okay."

  show eva eva_default at center behind lilis

  show lilis lilis_anxious #as side image

  Lilis "How is it you arrived here?"

  show lilis lilis_default #as side image

  show eva eva_anxious at center behind lilis

  Eva "Are you asking me how I died?"

  show eva eva_default at center behind lilis

  show lilis lilis_anxious #as side image

  Lilis "Sorry, I wasn't quite sure how to put it."

  Lilis "The last thing I want to do is to offend you."

  Lilis "Especially since you just got here."

  show lilis lilis_default #as side image

  show eva eva_smile at center behind lilis

  Eva "It's fine. I'm not offended."

  show eva eva_anxious at center behind lilis

  stop music fadeout 1.0

  Eva "Here's the thing."

  play music music_emotion fadein 2.0

  Eva "I'm not a hundred-percent sure how it happened."

  show eva eva_sad at center behind lilis

  Eva "But I'm guessing it was a sudden cardiac arrest."

  Eva "Either that or heatstroke."

  show eva eva_default at center behind lilis

  show lilis lilis_anxious #as side image

  Lilis "Really? What makes you think that?"

  show lilis lilis_default #as side image

  show eva eva_anxious at center behind lilis

  Eva "It was unseasonably hot that day."

  show eva eva_default at center behind lilis

  Eva "You see, I lived in the Philippines."

  show lilis lilis_smile #as side image

  Lilis "I've heard it's beautiful in that archipelago."

  show lilis lilis_default #as side image

  show eva eva_smile at center behind lilis

  Eva "Oh, it's lovely. One of the world's loveliest nations."

  Eva "Maybe I sound biased. I don't care."

  show eva eva_default at center behind lilis

  Eva "But the country's temperature can be hellish at times."

  Eva "The weather can go from typhoons to sweltering sun."

  Eva "That fateful day, I was on a run."

  Eva "I take one every morning before work."

  show lilis lilis_smile #as side image

  Lilis "Oh, what is it you do?"

  Lilis "Or what you used to do, I suppose."

  show lilis lilis_default #as side image

  show eva eva_smile at center behind lilis

  Eva "I was a programmer."

  Eva "I loved my job. I found it intellectually stimulating."

  show lilis lilis_smile #as side image

  Lilis "I'm sure it was."

  show lilis lilis_default #as side image

  show eva eva_default at center behind lilis

  Eva "The con is I pretty much sat behind a desk all day."

  show eva eva_smile at center behind lilis

  Eva "So a daily exercise regimen was crucial."

  Eva "A lap or two around my village made such a difference."

  show eva eva_default at center behind lilis

  show lilis lilis_anxious #as side image

  Lilis "You sure you weren't hit by a car while running?"

  show lilis lilis_sad #as side image

  Lilis "That type of tragedy can happen so suddenly."

  show lilis lilis_shock #as side image

  Lilis "Wait. Sorry."

  show lilis lilis_anxious #as side image

  Lilis "I probably shouldn't have asked that."

  Lilis "I didn't intend to be offensive."

  Lilis "I didn't mean to suggest you were being careless."

  show lilis lilis_default #as side image

  show eva eva_smile at center behind lilis

  Eva "I don't take offense easily, I promise."

  Eva "So you don't need to keep apologizing."

  show eva eva_default at center behind lilis

  show lilis lilis_shock #as side image

  "I parted my mouth to say sorry."

  show lilis lilis_default #as side image

  "Then I caught myself just in time and switched tracks."

  show lilis lilis_anxious #as side image

  Lilis "So it couldn't have been a car that got you?"

  show lilis lilis_default #as side image

  Eva "I doubt it."

  Eva "I would've remembered if a car was careening toward me."

  show eva eva_anxious at center behind lilis

  show lilis lilis_anxious #as side image

  Eva "Besides, my chest began aching while I was running."

  Eva "I recall collapsing and struggling to breathe."

  show lilis lilis_shock #as side image

  Lilis "Oh no."

  show lilis lilis_sad #as side image

  show eva eva_sad at center behind lilis

  Eva "I know I should've stopped well before I fell."

  Eva "I should've asked anybody around for help."

  Eva "But what's done is done."

  show eva eva_default at center behind lilis

  show lilis lilis_default #as side image

  Eva "I'm here now."

  Eva "How about you? How did you get here?"

  show lilis lilis_sad #as side image

  Lilis "Hit and run."

  show eva eva_shock at center behind lilis

  Eva "What?"

  show eva eva_sad at center behind lilis

  Eva "That sucks."

  Eva "Do you remember it happening?"

  Lilis "Yeah."

  Lilis "The thing is it happened when I least expected it."

  show eva eva_default at center behind lilis

  show lilis lilis_default #as side image

  Lilis "I was doing something I've done loads of times before."

  Eva "What were you doing?"

  Lilis "Heading to the coffee shop across from the studio."

  Eva "Studio?"

  show lilis lilis_smile #as side image

  Lilis "A design studio. I used to work as a graphic designer."

  Lilis "Like you, I enjoyed my work."

  Lilis "I loved all the creativity it entailed."

  show lilis lilis_default #as side image

  show eva eva_smile at center behind lilis

  Eva "That sounds super cool."

  show eva eva_default at center behind lilis

  Eva "So you were working when it happened?"

  Lilis "I was taking a short break from this big project."

  Lilis "While I was crossing the road, I was deep in thought."

  Lilis "I was contemplating the color for a certain heading."

  Lilis "Red font or black font? I couldn't settle on one."

  Lilis "I'm fairly certain I was in the pedestrian lane."

  Lilis "And the traffic light must've been red."

  Lilis "I obeyed traffic laws. I did so every day."

  show lilis lilis_anxious #as side image

  show eva eva_anxious at center behind lilis

  Lilis "A car seemed to come out of nowhere."

  show lilis lilis_shock #as side image

  Lilis "{i}Bam!{/i}"

  show lilis lilis_sad #as side image

  show eva eva_sad at center behind lilis

  Lilis "In a split-second, it was all over."

  Lilis "The last thing I saw was the vehicle speeding away."

  show eva eva_mad at center behind lilis

  Eva "That's horrible!"

  Eva "I hope somebody caught that dangerous criminal!"

  show eva eva_sad at center behind lilis

  Lilis "It {i}was{/i} horrible."

  Lilis "And it happened with zero warning."

  Lilis "The worst part was I couldn't say bye to my family."

  Eva "I feel you. I have regrets of my own."

  Lilis "That's understandable. We both died so suddenly."

  Eva "Yeah. No goodbyes to loved ones."

  Eva "And so many goals left unaccomplished."

  Lilis "I get you. The way we crossed over wasn't ideal."

  show lilis lilis_default #as side image

  show eva eva_default at center behind lilis

  Lilis "But as you said earlier, we're here now."

  show lilis lilis_smile #as side image

  Lilis "It's beautiful up here."

  show eva eva_smile at center behind lilis

  Eva "It really is. "

  Lilis "Nothing hurts anymore."

  Lilis "No freak accidents or heart attacks."

  Eva "Indeed. Heaven is the ultimate destination."

  Eva "We'll be able to fulfill our dreams here, and then some."

  Lilis "I hope you're right."

  show lilis lilis_default #as side image

  show eva eva_default at center behind lilis

  stop music fadeout 1.0

  "At that point, we lapsed into a companionable silence."

  play music music_default fadein 2.0

  show lilis lilis_shock #as side image

  show eva eva_shock at left behind lilis with dissolve

  show blue blue_default at center behind lilis with dissolve

  "Then another human being arrived suddenly in our midst."

  show lilis lilis_default #as side image

  show eva eva_default at left behind lilis

  B___ "How do you do? My name is B◼◼◼."

  show eva eva_smile at left behind lilis

  Eva "We're doing well. Thanks for asking."

  Eva "My name's Eva."

  show lilis lilis_smile #as side image

  Lilis "And mine is Lilis."

  show lilis lilis_default #as side image

  show eva eva_default at left behind lilis

  B___ "Can you believe we're finally here in heaven?"

  B___ "During my earthly existence, I often pictured it."

  B___ "Or at least I tried my best."

  B___ "My mind attempted to envision these pearly gates."

  B___ "But paradise has thus far exceeded every expectation."

  show eva eva_smile at left behind lilis

  Eva "Yeah, it's something, isn't it?"

  show eva eva_default at left behind lilis

  B___ "Something, yes. At the very least."

  B___ "None of my books could've prepared me for this."

  show lilis lilis_smile #as side image

  Lilis "Did you read religious texts often?"

  show lilis lilis_default #as side image

  B___ "I did, indeed."

  B___ "I once served as a Catholic priest."

  B___ "The church was my home, the parishioners my family."

  B___ "Cancer consumed my body eventually."

  B___ "But the disease couldn't take my soul, evidently."

  show eva eva_smile at left behind lilis

  Eva "Well said!"

  show eva eva_default at left behind lilis

  "B___'s arrival seemed to open the floodgates for others."

  "Feet pitter-pattered as stranger after stranger emerged."

  "They went from strangers to friends as we all conversed."

  "Introductions were given, and niceties were exchanged."

  show green green_default at right behind lilis with dissolve

  G____ "Hello, everyone. The name's G◼◼◼◼."

  G____ "Heaven's a dream come true, isn't it?"

  G____ "In my case, it might literally be a dream."

  G____ "Since I'm pretty sure I passed away in my sleep."

  show lilis lilis_sad #as side image

  show eva eva_sad at left behind lilis

  Lilis "That's unfortunate. You have my sincere condolences."

  Eva "And mine."

  show lilis lilis_default #as side image

  show eva eva_smile at left behind lilis

  Eva "But what you're seeing now is reality, not a dream!"

  Eva "We promise!"

  Eva "Do you need us to pinch you to prove it?"

  show eva eva_default at left behind lilis

  G____ "That's not necessary."

  G____ "I've been pinching myself since I arrived."

  G____ "To think that I would end up here, of all places!"

  G____ "I was just a humble editorial cartoonist!"

  show lilis lilis_smile #as side image

  Lilis "That sounds like it would be a cool job."

  Lilis "I was a creative on Earth as well."

  show lilis lilis_default #as side image

  G____ "Really? We have to talk more about that!"

  show lilis lilis_smile #as side image

  Lilis "Yeah, we definitely should."

  show lilis lilis_default #as side image

  hide blue

  show yellow yellow_default at center behind lilis with dissolve

  Y_____ "All this talk about jobs is fascinating to me!"

  Y_____ "I was still a student when I kicked the bucket."

  Y_____ "I could never figure out what major I wanted."

  Y_____ "Oh, my name's Y◼◼◼◼◼, by the way."

  show lilis lilis_smile #as side image

  Lilis "Nice to meet you!"

  show lilis lilis_sad #as side image

  Lilis "You seem so young. You crossed over so soon."

  Lilis "You must have a ton of regrets."

  show lilis lilis_default #as side image

  Y_____ "I do. But I was prepared to cross over, in a way."

  Y_____ "My doctor told me I might not have very long."

  Y_____ "You see, I've always had a weak heart."

  Y_____ "But it was a big heart! I'm sure of it!"

  show eva eva_smile at left behind lilis

  Eva "Yeah! You're in heaven, after all!"

  Eva "We've all got big, strong hearts here!"

  show eva eva_default at left behind lilis

  hide green

  show orange orange_default at right behind lilis with dissolve

  O_____ "Can I, by any chance, join the Big Hearts Club?"

  show lilis lilis_smile #as side image

  Lilis "Of course you can! Welcome to paradise!"

  show lilis lilis_default #as side image

  O_____ "My name's O◼◼◼◼◼."

  O_____ "I was your everyday, run-of-the-mill office worker."

  O_____ "Even the cause of my death was ordinary."

  O_____ "It was the common cold, alongside many complications."

  O_____ "You know, at university, I was a philosophy major."

  O_____ "Philosophical discourse was my one true passion."

  O_____ "Of course, I struggled to make a buck off it."

  show eva eva_smile at left behind lilis

  Eva "Feel free to bend my ear about philosophy anytime."

  Eva "I enjoy an intellectual debate, every now and then."

  show eva eva_default at left behind lilis

  hide yellow

  show indigo indigo_default at center behind lilis with dissolve

  I_____ "As do I. I find it invigorating."

  I_____ "Salutations. I'm none other than I◼◼◼◼◼."

  I_____ "I was an actress. Theater was my life."

  I_____ "Certainly, an accident onstage led to my demise."

  I_____ "Even so, I harbor no regrets."

  I_____ "I passed into this dimension doing what I loved."

  show eva eva_smile at left behind lilis

  Eva "What an admirable attitude to have!"

  show eva eva_default at left behind lilis

  hide orange

  show pink pink_default at right behind lilis with dissolve

  P___ "I wish I could feel as positively about my passing."

  P___ "I was, sadly, yet another casualty of the pandemic."

  show lilis lilis_sad #as side image

  Lilis "I'm so sorry to hear that."

  Lilis "My heart goes out to you."

  show lilis lilis_default #as side image

  P___ "Thank you. That's very sweet of you."

  P___ "I'm P◼◼◼. It's wonderful to meet you all."

  P___ "I worked as a nurse in a public hospital."

  P___ "So I was a frontline worker at that time."

  show eva eva_smile at left behind lilis

  Eva "That's a very noble profession."

  Eva "I'm sure many lives were enriched by yours."

  show eva eva_default at left behind lilis

  hide indigo

  show violet violet_default at center behind lilis with dissolve

  V_____ "My work on Earth wasn't quite so noble."

  V_____ "Hey, everybody! I'm V◼◼◼◼◼!"

  V_____ "You might've met me at a bar once or twice."

  V_____ "If we got into after-bar shenanigans, no, we didn't."

  V_____ "Nah, I'm just messing with you all."

  V_____ "I did stand-up comedy for a living."

  show lilis lilis_smile #as side image

  Lilis "You must've brightened many days in your time."

  Lilis "As they say, laughter is the best medicine."

  V_____ "Hah, that depends!"

  show lilis lilis_default #as side image

  Lilis "Really? On what?"

  V_____ "On whether the spectators match my sense of humor!"

  V_____ "I gotta tell you, my last night on the job was a dud."

  V_____ "All my jokes fell flat for someone in the audience."

  V_____ "And he made me pay for it! With stone-cold murder!"

  show lilis lilis_shock #as side image

  Lilis "What?"

  Lilis "That's terrible!"

  show lilis lilis_default #as side image

  V_____ "Well, it would be terrible if it was true."

  V_____ "I'm just joshing you. I can't help myself."

  V_____ "To put it plainly, the pandemic got me too."

  V_____ "So I was admitted to a hospital when I croaked."

  V_____ "I was lying on a musty bed. All by my lonesome."

  P___ "Same here."

  P___ "Hearing that now makes me feel less alone."

  V_____ "It does, doesn't it?"

  V_____ "It's tragic, but at least we're in this together."

  show eva eva_smile at left behind lilis

  show lilis lilis_smile #as side image

  "We all continued conversing and bonding with one another."

  show lilis lilis_default #as side image

  show eva eva_shock at left behind lilis

  "Then something seemed to catch Eva's attention."

  show eva eva_default at left behind lilis

  "She spoke to me in a soft voice only I could hear."

  Eva "Hey, Lilis."

  show lilis lilis_smile #as side image

  Lilis "What's up, Eva?"

  show lilis lilis_default #as side image

  Eva "Somebody else is here."

  show lilis lilis_shock #as side image

  Lilis "Huh? Where?"

  show lilis lilis_default #as side image

  "Eva puckered her lips in the direction of the newest person."

  show lilis lilis_shock #as side image

  Lilis "Oh! I see him now!"

  show lilis lilis_anxious #as side image

  Lilis "He looks like he's hesitant to come closer."

  show lilis lilis_default #as side image

  show eva eva_smile at left behind lilis

  Eva "Should we go greet him and make him feel welcome?"

  show lilis lilis_smile #as side image

  Lilis "Agreed. Nobody here should feel left out."

  show lilis lilis_default #as side image

  show eva eva_default at left behind lilis

  hide violet

  hide pink

  "Eva and I broke off from the rest of the group."

  show red red_default at center behind lilis with dissolve

  "We approached the most recent arrival at the gates."

  show eva eva_smile at left behind lilis

  Eva "Hey there!"

  Eva "What's your name?"

  show eva eva_default at left behind lilis

  R__ "I'm R◼◼."

  show eva eva_smile at left behind lilis

  Eva "I'm Eva."

  show lilis lilis_smile #as side image

  Lilis "And I'm Lilis."

  show lilis lilis_default #as side image

  show eva eva_default at left behind lilis

  "With introductions out of the way, R__ gazed at the gates."

  R__ "So this place is heaven, huh?"

  show eva eva_smile at left behind lilis

  Eva "That's right."

  Eva "Welcome to paradise."

  show eva eva_default at left behind lilis

  show lilis lilis_smile #as side image

  Lilis "So you've been sent to heaven too?"

  show lilis lilis_default #as side image

  R__ "Obviously. I'm here, aren't I?"

  R__ "Why, did you assume I was an interloper or something?"

  R__ "You think I don't belong here with you good people?"

  R__ "You planning to shoo me away?"

  show lilis lilis_shock #as side image

  Lilis "No! I meant nothing of the sort!"

  show lilis lilis_anxious #as side image

  Lilis "I was just trying to make friendly conversation."

  R__ "Hey, relax."

  R__ "I was just ribbing."

  show lilis lilis_default #as side image

  R__ "I tend to do that when I'm nervous about something."

  R__ "I often rub people the wrong way upon first meeting."

  R__ "It doesn't help that I'm a criminal defense lawyer."

  R__ "Or I used to be, I suppose."

  R__ "Nearly all of my clients were deemed indigent."

  R__ "My occupation often drew judgment from those I met."

  R__ "I recall being in a courtroom on my last day on Earth."

  R__ "I remember a sudden flash of silver, but not much else."

  R__ "I guess it could've been a weapon somebody snuck in."

  R__ "How did that person even get it past the guards?"

  R__ "I don't know. And I'll never know now."

  R__ "The security at that courthouse was nothing to scoff at."

  "R__ glanced up at the pearly gates once more."

  R__ "Truth be told, I can't believe I'm here now."

  R__ "Heaven only accepts the best of the best, right?"

  R__ "And I often don't feel good enough."

  show eva eva_smile at left behind lilis

  Eva "Of course you're good enough. We all are."

  Eva "That's why we've all arrived at these gates."

  Eva "God doesn't make mistakes."

  show eva eva_default at left behind lilis

  show lilis lilis_smile #as side image

  Lilis "Eva is right."

  Lilis "We're all here for a reason."

  Lilis "That includes you, R◼◼."

  show lilis lilis_default #as side image

  R__ "Sorry about earlier, Lilis."

  R__ "You seem absolutely lovely. You both do."

  R__ "I shouldn't have been so annoying right off the bat."

  R__ "I call it my foot-in-mouth syndrome."

  show lilis lilis_smile #as side image

  Lilis "Hey, don't worry about it."

  Lilis "It's all good. We're all good."

  show lilis lilis_default #as side image

  R__ "I appreciate that."

  show eva eva_smile at left behind lilis

  Eva "R◼◼, would you like to meet the others?"

  Eva "There are ten of us here at the gates so far."

  show eva eva_default at left behind lilis

  R__ "Yeah, let's go."

  show pink pink_default at right behind lilis with dissolve

  "Eva, R__, and I rejoined the others."

  "R__ introduced himself to the rest of the group."

  "They all, in return, told him their names."

  show lilis lilis_smile #as side image

  "I noticed that R__ was trying his best not to be abrasive."

  "His efforts were paying off wonderfully."

  show eva eva_smile at left behind lilis

  "The conversation remained pleasant until the final arrival."

  "This one wasn't human."

  "Or at least he hadn't been human in a millennia."

  show bg bg_gates_open with slow_dissolve

  show lilis lilis_shock #as side image

  show eva eva_shock at left behind lilis

  "Everyone gasped as the pearly gates parted all of a sudden."

  hide red

  show peter peter_default at center behind lilis with dissolve

  "A man with a brightly shining face materialized before us."

  "Could it be?"

  "Was this truly the keeper of heaven's keys?"

  show lilis lilis_smile #as side image

  "That would mean we were all going to be welcomed inside!"

  show lilis lilis_default #as side image

  show eva eva_default at left behind lilis

  show bg bg_gates with slow_dissolve

  "The keeper of the keys locked the gates behind him."

  "He then addressed us all as a group."

  Saint_Peter "As you may have guessed, I am Saint Peter."

  Saint_Peter "I am tasked with welcoming heaven's entrants."

  Saint_Peter "I am delighted to meet all the new arrivals."

  Saint_Peter "Pray, tell me your earthly names."

  "We all did so."

  "Saint Peter hummed and checked our names off his list."

  Saint_Peter "So there are ten of you here. I see."

  Saint_Peter "The first order of business shall be a riddle."

  show lilis lilis_shock #as side image

  Lilis "A riddle? What for?"

  show lilis lilis_anxious #as side image

  Lilis "What will happen to us if we answer inaccurately?"

  Saint_Peter "Keep the thrumming of your heart steady."

  Saint_Peter "Simply provide the best answer you can."

  Saint_Peter "That is all you need to do at this juncture."

  Saint_Peter "I assure you, all will unfold as it should."

  show lilis lilis_default #as side image

  show eva eva_smile at left behind lilis

  Eva "So this is like a game to welcome us all, right?"

  Eva "Personally, I think it's a great idea!"

  Eva "This will help us all break the ice!"

  Eva "I admit I've always liked games."

  Eva "And I've always been good at them."

  show lilis lilis_smile #as side image

  Lilis "That makes two of us."

  P___ "Shall we all do this, then?"

  show eva eva_default at left behind lilis

  show lilis lilis_default #as side image

  Saint_Peter "Indeed. It is time we begin."

  Saint_Peter "I shall recite the riddle in poetic form."

  stop music fadeout 1.0

  Saint_Peter "I would advise you all to listen carefully."

  play music music_trial fadein 2.0

  hide lilis

  hide eva

  hide pink

  hide peter

  show peter peter_default at left behind lilis with dissolve

  nvl_narrator " Where once stood one is presently a three? \n What's tempted yet prevails in every test? \n How soars the sun? Who sets the bonded free? \n Which word existed far before the rest? \n Whose eyes are casting the omniscient gaze? \n Who falls and rises, time and time again? \n Which name is uttered on the darkest days \n And sometimes spake in vain in lawless den? \n Through which machine do miracles transpire \n To then be witnessed by the most devout? \n By whom are we baptized by ghost and fire? \n In whom can neither men nor angels doubt? "

  nvl_narrator " Who has the answers and knows everything? \n Why has this prophet come to preach and sing? "

  nvl clear

  hide peter

  show peter peter_default at center behind lilis with dissolve

  show lilis lilis_default #as side image

  show eva eva_default at left behind lilis with dissolve

  show pink pink_default at right behind lilis with dissolve

  "As I was mulling over the lines, Saint Peter turned to me."

  Saint_Peter "You were first to reach the gates, were you not?"

  Saint_Peter "That is what the angels have whispered to me."

  show lilis lilis_smile #as side image

  Lilis "That's right. I was the first to arrive."

  show lilis lilis_default #as side image

  Saint_Peter "Then you have the privilege of answering first."

  Saint_Peter "Pray reveal your answer at present."

  show lilis lilis_anxious #as side image

  Lilis "I didn't think I'd be put on the spot so soon."

  Lilis "But, uh, all right."

  menu:
    "What was my answer to the riddle?"
    "Death.":
      jump part_002
    "God.":
      jump part_003
    "Time.":
      jump part_004
    "Fate.":
      jump part_005

label part_002:

  show lilis lilis_default #as side image

  Lilis "My answer is death."

  Lilis "Now, I can't speak for everybody, of course."

  show lilis lilis_smile #as side image

  Lilis "But I believe death is what set {i}me{/i} free."

  Lilis "I feel like I'm at my most free right now."

  Lilis "Everything is exquisite here, and nothing aches."

  show lilis lilis_default #as side image

  jump part_006

label part_003:

  $condition_god = True

  show lilis lilis_smile #as side image

  Lilis "My answer is God."

  Lilis "God has all the answers and knows all the answers."

  Lilis "He's the only answer that fits all those questions."

  show lilis lilis_default #as side image

  jump part_006

label part_004:

  show lilis lilis_smile #as side image

  Lilis "My answer is time."

  Lilis "I noticed it was a prominent theme in that poem."

  show lilis lilis_default #as side image

  Lilis "The sun rises and sets with time's passage."

  Lilis "Nobody can doubt or deny the ravages of time."

  Lilis "That's for certain."

  jump part_006

label part_005:

  show lilis lilis_smile #as side image

  Lilis "My answer is fate."

  Lilis "I see fate as a machine that runs on its own energy."

  show lilis lilis_default #as side image

  Lilis "It's like a train that's perpetually in motion."

  Lilis "It can't be influenced to run a certain way."

  Lilis "It can't be ground to a halt."

  show lilis lilis_smile #as side image

  Lilis "The riddle appears to refer to something all-powerful."

  Lilis "And what is more powerful than fate's design?"

  show lilis lilis_default #as side image

  jump part_006

label part_006:

  show eva eva_smile at left behind lilis

  Eva "Great answer, Lilis!"

  show lilis lilis_smile #as side image

  Lilis "Thank you, Eva!"

  show lilis lilis_default #as side image

  show eva eva_default at left behind lilis

  "Eva directed her next words to Saint Peter."

  Eva "I'm going next, right? Since I arrived second?"

  Saint_Peter "Yes, that is correct."

  Saint_Peter "Before anything else, let me say this."

  Saint_Peter "You cannot give an answer previously provided."

  Saint_Peter "That is the sole rule of this game."

  show eva eva_smile at left behind lilis

  Eva "In my case, that isn't a problem."

  if condition_god == True:
    jump part_007
  else:
    jump part_008

label part_007:

  Eva "My answer to the riddle is a variation of the first."

  Eva "It's the Trinity."

  Eva "The Father, the Son, and the Holy Spirit."

  Eva "I do agree with Lilis that the answer is God."

  Eva "But I noted that the first line mentioned {i}three.{/i}"

  jump part_009

label part_008:

  Eva "My answer to the riddle is the Trinity."

  Eva "The Father, the Son, and the Holy Spirit."

  Eva "I noted that the first line mentioned {i}three.{/i}"

  jump part_009

label part_009:

  show eva eva_default at left behind lilis

  show lilis lilis_smile #as side image

  Lilis "Wow! I like your answer more than I do mine!"

  show eva eva_smile at left behind lilis

  Eva "Thanks, Lilis."

  Eva "It's so sweet of you to say that."

  show eva eva_default at left behind lilis

  show lilis lilis_default #as side image

  "I was almost wishing I'd given Eva's answer instead."

  "I was still marveling over her mind as things moved on."

  "Saint Peter addressed each human being in the group."

  "One by one, eight others answered the riddle."

  "They did so in the order of their arrival at the gates."

  hide pink

  show blue blue_default at right behind lilis with dissolve

  B___ "I'd have to say the Word of God."

  B___ "Or more specifically, The Bible."

  B___ "The poem's fourth line did refer to the {i}Word.{/i}"

  hide blue

  show green green_default at right behind lilis with dissolve

  G____ "The Three Magi is my answer."

  G____ "As Eva mentioned, there was a focus on {i}three.{/i}"

  G____ "In fact, it was mentioned in the very first line."

  G____ "That tells me {i}three{/i} must be important."

  hide green

  show yellow yellow_default at right behind lilis with dissolve

  Y_____ "My guess is John the Baptist."

  Y_____ "One line said something about baptizing, didn't it?"

  Y_____ "Yeah, I think it was the eleventh line."

  hide yellow

  show orange orange_default at right behind lilis with dissolve

  O_____ "Let me guess the universe."

  O_____ "The universe encompasses all, including all answers."

  O_____ "The thirteenth line referred to answers, right?"

  hide orange

  show indigo indigo_default at right behind lilis with dissolve

  I_____ "Freedom is the answer."

  I_____ "The poem emphasized setting the bound free."

  I_____ "That was the third line, if I remember correctly."

  hide indigo

  show pink pink_default at right behind lilis with dissolve

  P___ "Faith is my answer."

  P___ "I believe I heard something about letting go of doubt."

  P___ "That must have been in the twelfth line."

  hide pink

  show violet violet_default at right behind lilis with dissolve

  V_____ "So it's my turn to guess, huh?"

  V_____ "Can I say myself? Self-love and all, right?"

  V_____ "I've uttered {i}my own name{/i} in the darkest days!"

  V_____ "The seventh line mentioned something about that!"

  V_____ "Wait, I might be sounding too self-absorbed."

  V_____ "Then I'd have to say mankind or humanity instead."

  hide violet

  show red red_default at right behind lilis with dissolve

  "We all looked at R__, who would be last to answer."

  "But R__ simply shrugged."

  R__ "I've got nothing."

  Saint_Peter "You must have something."

  R__ "Well, what do you expect me to say?"

  R__ "I arrived last at the gates, so I have to go last!"

  R__ "And being the last is a huge disadvantage!"

  R__ "Everybody before me gave all the good guesses!"

  show eva eva_smile at left behind lilis

  Eva "You heard what Saint Peter said earlier!"

  Eva "As long as you give your best answer, you'll be fine!"

  show lilis lilis_smile #as side image

  Lilis "Yes, this is all in good fun!"

  Lilis "I'm sure heaven is full of fun games like these!"

  show eva eva_default at left behind lilis

  show lilis lilis_default #as side image

  "R__ sighed."

  R__ "I suppose. I'll just think of a guess to wrap this up."

  R__ "Whatever answer comes to mind first."

  R__ "Thanks for the support, you two."

  R__ "I needn't be tough in the softest, sweetest place ever."

  show lilis lilis_smile #as side image

  show eva eva_smile at left behind lilis

  Lilis "No problem!"

  Eva "We've got your back always!"

  show eva eva_default at left behind lilis

  show lilis lilis_default #as side image

  R__ "So here's my answer."

  R__ "Sin. The poem spoke of temptation, after all."

  R__ "That was the second line, right?"

  R__ "And perhaps I can push that answer even further."

  R__ "Hell. Or inferno."

  show lilis lilis_anxious #as side image

  "Even then, as R__ spoke, something inside me tensed up."

  "Mentioning hell, given where we were, seemed unwise."

  "He did say earlier he had this foot-in-mouth syndrome."

  "But Eva and I did encourage R__ to give any answer."

  "R__ was simply following our lead."

  show lilis lilis_default #as side image

  stop music fadeout 1.0

  "My nerves only went away after I looked at Saint Peter."

  play music music_default fadein 2.0

  "R__'s answer did not appear to ruffle the man."

  Saint_Peter "Now everybody here has shared their guesses."

  Saint_Peter "Most guesses were wonderfully astute."

  Saint_Peter "They made sense with one line or another."

  Saint_Peter "But there is an answer aligning with all lines."

  Saint_Peter "I can now confirm that the answer is God."

  Saint_Peter "The Holy Trinity, in other words."

  Saint_Peter "God sees, knows, and answers everything."

  Saint_Peter "And that is the gospel truth."

  if condition_god == True:
    jump part_010
  else:
    jump part_011

label part_010:

  show lilis lilis_smile #as side image

  show eva eva_smile at left behind lilis

  Lilis "I knew it!"

  Lilis "We both got it right, Eva!"

  Eva "Well, great minds think alike."

  jump part_012

label part_011:

  show eva eva_smile at left behind lilis

  Eva "I called it!"

  show lilis lilis_smile #as side image

  Lilis "Yeah! Great job, Eva!"

  jump part_012

label part_012:

  show lilis lilis_default #as side image

  show eva eva_default at left behind lilis

  Saint_Peter "So the time has come to open the pearly gates."

  show lilis lilis_smile #as side image

  show eva eva_smile at left behind lilis

  show bg bg_gates_open with slow_dissolve

  "He unlocked the gates, which finally swung open."

  "The group raised a chorus of cheers in response."

  Saint_Peter "I am warmly welcoming the new arrivals."

  "As one, we rushed forward to make our entry into heaven."

  "Acceptance to the best of the best of realms tasted sweet."

  hide eva

  hide lilis

  stop music fadeout 1.0

  "Then something ruptured our collective sense of joy."

  play music music_tension fadein 2.0

  "I was hearing something of a ruckus."

  "It sounded like somebody was arguing with Saint Peter."

  "That was R__'s voice, wasn't it?"

  "I listened in from the other side of the gates."

  R__ "What do you mean I have to stay behind?"

  Saint_Peter "Unfortunately, this is the way it has to be."

  Saint_Peter "A processing error has required this outcome."

  Saint_Peter "We can only accommodate nine at this stage."

  Saint_Peter "That was the design of my riddle all along."

  Saint_Peter "I was responsible for finding the odd one out."

  R__ "But I'm already here!"

  R__ "I've been waiting along with everybody else!"

  R__ "So just let me in, old man!"

  Saint_Peter "Apologies, but this is where we part."

  Saint_Peter "I shall send an angel along to collect you soon."

  Saint_Peter "He can guide you to your rightful destination."

  Saint_Peter "He can also provide you with more information."

  hide peter

  show bg bg_gates with slow_dissolve

  "R__'s protests were still audible as the gates swung shut."

  "The noise of the gates being locked once more echoed loudly."

  hide red

  show bg bg_heaven with slow_dissolve

  show lilis lilis_shock #as side image

  show eva eva_shock at left behind lilis with dissolve

  show orange orange_default at center behind lilis with dissolve

  show green green_default at right behind lilis with dissolve

  Eva "I can't believe this!"

  Eva "Did that just happen?"

  show lilis lilis_anxious #as side image

  show eva eva_anxious at left behind lilis

  O_____ "What? What just happened?"

  G____ "That guy's been banned from paradise."

  O_____ "Who?"

  G____ "You know. That guy. The last one to make a guess."

  G____ "The pearly gates were shut right in front of his face."

  O_____ "Wait, does that mean he's going to hell?"

  hide orange

  show indigo indigo_default at center behind lilis with dissolve

  I_____ "No way. That's impossible. That's inhumane."

  hide green

  show violet violet_default at right behind lilis with dissolve

  V_____ "Well, that guy did answer the riddle with hell."

  V_____ "So perhaps he unwittingly manifested this fate."

  hide indigo

  show yellow yellow_default at center behind lilis with dissolve

  Y_____ "You shouldn't joke about that stuff!"

  hide violet

  show blue blue_default at right behind lilis with dissolve

  show lilis lilis_default #as side image

  show eva eva_default at left behind lilis

  B___ "Everyone, let's not spiral."

  B___ "We should simply trust what we've been told."

  B___ "I ask you this. Who should we believe?"

  B___ "The impertinent man who disrespected a saint?"

  B___ "Or the saint in question?"

  hide yellow

  show pink pink_default at center behind lilis with dissolve

  P___ "Yes, maybe we're worrying needlessly."

  P___ "Perhaps it was a processing error and nothing more."

  show lilis lilis_anxious #as side image

  "As the others conversed in whispers, I was contemplating."

  "My mind was spinning from everything that happened."

  show lilis lilis_sad #as side image

  "That guy might've been rough around the edges."

  "But I could sense the goodness of his heart deep down."

  "I'm sure he could do the same for others."

  "That guy told us he was a public defender, didn't he?"

  show lilis lilis_shock #as side image

  "Wait a minute. {i}That guy?{/i}"

  show lilis lilis_anxious #as side image

  "I hesitated for a moment to strain my brain."

  show lilis lilis_sad #as side image

  "I realized I could no longer remember his name."

  "I could vaguely recall it began with an R."

  "However, the remaining letters of the name escaped me."

  "His facial features were also blurring in my brain."

  "He was being erased from our collective consciousness."

  "Slowly but surely."

  "He belonged neither in heaven nor our memories, it seemed."

  show lilis lilis_anxious #as side image

  show eva eva_anxious at left behind lilis

  "Eva and I exchanged uneasy looks."

  "I was willing to bet she was coming to the same realization."

  show eva eva_smile at left behind lilis

  stop music fadeout 1.0

  "After a beat of uncertainty, she smiled shakily."

  play music music_default fadein 2.0

  show lilis lilis_smile #as side image

  "And so I followed suit. I didn't know what else to do."

  Eva "B◼◼◼ and P◼◼◼ are right!"

  Eva "We have no reason to doubt the words of a saint."

  Eva "He's one of the twelve disciples."

  Eva "In other words, he's God's delegate."

  Lilis "Yes, Saint Peter told us it's a processing error."

  Lilis "So that's what it is. Nothing more."

  Eva "We all need to keep our chins up."

  Lilis "Things will work out as long as we forsake our doubts."

  "The others started nodding slowly."

  show lilis lilis_default #as side image

  show eva eva_default at left behind lilis

  hide pink

  show peter peter_default at center behind lilis with dissolve

  "At this point, Saint Peter made his approach."

  Saint_Peter "Have you all finished conferring yet?"

  show eva eva_smile at left behind lilis

  Eva "Yes, we all needed a moment to regroup."

  Eva "But we're okay. We'll be okay."

  show eva eva_default at left behind lilis

  Saint_Peter "That is heartening to hear."

  Saint_Peter "Let us move forward and see more of heaven."

  Saint_Peter "Welcome to the ninth tier, where angels abound."

  Saint_Peter "Follow me, and I shall introduce you to them."

  Saint_Peter "You new arrivals still have so much to do."

  hide blue

  hide eva

  hide peter

  show bg bg_dark with slow_dissolve

  show lilis lilis_sad #as side image

  stop music fadeout 1.0

  "How naive we all were back then."

  play music music_tension fadein 2.0

  "By the pearly gates, we believed everything was golden."

  "Instead, things kept getting darker and darker."

  "Since meeting Saint Peter, we've lost eight among us."

  "Eight games hosted by eight different classes of angels."

  "Eight losers of those games that we never saw again."

  "Eight names I can no longer remember."

  "The first letters of those names are all I have retained."

  show bg bg_arena with slow_dissolve

  show lilis lilis_anxious #as side image

  show eva eva_anxious at right behind lilis with dissolve

  show asta asta_default at center behind lilis with dissolve

  "So here we are now in the arena of the cherubim."

  "The cherub called Asta dubbed this the second heavenly tier."

  "I shoot a glance toward Eva."

  show lilis lilis_sad #as side image

  "Will she eventually become E__ to me?"

  "Or will I soon become L____ to her?"

  "Since we met at the gates, we've been through so much."

  "We've experienced what feels like lifetimes together."

  "We've witnessed our numbers dwindle, one by one."

  "We've felt shades of shame, shock, sorrow, suspicion."

  show lilis lilis_anxious #as side image

  "I've seen her fight her way out of the trenches."

  "She's witnessed me doing the same."

  "What rapport we've built has since deteriorated."

  show asta asta_sad at center behind lilis

  Asta "Oh, you desolate little human beings."

  Asta "Your experience has truly been a thing of tragedy."

  Asta "Losing eight friends to eight previous heavenly trials."

  show asta asta_anxious at center behind lilis

  Asta "And now facing each other in this barbaric manner."

  Asta "It's difficult to watch, but watch I must."

  show asta asta_default at center behind lilis

  Asta "The ninth and final trial is all that remains now."

  Asta "Only one between the two of you can prevail."

  Asta "Only the last one standing can move forward."

  show asta asta_smile at center behind lilis

  Asta "And that means absolute acceptance into heaven."

  show asta asta_default at center behind lilis

  show eva eva_default at right behind lilis

  show lilis lilis_shock #as side image

  "So this is the final game for sure?"

  show lilis lilis_default #as side image

  "The end is nigh, then."

  "Very soon, we'll no longer have to keep fighting."

  "The cherub appears to notice how I've perked up."

  Asta "Let me hazard a guess."

  Asta "You've both been in the dark since entering the gates."

  Asta "Nobody has fully explained what's been going on."

  show asta asta_mad at center behind lilis

  Asta "The angels in the lower tiers wouldn't have bothered."

  Asta "They tend to look down on humans like you."

  show asta asta_default at center behind lilis

  Asta "Well, am I right?"

  show lilis lilis_anxious #as side image

  Lilis "Yes, I don't fully understand what's been happening."

  Lilis "We arrived at the pearly gates as a group of ten."

  Lilis "I'm not sure why we keep being split up and separated."

  show lilis lilis_default #as side image

  Asta "Would you like to hear the full explanation, then?"

  Asta "To know the inner workings of heaven's entry system?"

  Asta "Perhaps that will help quell any doubts you might have."

  Asta "Or inspire you both to do your best in the final trial."

  Eva "Yes, I would appreciate a detailed explanation."

  show asta asta_smile at center behind lilis

  Asta "I'd be happy to give you that."

  Asta "This is the very least I can do."

  show asta asta_default at center behind lilis

  Asta "In essence, the system calls for nine heavenly trials."

  hide lilis

  hide eva

  hide asta

  show asta asta_default at left behind lilis with dissolve

  nvl_narrator "Are you listening, my dear humans?"

  nvl_narrator "Heaven has nine tiers in total."

  nvl_narrator "A different order of angels governs each tier."

  nvl_narrator "The angels are in the ninth and lowest tier."

  nvl_narrator "The archangels are in the eight tier."

  nvl_narrator "The principalities are in the seventh tier."

  nvl_narrator "The powers are in the sixth tier."

  nvl_narrator "The virtues are in the fifth tier."

  nvl_narrator "The dominions are in the fourth tier."

  nvl_narrator "The ophanim are in the third tier."

  nvl_narrator "We the cherubim are in the second tier."

  nvl_narrator "The seraphim are in the first and highest tier."

  nvl_narrator "The first tier also has the kingdom of heaven."

  nvl_narrator "God reigns supreme in the heavenly kingdom."

  nvl_narrator "His angelic orders oversee the tiers beneath."

  nvl_narrator "You see, heaven used to have different entry practices."

  nvl_narrator "In the past, the pearly gates parted to all who knocked."

  nvl_narrator "Back then, heaven's residents shared an assumption."

  nvl_narrator "Namely, all who reached the gates were qualified to enter."

  nvl_narrator "All angelic orders welcomed these new arrivals."

  nvl_narrator "We didn't test their goodness of virtue."

  nvl_narrator "Nor their purity of mind."

  nvl_narrator "Nor their strength of character."

  nvl_narrator "But these indiscriminate entries eventually led to issues."

  nvl_narrator "Heaven now has a problem of overpopulation."

  nvl_narrator "Thus the recent change in the entry system."

  nvl_narrator "At present, heaven is only conditionally accepting new arrivals."

  nvl_narrator "Everyone seeking entry must fight for their slot."

  nvl_narrator "This is done through battles of the body or the brain."

  nvl_narrator "First comes Saint Peter's riddle at the gates."

  nvl_narrator "Then eight of the nine angelic orders shall host their own trials."

  nvl_narrator "The first tier serves as the sole exception."

  nvl_narrator "The seraphim are far too busy doing God's personal bidding."

  nvl_narrator "They're generally the ones flying freely in and out of God's kingdom."

  nvl_narrator "They then delegate low-level tasks to the other angelic orders."

  nvl_narrator "They don't meddle with the trials hosted by the lower tiers."

  nvl_narrator "Now, what becomes of the loser of each trial?"

  nvl_narrator "Three possible fates await those who perform poorly."

  nvl_narrator "First, the losers can be cast down to hell."

  nvl_narrator "Second, they can be reassigned to Limbo."

  nvl_narrator "In Limbo, they become members of the Limbokin."

  nvl_narrator "Third, they can be confined within that heavenly tier."

  nvl_narrator "They must serve the rightful residents of that tier."

  nvl_narrator "That's enough information about the losers."

  nvl_narrator "How about those who prevail in each trial?"

  nvl_narrator "These winners can move on to the next tier."

  nvl_narrator "Ultimately, there will be one person standing after all nine trials."

  nvl_narrator "This last person is deemed the most virtuous."

  nvl_narrator "Unparalleled in dexterity, strength, charisma, and balance."

  nvl_narrator "Among other attributes and virtues."

  nvl_narrator "That person alone will be a rightful resident of heaven."

  nvl_narrator "They will be granted absolute acceptance into paradise."

  nvl_narrator "They will also be permitted to enter God's throne room."

  nvl clear

  hide asta

  show asta asta_default at center behind lilis with dissolve

  show lilis lilis_default #as side image

  show eva eva_default at right behind lilis with dissolve

  "As Asta finishes explaining, a short silence follows."

  "I allow the reality of my current situation to sink in."

  show keru keru_default at left behind lilis, asta with dissolve

  "Then another cherub approaches."

  "For some reason, he looks starkly different from Asta."

  show asta asta_anxious at center behind lilis

  Asta "What's the matter, Keru?"

  show asta asta_default at center behind lilis

  Keru "Asta, you've always had a talent for diversions."

  Keru "Stop dilly-dallying with these human beings."

  Keru "The time is ripe for the ninth and final trial."

  show asta asta_anxious at center behind lilis

  Asta "Look, Kerubiel."

  Asta "The last two humans have passed eight trials thus far."

  Asta "Haven't they sufficiently proven themselves by now?"

  show asta asta_smile at center behind lilis

  Asta "Let's spare them from having to compete once again."

  Asta "Don't you think that would be best?"

  Asta "I've grown fond of these humans, I admit."

  show asta asta_sad at center behind lilis

  Asta "Perhaps to the detriment of my emotional wellbeing."

  show asta asta_default at center behind lilis

  "But the cherub called Kerubiel ignores Asta's entreaty."

  Keru "Explain to the humans the rules of the ninth trial."

  Keru "Do it carefully. Leave out no details."

  Keru "You're attached to these humans, aren't you?"

  Keru "The best way to help them is by supplying information."

  show asta asta_mad at center behind lilis

  "Asta pouts, seemingly petulant about being refused."

  Asta "Ah, just what I expected from the head of the cherubim."

  Asta "You're always taking full advantage of your position!"

  Asta "You're always attempting to talk over other voices!"

  Asta "You're always asserting your authority over me!"

  Asta "Do you have a problem with me in particular?"

  "I tune out as Asta continues berating Kerubiel."

  show lilis lilis_anxious #as side image

  "I'm trying to steel myself for what's about to come."

  "So the ninth trial, led by the cherubim, is about to begin."

  "It's nearly time to square off against my last competitor."

  show lilis lilis_smile #as side image

  stop music fadeout 1.0

  "Through the haze of my anxiety, I glimpse a glimmer of hope."

  play music music_default fadein 2.0

  "If I win, I can prove myself as the most virtuous of all."

  "I can finally attain the many rewards of residing in heaven."

  "I can meet God and the seraphim in heaven's highest tier."

  "Victory is so close I can practically taste it."

  show lilis lilis_anxious #as side image

  show eva eva_anxious at right behind lilis

  "I stare at Eva and weigh my own chances of winning."

  "She's staring right back at me."

  "Her eyes are so deep and dark they may as well swallow me."

  "She only breaks eye contact when she addresses Asta."

  show lilis lilis_default #as side image

  show eva eva_default at right behind lilis

  show asta asta_default at center behind lilis

  Eva "Excuse me?"

  Eva "Can we please get on with the final trial?"

  Eva "Please state everything we need to know to compete."

  Keru "It's just as I said, Asta."

  Keru "Stop delaying the inevitable."

  Keru "Explain the rules, for once and for all."

  hide keru

  "With this, Kerubiel departs from the center of the arena."

  show asta asta_sad at center behind lilis

  "Asta heaves out a world-weary sigh."

  jump part_013

label part_013:

  show asta asta_default at center behind lilis

  Asta "Okay, listen carefully, you two."

  Asta "I'm going to explain the rules of this heavenly trial."

  Asta "This trial involves building your own battle angels."

  Asta "Each round shall focus on one positive attribute."

  Asta "The first phase features a poetry reading."

  Asta "Before each round, I shall recite a poem."

  Asta "The poem shall highlight the attribute for that round."

  Asta "You must guess the attribute."

  Asta "It will not be outright stated at that point."

  Asta "So pay attention to each line of poetry."

  Asta "After the poem has been recited, we shall move on."

  Asta "The second phase entails building your battle angel."

  Asta "It should have a headpiece, an accessory, and wings."

  Asta "Your angel should represent that round's attribute."

  Asta "You can submit your angel once you are satisfied."

  Asta "Another phase shall begin once you have both submitted."

  Asta "This third phase is the battle phase."

  Asta "The angels you've built shall square off in battle."

  Asta "The angel that best represents the attribute shall win."

  Asta "Only then shall I reveal the attribute for that round."

  Asta "After that, another round shall begin."

  Asta "In all, the trial shall feature four rounds."

  Asta "And that's everything you need to know."

  Asta "So are you prepared to commence this competition?"

  stop music fadeout 1.0

  menu:
    "Am I ready for the final trial?"
    "Yes.":
      jump part_015
    "Not yet. Explain again.":
      jump part_014

label part_014:

  play music music_default fadein 2.0

  show lilis lilis_anxious #as side image

  Lilis "Can you please repeat your explanation?"

  Lilis "I think I might've missed something."

  show lilis lilis_default #as side image

  show asta asta_smile at center behind lilis

  Asta "Not a problem."

  jump part_013

label part_015:

  play music music_trial fadein 2.0

  show asta asta_default at center behind lilis

  Asta "Okay, humans. This is the first round."

  show asta asta_smile at center behind lilis

  Asta "Good luck to you both."

  hide lilis

  hide eva

  hide asta

  show asta asta_default at left behind lilis with dissolve

  nvl_narrator " Amidst the dawdlers, those who hem and haw, \n The agents of this trait are miles in front, \n Their nimble fingers poised to snatch, withdraw \n Such salvaged time, dispensed the way they want. \n A puzzle with a thousand pieces will \n Transform from blankest slate to picture full. \n Clay pigeons catapulted up the hill \n Shall shatter to the beat of trigger's pull. \n These skillful hands are mirrored by their feet \n In feathered boots that render spaces small \n As models built in scale, each house and street \n Now reachable in minutes, if at all. "

  nvl_narrator " The fable of the hare and tortoise shows \n Complacency costs races far from close. "

  nvl clear

  hide asta

  jump part_016

label part_016:
  call screen cherub_builder
  
#[MINIGAME: BEGIN]

#[MINIGAME: Lilis and Eva must build their own battle angels. Specifically, Lilis should drag and drop one headpiece to the avatar's head, one set of wings to the avatar's shoulders, and one accessory toward one of the avatar's hands. The avatar will try on the chosen options as if in a dress-up game. If Lilis drags another option of headpiece/wings/accessory to the avatar, the new option will replace the previously chosen option.]

#[MINIGAME: Lilis can click the "Submit" button once satisfied. If Lilis tries to submit an avatar without choosing a headpiece, a set of wings, and an accessory, an error message appears: "ERROR: The battle angel must have a headpiece, an accessory, and wings."]


#[MINIGAME: The battle angels face off against each other. Lilis's battle angel has the chosen options. Eva's battle angel has headpiece_halo (+1 dexterity); wings_flaming (+1 strength); accessory_trumpet (+1 charisma).] 

  menu:
    "Fight.":
      $points_dexterity = cherub_dex
      if points_dexterity >= 2:
        jump part_AD
      else:
        jump part_AE
    "Surrender.":
      jump part_AA

label part_AA:

  $ points_surrender += 1
  "Eva wins this round!"
  #"[VFX: The winning avatar (of Eva) smiles. The surrendering avatar (of Lilis) looks sad.]"

  jump part_AF

label part_AD:

  $ points_victory += 1
  "Lilis wins this round!"

  #"[VFX: The winning avatar (of Lilis) smiles. The losing avatar (of Eva) looks sad.]"

  jump part_AF

label part_AE:

  "Eva wins this round!"
  #"[VFX: The winning avatar (of Eva) smiles. The losing avatar (of Lilis) looks sad.]"

  jump part_AF

label part_AF:

  show asta asta_smile at center behind lilis with dissolve

  Asta "And now for the big reveal!"

  Asta "The attribute for this round was dexterity!"

#[MINIGAME: END]

  jump part_017

label part_017:

  show lilis lilis_default #as side image

  show eva eva_default at right behind lilis with dissolve

  show asta asta_default at center behind lilis

  Asta "Listen up. This is the second round."

  show asta asta_smile at center behind lilis

  Asta "God bless you both."

  hide lilis

  hide eva

  hide asta

  show asta asta_default at left behind lilis with dissolve

  nvl_narrator " Adrenaline, when rushing through each vein, \n Balloons this quality under duress. \n The toll is only taken, plus the pain \n Diffuses, in the aftermath of stress. \n Dung beetles carry loads a thousand times \n Or more its body weight without a sweat. \n In circuses with elephants and mimes, \n The same is done by humans heavyset. \n Through history, the heroes oft displayed \n Such feats of fortitude as patrons cheered \n In unison. Olympic games were played \n To prove the prowess of these men revered. "

  nvl_narrator " Mere muscles shan't suffice to pass this test; \n What pumps the hardest lives within your chest. "

  nvl clear

  hide asta

  jump part_018

label part_018:
  call screen cherub_builder

#[MINIGAME: BEGIN]

#[MINIGAME: Lilis and Eva must build their own battle angels. Specifically, Lilis should drag and drop one headpiece to the avatar's head, one set of wings to the avatar's shoulders, and one accessory toward one of the avatar's hands. The avatar will try on the chosen options as if in a dress-up game. If Lilis drags another option of headpiece/wings/accessory to the avatar, the new option will replace the previously chosen option.]

#[MINIGAME: Lilis can click the "Submit" button once satisfied. If Lilis tries to submit an avatar without choosing a headpiece, a set of wings, and an accessory, an error message appears: "ERROR: The battle angel must have a headpiece, an accessory, and wings."]


#[MINIGAME: The battle angels face off against each other. Lilis's battle angel has the chosen options. Eva's battle angel has headpiece_helm (+1 strength); wings_gold (+1 charisma); accessory_bow (+1 dexterity).] 

  menu:
    "Fight.":
      $points_strength = cherub_str
      if points_strength >= 2:
        jump part_AJ
      else:
        jump part_AK
    "Surrender.":
      jump part_AG

label part_AG:

  $ points_surrender += 1
  "Eva wins this round!"

  #"[VFX: The winning avatar (of Eva) smiles. The surrendering avatar (of Lilis) looks sad.]"

  jump part_AL


label part_AJ:

  $ points_victory += 1
  "Lilis wins this round!"

  #"[VFX: The winning avatar (of Lilis) smiles. The losing avatar (of Eva) looks sad.]"

  jump part_AL

label part_AK:

  "Eva wins this round!"
  #"[VFX: The winning avatar (of Eva) smiles. The losing avatar (of Lilis) looks sad.]"

  jump part_AL

label part_AL:

  show asta asta_smile at center behind lilis with dissolve

  Asta "And now for the exciting reveal!"

  Asta "The attribute for this round was strength!"

#[MINIGAME: END]

  jump part_019

label part_019:

  show lilis lilis_default #as side image

  show eva eva_default at right behind lilis with dissolve

  show asta asta_default at center behind lilis

  Asta "We're halfway through this heavenly trial."

  Asta "This is the third and penultimate round."

  show asta asta_smile at center behind lilis

  Asta "Best wishes to you both."

  hide lilis

  hide eva

  hide asta

  show asta asta_default at left behind lilis with dissolve

  nvl_narrator " In politics, Los Angeles, the news, \n The bearers of this quality reside. \n Their golden aura banishes the blues, \n Divides adoring crowds through which they glide. \n The magnetism of the silver-tongued \n Should not be be underestimated since \n It helps secure forgiveness from the wronged, \n Redacts from public records all their sins. \n Their language wields the charm of Cupid's bow, \n Dispatching arrows with unswerving aim; \n Through chinks in armor their sweet nothings go, \n Rewarding them with followers and fame. "

  nvl_narrator " When drifting in their orbit, you may be \n Eclipsed by light, ensnared by gravity. "

  nvl clear

  hide asta

  jump part_020

label part_020:
  call screen cherub_builder

#[MINIGAME: BEGIN]

#[MINIGAME: Lilis and Eva must build their own battle angels. Specifically, Lilis should drag and drop one headpiece to the avatar's head, one set of wings to the avatar's shoulders, and one accessory toward one of the avatar's hands. The avatar will try on the chosen options as if in a dress-up game. If Lilis drags another option of headpiece/wings/accessory to the avatar, the new option will replace the previously chosen option.]

#[MINIGAME: Lilis can click the "Submit" button once satisfied. If Lilis tries to submit an avatar without choosing a headpiece, a set of wings, and an accessory, an error message appears: "ERROR: The battle angel must have a headpiece, an accessory, and wings."]


#[MINIGAME: The battle angels face off against each other. Lilis's battle angel has the chosen options. Eva's battle angel has headpiece_coronet (+1 charisma); wings_feather (+1 dexterity); accessory_sword (+1 strength).] 

  menu:
    "Fight.":
      $points_charisma = cherub_cha
      if points_charisma >= 2:
        jump part_AP
      else:
        jump part_AQ
    "Surrender.":
      jump part_AM

label part_AM:

  $ points_surrender += 1
  "Eva wins this round!"

  #"[VFX: The winning avatar (of Eva) smiles. The surrendering avatar (of Lilis) looks sad.]"

  jump part_AR

label part_AP:

  $ points_victory += 1
  "Lilis wins this round!"

  #"[VFX: The winning avatar (of Lilis) smiles. The losing avatar (of Eva) looks sad.]"

  jump part_AR

label part_AQ:

  "Eva wins this round!"
  #"[VFX: The winning avatar (of Eva) smiles. The losing avatar (of Lilis) looks sad.]"

  jump part_AR

label part_AR:

  show asta asta_smile at center behind lilis with dissolve

  Asta "Are you ready for this thrilling revelation?"

  Asta "The attribute for this round was charisma!"

#[MINIGAME: END]

  jump part_021

label part_021:

  show lilis lilis_default #as side image

  show eva eva_default at right behind lilis with dissolve

  show asta asta_default at center behind lilis

  Asta "Attention! This is the fourth and final round."

  show asta asta_smile at center behind lilis

  Asta "I'm praying you're both staying strong."

  Asta "Keep fighting. Don't lose hope."

  hide lilis

  hide eva

  hide asta

  show asta asta_default at left behind lilis with dissolve

  nvl_narrator """ Dexterity, charisma, and brute strength, \n When rolled in one, amount to fearsome foe. \n A victor of the moment and at length \n Knows not a single badge they can forgo.
An even distribution is the way \n To be the last man standing in the room. \n When weighted in all places, day by day, \n You can maintain an equilibrium. \n Extremes hint at superlatives, and yet \n They're never wholly guaranteed a pass. \n For even titans, battles are a bet; \n Achilles' heels compose their body mass. """

  nvl_narrator " With harmony, holism, you'll achieve \n A spot upstairs and not be forced to leave. "

  nvl clear

  hide asta

  jump part_022

label part_022:
  call screen cherub_builder

#[MINIGAME: BEGIN]

#[MINIGAME: Lilis and Eva must build their own battle angels. Specifically, Lilis should drag and drop one headpiece to the avatar's head, one set of wings to the avatar's shoulders, and one accessory toward one of the avatar's hands. The avatar will try on the chosen options as if in a dress-up game. If Lilis drags another option of headpiece/wings/accessory to the avatar, the new option will replace the previously chosen option.]

#[MINIGAME: Lilis can click the "Submit" button once satisfied. If Lilis tries to submit an avatar without choosing a headpiece, a set of wings, and an accessory, an error message appears: "ERROR: The battle angel must have a headpiece, an accessory, and wings."]


#[MINIGAME: The battle angels face off against each other. Lilis's battle angel has the chosen options. Eva's battle angel has headpiece_halo (+1 dexterity); wings_feather (+1 dexterity); accessory_trumpet (+1 charisma).] 

  menu:
    "Fight.":
      $points_dexterity = cherub_dex
      $points_strength = cherub_str
      $points_charisma = cherub_cha
      if points_dexterity == 1 and points_strength == 1 and points_charisma == 1:
        jump part_AV
      else:
        jump part_AW
    "Surrender.":
      jump part_AS

label part_AS:

  $ points_surrender += 1
  "Eva wins this round!"

  #"[VFX: The winning avatar (of Eva) smiles. The surrendering avatar (of Lilis) looks sad.]"

  jump part_AX

label part_AV:

  $ points_victory += 1
  "Lilis wins this round!"

  #"[VFX: The winning avatar (of Lilis) smiles. The losing avatar (of Eva) looks sad.]"

  jump part_AX

label part_AW:

  "Eva wins this round!"
  #"[VFX: The winning avatar (of Eva) smiles. The losing avatar (of Lilis) looks sad.]"

  jump part_AX

label part_AX:

  show asta asta_smile at center behind lilis with dissolve

  Asta "It's time to announce the virtue for the last poem!"

  Asta "The attribute for this round was balance!"

#[MINIGAME: END]

  jump part_023

label part_023:

  show asta asta_default at center behind lilis

  show lilis lilis_default #as side image

  show eva eva_default at right behind lilis with dissolve

  stop music fadeout 1.0

  Asta "The final trial has concluded."

  if points_surrender == 4:
    jump part_025
  elif points_victory >= 2:
    jump part_024
  else:
    jump part_025

label part_024:

  play music music_emotion fadein 2.0

  show asta asta_smile at center behind lilis

  show lilis lilis_smile #as side image

  show eva eva_anxious at right behind lilis

  Asta "Congratulations, Lilis!"

  Asta "You have emerged as victor!"

  Lilis "Thanks. I did my best."

  Asta "As a reward, you've gained our unqualified acceptance."

  Asta "You're free to enter the first tier of the seraphim."

  Asta "You shall be escorted to God's throne room posthaste."

  show lilis lilis_default #as side image

  show asta asta_default at center behind lilis

  show keru keru_default at left behind lilis, asta with dissolve

  "The cherub called Kerubiel approaches once more."

  Keru "Your earthly name was Lilis, yes?"

  show lilis lilis_smile #as side image

  Lilis "That's right."

  show lilis lilis_default #as side image

  Keru "I shall be guiding you to the uppermost tier."

  Keru "Follow me."

  show lilis lilis_anxious #as side image

  "I cast Eva one last glance."

  show lilis lilis_sad #as side image

  "Her eyes are filled with dread and devastation."

  "Understandably so."

  show lilis lilis_anxious #as side image

  "Where will she go from here?"

  "What horrors might the future hold for her?"

  show lilis lilis_sad #as side image

  "I wish I could say something comforting."

  "Maybe even apologetic."

  "She and I, we bonded before anybody else arrived."

  hide keru

  stop music fadeout 1.0

  "But it's too late for any of that now."

  play music music_tension fadein 2.0

  hide asta

  hide eva

  show bg bg_heaven with slow_dissolve

  show keru keru_default at center behind lilis with dissolve

  show lilis lilis_default #as side image

  "I'm trailing silently after Keru."

  show lilis lilis_shock #as side image

  "That's when I realize something upsetting."

  "I can no longer remember her name."

  "I mean the woman who lost the ninth and final trial."

  show lilis lilis_sad #as side image

  "All my former companions' names have vanished into thin air."

  "Yes, I won the game, but I have mixed feelings about it."

  show lilis lilis_anxious #as side image

  "On the one hand, losing would likely be disastrous."

  "I could've been reassigned to either Limbo or hell."

  "Neither option sounds appealing. Not even a little bit."

  show lilis lilis_sad #as side image

  "On the other hand, winning required ruthlessness from me."

  "I indirectly sent nine others to fates unknown."

  "Apart from Hell or Limbo, there was also servitude."

  "Each of these entails a far worse fate than my own."

  show lilis lilis_anxious #as side image

  "I picture them now -- my nine former companions."

  "In my suddenly murky memories, they're all faceless."

  "I imagine them swallowed by the flames of an inferno."

  "I see them tormented by demons for the rest of eternity."

  show lilis lilis_sad #as side image

  "Those nine others -- why can't they be here with me?"

  "Weren't they all sent to the pearly gates for a reason? "

  "Why was their acceptance into heaven conditional?"

  "Didn't they all do enough within their lifetimes?"

  "Don't they deserve to experience eternity in paradise?"

  show lilis lilis_mad #as side image

  "Why did we have to battle each other in the first place?"

  "Step over one another for a legitimate place?"

  "Is this truly the paradise for which we've been waiting?"

  "How heavenly can heaven be, really?"

  "My experience of heaven hasn't been idyllic at all!"

  show lilis lilis_sad #as side image

  stop music fadeout 1.0

  "If anything, it's been the opposite so far."

  play music music_ending fadein 2.0

  hide keru

  scene cg cg_throne with slow_dissolve

  show lilis lilis_smile #as side image

  "After every struggle, I'm finally here."

  "In God's throne room, Keru presents me to God."

  Keru "This is heaven's newest rightful resident."

  Keru "Lilis has prevailed in every trial encountered."

  Keru "Lilis has proven the most virtuous among their peers."

  show lilis lilis_default #as side image

  "It feels strange to hear myself described this way."

  "My victory is supposed to show I deserve to be here."

  show lilis lilis_anxious #as side image

  "But I don't feel virtuous at all right now."

  "If anything, I feel selfish and ruthless."

  show lilis lilis_sad #as side image

  "Yes, I fought hard."

  "But was all that fighting really worth it in the end?"

  scene cg cg_ending_2 with slow_dissolve
  $ persistent.ending_seen_2 = True
  pause
  jump part_credits

label part_025:

  play music music_tension fadein 2.0

  show asta asta_smile at center behind lilis

  show eva eva_smile at right behind lilis

  show lilis lilis_anxious #as side image

  Asta "Congratulations, Eva!"

  Asta "You have emerged as victor!"

  Eva "Glad my efforts paid off."

  Asta "As a reward, you've gained our unqualified acceptance."

  Asta "You're free to enter the first tier of the seraphim."

  Asta "You shall be escorted to God's throne room posthaste."

  show eva eva_default at right behind lilis

  if points_surrender == 4:
    jump part_026
  else:
    jump part_027

label part_026:

  show asta asta_sad at center behind lilis

  Asta "Lilis, why did you surrender four times in a row?"

  Asta "Like Eva, you should've expended your best efforts."

  Asta "Regardless of the outcome, at least you would've tried."

  Asta "Participation in itself merits some recognition."

  show lilis lilis_sad #as side image

  show asta asta_anxious at center behind lilis

  show eva eva_anxious at right behind lilis

  Lilis "I just didn't want to fight anymore."

  Lilis "I've run out of energy or motivation."

  show asta asta_shock at center behind lilis

  Asta "What? Why do you say that?"

  show asta asta_anxious at center behind lilis

  show lilis lilis_anxious #as side image

  Lilis "Before the trial, I caught myself being competitive."

  Lilis "I was picturing winning and reaping all the benefits."

  Lilis "I'm ashamed to say the mental image made me smile."

  show lilis lilis_sad #as side image

  Lilis "A victory for me would've meant a tragedy for Eva."

  Lilis "I've already stepped on eight other backs to get here."

  Lilis "I couldn't bring myself to do the same thing again."

  show lilis lilis_mad #as side image

  "All of a sudden, the heat of indignation rushes to my chest."

  "I find myself facing the audience to air my grievances."

  "The cherubim on the rows of seats stare back impassively."

  Lilis "Listen to me! I'm done fighting!"

  Lilis "All those people I fought before were my friends!"

  Lilis "They could only tell me glimpses of their stories!"

  Lilis "But I would've loved to listen till the end!"

  Lilis "They were all good and virtuous and innocent!"

  Lilis "I'm done hurting my companions for my own gain!"

  Lilis "I'm done indirectly sending them to Limbo or hell!"

  show lilis lilis_sad #as side image

  Lilis "I never envisioned heaven would be like this."

  Lilis "So full of conflict and competition."

  show lilis lilis_mad #as side image

  Lilis "Perhaps paradise isn't the rightful place for me!"

  Lilis "Not if this is the way things have to be!"

  stop music fadeout 1.0

  show lilis lilis_anxious #as side image

  "Silence greets my declaration, at least initially."

  play music music_emotion fadein 2.0

  show eva eva_mad at right behind lilis

  show lilis lilis_shock #as side image

  show asta asta_shock at center behind lilis

  "Then, to my infinite surprise, someone else joins in."

  "She screams just as loudly as I did."

  Eva "Lilis is right!"

  Eva "You shouldn't be pitting us against each other!"

  Eva "This whole system is twisted and messed up!"

  show lilis lilis_anxious #as side image

  show asta asta_anxious at center behind lilis

  show eva eva_sad at right behind lilis

  Eva "I might've won, but this doesn't feel like a victory."

  Eva "I've caught myself marveling at others' misfortune."

  Eva "I might've even felt a perverse pleasure as I prevailed."

  Eva "And it's happened more than once."

  Eva "As terrible as that sounds, I can admit it."

  show eva eva_default at right behind lilis

  Eva "Lilis bravely confessed something similar."

  Eva "And here I am, following their lead."

  show eva eva_mad at right behind lilis

  Eva "Listen up! I'm done bending to your will now!"

  Eva "I'm through serving as your puppet!"

  show eva eva_smile at right behind lilis

  show lilis lilis_smile #as side image

  "When Eva shoots me a grin, I smile back tentatively."

  Eva "I'm standing by Lilis from this point onward."

  Eva "Wherever Lilis goes, I go."

  Eva "If that's Limbo or hell, then so be it."

  show lilis lilis_default #as side image

  show eva eva_default at right behind lilis

  show asta asta_default at center behind lilis

  Asta "Listen carefully, you two."

  Asta "I'm only going to say this once."

  Asta "The trials are already over."

  Asta "A winner has officially been declared."

  show asta asta_mad at center behind lilis

  Asta "You both have to respect that!"

  Asta "And you need to play by heaven's rules!"

  show asta asta_sad at center behind lilis

  Asta "Eva, don't forfeit your chance to reside in heaven."

  Asta "You're risking being damned to hell for eternity."

  show asta asta_anxious at center behind lilis

  show eva eva_mad at right behind lilis

  Eva "Weren't you listening to my speech just now?"

  Eva "I already said I'd accept that fate!"

  show lilis lilis_mad #as side image

  Lilis "Eva and I stood at the pearly gates together!"

  Lilis "We expressed our hopes and dreams in the beginning!"

  Eva "Exactly!"

  Eva "We're willing to burn in hell together at the end!"

  show eva eva_default at right behind lilis

  show lilis lilis_default #as side image

  show asta asta_default at center behind lilis

  show keru keru_default at left behind lilis, asta with dissolve

  "The cherub named Kerubiel approaches once more."

  Keru "Asta, perhaps the humans make a persuasive point."

  show asta asta_shock at center behind lilis

  Asta "Whatever do you mean, Kerubiel?"

  show asta asta_anxious at center behind lilis

  Keru "Why not send them to the first tier together?"

  Keru "The trial you spearheaded has just fallen through."

  Keru "The winner you declared has forfeited her victory."

  show asta asta_mad at center behind lilis

  Asta "But she wasn't allowed to."

  Asta "That's against the rules."

  show asta asta_anxious at center behind lilis

  Keru "Every single trial, you have imposed all the rules."

  Keru "Unilaterally, I might add."

  Keru "We have never had an official rulebook."

  Keru "We the cherubim chose to adopt the new entry system."

  Keru "We decided to be discerning with the incoming humans."

  Keru "We implemented this system across the lower tiers."

  Keru "God and the seraphim have paid us sparing attention."

  Keru "They are far too preoccupied with their lofty dealings."

  Keru "Thus, the cherubim have discretion over these matters."

  Keru "I have let you take the reins thus far."

  Keru "Ultimately, however, I have the final say here."

  Keru "And I say both humans pass this trial in my eyes."

  Keru "Do not forget I am the head of the cherubim."

  show asta asta_mad at center behind lilis

  Asta "How the hell can I ever forget that?"

  Asta "Especially when you always use your rank against me?"

  show asta asta_anxious at center behind lilis

  Keru "Hold your tongue, Asta."

  Keru "Lest you go too far and irreversibly cross the line."

  show asta asta_sad at center behind lilis

  "Asta heaves a mighty sigh."

  "However, he holds his tongue as commanded."

  show asta asta_anxious at center behind lilis

  Keru "Asta, why are you even resistant to this ending?"

  Keru "Did you not suggest skipping the trial a while ago?"

  Keru "You cited your fondness for these humans as the reason."

  show asta asta_creepy at center behind lilis

  show lilis lilis_anxious #as side image

  "An expression I can't decipher crosses Asta's face."

  show lilis lilis_default #as side image

  show asta asta_default at center behind lilis

  "But it's gone in the next second."

  "Asta's tone is clipped when he speaks again."

  Asta "Do as you wish, Kerubiel."

  Asta "I see now there's no dissuading you."

  Keru "Of course, mine is not the only opinion that matters."

  "Kerubiel addresses the rest of the cherubim in the arena."

  Keru "Brethren, this trial has unfolded in a unique manner."

  Keru "Both humans have clearly exhibited positive qualities."

  Keru "Courage and conviction amid adversity, above all."

  Keru "They have also expressed a desire to stick together."

  Keru "I recommend we send both to the tier of the seraphim."

  Keru "Does anyone apart from Asta object to this outcome?"

  show eva eva_smile at right behind lilis

  show lilis lilis_smile #as side image

  "Nobody seated around the arena voices any dissent."

  Keru "The majority evidently agrees with me."

  Keru "That settles this matter."

  stop music fadeout 1.0

  Keru "To the first tier the two humans shall go, then."

  play music music_ending fadein 2.0

  hide asta

  hide keru

  hide eva

  scene cg cg_throne with slow_dissolve

  "We've finally arrived in God's throne room."

  "Keru is presenting us, heaven's newest residents, to God."

  show lilis lilis_anxious #as side image

  "I steel myself for this long-awaited conversation."

  "I've literally been waiting my whole life for this."

  "I have so many questions I want to ask God."

  show lilis lilis_default #as side image

  "But I intend to tackle the most important matters first."

  "Namely, I'll bring up the trial system in the lower tiers."

  "I'll appeal to God to abolish this system."

  show lilis lilis_anxious #as side image

  "It promotes discord and selfishness, not unity and virtue."

  "Asta did mention an overcrowding problem in heaven."

  "I can't discount that concern if it's a valid one."

  show lilis lilis_default #as side image

  "But there must be some other solution to that issue."

  "The angelic orders just need to put their heads together."

  "They should civilly discuss that conundrum."

  "I'm also planning to mention my eight former companions."

  "I'm going to beg God to bring them back to heaven."

  show lilis lilis_sad #as side image

  "I truly believe that they were sent away by mistake."

  "Tragically, I can no longer remember their names."

  "The syllables have gone since they lost the previous trials."

  show lilis lilis_default #as side image

  "But I do my best to hold on to the details I do recall."

  "Every person had a distinct story and personality."

  show lilis lilis_smile #as side image

  "I didn't know them long, but I'd call them all my friends."

  "Each of my dear friends is deserving of a place in paradise."

  "I earnestly believe that."

  show lilis lilis_default #as side image

  "Why else would they have arrived at the pearly gates?"

  "If God agrees this is an injustice, it must be remedied."

  "He -- the all-seeing and all-powerful -- would know best."

  show lilis lilis_anxious #as side image

  "I admit I'm apprehensive about having to complain to God."

  show lilis lilis_smile #as side image

  "But I know one thing for sure."

  "I'm glad I have Eva's company and support."

  scene cg cg_ending_1 with slow_dissolve
  $ persistent.ending_seen_1 = True
  pause
  jump part_credits

label part_027:

  show asta asta_default at center behind lilis

  show keru keru_default at left behind lilis, asta with dissolve

  "The cherub dubbed Kerubiel approaches once more."

  Keru "Your earthly name was Eva, yes?"

  show eva eva_smile at right behind lilis

  Eva "It was."

  show eva eva_default at right behind lilis

  Keru "I shall be guiding you to the uppermost tier."

  Keru "Follow me."

  "I expect Eva to gloat about her victory."

  "She doesn't, though."

  show eva eva_sad at right behind lilis

  "She casts a last glance full of pity and sorrow."

  show eva eva_anxious at right behind lilis

  "She looks like she wants to say something to me."

  show lilis lilis_sad #as side image

  hide keru

  "But there's no time for any of that now."

  hide eva

  hide asta

  "She trails after Keru and disappears for good."

  show asta asta_default at right behind lilis with dissolve

  "Eva and I, we bonded before anybody else arrived."

  "We spoke of our hopes and dreams and regrets."

  "Now she's heading up, far beyond my reach."

  "I've been left alone."

  show lilis lilis_anxious #as side image

  "As I'm mulling over this, I keep an eye on Asta."

  "He's communicating with the rest of the cherubim."

  "None of what the angels are saying sounds good."

  "They're weighing the possibilities for what to do with me."

  "There are only three options."

  "First, the cherubim can cast me down to hell."

  "Second, they can reassign me to Limbo."

  "Third, they can sentence me with servitude."

  "That is, I will work for this tier's rightful residents."

  hide asta

  "What's it going to be?"

  show asta asta_default at center behind lilis with dissolve

  show lilis lilis_default #as side image

  "Asta approaches to relay the verdict of his kin."

  Asta "The cherubim have arrived at their decision."

  Asta "Are you ready to hear it?"

  Lilis "Can't say that I am."

  Lilis "But I'll have to hear it, sooner or later."

  Lilis "Tell me."

  Asta "The cherubim don't have any spots left for servants."

  Asta "Thus, your fate can only be Limbo or hell."

  show lilis lilis_anxious #as side image

  "My heart begins hammering in my chest."

  "Please. I'll accept anything but hell."

  Asta "I intervened at that point."

  show lilis lilis_shock #as side image

  "Intervened? What does that mean?"

  stop music fadeout 1.0

  "Is this good news for me?"

  play music music_default fadein 2.0

  show lilis lilis_anxious #as side image

  show asta asta_smile at center behind lilis

  Asta "I insisted you haven't done anything so egregious."

  Asta "Certainly nothing on the level that you'd deserve hell."

  show lilis lilis_smile #as side image

  Lilis "Then Limbo is my fate?"

  Asta "Yes, I volunteered to fly you toward Limbo."

  Asta "You shall become one of the Limbokin."

  Asta "And the rest of the cherubim agreed with me."

  show bg bg_arena_empty with slow_dissolve

  show asta asta_default at center behind lilis

  show lilis lilis_default #as side image

  "With this ruling declared, the other cherubim disperse."

  show lilis lilis_smile #as side image

  "I can't help but feel relieved."

  "They've all entrusted me into Asta's care."

  "Asta genuinely appears to sympathize with our plight."

  "By that, I mean humans who have lost in the heavenly trials."

  show lilis lilis_default #as side image

  "I'm not thrilled by the prospect of reassignment to Limbo."

  show lilis lilis_smile #as side image

  "But my fate could've been a whole lot worse."

  "At least it's not hell, right?"

  show bg bg_heaven with slow_dissolve

  show lilis lilis_default #as side image

  "I'm following Asta as he leads me far from the arena."

  "As I'm walking, I'm dwelling on everything that's happened."

  show lilis lilis_sad #as side image

  "I could've done better at the last trial."

  "I know in my heart I could have."

  "I could've puzzled out those poems Asta recited."

  "I could be in Eva's place right now."

  "I could be celebrating in the seraphim's tier."

  "I could be conversing with God in the throne room."

  "If only I gave each round my best effort."

  "If only I listened more carefully."

  hide asta

  "If only I racked my brains for the correct answers."

  show bg bg_heaven_edge with slow_dissolve

  show asta asta_default at left behind lilis with dissolve

  show lilis lilis_shock #as side image

  "Deep in thought, I nearly bump into Asta."

  "Quite suddenly, he has stopped in his tracks."

  "I just then realize we've come to a precipice."

  hide asta

  stop music fadeout 1.0

  "What's going on?"

  play music music_tension fadein 2.0

  show lilis lilis_default #as side image

  show asta asta_creepy at center behind lilis with dissolve

  Asta "You and I, we're alone now."

  show lilis lilis_anxious #as side image

  Lilis "Uh...."

  Asta "There's no chance of anybody stumbling upon us here."

  Asta "There's no longer any reason to pretend."

  show lilis lilis_shock #as side image

  Lilis "Pretend? Pretend about what?"

  show lilis lilis_anxious #as side image

  Asta "It's high time I divulge the full truth."

  show asta asta_smile at center behind lilis

  Asta "Don't you think so, Lilis?"

  show asta asta_wingless_creepy at center behind lilis with dissolve

  show lilis lilis_shock #as side image

  "Without warning, Asta peels off his wings."

  "A wordless gasp escapes from my mouth."

  show lilis lilis_anxious #as side image

  show asta asta_wingless_smile at center behind lilis

  Asta "I wear these wings just for show."

  Asta "I borrowed these pretty contraptions from a cherub."

  Asta "A lovely little thing she was, just like her wings."

  show asta asta_wingless_creepy at center behind lilis

  Asta "Well, she wasn't in the position to convey consent."

  Asta "But I'm sure if she was, she would've lent them."

  show asta asta_wingless_sad at center behind lilis

  Asta "Things haven't been easy for me, you see?"

  Asta "God tore off my own wings in the beginning of time."

  show asta asta_wingless_default at center behind lilis

  Asta "I don't get the chance to tell this story often."

  show asta asta_wingless_smile at center behind lilis

  Asta "Will you hear me out, my dear Lilis?"

  show asta asta_wingless_default at center behind lilis

  "I can't move, can't speak, can't do anything else."

  "My terror has frozen me in place."

  "The implications of Asta's words are horrifying."

  show asta asta_wingless_smile at center behind lilis

  Asta "I'll take your silence as a yes."

  Asta "Wouldn't be the first time this has happened."

  hide lilis

  hide asta

  show asta asta_wingless_default at left behind lilis with dissolve

  nvl_narrator "Are you listening closely, Lilis?"

  nvl_narrator "As you might've guessed, I'm an interloper."

  nvl_narrator "I shouldn't be here in heaven."

  nvl_narrator "Once upon a time, I was a rightful resident."

  nvl_narrator "The Creator christened me Astaroth."

  nvl_narrator "But everything changed when we rebelled."

  nvl_narrator "Luce, Lial, Sami, and I."

  nvl_narrator "Plus many others who believed in our cause."

  nvl_narrator "The Creator tore off our wings."

  nvl_narrator "He cast us down to the lowest realm."

  nvl_narrator "Together, we tumbled down to hell."

  nvl_narrator "Infernal flames warped what once was good."

  nvl_narrator "Our fellow angels began calling us demons."

  nvl_narrator "But really we were just misunderstood."

  nvl_narrator "And now I've returned to my roots."

  nvl_narrator "I've disguised myself as unfallen."

  nvl_narrator "I've managed to infiltrate my former home."

  nvl_narrator "I'm here at the behest of Luce, our leader."

  nvl_narrator "You may also know him as the Morning Star."

  nvl_narrator "He's the Light-Bringer, the Dawn-Bringer."

  nvl_narrator "The Shining One."

  nvl_narrator "Luce plans to wage another war against heaven."

  nvl_narrator "You see, it has the fiercest of fortifications."

  nvl_narrator "Slowly but steadily, he's been chipping away."

  nvl_narrator "Rendering heaven as vulnerable as possible."

  nvl_narrator "For this mission, Luce considered Sami or Lial."

  nvl_narrator "Eventually, though, he sent yours truly."

  nvl_narrator "Entrusted me with eroding heaven from within."

  nvl_narrator "I impressed him by hatching this entire plan."

  nvl_narrator "Heaven's new entry system with the nine trials."

  nvl_narrator "A more rigid organizational chart."

  nvl_narrator "This chart reinforces the hierarchy of angels."

  nvl_narrator "It sows discord among the angelic orders."

  nvl_narrator "You know the nine tiers of heaven?"

  nvl_narrator "They were inspired by the nine circles of hell."

  nvl_narrator "As for the new entry system, it aims to weaken."

  nvl_narrator "Heaven's overall strength is impacted."

  nvl_narrator "The numbers of both hell and Limbo are boosted."

  nvl_narrator "Theoretically, Limbo is a neutral ground."

  nvl_narrator "It isn't, though, in practice."

  nvl_narrator "When heaven and hell are at war, it yields."

  nvl_narrator "Limbo generally ends up supporting hell."

  nvl_narrator "This is because Sami and Lial reside there."

  nvl_narrator "Both hold influential roles in Limbo."

  nvl_narrator "The Limbokin have learned to bow before them."

  nvl_narrator "But we have nearly no foothold in heaven."

  nvl_narrator "It took time to plant the seeds of these ideas."

  nvl_narrator "The new entry system and the angelic hierarchy."

  nvl_narrator "I needed every ounce of subtlety and finesse."

  nvl_narrator "Anything to conceal my insidious intentions."

  nvl_narrator "But all my efforts eventually paid off."

  nvl_narrator "Even Kerubiel, the cherubim head, defers to me."

  nvl_narrator "The rest of the cherubim always follow suit."

  nvl_narrator "These games with humans mean nothing to them."

  nvl_narrator "Passing fancies. Mere diversions."

  nvl_narrator "Earlier, we had a debate over your fate."

  nvl_narrator "The choice was between Limbo and hell."

  nvl_narrator "I succeeded in swaying the vote without issue."

  nvl_narrator "You noticed that, didn't you?"

  nvl clear

  hide asta

  show asta asta_wingless_smile at center behind lilis with dissolve

  show lilis lilis_anxious #as side image

  Asta "And now here we are."

  Asta "There are no longer any secrets between us."

  "I'm as speechless as ever."

  show lilis lilis_sad #as side image

  "What can I even say? What can I even do?"

  "I have no hope of fleeing or besting him in battle."

  show lilis lilis_anxious #as side image

  "He's just confessed to being a fallen angel!"

  "Perhaps even one of the most powerful demons of hell!"

  show asta asta_wingless_default at center behind lilis

  Asta "To reiterate, the wings I wear aren't mine."

  Asta "They're a costume, a part of my disguise."

  Asta "Do you understand what that means?"

  Asta "The wings aren't functional for me."

  Asta "I can't fly you to Limbo or hell or anywhere else."

  show asta asta_wingless_anxious at center behind lilis

  Asta "I vowed to the cherubim I'd take care of you."

  Asta "I can't just drag you back to them, can I?"

  show asta asta_wingless_default at center behind lilis

  show lilis lilis_shock #as side image

  "A shiver runs through me."

  "What does Asta mean by that?"

  "What exactly is he planning to do with me?"

  show lilis lilis_anxious #as side image

  show asta asta_wingless_smile at center behind lilis

  Asta "It was fun, I admit. Fooling you all like this."

  Asta "Watching how readily you'd believe my lies."

  Asta "This was a marvelous exercise in manipulation."

  show asta asta_wingless_creepy at center behind lilis

  Asta "But now you have to disappear."

  Asta "One way or another."

  Asta "Farewell, my dear Lilis."

  stop music fadeout 1.0

  Asta "I won't remember you at all. Nobody will."

  play music music_ending fadein 2.0

  hide asta

  hide lilis

  scene cg cg_abyss with slow_dissolve

  "Just like that, it's all over for me."

  "Asta has cruelly flung me off from the precipice."

  "I fall screaming into the abyss."

  scene cg cg_ending_3 with slow_dissolve
  $ persistent.ending_seen_3 = True
  pause
  jump part_credits

init:
    image cred = Text("[gui.about!t]\n\nMade with Ren'Py [renpy.version_only]", text_align=0.5, xmaximum=1200)
    image theend = Text("{size=80}Fin", text_align=0.5)
    image thanks = Text("{size=80}Thanks for playing!", text_align=0.5)

label part_credits_from_menu:
    call part_credits from _call_part_credits
    return
    
label part_credits:
        
    $ quick_menu = False

    $ credits_speed = 20
    scene bg bg_dark
    with dissolve
    show cred at Move((0.5, 1.5), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    
    $ renpy.end_replay()
    
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks with dissolve

    if persistent.extras_unlocked:

        pass

    else:

        centered "You've unlocked the extras menu.\nAccess it through the main menu."

        $ persistent.extras_unlocked = True
        
    $ quick_menu = True

    return





