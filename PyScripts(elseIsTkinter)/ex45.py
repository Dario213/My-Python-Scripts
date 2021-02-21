from random import randint
from sys import exit
from textwrap import dedent
from sys import argv


script, filename, filename2, filename3 = argv
trezor_kod = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}{randint(1,9)}"
pismo = open(filename)
transakcije = open(filename2)
nalazi = open(filename3)


class Scene(object):

    def enter(self):
        print("This scene is not configured.")
        print("Sunclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finish')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    message = ["Wow that was terrible, my dog is better than you.",
               "What was that, you are worse than one nerd from my class.",
               "What a shame...your mom would be sooo proud of you now.",
               "I guess you are stupid...",
               "Incredible IQ you have I see...",
               "Hmm, who was your teacher, I need to speak with him.",
               "Did you ever go to school?!",
               "You are such a looser",
               "Can't believe that you would let Plenkovic win"]

    def enter(self):
        print("\n\r",Death.message[randint(0, len(self.message)-1)],"\n")
        exit(1)

class MUPCenter(Scene):

    def enter(self):
        print(dedent("""
              Dugo smo sumnjali na veliko pranje novca u vrhu vlade.
              U MUP-u smo pokrenuli istragu kojom bismo utvrdili nase hipoteze.
              Kako bismo uspijeli utvrditi išta, poslali smo agente da prisluskuju
              Plenkovica i ministre. Nakon mjesec dana utvrdili smo sumnjive kretnje
              clanova vlade te njihove kontakte sa bivsim vlasnikom Agrokora
              Ivicom Todoricem. Naime Ivicu smo isto istrazivali te utvrdili velike
              organizirane pothvate korupcije te pranja novca.
              \n\n
              O dubljoj istrazi cemo sada odluciti zbog ove informacije.
              Primili smo prijetece pismo sa anonimne adrese.
              Ovo je to pismo: {}\n\n
              \r{}""".format(filename, pismo.read())))
        print("\n\nSto cemo sada, ovo je opasno.\nSjeti se samo teroristickog napada na Markov Trg.")
        print("Pismo je zanimljivo, rukopis te podsjeca na jedno koje si dobio iz Markova Trga.\nMozda je od premijerove tajnice...")
        print("Nije to dobro; Ali ok, na tebi je, ipak si ti šef MUP-a...")

        action = input("[CONTINUE?]> ")

        if action == "Da":
            print("\n\nTvoj odabir je donio euforiju u postaji.")
            print("Ljudi su odmah prionuli na posao te odlucili nastaviti sa radom.")
            print("Utvrdili su da se rukopis 70% poklapa sa onim koji si dobio prije dvije godine.")
            print("Ovim podatkom si motiviran da napravis premet u tajnicinoj kuci")
            print("\n\n")

            return 'Suspect_House'

        elif action == "Ne":
            print("\n\nOdlucio si da neces ici u daljnju istragu.")
            print("Tvoji ljudi su poceli bacati sale o tebi kada bi prosao pored njih.")
            print("Njima si ispao kukavica i vise te ne mogu pogledati u oci a da se ne nasmiju.")
            print("Dva tjedna poslije si krenuo na posao kao obicno")
            print("Kada si upalio motor, primijetio si papir sa istim rukopisom kao pismo.")
            print("Samo sto je ovaj puta pisala samo jedna rijec.")
            print("\nBUM!\n")

            return 'Death'

        else:
            print("\nNIJE IZVRSENO!\n")
            return 'MUP_Center'


class SuspectHouse(Scene):

    def enter(self):
        print("\n\nDolaskom na adresu odmah vidiš nešto jako sumnjivo.")
        print("Ti i tvoji kolege ste blenuli kda ste vidjeli njenu kucu.")
        print("Bolje ovu nekretninu nazvati vilom.")
        print("Odakle tajnici toliko novca za ovakvu trokatnicu sa tri bazena.")
        print("Jasno je da je ovo ukradeni novac.")
        print("Usli ste u kucu te ste krenuli s premetom.")
        print("Tvoji kolege su nasli dvije vrece sa 3 000 000 kuna.")
        print("Dok su ti donijeli vrece ti si pretrazivao poruke i datoteke na njenom racunalu.")
        print("Nisi nista zanimljivo nasao osim razgovora sa Petekom i Kuscevicem.")
        print("Tamo su pricali o nekretninama...")
        print("Zaci Kuscevic je njoj sagradio vilu, ali nista od njega. On je u zatvoru od pretprosle godine.")
        print("Ali si nasao mail koji salje Plenkovicu.")
        print(f"Pise samo neki cetveroznamenkasti broj : \n\r{trezor_kod}")
        print("Dobro to, ali ove pare i vile su jako sumnjive.")
        print("Gdje cemo sada sefe?")

        while True:
            gdje = input("[GDJE?]> ")

            if gdje == "Porezna Uprava":
                print("\nDobro, ima logike.")
                print("Krecemo u poreznu upravu\n\n")
                return 'Porezna_Uprava'
            elif gdje == "Drzavna Banka":
                print("\nSefe, imam jedan prijedlog")
                print("bil bi bilo pametno da odemo u Poreznu Upravu provjeriti njene transakcije?")
                print("Tamo bismo mogli izvuci jos neke informacije.\n\n")
            else:
                print("NIJE IZVRSENO\n\n")



