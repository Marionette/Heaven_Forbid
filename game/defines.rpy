init:
    ###### POSITION DEFINES ############
    #transform farleft:
    #  yalign 1.0 xanchor .5 xalign 0.0
    #transform left:
    #  yalign 1.0 xanchor .5 xalign 0.25
      
    #transform right:
    #  yalign 1.0 xanchor .5 xalign 0.75
    
    transform battle_right:
        rotate 0
        yalign 0.5
        xalign 1.0
        transform_anchor True
    transform battle_left:
        rotate 0
        yalign 0.5
        xalign 0.0
        transform_anchor True
    
    ######### MISC DEFINES #############
    define slow_dissolve = Dissolve(2.0)
        
    #default headpiece_halo = False
    #default headpiece_helm = False
    #default headpiece_coronet = False
    #default wings_feather = False
    #default wings_flaming = False
    #default wings_gold = False
    #default accessory_bow = False
    #default accessory_sword = False
    #default accessory_trumpet = False
    default condition_god = False
    default points_dexterity = 0
    default points_strength = 0
    default points_charisma = 0
    default points_victory = 0
    default points_surrender = 0
    default ab_default = "avatar_blue default_1"
    default ab_sad = "avatar_blue sad_1"
    default ab_smile = "avatar_blue smile_1"
    
    # Declare characters used by this game. The color argument colorizes the
    # name of the character.

    ######### CHARACTER DEFINES #############
    define Lilis = Character("Lilis", image="lilis")
    define Eva = Character("Eva", image="eva")
    define Asta = Character("Asta", image="asta")
    define Cherub = Character("Cherub", image="asta")
    define Keru = Character("Keru", image="keru")
    define Saint_Peter = Character("Saint Peter", image="peter")
    define R__ = Character("R__", image="red")
    define O_____ = Character("O_____", image="orange")
    define Y_____ = Character("Y_____", image="yellow")
    define G____ = Character("G____", image="green")
    define B___ = Character("B___", image="blue")
    define I_____ = Character("I_____", image="indigo")
    define V_____ = Character("V_____", image="violet")
    define P___ = Character("P___", image="pink")
    
    define narrator = Character(None, image="lilis")
    define nvl_narrator = Character(None, kind=nvl, image="lilis")
  
    
    ######### SOUND DEFINES ############# 
    $music_default = "audio/music_default.mp3"
    $music_emotion = "audio/music_emotion.mp3"
    $music_ending = "audio/music_ending.mp3"
    $music_menu = "audio/music_menu.mp3"
    $music_tension = "audio/music_tension.mp3"
    $music_trial = "audio/music_trial.mp3"

    ######### CG/BG IMAGE DEFINES #############
    image black = Solid("#000000")  
    image bg black = Solid("#000000")     
    image bg white = Solid("#ffffff")
    
    #Backgrounds
    image bg bg_arena = im.FactorScale("images/bg_arena.png",0.5)
    image bg bg_arena_empty = im.FactorScale("images/bg_arena_empty.png",0.5)
    image bg bg_dark = im.FactorScale("images/bg_dark.png",0.5)
    image bg bg_gates = im.FactorScale("images/bg_gates.png",0.5)
    image bg bg_gates_open = im.FactorScale("images/bg_gates_open.png",0.5)
    image bg bg_heaven = im.FactorScale("images/bg_heaven.png",0.5)
    image bg bg_heaven_edge = im.FactorScale("images/bg_heaven_edge.png",0.5)

    #CG images 
    image cg cg_abyss = im.FactorScale("images/cg_abyss.png",0.5)
    image cg cg_ending_1 = im.FactorScale("images/cg_ending_1.png",0.5)
    image cg cg_ending_2 = im.FactorScale("images/cg_ending_2.png",0.5)
    image cg cg_ending_3 = im.FactorScale("images/cg_ending_3.png",0.5)
    image cg cg_throne = im.FactorScale("images/cg_throne.png",0.5)

    #Sprites   
    image side lilis lilis_anxious = im.Crop(im.FactorScale("images/lilis_anxious.png",0.45),300,0,700,1000)
    image side lilis lilis_default = im.Crop(im.FactorScale("images/lilis_default.png",0.45),300,0,700,1000)
    image side lilis lilis_mad = im.Crop(im.FactorScale("images/lilis_mad.png",0.45),300,0,700,1000)
    image side lilis lilis_sad = im.Crop(im.FactorScale("images/lilis_sad.png",0.45),300,0,700,1000)
    image side lilis lilis_shock = im.Crop(im.FactorScale("images/lilis_shock.png",0.45),300,0,700,1000)
    image side lilis lilis_smile = im.Crop(im.FactorScale("images/lilis_smile.png",0.45),300,0,700,1000)
    
    #Invisible character images to go with side images
    image lilis lilis_anxious = "images/empty.png"
    image lilis lilis_default = "images/empty.png"
    image lilis lilis_mad = "images/empty.png"
    image lilis lilis_sad = "images/empty.png"
    image lilis lilis_shock = "images/empty.png"
    image lilis lilis_smile = "images/empty.png"

    image asta asta_anxious = im.FactorScale("images/asta_anxious.png",0.45)
    image asta asta_creepy = im.FactorScale("images/asta_creepy.png",0.45)
    image asta asta_default = im.FactorScale("images/asta_default.png",0.45)
    image asta asta_mad = im.FactorScale("images/asta_mad.png",0.45)
    image asta asta_sad = im.FactorScale("images/asta_sad.png",0.45)
    image asta asta_shock = im.FactorScale("images/asta_shock.png",0.45)
    image asta asta_smile = im.FactorScale("images/asta_smile.png",0.45)

    image asta asta_wingless_anxious = im.FactorScale("images/asta_wingless_anxious.png",0.45)
    image asta asta_wingless_creepy = im.FactorScale("images/asta_wingless_creepy.png",0.45)
    image asta asta_wingless_default = im.FactorScale("images/asta_wingless_default.png",0.45)
    image asta asta_wingless_mad = im.FactorScale("images/asta_wingless_mad.png",0.45)
    image asta asta_wingless_sad = im.FactorScale("images/asta_wingless_sad.png",0.45)
    image asta asta_wingless_shock = im.FactorScale("images/asta_wingless_shock.png",0.45)
    image asta asta_wingless_smile = im.FactorScale("images/asta_wingless_smile.png",0.45)

    image avatar_blue default_1 = im.FactorScale("images/avatar_blue_default_1.png",0.45)
    image avatar_blue default_2 = im.FactorScale("images/avatar_blue_default_2.png",0.45)
    image avatar_blue default_3 = im.FactorScale("images/avatar_blue_default_3.png",0.45)
    image avatar_blue default_4 = im.FactorScale("images/avatar_blue_default_4.png",0.45)
    image avatar_blue sad_1 = im.FactorScale("images/avatar_blue_sad_1.png",0.45)
    image avatar_blue sad_2 = im.FactorScale("images/avatar_blue_sad_2.png",0.45)
    image avatar_blue sad_3 = im.FactorScale("images/avatar_blue_sad_3.png",0.45)
    image avatar_blue sad_4 = im.FactorScale("images/avatar_blue_sad_4.png",0.45)
    image avatar_blue smile_1 = im.FactorScale("images/avatar_blue_smile_1.png",0.45)
    image avatar_blue smile_2 = im.FactorScale("images/avatar_blue_smile_2.png",0.45)
    image avatar_blue smile_3 = im.FactorScale("images/avatar_blue_smile_3.png",0.45)
    image avatar_blue smile_4 = im.FactorScale("images/avatar_blue_smile_4.png",0.45)

    image eva eva_anxious = im.FactorScale("images/eva_anxious.png",0.45)
    image eva eva_default = im.FactorScale("images/eva_default.png",0.45)
    image eva eva_mad = im.FactorScale("images/eva_mad.png",0.45)
    image eva eva_sad = im.FactorScale("images/eva_sad.png",0.45)
    image eva eva_shock = im.FactorScale("images/eva_shock.png",0.45)
    image eva eva_smile = im.FactorScale("images/eva_smile.png",0.45)

    image keru keru_default  = im.FactorScale("images/keru_default_.png",0.45)
    image peter peter_default = im.FactorScale("images/peter_default.png",0.45)

    image blue blue_default = im.FactorScale("images/blue_default.png",0.45)
    image green green_default = im.FactorScale("images/green_default.png",0.45)
    image indigo indigo_default = im.FactorScale("images/indigo_default.png",0.45)
    image orange orange_default = im.FactorScale("images/orange_default.png",0.45)
    image pink pink_default = im.FactorScale("images/pink_default.png",0.45)
    image red red_default = im.FactorScale("images/red_default.png",0.45)
    image violet violet_default = im.FactorScale("images/violet_default.png",0.45)
    image yellow yellow_default = im.FactorScale("images/yellow_default.png",0.45)
    
    image avatar_blue default_1 = im.Crop("images/avatar_blue_default_1.png", 900,0,1020,1080)
    image avatar_blue default_2 = im.Crop("images/avatar_blue_default_2.png", 900,0,1020,1080)
    image avatar_blue default_3 = im.Crop("images/avatar_blue_default_3.png", 900,0,1020,1080)
    image avatar_blue default_4 = im.Crop("images/avatar_blue_default_4.png", 900,0,1020,1080)
    
    image avatar_blue sad_1 = im.Crop("images/avatar_blue_sad_1.png", 900,0,1020,1080)
    image avatar_blue sad_2 = im.Crop("images/avatar_blue_sad_2.png", 900,0,1020,1080)
    image avatar_blue sad_3 = im.Crop("images/avatar_blue_sad_3.png", 900,0,1020,1080)
    image avatar_blue sad_4 = im.Crop("images/avatar_blue_sad_4.png", 900,0,1020,1080)
    
    image avatar_blue smile_1 = im.Crop("images/avatar_blue_smile_1.png", 900,0,1020,1080)
    image avatar_blue smile_2 = im.Crop("images/avatar_blue_smile_2.png", 900,0,1020,1080)
    image avatar_blue smile_3 = im.Crop("images/avatar_blue_smile_3.png", 900,0,1020,1080)
    image avatar_blue smile_4 = im.Crop("images/avatar_blue_smile_4.png", 900,0,1020,1080)