# Rayanne, Alex, Nathan

import locale
import fltica
from random import randint

# Variable gérant tous les paramètres principaux
settings = {'sizex': 800, 'sizey': 600,
            'lang': 'eng' if "English" in locale.setlocale(locale.LC_ALL, '') else 'jp' if "Japanese" in locale.setlocale(locale.LC_ALL, '') else 'fr',
            'maxMatch': 3, 'misere': False, 'theme': 'Minecraft', 'updateValue': 1, 'oldScreen': (0, 0), 'gameMode':'PvP',
            'lines':[15]}

# Dictionnaire contenant les textes dans chaques langues
text = {'eng': {
    'Play': 'Play',
    'Settings': 'Options',
    'Quit': 'Quit',
    'missingFont': 'Please install the provided font for a better experience.',
    'Theme': 'Theme',
    'Lang': 'Language',
    'Fullscreen': 'Fullscreen',
    'Resolution': 'Apply resolution',
    'FullscreenEnabled': 'Fullscreen mode enabled',
    'ScreenSizeError': 'Bad resolution',
    'Back': 'Back',
    'Ready': 'Ready',
    'Player': 'player',
    'Mode':'Game mode',
    'Misere':'Misery mode',
    'Enabled':'Enabled',
    'Disabled':'Disabled',
    'Marienbad':'Configure Marienbad',
    'Save':'Save',
    'Line':'Line ',
    'LineIvalid':'Invalid value at line ',
    'NoValue':'No value',
    'Objects':'Objects:',
    'MaxDraw':'Draw:',
    'Wins':' wins!',
    'VictoryFor':'Victory for ',
    'LMB':'Left click to restart',
    'RMB':'Right click for title screen'
    },
    'fr': {
    'Play': 'Jouer',
    'Settings': 'Options',
    'Quit': 'Quitter',
    'missingFont': 'Veuillez installer la police fournie pour une meilleure expérience.',
    'Theme': 'Thème',
    'Lang': 'Langue',
    'Fullscreen': 'Plein écran',
    'Resolution': 'Appliquer la résolution',
    'FullscreenEnabled': 'Mode plein écran activé',
    'ScreenSizeError': 'Mauvaise résolution',
    'Back': 'Retour',
    'Ready': 'Prêt',
    'Player': 'Joueur',
    'Mode':'Mode de jeu',
    'Misere':'Mode misère',
    'Enabled':'Activé',
    'Disabled':'Désactivé',
    'Marienbad':'Configurer Marienbad',
    'Save':'Sauvegarder',
    'Line':'Ligne ',
    'LineIvalid':'Valeur invalide en ligne ',
    'NoValue':'Aucune valeur indiqué',
    'Objects':'Objets:',
    'MaxDraw':'Tirages:',
    'Wins':' a gagné !',
    'VictoryFor':'Victoires pour ',
    'LMB':'Clique gauche pour recommencer',
    'RMB':'Clique droit pour écran titre'
    },
    'jp': {
    'Play': 'プレー',
    'Settings': 'セッティング',
    'Quit': 'ゲームをやめる',
    'missingFont': 'より良い体験のために、提供されたフォントをインストールしてください。',
    'Theme': 'テーマ',
    'Lang': '言語',
    'Fullscreen': '全画面表示',
    'Resolution': '画面解像度を適用する',
    'FullscreenEnabled': 'フルスクリーンモードが有効',
    'ScreenSizeError': '画面の解像度が悪い',
    'Back': 'バック',
    'Ready': '準備',
    'Player': 'プレーヤー',
    'Mode':'ゲームモード',
    'Misere':'惨めさモード',
    'Enabled':'オン',
    'Disabled':'オフ',
    'Marienbad':'マリエンバードの設定',
    'Save':'セーブ',
    'Line':'ライン ',
    'LineIvalid':' 行目に無効な値がある',
    'NoValue':'値が表示されない',
    'Objects':'オブジェクト:',
    'MaxDraw':'最大ドロー:',
    'Wins':' が勝った! !',
    'VictoryFor':'勝利の',
    'LMB':'左クリックで再スタート',
    'RMB':'右クリックでタイトル画面'
    }
}

