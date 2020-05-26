from classes.game import Player, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Create jutsus
FireBall = Spell("Fireball Jutsu", 25, 70, "Black")
Chidori = Spell("Chidori", 50, 150, "Black")
WaterDragon = Spell("Water Dragon Jutsu", 30, 70, "Black")
Rasengan = Spell("Rasengan", 50, 150, "Black")
FlowerBlossom = Spell("Super Flower Blossom", 35, 100, "Black")
MudWall = Spell("Dotton: Mud Wall", 60, 35, "Grey")

# Create cure jutsus
Cure = Spell("Heal Jutsu", 25, 600, "White")
SuperCure = Spell("Super Heal Jutsu", 35, 1200, "White")


# Enemy jutsus
Sussano = Spell("Limbo", 60, 250, "Black")
ChibakuTensei = Spell("Chibaku Tensei", 100, 350, "Black")
Kamui = Spell("Kamui", 60, 250, "Black")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 100)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 150)
superpotion = Item("Super-Potion", "potion", "Heals 1000 HP", 200)
elixir = Item("Elixir", "elixir", "Fully restores HP of one party", 100000)
hielixir = Item("MegaElixir", "elixir", "Fully restores HP/MP", 100000)
shuriken = Item("Shuriken", "attack", "Deals 100 damage", 100)

# Creating indivudal items
player_items = [{'item': potion, 'Quantity': 2},
                {'item': superpotion, 'Quantity': 2},
                {'item': shuriken, 'Quantity': 3}]

player2_items = [{'item': potion, 'Quantity': 1},
                 {'item': shuriken, 'Quantity': 5}]

player3_items = [{'item': potion, 'Quantity': 3},
                 {'item': hipotion, 'Quantity': 1},
                 {'item': superpotion, 'Quantity': 2},
                 {'item': elixir, 'Quantity': 1}]

# Instantiate Characters
Naruto = Player("Naruto   ", 3800, 300, 80, 20, [Rasengan], player_items, "Modo Sennin")
Sasuke = Player("Sasuke   ", 3200, 250, 150, 30, [FireBall, Chidori], player2_items, "Sharingan")
Sakura = Player("Sakura   ", 4200, 180, 120, 15, [FlowerBlossom, Cure, SuperCure], player3_items, "Byakugou")
Kakashi = Player("Kakashi  ", 3000, 180, 90, 25, [FireBall, Chidori, WaterDragon, MudWall], player_items, "Sharingan")

allCharacters = [Naruto, Sasuke, Sakura, Kakashi]

# Instantiate Enemies
enemy1 = Player("Obito   ", 5000, 150, 200, 25, [FireBall, Kamui], [], "Sharingan")
enemy2 = Player("Madara  ", 8000, 180, 250, 30, [FireBall, Sussano], [], "Sharingan")
enemy3 = Player("Pain    ", 4000, 200, 200, 25, [FireBall, WaterDragon, ChibakuTensei], [], "Rinnegan")

players = []
enemies = [enemy1, enemy2, enemy3]

running = False
i = 0

def check_if_game_is_over():
    global running
    # check if game is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    # Check if player won
    if defeated_enemies == len(enemies):
        print(bcolors.OKGREEN + "\n\n" + "You Win!"+ "\n\n" + bcolors.ENDC)
        running = False

    # check if enemy won
    elif defeated_players == len(players):
        print(bcolors.FAIL + "\n\n" + "You Lost!"+ "\n\n" + bcolors.ENDC)
        running = False

print(bcolors.FAIL + bcolors.B0LD + "Let's go!" + bcolors.ENDC)


