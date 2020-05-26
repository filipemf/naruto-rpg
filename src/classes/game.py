import random
from classes.inventory import Item
from classes.magic import Spell

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    B0LD = "\033[1m"
    UNDERLINE = "\033[4m"


class Player:
    def __init__(self, name, hp, mp, atk, df, magic, items, ability):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk - 20
        self.atkh = atk + 20
        self.df = df
        self.magic = magic
        self.items = items
        self.name = name
        self.actions = ['Attack', 'Jutsus', 'Items']
        self.ability = ability

        self.are_using_ability = False


    def check_actions(self):
        if self.are_using_ability == True:
            self.actions = ['Attack', 'Jutsus', 'Items', 'Disable Ability']

        if self.are_using_ability == False:
            self.actions = ['Attack', 'Jutsus', 'Items', 'Active Ability']

    def active_ability(self):
        if self.ability == 'Sharingan' and self.are_using_ability == False:

            #What ability will do
            self.atkh+=40
            self.atkl+=40
            print(bcolors.OKBLUE+"By the use of "+bcolors.FAIL+"SHARINGAN"+bcolors.OKBLUE+", your attacks are raised by 40 points, but this will consume you chakra"+bcolors.ENDC)
            
            #If is Kakashi
            if self.name == "Kakashi  ":
                self.magic.append(Spell("Kamui", 45, 250, "Black"))
            
            self.are_using_ability = True


        elif self.ability == 'Byakugou' and self.are_using_ability == False:

            self.hp +=800
            self.atkh+=20
            self.atkl+=20
            print(bcolors.OKBLUE+"By the use of "+bcolors.OKGREEN +"BYAKUGOU"+bcolors.OKBLUE+", your HP are being raised by 800 points, and your attacks in 20 points"+bcolors.ENDC)
            
            self.are_using_ability = True


        elif self.ability == 'Modo Sennin' and self.are_using_ability == False:
            self.mp+=35
            self.atkh+=35
            self.atkl+=35      

            print(bcolors.OKBLUE+"By the use of "+bcolors.OKGREEN +"MODO SENNIN"+bcolors.OKBLUE+", you obtained 35 additional points of chakra, 15 points of attack and you acquired a new jutsu: RasenShuriken. But your chakra will be decreased by 25% each turn"+bcolors.ENDC)
            
            self.magic.append(Spell("RasenShuriken", 80, 450, "Black"))

            self.are_using_ability = True

    def disable_ability(self):
        if self.are_using_ability == True and self.are_using_ability == True:
            if self.ability == 'Modo Sennin':
                for jutsu in self.magic:
                    if jutsu.name == 'RasenShuriken':
                        self.magic.remove(jutsu)
                self.atkh-=35
                self.atkl-=35 

            if self.ability == 'Sharingan' and self.name == "Kakashi  ":
                for jutsu in self.magic:
                    if jutsu.name == 'Kamui':
                        self.magic.remove(jutsu)

                self.atkh-=40
                self.atkl-=40
            
            self.are_using_ability = False

            #Custo de ter ativado a habilidade
            ##self.hp -= (self.hp*10)/100
            ##self.mp -= (self.mp*10)/100
            ##self.atkl -= (self.atkl*10)/100
            ##self.atkh -= (self.atkh*10)/100
            ##self.df -= (self.df*10)/100

    def generate_damage(self):
        return random.randrange(round(self.atkl,0), round(self.atkh,0))

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def take_damage(self, dmg):
        self.hp -= (dmg-self.df)
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def choose_action(self):
        i = 1
        print("\n" + "    " + bcolors.B0LD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.B0LD + "    Actions" + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ':', item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.B0LD + "Jutsus" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ':', spell.name, '(cost: ', str(spell.cost) + ')'+" damage: "+str(spell.dmg))
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.B0LD + "ITEMS" + bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item['item'].name, ":", item['item'].description, "x(" +
                  str(item['Quantity']) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.B0LD + "    Target:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + "." + enemy.name)
                i += 1
        choice = int(input("    choose a target: ")) - 1
        return choice

    def choose_allie(self, players):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.B0LD + "        Escolha um alvo de cura:" + bcolors.ENDC)
        for player in players:
            print("        " + str(i) + ':', player.name)
            i += 1
        choice = int(input("    escolha um alvo: ")) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = ((self.hp / self.max_hp) * 100) / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp += hp_string

        print("                              __________________________________________________")
        print(bcolors.B0LD + self.name + "         " +
              current_hp + " |" + bcolors.FAIL +
              hp_bar + bcolors.ENDC + "|")

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp/self.max_hp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.max_mp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(round(self.hp)) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 9:
            decr = 9 - len(hp_string)
            while decr > 0:
                current_hp += " "
                decr -= 1
            current_hp += hp_string
        else:
            current_hp += hp_string

        mp_string = str(round(self.mp)) + "/" + str(self.max_mp)
        current_mp = ""

        if len(mp_string) < 7:
            decr = 7 - len(mp_string)
            while decr > 0:
                current_mp += " "
                decr -= 1
            current_mp += mp_string
        else:
            current_mp += mp_string

        print("                             _________________________                    __________")
        print(bcolors.B0LD + self.name + "         " +
              current_hp + " |" + bcolors.OKGREEN +
              hp_bar +
              bcolors.ENDC + bcolors.B0LD + "|          " +
              current_mp + " |" + bcolors.OKBLUE +
              mp_bar + bcolors.ENDC + "|")

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = self.get_hp() / self.max_hp * 100

        if self.mp < spell.cost and spell.type == "White" and pct > 50:
            return self.choose_enemy_spell()
        else:
            return spell, magic_dmg