class MarkovTrg(Scene):

    def enter(self):
        print("Pozvali ste specijalnu policiju te s njom provalili na sastanak Vlade.")
        print("Nju ste silom izveli van na ulicu.")
        print("Zavezali joj lisicne te bacili u kombi.")
        print("U to vrijeme Vlada je bila sokirana, odveli su ju na ispitivanje.")
        print("Vidio si cudnu torbu unutra, izgleda kao da su poluge unutra.")
        print("Cudno je i sumnjivo, ali moras do Ivonine kuce da ju pretrazis ponovno.")
        print("Tocnije njenu supu...")
        print("Idemo...\n\n")

        return 'Suspect_Workshop'



class SuspectFight(Scene):

    def enter(self):
        print("Na sudu kreces donositi argumente kojima ces zatvoriti cijelu Vladu.")
        argumenti = [
            "Zlato u banci",
            "Na mjestu pljacke",
            "Razgovori sa Ivicom Todoricem",
            "Zice i nacrti u Ivoninoj supi",
            "Transakcije na Ivoninom racunu",
            "Vila s bazenom",
            "Prijetece pismo",
            "Razgovori sa Petekom i Kuscevicem"
        ]

        while len(argumenti) > 0:
            pokusaji = len(argumenti) + 3

            if pokusaji > 0:

                argument = input("[ARGUMENT]> ")

                if argument in argumenti:
                    print("Bravo, to je tocno...")
                    argumenti.remove(argument)
                    print(f"Jos {len(argumenti)} argumenata ostalo.")
                    pokusaji -= 1
                else:
                    print("To nije dobar argument")
                    print(f"Imas jos {pokusaji} pokusaja.")
                    pokusaji -= 1
            else:
                print("Nisi naveo sve argumente.")
                print("Izasli ste van. Vlada je nazvala nekog...")
                print("Nakon 5 sekundi snajper te ubio.")

                return 'Death'

        if len(argumenti) == 0:
            print("Bravo, uhitili smo citavi vrh Hrvatske.")
            print("Zavrsio si na svim stranicama svijeta.")
            print("Svaka cast...")

            return 'Finished'



class SuspectWorkshop(Scene):
    def enter(self):
        print("Usao si u supu i nasao nesto zanimljivo.")
        print("Vidio si zice i nitrogen.")
        print("Pored su bili srafcigeri i matice te staklo-plastika.")
        print("Na zidu je zalijepljen nacrt neke zgrade...")
        print("U medjuvremenu si dobio nalaze ispitivanja.")
        print(f"Evo poruke s filom {filename3}:")
        print(nalazi.read())
        print("\n\n")
        print("Dobro, dosta je za danas. Idemo spavati...\nBio je naporan vikend\n")
        spavati = input("[SPAVATI]> ")

        if spavati == "Da":
            print("Pametno, umro bi u igri da nisi...")
            print("Sutra idemo ispitati poslodavce u banci.")
            print("Laku noc...\n\n\n")
            print("Yaaawn, Ustao si i ides napraviti dorucak.")
            print("Prije dorucka si dobio poziv da je u tijeku pljacka banke te da je sve eksplodiralo.")
            print("Hitno te trebaju.")
            print("Hoces li pojesti dorucak ili krenuti tamo.")

            while True:
                idi = input("[PROMISLI]> ")

                if idi == "Pojedi dorucak":
                    print("\nOdabrao si da pojedes dorucak.")
                    print("Kada si zavrsio, pljacka je bila gotova.")
                    print("Ispred balkona doletio je helikopter s Vladinim grbom na sebi...")
                    print("Ispalili su RPG te si umro na licu mjesta.\n\n")
                    return 'Death'

                elif idi == "Kreni tamo":
                    print("Krenuo si u banku...\n\n")
                    return 'Escape_Tunnel'
                else:
                    print("NIJE IZVRSENO!!")

        else:
            print("Umro si od nesanice...\n")
            return 'Death'


