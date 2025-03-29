################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Gallery  ####################################################################
################################################################################
init:
  
  image gallerylock_button = "gui/button/gallery_locked.png"
  
  #CG images 
  image cg_abyss_button = im.Scale("images/cg_abyss.png", 383, 215)
  image cg_throne_button = im.Scale("images/cg_throne.png", 383, 215)
  
  #image cg_ending_01_button = im.Scale("images/cg/cg_ending_01.jpg", 383, 215)
  #image cg_ending_02_button = im.Scale("images/cg/cg_ending_02.jpg", 383, 215)
  #image cg_ending_03_button = im.Scale("images/cg/cg_ending_03.jpg", 383, 215)
    
  image bg_gates_button = im.Scale("images/bg_gates.png", 383, 215)
  image bg_heaven_button = im.Scale("images/bg_heaven.png", 383, 215)
  image bg_heaven_edge_button = im.Scale("images/bg_heaven_edge.png", 383, 215)
  image bg_arena_button = im.Scale("images/bg_arena.png", 383, 215)
    

init python:
    g_cg = Gallery()  
        
    g_cg.button("cg cg_abyss")
    g_cg.image("cg cg_abyss")
    g_cg.unlock("cg cg_abyss")
    
    g_cg.button("cg cg_throne")
    g_cg.image("cg cg_throne")
    g_cg.unlock("cg cg_throne")

    
    g_cg.locked_button = "gallerylock_button"
    
    #----------------------------------------
    
    g_bg = Gallery()
        
    g_bg.button("bg bg_gates")
    g_bg.unlock_image("bg bg_gates")
    g_bg.unlock_image("bg bg_gates_open")
    
    g_bg.button("bg bg_arena")
    g_bg.unlock_image("bg bg_arena")
    g_bg.unlock_image("bg bg_arena_empty")
    
    g_bg.button("bg bg_heaven")
    g_bg.unlock_image("bg bg_heaven")
    
    g_bg.button("bg bg_heaven_edge")
    g_bg.unlock_image("bg bg_heaven_edge")
    
    g_bg.locked_button = "gallerylock_button"
    #----------------------------------------
    current_page = 1