def initialize_game():
    global players
    global allCharacters

    countCharacters = 0
    while countCharacters != 3:
        i=1
        for character in allCharacters:
            print("        " + str(i) + ':', character.name)
            i+=1
        countCharacters+=1
        choices = (input("    choose a character (type his/her name): ")).lower().strip()
        #print(choices)
        if choices == "naruto":
            #print("ues")
            players.append(Naruto)
            allCharacters.remove(Naruto)
        if choices == "sasuke":
            #print(character.name+choices+players)
            players.append(Sasuke)
            allCharacters.remove(Sasuke)
        if choices == "kakashi":
            #print(character.name+choices+players)
            players.append(Kakashi)
            allCharacters.remove(Kakashi)
        if choices == "sakura":
            #print(character.name+choices+players)
            players.append(Sakura)
            allCharacters.remove(Sakura)

def start_game():
    print("="*80)
    print("                                   Naruto RPG                by: @filipemf")
    print("This is a RPG fan made game based on Naruto anime and characters. Select one of the following options bellow (option's number) to continue.")
    print("1. Start!")
    print("2. Instructions")
    print("3. Credits")
    choice = int(input("Your option: "))
    print("="*80)
    return choice

choice = start_game()

if choice == 1:
    initialize_game()
    running = True

elif choice == 2:
    print("                                   INSTRUCTIONS")
    print("In this game, each character has stats (hp, attack, defense, chakra, jutsus and items). One of the game experiences is simulate a battle with consequences, so, each action matters and some have side effects."+
     "\n"+"You can't go back on your realtime actions. Good luck, ninja!"+"\n\n")
    choice = str(input("Want to start, or quit? ")).lower().strip()
    if choice.lower() == "iniciar" or choice.lower() == "sim" or choice.lower()=="yes" or choice.lower()=="start" :
        initialize_game()
        running = True
    else:
        print("Okay! See you soon!")
        running = False

elif choice == 3:
    print("                                   CREDITS")
    print("\n"+"Created by: Filipe Marques Ferreira"+"\n"+
        "GitHub: filipemf"+"\n\n")

else:
    print("Select a valid option!")



