# Rayanne, Alex, Nathan

from fltica import abscisse_souris, ordonnee_souris
from gameMain import game, settings, fltica, theme, text, eraseSetTheme, Player, players, loadSave, writeSave

# Liste couleurs possibles
colors = ['white', 'red', 'blue', 'green', 'maroon', 'pink', 'cyan', 'tomato', 'blue violet', 'yellow', 'black']


def showMainMenu():
    """
    Affiche l'écran titre et renvoie la liste de boutons de cet écran titre.
    """
    fltica.mise_a_jour()
    fltica.image(settings['sizex']/2, settings['sizey']/8, theme[settings['theme']]['gameName'])
    buttonList = []
    buttonList.append(fltica.Button(theme[settings['theme']]['buttonPosx'], settings['sizey']/1.6, text[settings['lang']]['Quit'], quit, color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage=theme[settings['theme']]['buttonAnc'], size=18, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    buttonList.append(fltica.Button(theme[settings['theme']]['buttonPosx'], settings['sizey']/2.0, text[settings['lang']]['Settings'], settingsMenu, color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage=theme[settings['theme']]['buttonAnc'], size=18, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    buttonList.append(fltica.Button(theme[settings['theme']]['buttonPosx'], settings['sizey']/2.65, text[settings['lang']]['Play'], launchGame, color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage=theme[settings['theme']]['buttonAnc'], size=18, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    if theme[settings['theme']]['buttonBg']:
        for button in buttonList:
            button.setBgImg(theme[settings['theme']]['buttonBg'], theme[settings['theme']]['buttonBgOn'], 300, 600, 60)
    return buttonList


def setReady(e, widgetNb, playerNb, colorId):
    """
    Marque un joueur comme prêt à jouer.
    """
    fltica.efface(widgetNb)
    fltica.efface('player'+str(playerNb))
    if playerNb == 1:
        fltica.texte(settings['sizex']/3.33, (settings['sizey']//3.33)+120, e.get(), colors[colorId[0]], 'center', theme[settings['theme']]['font'], 14)
        players[0] = Player(e.get(), colors[colorId[0]])
        players[0].nextPlay = True
    elif playerNb == 2:
        fltica.texte(int(settings['sizex']-settings['sizex']/3.33), (settings['sizey']//3.33)+120, e.get(), colors[colorId[1]], 'center', theme[settings['theme']]['font'], 14)
        players[1] = Player(e.get(), colors[colorId[1]])
    return 1


def changeColorHandler(tev, colorId):
    """
    Gère le changement de couleurs des joueurs en fonction de la liste "colors".
    """
    if (settings['sizey']//3.33 + 100) <= ordonnee_souris() <= (settings['sizey']//3.33 + 140):
        if ((settings['sizex']/3.33) - 60 <= abscisse_souris() <= (settings['sizex']/3.33) + 60):
            if tev == 'ClicGauche' and not(players[0]):
                if colorId[0] < 10:
                    colorId[0] += 1
                else:
                    colorId[0] = 0
                fltica.efface('player1')
                fltica.texte(settings['sizex']/3.33, (settings['sizey']//3.33)+120, text[settings['lang']]['Player']+' 1', colors[colorId[0]], 'center', theme[settings['theme']]['font'], 14, 'player1')
            elif tev == 'ClicDroit' and not(players[0]):
                if colorId[0] > 0:
                    colorId[0] -= 1
                else:
                    colorId[0] = 10
                fltica.efface('player1')
                fltica.texte(settings['sizex']/3.33, (settings['sizey']//3.33)+120, text[settings['lang']]['Player']+' 1', colors[colorId[0]], 'center', theme[settings['theme']]['font'], 14, 'player1')
        elif (int(settings['sizex']-settings['sizex']/3.33) - 60 <= abscisse_souris() <= int(settings['sizex']-settings['sizex']/3.33) + 60):
            if tev == 'ClicGauche' and not(players[1]):
                if colorId[1] < 10:
                    colorId[1] += 1
                else:
                    colorId[1] = 0
                fltica.efface('player2')
                fltica.texte(int(settings['sizex']-settings['sizex']/3.33), (settings['sizey']//3.33)+120, text[settings['lang']]['Player']+' 2', colors[colorId[1]], 'center', theme[settings['theme']]['font'], 14, 'player2')
            elif tev == 'ClicDroit' and not(players[1]):
                if colorId[1] > 0:
                    colorId[1] -= 1
                else:
                    colorId[1] = 10
                fltica.efface('player2')
                fltica.texte(int(settings['sizex']-settings['sizex']/3.33), (settings['sizey']//3.33)+120, text[settings['lang']]['Player']+' 2', colors[colorId[1]], 'center', theme[settings['theme']]['font'], 14, 'player2')


def launchGame():
    """
    Gère l'affichage et la manipulation de l'écran de sélection de noms.
    """
    eraseSetTheme()
    colorId = [1, 2]
    e1 = fltica.tk.Entry(fltica.__canevas.root)
    e1nb = fltica.__canevas.canvas.create_window(settings['sizex']/3.33, (settings['sizey']//3.33)+80, window=e1)
    e2 = fltica.tk.Entry(fltica.__canevas.root)
    e2nb = fltica.__canevas.canvas.create_window(int(settings['sizex']-settings['sizex']/3.33), (settings['sizey']//3.33)+80, window=e2)
    buttonList = []
    buttonList.append(fltica.Button(int(settings['sizex']/3.33), settings['sizey']//3, text[settings['lang']]['Ready'], lambda: setReady(e1, e1nb, 1, colorId), color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage='center', size=14, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    buttonList.append(fltica.Button(int(settings['sizex']-settings['sizex']/3.33), settings['sizey']//3, text[settings['lang']]['Ready'], lambda: setReady(e2, e2nb, 2, colorId), color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage='center', size=14, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    fltica.texte(settings['sizex']/3.33, (settings['sizey']//3.33)+120, text[settings['lang']]['Player']+' 1', colors[colorId[0]], 'center', theme[settings['theme']]['font'], 14, 'player1')
    fltica.texte(int(settings['sizex']-settings['sizex']/3.33), (settings['sizey']//3.33)+120, text[settings['lang']]['Player']+' 2', colors[colorId[1]], 'center', theme[settings['theme']]['font'], 14, 'player2')
    if theme[settings['theme']]['buttonBg']:
        for button in buttonList:
            button.setBgImg(theme[settings['theme']]['buttonBg'], theme[settings['theme']]['buttonBgOn'], 150, 300, 40)
    while not(players[0] and players[1]):
        fltica.mise_a_jour()
        ev = fltica.donne_ev()
        tev = fltica.type_ev(ev)
        for button in buttonList:
            tev = button.update(tev)
        changeColorHandler(tev, colorId)
        if tev == 'Quitte':
            exit()
        elif tev == 'Touche' and fltica.touche_pressee('Escape'):
            fltica.mise_a_jour()
            eraseSetTheme()
            settings['updateValue'] = 2
            break
    if settings['updateValue'] == 1:
        fltica.__canevas.canvas.focus_force()
        game()


def updateMenu(buttonList):
    """
    Met à jour l'écran titre et gère les retours à ce dernier.
    """
    while settings['updateValue'] == 1:
        ev = fltica.donne_ev()
        tev = fltica.type_ev(ev)
        fltica.mise_a_jour()
        for elem in buttonList:
            elem.update(tev)
        if tev == 'Touche' or tev == 'Quitte':
            if fltica.touche_pressee('Escape') or tev == 'Quitte':
                exit()
    while settings['updateValue'] == 2:
        settings['updateValue'] = 1
        settingsMenu()
    settings['updateValue'] = 1


def setWindowSettings():
    """
    Défini les paramètres de la fenêtre tel que le nom ou les polices disponibles.
    """
    global e1, e2, e3
    # fltica.__canevas.root.iconbitmap('images/cigle-Eiffel.ico') # Windows only ?
    fltica.__canevas.root.resizable(False, False)
    fltica.__canevas.root.title('Jeux de Nim')
    if 'Minecraftia' in fltica.tk.font.families():
        theme['Minecraft']['font'] = 'Minecraftia'
    else:
        print(text[settings['lang']]['missingFont'])
    fltica.image(0, 0, theme[settings['theme']]['background'], settings['sizex'], settings['sizey'], 'nw')
    fltica.texte(0, 0, 'ver alpha release', '#505050', police=theme[settings['theme']]['font'], taille=15)


def setTheme():
    """
    Gère la gestion de changement de thème.
    """
    if settings['theme'] == 'Minecraft':
        settings['theme'] = 'Allumette'
    else:
        settings['theme'] = 'Minecraft'
    eraseSetTheme()
    settings['updateValue'] = 2


def setLang():
    """
    Gère la gestion de changement de langue.
    """
    if settings['lang'] == 'jp':
        settings['lang'] = 'fr'
    elif settings['lang'] == 'fr':
        settings['lang'] = 'eng'
    else:
        settings['lang'] = 'jp'
    eraseSetTheme()
    settings['updateValue'] = 2


def setFullscreen():
    """
    Récupère la taille de l'écran pour afficher la fenêtre en plein-écran.
    Stock dans settings['oldScreen'] l'ancienne taille d'écran pour pouvoir revenir au mode fenêtré.
    """
    fltica.attente(0.1)
    try:
        fltica.__canevas.canvas.after_cancel(fltica.after_id)
    except AttributeError:
        pass
    if not(fltica.__canevas.root.attributes('-fullscreen')):
        settings['oldScreen'] = settings['sizex'], settings['sizey']
        settings['sizex'] = fltica.__canevas.root.winfo_screenwidth()
        settings['sizey'] = fltica.__canevas.root.winfo_screenheight()
        theme['Minecraft']['buttonPosx'] = settings['sizex']//2
        fltica.ferme_fenetre()
        fltica.cree_fenetre(settings['sizex'], settings['sizey'])
        fltica.__canevas.root.attributes('-fullscreen', True)
        fltica.__canevas.canvas.focus_force()
    else:
        settings['sizex'], settings['sizey'] = settings['oldScreen']
        theme['Minecraft']['buttonPosx'] = settings['sizex']//2
        fltica.ferme_fenetre()
        fltica.cree_fenetre(settings['sizex'], settings['sizey'])
        fltica.__canevas.root.attributes('-fullscreen', False)
        fltica.__canevas.canvas.focus_force()
    settings['updateValue'] = 2
    setWindowSettings()


def changeRes():
    """
    Vérifie l'entry de la résolution et ferme puis rouvre une nouvelle fenêtre avec les nouvelles dimensions.
    """
    if fltica.__canevas.root.attributes('-fullscreen'):
        return
    res = e1.get()
    x = ''
    y = ''
    nb = 0
    for nb, i in enumerate(res):
        if i.isnumeric():
            x = x+i
        elif len(x) > 0:
            break
    for i in res[nb::]:
        if i.isnumeric():
            y = y+i
        elif len(y) > 0:
            break
    if x and y:
        x = int(x)
        y = int(y)
        if ((x >= 600 and x <= fltica.__canevas.root.winfo_screenwidth()+100) and (y >= 500 and y <= fltica.__canevas.root.winfo_screenwidth()+100)):
            settings['sizex'], settings['sizey'] = x, y
            theme['Minecraft']['buttonPosx'] = settings['sizex']//2
            fltica.ferme_fenetre()
            fltica.cree_fenetre(settings['sizex'], settings['sizey'])
            settings['updateValue'] = 2
            setWindowSettings()
            return
    fltica.efface("sizeErr")
    fltica.texte(int(settings['sizex']/2), 60, text[settings['lang']]['ScreenSizeError'], 'Red', 'center', theme[settings['theme']]['font'], 14, "sizeErr")


def updateSettings():
    """
    Met à jour le nombre d'allumettes (mode normal) et le nombre de tirage maximum.
    """
    nbObj = e2.get()
    nbDraw = e3.get()
    if nbObj.isnumeric() and 0 < int(nbObj) <= 100:
        settings['lines'] = [int(nbObj)]
    if nbDraw.isnumeric() and 0 < int(nbDraw) <= 100:
        settings['maxMatch'] = int(nbDraw)


def back():
    """
    Gère le retour vers l'écran titre.
    """
    fltica.mise_a_jour()
    updateSettings()
    eraseSetTheme()
    settings['updateValue'] = 0


def backSettings():
    """
    Gère le retour vers l'écran des paramètres.
    """
    fltica.mise_a_jour()
    eraseSetTheme()
    settings['updateValue'] = 2


def changeMiseryMode():
    """
    Active ou désactive le mode misère.
    """
    fltica.efface("sizeErr")
    settings['misere'] = not settings['misere']
    fltica.efface('misere')
    fltica.texte(int(settings['sizex']/3.33), (settings['sizey']//3+50), text[settings['lang']]['Enabled'] if settings['misere'] else text[settings['lang']]['Disabled'], 'red' if settings['misere'] else 'green', 'center', theme[settings['theme']]['font'], 14, 'misere')


def changePlayerMode():
    """
    Change le mode de jeu (ici, seulement entre JcJ et Ordinateur niveau facile)
    """
    fltica.efface("sizeErr")
    fltica.efface("mode")
    settings['gameMode'] = "easy" if settings['gameMode'].lower() == 'pvp' else 'PvP'
    fltica.texte(int(settings['sizex']-settings['sizex']/3.33), (settings['sizey']//3+50), settings['gameMode'].capitalize(), getModeColor(), 'center', theme[settings['theme']]['font'], 14, 'mode')
    
    


def getModeColor():
    """
    Renvoi la couleur corréspondante au mode de jeu.
    """
    return 'white' if settings['gameMode'].lower() == 'pvp' else 'green'

def saveMarienbad():
    """
    Vérifie puis sauvegarde les données de entry pour le mode de jeu Marienbad
    """
    toSave = []
    fltica.efface('emptyError')
    fltica.efface('lineError')
    for i, elem in enumerate(entryList):
        if not(elem.get() == ''):
            if elem.get().isnumeric() and int(elem.get()) <= 50:
                toSave.append(int(elem.get()))
            else:
                if settings['lang'] == 'jp':
                    fltica.texte(275, 20+i*(settings['sizey'])/20, '<-'+ str(i+1)+ text[settings['lang']]['LineIvalid'], 'red', 'w', theme[settings['theme']]['font'], 12, 'lineError')
                else:
                    fltica.texte(275, 20+i*(settings['sizey'])/20, '<-'+ text[settings['lang']]['LineIvalid'] +str(i+1), 'red', 'w', theme[settings['theme']]['font'], 12, 'lineError')
                return
    if toSave == []:
        fltica.texte(settings['sizex']//1.33, settings['sizey']//1.75, text[settings['lang']]['NoValue'], 'red', 'center', theme[settings['theme']]['font'], 12, 'emptyError')
    else:
        settings['lines'] = toSave


def MarienbadConfig():
    """
    Affiche et gère le menu Marienbad.
    """
    updateSettings()
    eraseSetTheme()
    fltica.texte(settings['sizex']-20, 20, 'Marienbad', theme[settings['theme']]['fontColor'], 'e', theme[settings['theme']]['font'], 12)
    buttonList = []
    buttonList.append(fltica.Button(settings['sizex']//1.33, settings['sizey']//1.25, text[settings['lang']]['Back'], backSettings, color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage='center', size=14, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    buttonList.append(fltica.Button(settings['sizex']//1.33, settings['sizey']//1.5, text[settings['lang']]['Save'], saveMarienbad, color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage='center', size=14, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    
    global entryList
    entryList = []
    for _ in range(20):
        entryList.append(fltica.tk.Entry(fltica.__canevas.root))
    for i, entry in enumerate(entryList):
        fltica.texte(20, 20+i*(settings['sizey'])/20, text[settings['lang']]['Line']+' '+str(i+1)+':', theme[settings['theme']]['fontColor'], 'w', theme[settings['theme']]['font'], 14)
        fltica.__canevas.canvas.create_window(150, 20+i*(settings['sizey'])/20,anchor='w' ,window=entry)

    if theme[settings['theme']]['buttonBg']:
        for button in buttonList:
            button.setBgImg(theme[settings['theme']]['buttonBg'], theme[settings['theme']]['buttonBgOn'], 150, 300, 40)
    while settings['updateValue'] == 1:
        fltica.mise_a_jour()
        ev = fltica.donne_ev()
        tev = fltica.type_ev(ev)
        for button in buttonList:
            tev = button.update(tev)
        if tev == 'Quitte':
            exit()
        elif tev == 'Touche' and fltica.touche_pressee('Escape'):
            fltica.mise_a_jour()
            backSettings()


def settingsMenu():
    """
    Affiche et gère le menu des paramètres
    """
    global e1, e2, e3
    eraseSetTheme()
    fltica.texte(settings['sizex']//2, 20, text[settings['lang']]['Settings'], theme[settings['theme']]['fontColor'], 'center', theme[settings['theme']]['font'], 12)
    buttonList = []
    buttonList.append(fltica.Button(int(settings['sizex']/3.33), settings['sizey']//4.25, text[settings['lang']]['Theme'], setTheme, color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage='center', size=14, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    buttonList.append(fltica.Button(int(settings['sizex']-settings['sizex']/3.33), settings['sizey']//4.25, text[settings['lang']]['Lang'], setLang, color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage='center', size=14, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    buttonList.append(fltica.Button(int(settings['sizex']/3.33), settings['sizey']//1.50, text[settings['lang']]['Fullscreen'], setFullscreen, color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage='center', size=14, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    buttonList.append(fltica.Button(int(settings['sizex']-settings['sizex']/3.33), settings['sizey']//1.5, text[settings['lang']]['Resolution'], changeRes, color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage='center', size=14, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    buttonList.append(fltica.Button(int(settings['sizex']/3.33), settings['sizey']//3, text[settings['lang']]['Misere'], changeMiseryMode, color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage='center', size=14, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    buttonList.append(fltica.Button(int(settings['sizex']-settings['sizex']/3.33), settings['sizey']//3, text[settings['lang']]['Mode'], changePlayerMode, color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage='center', size=14, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    buttonList.append(fltica.Button(int(settings['sizex']/2), settings['sizey']//1.75, text[settings['lang']]['Marienbad'], MarienbadConfig, color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage='center', size=14, hoverColor=theme[settings['theme']]['buttonHoverColor']))


    fltica.texte(int(settings['sizex']-settings['sizex']/3.33), (settings['sizey']//3+50), settings['gameMode'].capitalize(), getModeColor(), 'center', theme[settings['theme']]['font'], 14, 'mode')
    fltica.texte(int(settings['sizex']/3.33), (settings['sizey']//3+50), text[settings['lang']]['Enabled'] if settings['misere'] else text[settings['lang']]['Disabled'], 'red' if settings['misere'] else 'green', 'center', theme[settings['theme']]['font'], 14, 'misere')
    buttonList.append(fltica.Button(settings['sizex']//2, settings['sizey']//1.25, text[settings['lang']]['Back'], back, color=theme[settings['theme']]['fontColor'], font=theme[settings['theme']]['font'], ancrage='center', size=14, hoverColor=theme[settings['theme']]['buttonHoverColor']))
    if not(fltica.__canevas.root.attributes('-fullscreen')):
        e1 = fltica.tk.Entry(fltica.__canevas.root)
        fltica.__canevas.canvas.create_window(int(settings['sizex']-settings['sizex']/3.33), (settings['sizey']//1.5)+40, window=e1)
    else:
        fltica.texte(int(settings['sizex']-settings['sizex']/3.33), (settings['sizey']//1.5)+80, text[settings['lang']]['FullscreenEnabled'], theme[settings['theme']]['fontColor'], 'center', theme[settings['theme']]['font'], 14)

    # Number of objects
    fltica.texte(int(settings['sizex']/3.33)-75, settings['sizey']//2, text[settings['lang']]['Objects'], 'white', ancrage='center',police=theme[settings['theme']]['font'], taille=14)
    e2 = fltica.tk.Entry(fltica.__canevas.root)
    e2.insert(fltica.tk.END, str(settings['lines'][0]) if len(settings['lines']) == 1 else 'Marienbad')
    fltica.__canevas.canvas.create_window((settings['sizex']/3.33), (settings['sizey']//2),anchor='w' ,window=e2)

    # Max draw
    fltica.texte(int(settings['sizex']-settings['sizex']/3.33)-75, settings['sizey']//2, text[settings['lang']]['MaxDraw'], 'white', ancrage='center',police=theme[settings['theme']]['font'], taille=14)
    e3 = fltica.tk.Entry(fltica.__canevas.root)
    e3.insert(fltica.tk.END, str(settings['maxMatch']))
    fltica.__canevas.canvas.create_window(int(settings['sizex']-settings['sizex']/3.33), (settings['sizey']//2),anchor='w' ,window=e3)

    if theme[settings['theme']]['buttonBg']:
        for button in buttonList:
            button.setBgImg(theme[settings['theme']]['buttonBg'], theme[settings['theme']]['buttonBgOn'], 150, 300, 40)
    while settings['updateValue'] == 1:
        fltica.mise_a_jour()
        ev = fltica.donne_ev()
        tev = fltica.type_ev(ev)
        for button in buttonList:
            tev = button.update(tev)
        if tev == 'Quitte':
            exit()
        elif tev == 'Touche' and fltica.touche_pressee('Escape'):
            fltica.mise_a_jour()
            back()


def main():
    fltica.cree_fenetre(settings['sizex'], settings['sizey'])
    setWindowSettings()
    while True:
        buttonList = showMainMenu()
        updateMenu(buttonList)