## CG Gallery screen ##################################################################
screen cg_gallery():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("CG Gallery"), extra_navigation=True):

        grid 2 1:
            xoffset 100
            yoffset 200
            xspacing 150
            yspacing 50
            #xfill True
            xalign 0.5
            yalign 0.5

            # Call make_button to show a particular button.
            if current_page == 1:
                button:
                  add g_cg.make_button("cg cg_throne", "cg_throne_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
                button:
                  add g_cg.make_button("cg cg_abyss", "cg_abyss_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
              
            
        #hbox:
        #    style_prefix "page"
        #    
        #    xfill True
        #    #xalign 0.5
        #    yalign 0.5
        #    xoffset -0
        #
        #    spacing gui.page_spacing
        #
        #    textbutton _("{size=+50}<{/size}") xalign 0.0 xoffset -40 action [SetVariable('current_page', 1), ShowMenu("cg_gallery")]
        #
        #    textbutton _("{size=+50}>{/size}") xalign 1.0 xoffset 0  action [SetVariable('current_page', 2), ShowMenu("cg_gallery")]
              
screen bg_gallery():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("BG Gallery"), extra_navigation=True):

        grid 2 2:
            xoffset 100
            yoffset 100
            xspacing 150
            yspacing 50
            #xfill True
            xalign 0.5
            yalign 0.5

            # Call make_button to show a particular button.
            button:
              add g_bg.make_button("bg bg_gates", "bg_gates_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_bg.make_button("bg bg_heaven", "bg_heaven_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_bg.make_button("bg bg_heaven_edge", "bg_heaven_edge_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            button:
              add g_bg.make_button("bg bg_arena", "bg_arena_button", xalign=0.5, yalign=0.55) xoffset -5 yoffset -5
            #null
              
    
    

################################################################################
## Music Box  ##################################################################
################################################################################

## Music Box setup #############################################################

init python:
    mr = MusicRoom()
    
    ######## ADD MUSIC FILES HERE ##############
    
    # Add music file references here.
    # The format goes:
    # ["path to music file.ogg",'Title', 'Composer']
    
    song_list = [ 
                ["audio/music_default.mp3",'Heaven','Beans'],
                ["audio/music_trial.mp3",'Trial','Beans'],
                ["audio/music_tension.mp3",'Tension','Beans'], 
                ["audio/music_emotion.mp3",'Emotion','Beans'],   
                ["audio/music_menu.mp3",'Menu Music','Beans'],
                ["audio/music_ending.mp3",'Ending Theme','Beans'],                 
                ]
    
    # This lists default values for song_name and song_description to prevent errors.
    song_name = ""
    song_description = ""
    
    # This automatically adds an mr.add record for every song in the list.
    # Songs are always unlocked while always_unlocked = True.
    for track in song_list:
        mr.add(track[0], always_unlocked = True, action=[SetVariable('current_track', track[0]), SetVariable("song_name",track[1]),SetVariable("song_description",track[2])])
    
    #default to the first song    
    current_track = song_list[0][0] 
    
## Music Box screen ############################################################
transform disk_fade_mr():
    rotate 0
    xpos 300
    ypos 450
    zoom 0.3
    alpha 0.7
    #parallel:
    #  linear 5.0 alpha 0.7
    #  linear 5.0 alpha 0.9
    #  repeat
    #parallel:
    #  linear 1.0 xpos 300
    #  linear 1.0 xpos 250
    #  repeat
    parallel:
      linear 1.0 rotate 30
      linear 1.0 rotate -20
      repeat
transform disk_nofade_mr():
    rotate 0
    xpos 300
    ypos 450
    zoom 0.3
    alpha 0.7

screen musicbox():

    default loopMatch = ""
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Music Box"), extra_navigation=True):
    
        if not renpy.music.is_playing():
          add "images/asta_sad.png" yalign 0.3 at disk_nofade_mr()
        else:
          add "images/asta_smile.png" yalign 0.3 at disk_fade_mr()

        hbox:
          xfill True
          vbox:
            xoffset 50
            style_prefix "playlist"
            spacing -10
                  
            $count = 0
            label "Tracks:" xoffset -20
            for track in song_list:
              textbutton "[track[1]]"  xoffset 0 action  mr.Play(track[0])#[SetVariable('current_track', track[0]), mr.Play(track[0])]
              $count +=1
          #add "gui/overlay/options_extra_verticalbar.png"
          vbox:
            xalign 1.0
            yalign 0.7
            xoffset 10
            xfill True
            vbox:
              xalign 0.5 yalign 0.55
              yoffset -100
              spacing 15
              label song_name:
                  xalign 0.5
                  text_size 55
                  #text_outlines [ (5, "#fff1", 0, 0), (3, "#fff2", 0, 0),  (1, "#fff4", 0, 0) ]
              label song_description.upper():
                  xalign 0.5
                  #outlines [ (1, "#000000", 0, 0)]
          
            vbox:
              xalign 0.5 yalign 0.55
              spacing 10
              style_prefix "playback"
              frame:
                #xalign 0.5
                background None
                area (0,0, 400, 160)
                hbox:
                  xalign 0.5
                  textbutton "Previous":
                      action [
                              mr.Previous()
                              ]
                  if not renpy.music.is_playing():
                    textbutton "Play":
                        action [
                                SetVariable('current_track', renpy.music.get_playing()), 
                                mr.Play(current_track)
                                ]
                  else:
                    textbutton "Pause":
                        action [
                                SetVariable('current_track', renpy.music.get_playing()),
                                mr.Stop()
                                ]
                  
                  textbutton "Next":
                      action [
                              mr.Next()
                              ]
    
    # Make music change upon entering / exiting room.
    on "replace" action Stop("music")
    on "replaced" action Play("music", config.main_menu_music, fadeout=1.0)
    
style playlist_button is gui_button
style playlist_button_text is gui_button_text
style playback_button is radio_button
style playback_button_text is radio_button_text

style playlist_button:
    right_padding 30
    top_padding 30
    #idle_background Frame("gui/button/button_idle.png", Borders(0, 0, 80, 0))
    #hover_background Frame("gui/button/button_hover.png", Borders(0, 0, 80, 0))
    #selected_background Frame("gui/button/button_hover.png", Borders(0, 0, 80, 0))
    #xsize 550
    #ysize 100
    
style playlist_button_text:
    #outlines [ (2, "#000000", 0, 0),(0, "#ffffff", 0, 0)]
    #hover_outlines [ (0, "#000000", 0, 0),(2, "#ffffff", 0, 0)]
    xalign 0.0

#style playback_button_text:
    #outlines [ (2, "#000000", 0, 0),(0, "#ffffff", 0, 0)]
    #hover_outlines [ (0, "#000000", 0, 0),(2, "#ffffff", 0, 0)]
#style playback_button:
  #xsize 250
  
## Endings screen ############################################################

screen endings():

    default loopMatch = ""
    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Endings"), extra_navigation=True):  
            
            vbox:
                xsize 1050
                yfill True
                spacing 0
                style_prefix "endings"

                if persistent.ending_seen_1:
                    text "True Ending: Unite" text_align 0.5 xalign 0.5
                else:
                    text "Ending 1: ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_2:
                    text "\"Good\" Ending: Rise" text_align 0.5 xalign 0.5
                else:
                    text "Ending 2: ???" text_align 0.5 xalign 0.5
                if persistent.ending_seen_3:
                    text "Bad Ending: Fall" text_align 0.5 xalign 0.5
                else:
                    text "Ending 3: ???" text_align 0.5 xalign 0.5
style endings_text is history_text

style endings_text:
  size 44
  font gui.name_text_font
  outlines [ (2, "#000000", 0, 0),(0, "#ffffff", 0, 0)]
  
style gui_overlay_title:
  size 22