# Merci à Nelson pour l'idée du thème Minecraft
theme = {'Minecraft': {
    'background': 'images/Minecraft/backMC.png',
    'font': 'Helvetica',
    'fontColor': 'white',
    'match1': 'images/Minecraft/redstone_torch.png',
    'match2': 'images/Minecraft/redstone_torch_off.png',
    'buttonBg': 'images/Minecraft/buttonBg.png',
    'buttonBgOn': 'images/Minecraft/buttonBgOn.png',
    'buttonHoverColor': '#ffff00',
    'buttonPosx': settings['sizex']//2,
    'buttonAnc': 'center',
    'gameName': 'images/Minecraft/gameName.png'
    },
        'Allumette': {
    'background': 'images/Allumette/backAl.jpg',
    'font': 'Helvetica',
    'fontColor': 'black',
    'match1': 'images/Allumette/allumette.png',
    'match2': 'images/Allumette/allumette_off.png',
    'buttonBg': '',
    'buttonBgOn': '',
    'buttonHoverColor': 'Red',
    'buttonPosx': 5,
    'buttonAnc': 'w',
    'gameName': 'images/Allumette/gameName.png'
    }
}


class Player:
    """
    Cette classe contient toute les variables utile et propre aux joueurs.
    Elle demande un nom (le nom du joueur) et une couleur (compatible tkinter).
    """
    def __init__(self, name, color):
        self.name = name
        self.matchDrawed = 0
        self.victory = 0
        self.nextPlay = False
        self.color = color
        self.numberSelected = 0
        self.selectedLine = None


players = [None, None]


def loadSave():
    """
    Idée de sauvegade abandonnée.
    """
    pass


def writeSave():
    """
    Idée de sauvegade abandonnée.
    """
    pass


def getMltp():
    """
    Calcul un multiplieur pour les images en fonction de la taille de la fenêtre, du nombre de lignes (mode Marienbad)
    et du nombre d'objet et renvoit le plus petit des deux (ce qui permet de n'avoir aucun objet qui sort de l'écran).
    """
    objNb = max(settings['lines'])
    tailleMaxY = (settings['sizey']-70)/(imagey*len(settings['lines']))
    tailleMaxX = (settings['sizex'])/objNb/imagex
    return min(tailleMaxY, tailleMaxX)

def selectMatch(listMatch, player, sizeMp):
    """
    Fonction appelé après un clique. Permet de savoir où est la souris par rapport à tous les éléments présent dans listMatch.
    Si une allumette est présente et que le coup est valide, change l'image et ajoute un coup au joueur.
    Cette fonction définie aussi la ligne jouée.
    """
    for j in range(len(settings['lines'])):
        if player.selectedLine == None or player.selectedLine == j:
            if (50+j*(imagey*sizeMp) <= fltica.ordonnee_souris() <= 50+imagey*sizeMp+j*((imagey)*sizeMp)) and (player.numberSelected < settings['maxMatch']):
                for i in range(len(listMatch)):
                    if (len(listMatch[i]) == 2) and (listMatch[i][1][0]*sizeMp <= fltica.abscisse_souris() <= (listMatch[i][1][0]+imagex)*sizeMp) and (50+listMatch[i][1][1]*sizeMp <= fltica.ordonnee_souris() <= 50+(listMatch[i][1][1]+imagey)*sizeMp):
                        fltica.efface(listMatch[i][0])
                        listMatch[i][0] = fltica.image(int(listMatch[i][1][0]*sizeMp), int(50+listMatch[i][1][1]*sizeMp), theme[settings['theme']]['match1'], int(imagex*sizeMp), int(imagey*sizeMp), ancrage='nw')
                        listMatch[i].append(0)
                        player.numberSelected += 1
                        player.selectedLine = j


def unselectMatch(listMatch, player, sizeMp):
    """
    Similaire à la fonction "selectMatch" mais permet de désélectionner l'allumette.
    """
    for j in range(len(settings['lines'])):
        if (50+j*(imagey*sizeMp) <= fltica.ordonnee_souris() <= 50+imagey*sizeMp+j*((imagey)*sizeMp)) and (player.numberSelected > 0):
            for i in range(len(listMatch)):
                if (listMatch[i][1][0]*sizeMp <= fltica.abscisse_souris() <= (listMatch[i][1][0]+imagex)*sizeMp) and (50+listMatch[i][1][1]*sizeMp <= fltica.ordonnee_souris() <= 50+(listMatch[i][1][1]+imagey)*sizeMp):
                    if len(listMatch[i]) == 3:
                        fltica.efface(listMatch[i].pop())
                        fltica.efface(listMatch[i].pop(0))
                        listMatch[i].insert(0, fltica.image(int(listMatch[i][0][0]*sizeMp), int(50+listMatch[i][0][1]*sizeMp), theme[settings['theme']]['match2'], int(imagex*sizeMp), int(imagey*sizeMp), ancrage='nw'))
                        player.numberSelected -= 1
                        if player.numberSelected == 0:
                            player.selectedLine = None