class PoreznaUprava(Scene):

    def enter(self):


        print("Ulazis sa svojim kolegama u Upravu.")
        print("Dosao si na salter te zelis pristupiti tajnicinim transakcijama")
        print("u zadnje tri godine.")
        print("Samo trebas pitati gospodju na salteru")
        print("Gospodja zna da ste glavni iz MUP-a")
        print("Ime tajnice je Ivona Ferencic.\n\n")

        while True:
            pitanje = input("[PITAJ]> ")

            if pitanje == "Molim transakcije Ivone Ferencic":
                print("Gospodja ti je razvrstala transakcije\n")
                print("Tako sto ti je dala najvece transakcije")
                print("te posiljatelje.")
                print("Isprintala ih je sve te dala ti papir: ")
                print(transakcije.read())
                print("Zahvali se gospodji:")
                zahvali = input("[ZAHVALI]> ")
                print("\nNema na cemu!")
                print("\nOvo je jako strasno.")
                print("Koliki su samo iznosi na papiru.")
                print("A, gle posiljatelje, o moj bozzzeee.")
                print("Idemo hitno u Drzavnu Banku")

                return 'Drzavna_Banka'

            else:
                print("Molim, nema sanse majmune jedan...")
                print("Mrs van dok ne nazovem osiguranjeeee.")

                return 'Death'


class DrzavnaBanka(Scene):

    def enter(self):
        print("Ulazis unutra te se nadjes na salteru.")
        print("Tamo pokazes nalog za pregled Ivoninog trezora.")
        print("Usao si u trezor, ali trazi te da upises potvrdni kod.")
        print("Ako pogrijesis 3 puta pali se alarm i zakljucava se sve do prepoznavanja lica i glasa.")
        print("Unesi kod za otvaranje sefa!")
        pokusaji = 3
        while pokusaji > 0:
            kod = input("[KOD]> ")
            if kod == trezor_kod:
                print("Upisao si tocan kod i usao si u sef.")
                print("Nasao si 300 poluga zlata svaka 50kg. 48 karatno zlato!?")
                print("Odakle ovo u njenom trezoru.")
                print("Ovo je dovoljno da privedemo nju za ispitivanje.")
                print("Idemo na Markov Trg.\n")
                return 'Markov_Trg'
            else:
                print("BZZZEEEEEDDD!")
                pokusaji -= 1

        print("Nema vise pokusaja!!!\n\n")
        print("Alarm se ukljucio i dosla je vojska koja te ubila na licu mjesta.\n")
        return 'Death'


class Finished(Scene):

    def enter(self):
        print("Izradio: Dario Adamovic\n\n")
        print("Datum zavrsetka: 7.12.2020 - 11:05")
        print("Linija koda: 363 (malo)")
        print("Trajanje izrade: 7 dana, 8 sati.")
        print("Hvala na igrranju!")
        print("\n\n\tGAME WON!!")
        exit(0)


class EscapeTunnel(Scene):

    def enter(self):
        print("Ulaskom u banku krenuo si premo glavnom trezoru...")
        print("Unutra je ogromna rupa od eksplozije.")
        print("Stigli ste na vrijeme te priveli Ivonu Ferencic, ministra Corica, Ivicu Todorica, ministra Kujundcica, i ANDREJA PLENKOVICA")
        print("Krenuo si na ispitivanje...\n\n")

        return 'Suspect_Fight'


class Map(object):

    scenes = {
        'MUP_Center': MUPCenter(),
        'Suspect_Fight': SuspectFight(),
        'Porezna_Uprava': PoreznaUprava(),
        'Escape_Tunnel': EscapeTunnel(),
        'Finished': Finished(),
        'Markov_Trg': MarkovTrg(),
        'Suspect_Workshop': SuspectWorkshop(),
        'Suspect_House': SuspectHouse(),
        'Death': Death(),
        'Drzavna_Banka': DrzavnaBanka()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene


    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val


    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('MUP_Center')
a_game = Engine(a_map)
a_game.play()

pismo.close()
transakcije.close()
nalazi.close()
