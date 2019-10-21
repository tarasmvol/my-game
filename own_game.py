from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is still to come")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #printing the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You are dead. And the rest doensn't matter",
        "Loser!",
        "My granny computes better than you!"
    ]

    def enter(self):
        print (Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralSquare(Scene):

    def enter(self):
        print(dedent("""
            You just finished University and walking around the city looking for the job. Suddently you see
            the Stranger in black suit and white hat is coming up to you saying:
            "Dear, young gentelam, you are looking for sense in life and wanna to find a job?"
            Your actions: print "hit the stranager with my leg", "spit into the stranger's face", "I say, yes"."""))

        action = input("print your action > ")

        if action == "hit the stranger with my leg":
            print("The stranger steps back and you fall apart into small pieces")
            return 'death'

        elif action == "spit into the stranger's face":
            print (dedent("""
                Suddenly you become as small as an ant and drown to death in your saliva.
                """))

            return 'death'

        elif action == "I say, yes":
            print(dedent(""""
                The world around you starts to melt and suddenly you fall down through the rabit's hole
                """))

            return 'president_palace'

        else:
            print("Learn to make right choices and learn to type. Life is not a supermarket.")

            return 'central_square'

class PresidentPalace(Scene):

    def enter(self):
        print(dedent("""
            You find yourself in the Presidential Palace. There is big and wide mable table with big bag with
            electronic lock on it. What's your next step? Will you follow your destiny and become a President or
            try to unlock the bag? (print "become a president" or "unlock the bag")
            """))

        choice = input ("Your action > ")

        if choice == "become a president":

            print(dedent("""Current president rushes through the door with iron pan and smashes your head into pieces.
                Nice try.
                """))

            return 'death'

        elif choice == "unlock the bag":
            print("""Code consist of 1 digit from 1 to 10.You've got to make a guess
                and enter one digit that determines your destiny. Only 8 tries.""")

            code = f"{randint(1,3)}"
            guess = input ("[keypad]> ")
            guesses = 0

            while int(guess) != int(code) and guesses < 6:
                print("ChikChikChik! The lock still closed")
                guesses += 1
                guess = input("[keypad]...'one more try',- says the bag> ")

            if guess == code:
                print (dedent("""
                    The lock clicks open and you see a big pile of money inside the bag.
                    You put as much as possible money into your pockets and run as fast
                    as you can towards the windon of the Presidential Palace
                    """))

                return 'square_again'

            else:
                print(dedent("""
                    The lock buzzles one last time. And you hear the voice from above:'Fool, you.
                    I cheated you. Indeed you had only 6 choices not 8. I am sorry, but you've got to die'
                    """))

                return 'death'

        else:
            print("Learn to make right choices and learn to type. Life is not a supermarket.")
            return 'president_palace'

class SquareAgain(Scene):

    def enter(self):
        print(dedent("""
            You jump out of the window of Presidential Palace and find yourself in the square, where
            the Strager have met you. You see President with his bodyguards close to you. What's your next action?
            ("hit the president", "throw the bomb to bodyguards", "I say 'Glory to President!' and slowly walk away")
            """))

        action = input("Your action?> ")

        if action == "hit the president":
            print (dedent("""
                The President falls down and his bodyguards start to kick your ass.
                """))
            return 'death'

        elif action == "throw the bomb to bodyguards":
            print(dedent("""
                You don't have a bomb. So you throw the empty air. THe President becomes agnry and hits
                your face and his bodyguars take all money from your pockets. You immediately starve to
                death
                """))
            return 'death'

        elif action == "I say 'Glory to President!' and slowly walk away":
            return 'escape'
        else:
            print("Learn to make right choices and learn to type. Life is not a supermarket.")
            return "square_again"

class Escape(Scene):

    def enter(self):
        print(dedent("""
            You slowly come up to the Presidential car and nobody sees you. The car has 4 doors.
            which door will you open: 1, 2, or 3 or maybe 4? Enter the number.
            """))
        good_door = randint(1,4)

        guess = input ("I enter door...> ")

        while int(guess) != int(good_door):
            print ("the door is locked, try the other one")
            guess = input ("I enter door...> ")

        print(dedent("""
            You enter the car and flee away with Presidential car and pockets full of money.
            The only thing - you still have no job and the President and his guards will chase you now for the rest of
            your life. You won!"""))

        return 'finished'

class Finished(Scene):

    def enter(self):
        print("Lucky you! Good job! Keep like that! Don't repeat it in real life!")
        return 'finished'

class Map(object):
    scenes = {
        'central_square': CentralSquare(),
        'president_palace': PresidentPalace(),
        'escape': Escape(),
        'square_again': SquareAgain(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_square')
a_game = Engine(a_map)
a_game.play()