def drawMatch(listMatch, playerList):
    """
    Retire toutes les allummettes sélectionnées par les joueurs.
    """
    if playerList[0].numberSelected or playerList[1].numberSelected:
        toPop = []
        for i in range(len(listMatch)):
            if len(listMatch[i]) == 3:
                fltica.efface(listMatch[i][0])
                toPop.append(i)
        for i in toPop[::-1]:
            listMatch.pop(i)
        fltica.efface('name')
        if settings['theme'] == 'Minecraft':
            fltica.animated_image(settings['sizex']//2, settings['sizey']//2, settings['sizex'], settings['sizey'], 'images/explosion.gif')
            fltica.jouerSon('sounds/explode'+str(randint(1, 4))+'.mp3')
        if playerList[0].nextPlay:
            fltica.texte(10, 10, playerList[1].name, tag='name', couleur=playerList[1].color, police=theme[settings['theme']]['font'])
            playerList[0].matchDrawed += len(toPop)
            playerList[0].nextPlay = False
            playerList[0].numberSelected = 0
            playerList[0].selectedLine = None
            playerList[1].nextPlay = True
        else:
            fltica.texte(10, 10, playerList[0].name, tag='name', couleur=playerList[0].color, police=theme[settings['theme']]['font'])
            playerList[1].matchDrawed += len(toPop)
            playerList[1].nextPlay = False
            playerList[1].numberSelected = 0
            playerList[1].selectedLine = None
            playerList[0].nextPlay = True


def eraseSetTheme():
    """
    Vide complètement la fenêtre puis remet le background du thème
    """
    fltica.efface_tout()
    fltica.image(0, 0, theme[settings['theme']]['background'], settings['sizex'], settings['sizey'], 'nw')

def setMatches(listMatch):
    """
    Rempli la liste d'allumettes et affiche chacune des allumettes.
    """
    sizeMultiplier = getMltp()
    eraseSetTheme()
    for j in range(len(settings['lines'])):
        for i in range(settings['lines'][j]):
            listMatch.append([fltica.image(int((imagex*i)*sizeMultiplier), 50+j*(imagey*sizeMultiplier), theme[settings['theme']]['match2'], int(imagex*sizeMultiplier), int(imagey*sizeMultiplier), ancrage='nw'), [imagex*i, imagey*j]])
      

def gestionInput(player1, player2, listMatch):
    """
    Dans le mode PvP, gère les entrées des deux joueurs.
    """
    fltica.texte(10, 10, player1.name if player1.nextPlay else player2.name, tag='name', couleur=player1.color if player1.nextPlay else player2.color, police=theme[settings['theme']]['font'])
    sizeMultiplier = getMltp()
    while len(listMatch) > 0:
        ev = fltica.donne_ev()
        tev = fltica.type_ev(ev)
        
        if tev == 'ClicGauche':
            selectMatch(listMatch, player1, sizeMultiplier) if player1.nextPlay else selectMatch(listMatch, player2, sizeMultiplier)
        if tev == 'ClicDroit':
            unselectMatch(listMatch, player1, sizeMultiplier) if player1.nextPlay else unselectMatch(listMatch, player2, sizeMultiplier)
        if tev == 'Touche':
            if fltica.touche(ev) == 'space':
                drawMatch(listMatch, players)
        fltica.mise_a_jour()
        if tev == 'Quitte':
            exit()


def easyBot(player1, player2, listMatch):
    """
    Fais jouer aléatoirement l'ordinateur et gère aussi les entrées du joueur.
    """
    fltica.texte(10, 10, player1.name, tag='name', couleur=player1.color if player1.nextPlay else player2.color, police=theme[settings['theme']]['font'])
    sizeMultiplier = getMltp()
    while len(listMatch) > 0:
        fltica.mise_a_jour()
        if player2.nextPlay:
            toPop = []
            end = False
            i = 0
            firstMatch = randint(0, len(listMatch)-1)
            nbMatch = randint(1, settings['maxMatch'])
            line = listMatch[firstMatch][1][1]
            while len(toPop) < nbMatch and not(end):
                if listMatch[i][1][1] == line:
                    toPop.append(i)
                i += 1
                if i >= len(listMatch):
                    end = True
            for i in range(len(toPop)):
                fltica.efface(listMatch[toPop[i]][0])
            for i in toPop[::-1]:
                listMatch.pop(i)
            player2.nextPlay = False
            player1.nextPlay = True
        else:
            fltica.efface('name')
            fltica.texte(10, 10, player1.name, tag='name', couleur=player1.color if player1.nextPlay else player2.color, police=theme[settings['theme']]['font'])
            while player1.nextPlay:
                ev = fltica.donne_ev()
                tev = fltica.type_ev(ev)
                if tev == 'ClicGauche':
                    selectMatch(listMatch, player1, sizeMultiplier) if player1.nextPlay else selectMatch(listMatch, player2, sizeMultiplier)
                if tev == 'ClicDroit':
                    unselectMatch(listMatch, player1, sizeMultiplier) if player1.nextPlay else unselectMatch(listMatch, player2, sizeMultiplier)
                if tev == 'Touche':
                    if fltica.touche(ev) == 'space':
                        drawMatch(listMatch, [player1, player2])
                fltica.mise_a_jour()
                if tev == 'Quitte':
                    exit()




def game():
    """
    Fonction principale. Créée les variables nécessaires et gère l'affichage des victoires.
    """
    global imagex, imagey
    imagex, imagey = fltica.Image.open(theme[settings['theme']]['match1']).size
    listMatch = []
    setMatches(listMatch)
    players[1].nextPlay = True
    if settings['gameMode'] == 'easy':
        easyBot(players[0], players[1], listMatch)
    else:
        gestionInput(players[0], players[1], listMatch)
    eraseSetTheme()
    if settings['theme'] == 'Minecraft':
        fltica.jouerSon('sounds/hit'+str(randint(1, 3))+'.mp3')
    if not(settings['misere']):
        if players[0].nextPlay:
            players[0].nextPlay = False
            players[1].nextPlay = True
        else:
            players[0].nextPlay = True
            players[1].nextPlay = False
    if players[0].nextPlay:
        players[0].victory += 1
    else:
        players[1].victory += 1
    fltica.texte(settings['sizex']//2, settings['sizey']//4, players[0].name + text[settings['lang']]['Wins'] if players[0].nextPlay else players[1].name + text[settings['lang']]['Wins'], couleur=players[0].color if players[0].nextPlay else players[1].color, ancrage="center", police=theme[settings['theme']]['font'])
    fltica.texte(settings['sizex']//2, settings['sizey']//2, text[settings['lang']]['VictoryFor'] + players[0].name + ' : ' + str(players[0].victory), couleur=players[0].color, ancrage="center", police=theme[settings['theme']]['font'])
    fltica.texte(settings['sizex']//2, settings['sizey']//1.75, text[settings['lang']]['VictoryFor'] + players[1].name + ' : ' + str(players[1].victory), couleur=players[1].color, ancrage="center", police=theme[settings['theme']]['font'])
    fltica.texte(settings['sizex']//2, settings['sizey']//1.5, text[settings['lang']]['LMB'], ancrage="center", police=theme[settings['theme']]['font'], couleur=theme[settings['theme']]['fontColor'])
    fltica.texte(settings['sizex']//2, settings['sizey']//1.25, text[settings['lang']]['RMB'], ancrage="center", police=theme[settings['theme']]['font'], couleur=theme[settings['theme']]['fontColor'])
    if not(settings['misere']):
        if players[0].nextPlay:
            players[0].nextPlay = False
            players[1].nextPlay = True
        else:
            players[0].nextPlay = True
            players[1].nextPlay = False
    fltica.mise_a_jour()
    while True:
        ev = fltica.donne_ev()
        tev = fltica.type_ev(ev)
        fltica.mise_a_jour()
        if tev == 'ClicDroit':
            settings['updateValue'] = 0
            eraseSetTheme()
            fltica.attente(0.1)
            return
        if tev == 'ClicGauche':
            eraseSetTheme()
            break
    game()
