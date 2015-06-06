from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finalscene')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a loser.",
         "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Opening_Scene(Scene):

    def enter(self):
        print "The Tardis is spinning out of control in the cosmos. It explodes"
        print "unexpectedly ending our entire universe both real and imagined"
        print "into one cosmic paradox."
        print "Ready for an adventure? Press ENTER to continue, or CRTL + C to"
        print "turn back now..."
        raw_input("> ")
        
        print "Like waking up from a dream we see Furiosa from Mad Max opening"
        print "up and standing to see the island of Jurassic Park for the first"
        print "time.  Confused and fearful by the strange sounds and sights she"
        print "is pulled to a long lost familiar ring of a free-standing NYC"
        print "payphone. It's a little sticky and revolting, but she answers it"
        print "anyway..."
        print "\n"
        print "\"Hello? \""
        print "\n"
        print "The voice on the other end is authoritative and insistent."
        print "\" You don't know me but my name is Ripley. You need to move"
        print "fast and collect as many weapons as possible. There is a very"
        print "nasty alien stalking you with acid for blood and a tail that"
        print "will slice you in half. Get to me as fast as you can, there is a"
        print "thing called an iPhone on the ground next to you...it will help"
        print "you, bring it to me. Look ahead, do you see a Rock Candy"
        print "Mountain? I'm at the top, it is safe here! \""
        return 'scene1'

class Scene_1(Scene):

    def enter(self):
        print "Furiosa picks up the iPhone, and a nearby backpack that has"
        print "several weapons and some essentials. She looks at the iPhone and"
        print "is mesmerized momentarily by the game Candy Crush. Her attention"
        print "quickly shifts to the sky, because from overhead a pterodactyl"
        print "approaches and she reaches into her backpack to find a shotgun."
        print "\n"
        print "Choose: 'shoot', 'throw the iPhone' or 'run away'?"

        action = raw_input("> ")
        
        if action == "shoot":
            print "Furiosa fires away and blows the pterodactyl to pieces."
            print "She turns to see a strange looking machine called a Segway!"
            print "Looking closely at it, it's covered in blood and says"
            print "'Property of Segway Steve'. She shrugs and gets on the"
            print "segway and proceeds towards the forest."
            return 'scene2'

        elif action == "throw the iPhone":
            print "Furiosa winds up and hurls the iPhone at the pterodactyl."
            print "But it ends up being more of a easy lob in the dinosaur's"
            print "general direction. The pterodactyl laughs and screeches: \""
            print "ANDROID WILL PREVAIL!\" and eats Furiosa."
            return 'death'

        elif action == "run away":
            print "Furiosa sprints away from the pterodactyl but only makes it"
            print "three steps before the giant ancient pterosaur swoops down"
            print "and gobbles her up."
            return 'death'

        else:
            print "DOES NOT COMPUTE!"
            return 'scene1'

class Scene_2(Scene):

    def enter(self):
        print "description of scene 2"

        action = raw_input("> ")

        if action == "option_a":
            print "outcome of option_a"
            return 'scene3'

        elif action == "option_b":
            print "outcome of option_b"
            return 'death'

        elif action == "option_c":
            print "outcome of option c"
            return 'death'

        else:
            print "DOES NOT COMPUTE!"
            return 'scene2'

class Scene_3(Scene):

    def enter(self):
        print "description of scene 3"

        action = raw_input("> ")

        if action == "option_a":
            print "outcome of option_a"
            return 'scene4'

        elif action == "option_b":
            print "outcome of option_b"
            return 'death'

        elif action == "option_c":
            print "outcome of option c"
            return 'death'

        else:
            print "DOES NOT COMPUTE!"
            return 'scene3'      

class Scene_4(Scene):

    def enter(self):
       print "Scene 4 description"

       action = raw_input("> ")

       if action == "option_a":
           print "Option A description"
           return 'finalscene'

       elif action == "option_b":
           print "Option B description"
           return 'death'

       elif action == "option_c":
           print "Option C description"
           return 'death'

       else:
           print "DOES NOT COMPUTE!"
           return 'scene4'

class Final_Scene(Scene):

    def enter(self):
        print "You won! Good job."
        exit()

class Map(object):

    scenes = {
        'openingscene': Opening_Scene(),
        'scene1': Scene_1(),
        'scene2': Scene_2(),
        'scene3': Scene_3(),
        'scene4': Scene_4(),
        'finalscene': Final_Scene(),
        'death': Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('openingscene')
a_game = Engine(a_map)
a_game.play()