while running:
    print("="*80)
    print("Name                          HP                                          CHAKRA   ")

    # Get all players Stats
    for player in players:

        # Handle ability side efects
        if player.are_using_ability == True:

            chakraPerCent = (player.mp/player.max_mp)*100
            if chakraPerCent>30 and player.name == "Naruto   ":
                mpToReduce = (player.mp*25)/100
                int(mpToReduce)

                player.mp -= mpToReduce
                int(player.mp)

            if chakraPerCent>30 and player.name != "Naruto   ":
                mpToReduce = (player.mp*10)/100
                int(mpToReduce)

                player.mp -= mpToReduce
                int(player.mp)


            elif chakraPerCent<30:
                player.disable_ability()

        player.get_stats()

    # Separate enemies and player stats
    print("=" * 38 + bcolors.FAIL + "Enemys" + bcolors.ENDC + "=" * 38)

    # Get all enemies stats
    for enemy in enemies:
        enemy.get_enemy_stats()

    #Start player action
    for player in players:
        abilityOption = player.check_actions()

        check_if_game_is_over()
        if player.get_hp()==0:
            del player
            continue
        player.choose_action()
        choice = input("    Choose an action: ")
        index = int(choice)-1

        # If player chooses attack
        if index == 0:
            check_if_game_is_over()
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            
            enemies[enemy].take_damage(dmg)
            print(bcolors.OKBLUE+"\n"+player.name+ " attacked " +enemies[enemy].name + " using taijutsu, causing ", dmg, " of damage!"+bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name, " has died.")
                del enemies[enemy]

        # If player chooses jutsus
        elif index == 1:
            check_if_game_is_over()
            player.choose_magic()
            magic_choice = int(input("    Choose a jutsu: ")) - 1

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nYou don't have enough chakra to do this!" + bcolors.ENDC)
                continue

            if spell.type == "White":
                player.reduce_mp(spell.cost)
                allie = player.choose_allie(players)
                players[allie].heal(magic_dmg)
                print(bcolors.OKGREEN + "\n" + spell.name + " healed" + str(magic_dmg), " HP on: ", players[allie].name + bcolors.ENDC)
                continue

            elif spell.type == "Black":

                if spell.name == "Fireball Jutsu":
                    index = 0
                    for enemy in enemies:
                        enemy.take_damage(magic_dmg)
                        if enemy.get_hp() == 0:
                            print(enemies[enemy].name, " has died.")
                            del enemies[enemy]
                        index += 1
                    player.reduce_mp(spell.cost)
                    print(bcolors.OKBLUE +"All enemys ",str(magic_dmg)+ " from: ", spell.name+ bcolors.ENDC)
                    continue    


                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)

                player.reduce_mp(spell.cost)
                enemy1.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " caused", str(magic_dmg), " points of damage to: " +
                      enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name, " has died.")
                    del enemies[enemy]

        #If player chooses items
        elif index == 2:
            check_if_game_is_over()
            player.choose_item()
            item_choice = (int(input("Escolha um item: ")))-1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["Quantity"] == 0:
                print(bcolors.FAIL + "\n" + "Nenhum restante...." + bcolors.ENDC)
                continue

            player.items[item_choice]["Quantity"] -= 1

            if item.type == "potion":
                allie = player.choose_allie(players)
                players[allie].heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " curou ", str(item.prop), " de HP" + bcolors.ENDC)

            elif item.type == "elixir":
                if item.name == "MegaElixir":
                    for i in players:
                        i.hp = i.max_hp
                        i.mp = i.max_mp
                else:
                    player.hp = player.max_hp
                    player.mp = player.max_mp
                print(bcolors.OKGREEN + "\n" + item.name + " restaurou totalmente o HP/Chakra" + bcolors.ENDC)

            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                enemy1.take_damage(item.prop)

                print(bcolors.FAIL + "\n" + item.name + " causou " + str(item.prop) +
                      " pontos de dano em " + enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name, "morreu.")
                    del enemies[enemy]

        elif index == 3 and player.are_using_ability == False:
            player.active_ability()

        elif index == 3 and player.are_using_ability == True:
            #print(bcolors.FAIL+ "Ability already used!. You'll loose one turn."+bcolors.ENDC)
            print(bcolors.FAIL+ "Disabling ability..."+bcolors.ENDC)
            player.disable_ability()

    # check if game is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    # Check if player won
    if defeated_enemies == len(enemies):
        print(bcolors.OKGREEN + "Você venceu!" + bcolors.ENDC)
        running = False

    # check if enemy won
    elif defeated_players == len(players):
        print(bcolors.FAIL + "Você perdeu!" + bcolors.ENDC)
        running = False




    # Enemy attack Phase
    for enemy in enemies:

        enemy_choice = random.randrange(0, 2)

        print('\n')
        if enemy_choice == 0:
            # choose attack
            target = random.randrange(0, len(players))
            enemy_dmg = enemy.generate_damage()

            players[target].take_damage(enemy_dmg)
            print(bcolors.FAIL + enemy.name + " caused", str(enemy_dmg), " points of damage to " +
                  players[target].name+" using taijutsu!" + bcolors.ENDC)
            if players[target].get_hp() == 0:
                        print(players[target].name, " has died.")
                        del players[target]
            check_if_game_is_over()

        if enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "White":
                enemy.heal(magic_dmg)

                print(bcolors.OKBLUE + spell.name + "healed" + enemy.name +
                      " HP by: " + str(magic_dmg)+ bcolors.ENDC)

            elif spell.type == "Black":
                try:
                    target = random.randrange(0, len(players))
                    players[target].take_damage(magic_dmg)

                    print(bcolors.FAIL + enemy.name + " caused ", str(magic_dmg), " points of damage to: " +
                    players[target].name+" using: ",  spell.name + bcolors.ENDC)

                    if players[target].get_hp() == 0:
                        print(players[target].name, " has died.")
                        del players[target]
                    check_if_game_is_over()
                except:
                    print(bcolors.FAIL + "Ops! Something went wrong... =(" + bcolors.ENDC)
                    running = False
                