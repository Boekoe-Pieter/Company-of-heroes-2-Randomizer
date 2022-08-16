# -*- coding: utf-8 -*-
# """
# Created on Mon Aug  1 22:12:12 2022

# @author: Piete
# """

# "Company of Heroes 2 Randomizer"
# "for Inhouse and Automatch"
# "for 1v1, 2v2, 3v3 and 4v4"

#"Imports"
from ast import Delete, Global
import random
from tkinter import *
from functools import partial
import tkinter as tk
from tkinter import ttk
import re
from pathlib import Path

#"List of factions and commanders"
Teamlist = ['Allied', 'Axis']
FactionsAxis = ['OKW','Wehrmacht']
FactionsAllies = ['USSR','USF','Brits',]
Commanders_USSR = ['Advanced Warfare Tactics', 'Airborne Troops Tactics','Anti Infantry Tactics','Armored Assault Doctrine','Conscripts Support Tactics','Counterattack Tactics','Defensive Tactics','Guards Motor Coordination Tactics','Guard Rifle Combined Arms Tactics','Lend Lease Tactics','Mechanized Support Tactics','NKVD Disruption Tactics','Partisan Tactics','Shock Motor Heavy Tactics','Shock Rifle Frontline Tactics','Soviet Combined Arms Army','Soviet Industry Tactics','Soviet Reserve Army','Soviet Shock Army','Tank Hunter Tactics','Terror Tactics','Urban Defense Tactics']
Commanders_USF = ['Airborne Company', 'Armor Company', 'Heavy Cavalry Company', 'Infantry Company', 'Mechanized Company', 'Recon Support Company', 'Rifle Company', 'Tactical Support Company', 'Urban Assault Company']
Commanders_Brits = ['Advanced Emplacement Regiment', 'Commando Regiment', 'Lend Lease Assault Regiment', 'Mobile Assault Regiment', 'Royal Artillery Regiment', 'Royal Engineer Regiment', 'Special Weapons Regiment', 'Tactical Support Regiment', 'Vanguard Operations Regiment']
Commanders_OKW = ['Breakthrough Doctrine','Elite Armored Doctrine', 'Feuersturm Doctrine', 'Fortifications Doctrine', 'Grand Offensive Doctrine', 'Luftwaffe Ground Forces Doctrine', 'Overwatch Doctrine', 'Scavenge Doctrine', 'Special Operations Doctrine']
Commanders_Wehrmacht = ['Assault Support Doctrine', 'Blitzkrieg Doctrine','Close Air Support Doctrine','Defensive Doctrine','Elite Troops Doctrine','Encirclement Doctrine','Festung Armor Doctrine', 'Festung Support Doctrine','Fortified Armor Doctrine','German Infantry Doctrine','German Mechanized Doctrine','Jaeger Armor Doctrine','Jeager Infantry Doctrine', 'Joint Operations Doctrine', 'Lighting War Doctrine', 'Luftwaffe Supply Doctrine', 'Mechanized Assault Doctrine', 'Mobile Defense Doctrine', 'Osttruppen Doctrine', 'Spearhead Doctrine','Storm Doctrine','Strategic Reserves Doctrine']


#list op maps
maps_4v4 = ['Essen Steelworks','Hill 400','La Gleize','Steppes','City 17','General Mud','Red Ball Express','Whiteball Express','Lanzerath Ambush','Lienne Forest','Lorch Assault','Nordwind','Port of Hamburg','Road to Arnhem','Vielsam']
maps_3v3 = ['Across the Rhine','Essen Steelworks','Ettlebruck Station','La Gleize','Oka River Winter','Steppes','General Mud','Angermunde','Red Ball Express','Whiteball Express','Fields of Winnekendonk','Hill 400','Port of Hamburg','Rzhev Winter','Lienne Forest']
maps_2v2 = ['Minsk Pocket','Rails and Metal','Road to Kharkov','Moscow Outskirts','Eindhoven Country','Allience of Defiance','Belgorod','Crossing in the Woods','Elst Outskirts','Fields of Winnekendonk','Highway to Baku','Wolfheze']
maps_1v1 = ['Kholodny Ferma','Langreskaya','Amilly Fields','Bayeux','Bocage','Crossing in the Woods','Mill Road','Nexus','Ploiesti Outskirts','Crossroads','Crossroads Winter','Vilshanka']


# Save input names for Inhouse random
cwd = Path.cwd()


def WriteToFile(names):
    with  open(str(cwd)+"\input.txt", "w")  as savednameswrite:
        savednameswrite.write(str(names))
        savednameswrite.close()
def readfile():
    with open(str(cwd)+"\input.txt") as savednames:
        lines = savednames.readlines()
        savednames.close()
    names = re.findall(r"'(\w+)'", str(lines))
    return names

# Save input names for Automatch
def WriteToFileAutomatch(namesAutomatch):
    with  open(str(cwd)+"\inputAutomatch.txt", "w")  as savednameswriteAutomatch:
        savednameswriteAutomatch.write(str(namesAutomatch))
        savednameswriteAutomatch.close()

def readfileAutomatch():
    with open(str(cwd)+"\inputAutomatch.txt") as savednamesAutomatch:
        lines = savednamesAutomatch.readlines()
        savednamesAutomatch.close()
    namesAutomatch = re.findall(r"'(\w+)'", str(lines))
    return namesAutomatch




#POP UP SCREEN
screen = Tk()
screen.geometry("1000x700")
screen.title("COH2 Randomizer")
bg = tk.PhotoImage(file=str(cwd)+ '\Images\coh2 background.png')
frame = ttk.Frame(screen)
canvas = Canvas(screen)
canvas.create_image(0,0, image=bg, anchor=(NW))
canvas.pack(fill="both",expand=True)


#CODE FOR ASKING AXIS, ALLIED or RANDOM for AUTOMATCH
def show_Automatch_options():
    global teamconfigAutomatch, Axisbutton,AlliedButton,RandomButton
    teamconfigAutomatch = canvas.create_text(140,150,text=' Random or Pre-made Teams?',fill = 'black', font=('times',12,'bold'), anchor = W , tag = 'teamconfigAutomatch')
    Axisbutton = Button(text='Axis Team',command= show_Automatch_options_V_mode_AXIS)
    Axisbutton.place(x=133,y=180)
    AlliedButton = Button(text='Allied Team',command=show_Automatch_options_V_mode_ALLIED)
    AlliedButton.place(x=250,y=180)
    RandomButton = Button(text='Random Team',command=show_Automatch_options_V_mode_RANDOM)
    RandomButton.place(x=350,y=180)
    #deleting Inhouse when clicking Automatch
    RandomTeam.destroy()
    PreMadeButton.destroy()
    #deleting modes
    canvas.delete('modeconfig')

    if  randominhouseteam == 'deletethis1':
        mode_1v1_INHOUSE_RANDOM.destroy()
        mode_2v2_INHOUSE_RANDOM.destroy()
        mode_3v3_INHOUSE_RANDOM.destroy() 
        mode_4v4_INHOUSE_RANDOM.destroy()
        #deleting teaminput
        GenerateRandomTeam.destroy()
        #deleting teamoutput
        deleteTeamDisplay()
        deletefactionimages()
        deletecommanderimages()
        deletemapimages()
    elif INHOUSE_premade_TEAMS == 'deletethis2':
        GenerateAxisteam.destroy()
        GenerateAlliedteam.destroy()
        mode_1v1_Inhouse_Pre_Made.destroy()
        mode_2v2_Inhouse_Pre_Made.destroy()
        mode_3v3_Inhouse_Pre_Made.destroy() 
        mode_4v4_Inhouse_Pre_Made.destroy()
        #deleting teaminput
        
        #deleting teamoutput
        deleteTeamDisplay()
        deletefactionimages()
        deletecommanderimages()
        deletemapimages()



#CODE FOR ASKING RANDOM OR PRE-MADE TEAMS FOR INHOUSE
def show_Inhouse_options():
    global RandomTeam,PreMadeButton,teamconfigInhouse
    teamconfigInhouse = canvas.create_text(140,150,text=' Random or Pre-made Teams?',fill = 'black', font=('times',12,'bold'), anchor = W,tag = 'teamconfigInhouse')
    RandomTeam = Button(canvas, text='Random Team',command=show_Inhouse_options_V_mode)
    RandomTeam.place(x=133,y=180)
    PreMadeButton = Button(canvas, text='Pre-made Team',command=show_Inhouse_options_V_mode_PRE_MADE)
    PreMadeButton.place(x=300,y=180)
    #deleting Automatch when clicking Inhouse
    Axisbutton.destroy()
    AlliedButton.destroy()
    RandomButton.destroy()
    canvas.delete('teamconfigAutomatch')  
    #deleting modes
    canvas.delete('modeconfig')
    if automatch_axis == 'deletethis3':
        mode_1v1_automatch_axis.destroy() 
        mode_2v2_automatch_axis.destroy()
        mode_3v3_automatch_axis.destroy()
        mode_4v4_automatch_axis.destroy()
        #deleting teaminput
        GenerateTeamAxis.destroy()

    elif automatch_allies == 'deletethis4':
        mode_1v1_automatch_allied.destroy() 
        mode_2v2_automatch_allied.destroy()
        mode_3v3_automatch_allied.destroy()
        mode_4v4_automatch_allied.destroy()
        #deleting teaminput
        GenerateTeamAllied.destroy()

    elif automatch_random == 'deletethis5':
        mode_1v1_automatch_random.destroy() 
        mode_2v2_automatch_random.destroy()
        mode_3v3_automatch_random.destroy()
        mode_4v4_automatch_random.destroy()
        #deleting teaminput
        GenerateTeamRandom.destroy()


    #deleting teamoutput
    deleteTeamDisplay()
    deletefactionimages()
    deletecommanderimages()
    deletemapimages()
#"CODE FOR ASKING INHOUSE OR AUTOMATCH"
canvas.create_text(250,50, text='Press Inhouse or Automatch',fill = 'black', font=('times',12,'bold'))
button_inhouse= tk.Button(canvas, text='Inhouse', command= partial(show_Inhouse_options), activebackground='green').place(x=133,y=80)
button_Automatch= tk.Button(canvas,text='Automatch', command= partial(show_Automatch_options), activebackground='green').place(x=300,y=80)

  

####################################################################################################################################################################################################################################################################################################################################################################################################################################################
###############   INHOUSE RANDOM TEAMS      ########################################################################################################################################################################################################################################################################################################################################################################################################################################################################
####################################################################################################################################################################################################################################################################################################################################################################################################################################################
#"CODE FOR ASKING 1V1, 2V2, 3V3, 4V4 FOR INHOUSE"
randominhouseteam = 1
def show_Inhouse_options_V_mode():
    global mode_1v1_INHOUSE_RANDOM, mode_2v2_INHOUSE_RANDOM, mode_3v3_INHOUSE_RANDOM, mode_4v4_INHOUSE_RANDOM, mode_inhouse, randominhouseteam
    _y = 280
    mode_inhouse = canvas.create_text(200,240,text=' Which mode:',fill = 'black', font=('times',12,'bold'), anchor = W, tag='modeconfig')
    mode_1v1_INHOUSE_RANDOM = tk.Button(text='1v1', command=partial(playernames, 2))
    mode_1v1_INHOUSE_RANDOM.place(x=150,y=_y)
    mode_2v2_INHOUSE_RANDOM = Button(text='2v2' , command=partial(playernames, 4))
    mode_2v2_INHOUSE_RANDOM.place(x=200,y=_y)
    mode_3v3_INHOUSE_RANDOM = Button(text='3v3' , command=partial(playernames, 6))
    mode_3v3_INHOUSE_RANDOM.place(x=250,y=_y)
    mode_4v4_INHOUSE_RANDOM = Button(text='4v4' , command=partial(playernames, 8))
    mode_4v4_INHOUSE_RANDOM.place(x=300,y=_y)
    randominhouseteam = 'deletethis1'
    
    if INHOUSE_premade_TEAMS == 'deletethis2':
        GenerateAxisteam.destroy()
        GenerateAlliedteam.destroy()
        mode_1v1_Inhouse_Pre_Made.destroy()
        mode_2v2_Inhouse_Pre_Made.destroy()
        mode_3v3_Inhouse_Pre_Made.destroy() 
        mode_4v4_Inhouse_Pre_Made.destroy()
        #deleting teaminput
        
        #deleting teamoutput
        deleteTeamDisplay()
        deletefactionimages()
        deletecommanderimages()
        deletemapimages()

#"CODE FOR LISTING PLAYERS INHOUSE TEAM"
Namelist = []
names_entry_players = []
names = StringVar()
def button_command():
    deleteTeamDisplay()
    deletefactionimages()
    deletecommanderimages()
    deletemapimages()
    Namelist = []
    for i in range(len(names_entry_players)):
        Namelist.append(names_entry_players[i].get())
    WriteToFile(Namelist)
#"Giving Players Team"
    Playersteam = int(len(names_entry_players)/2)
    AxisPlayers = random.sample(Namelist,k=Playersteam)
    for i in range(0,Playersteam):
        Namelist.remove(AxisPlayers[i])
    AlliedPlayers = Namelist  
#"Choosing Factions"
    AxisFactions = random.choices(FactionsAxis,k=len(AxisPlayers))
    AlliedFactions = random.choices(FactionsAllies,k=len(AlliedPlayers))
#"Choosing Commanders For Factions"
    Axiscommanders = [] #array
    for i in range(0,len(AxisFactions)):
        if (AxisFactions[i] == 'Wehrmacht'):
            Axiscommanders.append(random.choice(Commanders_Wehrmacht))
        else:
            Axiscommanders.append(random.choice(Commanders_OKW))   

    Alliedcommanders = [] #array
    for i in range(0,len(AlliedPlayers)):
        if (AlliedFactions[i] == 'USSR'):
            Alliedcommanders.append(random.choice(Commanders_USSR))
        elif (AlliedFactions[i] == 'USF'):
            Alliedcommanders.append(random.choice(Commanders_USF))
        else:
            Alliedcommanders.append(random.choice(Commanders_Brits))

    # if len(names_entry_players) == 8:
    #     Map_list_inhouse_4v4 = random.sample(maps_4v4,1)
    TeamResults(AxisPlayers,AlliedPlayers,AxisFactions,AlliedFactions,Axiscommanders,Alliedcommanders)#,Map_list_inhouse_4v4)
def playernames(amountplayers):
    global GenerateRandomTeam, players_entry
    returnnames= readfile()
    GenerateRandomTeam = Button(text='Generate Teams',command=button_command)
    GenerateRandomTeam.place(x=200,y=400)
    for i in range(amountplayers):
        _y=350
        names = StringVar()
        players_entry = Entry(screen,textvariable=names)
        if returnnames:
            if i < len(returnnames):
                players_entry.insert(END,returnnames[i])   
        players_entry.place(x=50+(i*100),y=_y)
        names_entry_players.append(players_entry)

#######################################################################################################################################################################################################################################################################################################################################
####################     INHOUSE PRE-MADE TEAMS            ###################################################################################################################################################################################################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################################################################
# "CODE FOR ASKING 1V1, 2V2, 3V3, 4V4 FOR AUTOMATCH"
INHOUSE_premade_TEAMS = 1
def show_Inhouse_options_V_mode_PRE_MADE():

    if  randominhouseteam == 'deletethis1':
        mode_1v1_INHOUSE_RANDOM.destroy()
        mode_2v2_INHOUSE_RANDOM.destroy()
        mode_3v3_INHOUSE_RANDOM.destroy() 
        mode_4v4_INHOUSE_RANDOM.destroy()
        #deleting teaminput
        GenerateRandomTeam.destroy()
        players_entry.destroy()
        #deleting teamoutput
        deleteTeamDisplay()
        deletefactionimages()
        deletecommanderimages()
        deletemapimages()   

    _y = 280
    global mode_1v1_Inhouse_Pre_Made, mode_2v2_Inhouse_Pre_Made, mode_3v3_Inhouse_Pre_Made, mode_4v4_Inhouse_Pre_Made,INHOUSE_premade_TEAMS
    canvas.create_text(200,240,text=' Which mode:',fill = 'black', font=('times',12,'bold'), anchor = W, tag='modeconfig')
    mode_1v1_Inhouse_Pre_Made = Button(text='1v1', command=partial(playernames_premade, 1) )
    mode_1v1_Inhouse_Pre_Made.place(x=150,y=_y)
    mode_2v2_Inhouse_Pre_Made = Button(text='2v2' , command=partial(playernames_premade, 2) )
    mode_2v2_Inhouse_Pre_Made.place(x=200,y=_y)
    mode_3v3_Inhouse_Pre_Made = Button(text='3v3' , command=partial(playernames_premade, 3) )
    mode_3v3_Inhouse_Pre_Made.place(x=250,y=_y)
    mode_4v4_Inhouse_Pre_Made = Button(text='4v4' , command=partial(playernames_premade, 4) )
    mode_4v4_Inhouse_Pre_Made.place(x=300,y=_y)
    INHOUSE_premade_TEAMS = 'deletethis2'





# "CODE FOR LISTING PLAYERS FILL IN AXIS PLAYERS"
Namelist_axis = []
names_entry_players_axis = []
names_axis = StringVar()
def button_command_axis():
    for i in range(len(names_entry_players_axis)):
        Namelist_axis.append(names_entry_players_axis[i].get())
    if len(Namelist_axis) == len(names_entry_players_axis):
        fill_in_allied(len(names_entry_players_axis)) 
    AxisFactions_premade = random.choices(FactionsAxis,k=len(names_entry_players_axis))          #randomizer for factions
#"Choosing Commanders For Factions"
    Axiscommanders_premade = []
    for i in range(0,len(names_entry_players_axis)):                                                  #randomizer for commanders
        if (AxisFactions_premade[i] == 'Wehrmacht'):
            Axiscommanders_premade.append(random.choice(Commanders_Wehrmacht))
        else:
            Axiscommanders_premade.append(random.choice(Commanders_OKW))   
    deleteTeamDisplay()
    deletefactionimages()
    deletecommanderimages()
    deletemapimages()
    TeamResults_Premade_axis(Namelist_axis,AxisFactions_premade,Axiscommanders_premade)
    INHOUSE_premade_TEAMS = 'deletethis2'
#CODE FOR LISTING AXIS PLAYERS
def playernames_premade(amountplayers):
    global GenerateAxisteam
    GenerateAxisteam = Button(text='Generate Axis Team',command=button_command_axis)
    GenerateAxisteam.place(x=200,y=400)
    for i in range(amountplayers):
        _y=350
        names_axis = StringVar()
        players_entry_axis = Entry(screen,textvariable=names_axis)
        players_entry_axis.place(x=50+(i*100),y=_y)
        names_entry_players_axis.append(players_entry_axis)

def fill_in_allied(amountplayers):
    Namelist_allied = []
    names_entry_players_allied = []
    names_allied = StringVar()
    def button_command_allied():
        global Reroll, Map_list_inhouse_4v4_premade
        # Reroll = Button(screen, text= "Reroll", command=deleteall)
        # Reroll.place(x=400,y=400)
        for i in range(len(names_entry_players_allied)):
            Namelist_allied.append(names_entry_players_allied[i].get())
        AlliedFactions_premade = random.choices(FactionsAllies,k=len(names_entry_players_allied))         #randomizer for factions
        Alliedcommanders_premade = [] #array
        for i in range(0,len(names_entry_players_allied)):                                                #randomizer for commanders
            if (AlliedFactions_premade[i] == 'USSR'):
                Alliedcommanders_premade.append(random.choice(Commanders_USSR))
            elif (AlliedFactions_premade[i] == 'USF'):
                Alliedcommanders_premade.append(random.choice(Commanders_USF))
            else:
                Alliedcommanders_premade.append(random.choice(Commanders_Brits))

        if len(names_entry_players_allied) == 4:
            Map_list_inhouse_4v4_premade = random.sample(maps_4v4,1)
        TeamResults_Premade_allied(Namelist_allied,AlliedFactions_premade,Alliedcommanders_premade)
#"CODE FOR LISTING PLAYERS FILL IN ALLIED PLAYERS"
    global GenerateAlliedteam
    GenerateAlliedteam = Button(text='Generate Allied Team',command=button_command_allied)
    GenerateAlliedteam.place(x=600,y=400)
    for i in range(amountplayers):
        _y=350
        names_allied = StringVar()
        players_entry_allied = Entry(screen,textvariable=names_allied)
        players_entry_allied.place(x=450+(i*100),y=_y)
        names_entry_players_allied.append(players_entry_allied)



#######################################################################################################################################################################################################################################################################################################################################
####################     AUTOMATCH AXIS        ###################################################################################################################################################################################################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################################################################
# "CODE FOR ASKING 1V1, 2V2, 3V3, 4V4 FOR AUTOMATCH"
automatch_axis = 1
def show_Automatch_options_V_mode_AXIS():
 
    #deleting modes
    canvas.delete('modeconfig')
    if automatch_allies == 'deletethis4':
        mode_1v1_automatch_allied.destroy() 
        mode_2v2_automatch_allied.destroy()
        mode_3v3_automatch_allied.destroy()
        mode_4v4_automatch_allied.destroy()
        #deleting teaminput
        GenerateTeamAllied.destroy()
        deleteTeamDisplay()
    elif automatch_random == 'deletethis5':
        mode_1v1_automatch_random.destroy() 
        mode_2v2_automatch_random.destroy()
        mode_3v3_automatch_random.destroy()
        mode_4v4_automatch_random.destroy()
        #deleting teaminput
        GenerateTeamRandom.destroy()
        deleteTeamDisplay()
        deletefactionimages()
        deletecommanderimages()
        deletemapimages()


    global mode_1v1_automatch_axis, mode_2v2_automatch_axis, mode_3v3_automatch_axis, mode_4v4_automatch_axis, automatch_axis
    _y = 280
    canvas.create_text(200,240,text=' Which mode:',fill = 'black', font=('times',12,'bold'), anchor = W, tag='modeconfig')
    mode_1v1_automatch_axis = Button(text='1v1', command=partial(playernames_Automatch_axis, 1) )
    mode_1v1_automatch_axis.place(x=150,y=_y)
    mode_2v2_automatch_axis = Button(text='2v2' , command=partial(playernames_Automatch_axis, 2) )
    mode_2v2_automatch_axis.place(x=200,y=_y)
    mode_3v3_automatch_axis = Button(text='3v3' , command=partial(playernames_Automatch_axis, 3) )
    mode_3v3_automatch_axis.place(x=250,y=_y)
    mode_4v4_automatch_axis = Button(text='4v4' , command=partial(playernames_Automatch_axis, 4) )
    mode_4v4_automatch_axis.place(x=300,y=_y)
    automatch_axis = 'deletethis3'
# "CODE FOR LISTING PLAYERS FILL IN AXIS PLAYERS"
Namelist_axis_automatch = []
names_entry_players_axis_automatch = []
names_axis_automatch = StringVar()
def button_command_Automatch():
    Namelist_axis_automatch = []
    for i in range(len(names_entry_players_axis_automatch)):
        Namelist_axis_automatch.append(names_entry_players_axis_automatch[i].get())
    WriteToFileAutomatch(Namelist_axis_automatch)
    AxisFactions_Automatch = random.choices(FactionsAxis,k=len(names_entry_players_axis_automatch))          #randomizer for factions
#"Choosing Commanders For Factions"
    Axiscommanders_Automatch = []
    for i in range(0,len(Namelist_axis_automatch)):                                                  #randomizer for commanders
        if (AxisFactions_Automatch[i] == 'Wehrmacht'):
            Axiscommanders_Automatch.append(random.choice(Commanders_Wehrmacht))
        else:
            Axiscommanders_Automatch.append(random.choice(Commanders_OKW))   
    deleteTeamDisplay()
    deletefactionimages()
    deletecommanderimages()
    deletemapimages()
    TeamResults_Automatch_axis(Namelist_axis_automatch,AxisFactions_Automatch,Axiscommanders_Automatch)
#CODE FOR LISTING AXIS PLAYERS
def playernames_Automatch_axis(amountplayers):
    global GenerateTeamAxis
    GenerateTeamAxis = Button(text='Generate Team',command=button_command_Automatch)
    GenerateTeamAxis.place(x=200,y=400)
    StoredNamesAutomatch = readfileAutomatch()
    for i in range(amountplayers):
        _y=350
        names_axis_automatch = StringVar()
        players_entry_axis_automatch = Entry(screen,textvariable=names_axis_automatch)
        if StoredNamesAutomatch:
            if i < len(StoredNamesAutomatch):
                players_entry_axis_automatch.insert(END,StoredNamesAutomatch[i])  
        players_entry_axis_automatch.place(x=50+(i*100),y=_y)
        names_entry_players_axis_automatch.append(players_entry_axis_automatch)



######################################################################################################################################################################################################################################################################################################################################
###################     AUTOMATCH ALLIES        ###################################################################################################################################################################################################################################################################################################################################################################################################################################################
######################################################################################################################################################################################################################################################################################################################################
# "CODE FOR ASKING 1V1, 2V2, 3V3, 4V4 FOR AUTOMATCH"
automatch_allies = 1
def show_Automatch_options_V_mode_ALLIED():
    #deleting modes
    canvas.delete('modeconfig')
    if automatch_axis == 'deletethis3':
        mode_1v1_automatch_axis.destroy() 
        mode_2v2_automatch_axis.destroy()
        mode_3v3_automatch_axis.destroy()
        mode_4v4_automatch_axis.destroy()
        #deleting teaminput
        GenerateTeamAxis.destroy()
        deleteTeamDisplay()
    elif automatch_random == 'deletethis5':
        mode_1v1_automatch_random.destroy() 
        mode_2v2_automatch_random.destroy()
        mode_3v3_automatch_random.destroy()
        mode_4v4_automatch_random.destroy()
        #deleting teaminput
        GenerateTeamRandom.destroy()
        deleteTeamDisplay()
        deletefactionimages()
        deletecommanderimages()
        deletemapimages()

    global mode_1v1_automatch_allied, mode_2v2_automatch_allied,mode_3v3_automatch_allied, mode_4v4_automatch_allied, automatch_allies
    _y = 280
    canvas.create_text(200,240,text=' Which mode:',fill = 'black', font=('times',12,'bold'), anchor = W, tag='modeconfig')    
    mode_1v1_automatch_allied = Button(text='1v1', command=partial(playernames_Automatch_allied, 1) )
    mode_1v1_automatch_allied.place(x=150,y=_y)
    mode_2v2_automatch_allied = Button(text='2v2' , command=partial(playernames_Automatch_allied, 2) )
    mode_2v2_automatch_allied.place(x=200,y=_y)
    mode_3v3_automatch_allied = Button(text='3v3' , command=partial(playernames_Automatch_allied, 3) )
    mode_3v3_automatch_allied.place(x=250,y=_y)
    mode_4v4_automatch_allied = Button(text='4v4' , command=partial(playernames_Automatch_allied, 4) )
    mode_4v4_automatch_allied.place(x=300,y=_y)
    automatch_allies = 'deletethis4'

# "CODE FOR LISTING PLAYERS FILL IN ALLIED PLAYERS"
Namelist_allied_automatch = []
names_entry_players_allied_automatch = []
names_allied_automatch = StringVar()
def button_command_Automatch_allied():
    Namelist_allied_automatch = []
    for i in range(len(names_entry_players_allied_automatch)):
        Namelist_allied_automatch.append(names_entry_players_allied_automatch[i].get())
    WriteToFileAutomatch(Namelist_allied_automatch)
    AlliedFactions_automatch = random.choices(FactionsAllies,k=len(names_entry_players_allied_automatch))         #randomizer for factions
    Alliedcommanders_Automatch = [] #array
    for i in range(0,len(names_entry_players_allied_automatch)):                                                #randomizer for commanders
        if (AlliedFactions_automatch[i] == 'USSR'):
            Alliedcommanders_Automatch.append(random.choice(Commanders_USSR))
        elif (AlliedFactions_automatch[i] == 'USF'):
            Alliedcommanders_Automatch.append(random.choice(Commanders_USF))
        else:
            Alliedcommanders_Automatch.append(random.choice(Commanders_Brits))   
    deleteTeamDisplay()
    deletefactionimages()
    deletecommanderimages()
    deletemapimages()
    TeamResults_Automatch_allies(Namelist_allied_automatch,AlliedFactions_automatch,Alliedcommanders_Automatch)
#CODE FOR LISTING ALLIED PLAYERS
def playernames_Automatch_allied(amountplayers):
    global GenerateTeamAllied
    GenerateTeamAllied = Button(text='Generate Team',command=button_command_Automatch_allied)
    GenerateTeamAllied.place(x=200,y=400)
    StoredNamesAutomatch_allied = readfileAutomatch()
    for i in range(amountplayers):
        _y=350
        names_allied_automatch = StringVar()
        players_entry_allied_automatch = Entry(screen,textvariable=names_allied_automatch)
        if StoredNamesAutomatch_allied:
            if i < len(StoredNamesAutomatch_allied):
                players_entry_allied_automatch.insert(END,StoredNamesAutomatch_allied[i])  
        players_entry_allied_automatch.place(x=50+(i*100),y=_y)
        names_entry_players_allied_automatch.append(players_entry_allied_automatch)



######################################################################################################################################################################################################################################################################################################################################
###################     AUTOMATCH RANDOM        ###################################################################################################################################################################################################################################################################################################################################################################################################################################################
######################################################################################################################################################################################################################################################################################################################################
# "CODE FOR ASKING 1V1, 2V2, 3V3, 4V4 FOR AUTOMATCH"
automatch_random = 1
def show_Automatch_options_V_mode_RANDOM():
    #deleting modes
    canvas.delete('modeconfig')
    if automatch_axis == 'deletethis3':
        mode_1v1_automatch_axis.destroy() 
        mode_2v2_automatch_axis.destroy()
        mode_3v3_automatch_axis.destroy()
        mode_4v4_automatch_axis.destroy()
        #deleting teaminput
        GenerateTeamAxis.destroy()
        deleteTeamDisplay()
    elif automatch_allies == 'deletethis4':
        mode_1v1_automatch_allied.destroy() 
        mode_2v2_automatch_allied.destroy()
        mode_3v3_automatch_allied.destroy()
        mode_4v4_automatch_allied.destroy()
        #deleting teaminput
        GenerateTeamAllied.destroy()
        deleteTeamDisplay()


    global mode_1v1_automatch_random, mode_2v2_automatch_random,mode_3v3_automatch_random, mode_4v4_automatch_random, automatch_random
    _y = 280
    canvas.create_text(200,240,text=' Which mode:',fill = 'black', font=('times',12,'bold'), anchor = W, tag='modeconfig')
    mode_1v1_automatch_random = Button(text='1v1', command=partial(playernames_Automatch_RANDOM, 1) )
    mode_1v1_automatch_random.place(x=150,y=_y)
    mode_2v2_automatch_random = Button(text='2v2' , command=partial(playernames_Automatch_RANDOM, 2) )
    mode_2v2_automatch_random.place(x=200,y=_y)
    mode_3v3_automatch_random = Button(text='3v3' , command=partial(playernames_Automatch_RANDOM, 3) )
    mode_3v3_automatch_random.place(x=250,y=_y)
    mode_4v4_automatch_random = Button(text='4v4' , command=partial(playernames_Automatch_RANDOM, 4) )
    mode_4v4_automatch_random.place(x=300,y=_y)
    automatch_random = 'deletethis5'

# "CODE FOR LISTING PLAYERS FILL IN ALLIED PLAYERS"
Namelist_random_automatch = []
names_entry_players_random_automatch = []
names_random_automatch = StringVar()
def button_command_Automatch_RANDOM():
    Namelist_random_automatch = []
    for i in range(len(names_entry_players_random_automatch)):                                                          
        Namelist_random_automatch.append(names_entry_players_random_automatch[i].get())
    RandomTeam = random.sample(Teamlist,k=1)                                                                                 #randomizer for Team                                       
    WriteToFileAutomatch(Namelist_allied_automatch)
    RandomFactions = []  
    for i in range(len(names_entry_players_random_automatch)):
        if RandomTeam[0] == 'Axis':
            RandomFactions.append(random.choice(FactionsAxis))            
        else:
            RandomFactions.append(random.choice(FactionsAllies))                                                              #randomizer for factions
    Randomcommanders_Automatch = [] #array
    for i in range(0,len(names_entry_players_random_automatch)):                                                              #randomizer for commanders
        if (RandomFactions[i] == 'USSR'):
            Randomcommanders_Automatch.append(random.choice(Commanders_USSR))
        elif (RandomFactions[i] == 'USF'):
            Randomcommanders_Automatch.append(random.choice(Commanders_USF))
        elif  (RandomFactions[i]== 'Brits'):
            Randomcommanders_Automatch.append(random.choice(Commanders_Brits))
        elif (RandomFactions[i]== 'Wehrmacht'):
            Randomcommanders_Automatch.append(random.choice(Commanders_Wehrmacht))
        else:
            Randomcommanders_Automatch.append(random.choice(Commanders_OKW)) 
    deleteTeamDisplay()
    deletefactionimages()
    deletecommanderimages()
    deletemapimages()

    TeamResults_Automatch_RANDOM(Namelist_random_automatch,RandomFactions,Randomcommanders_Automatch)
#CODE FOR LISTING PLAYERS
def playernames_Automatch_RANDOM(amountplayers):
    global GenerateTeamRandom
    GenerateTeamRandom = Button(text='Generate Team',command=button_command_Automatch_RANDOM)
    GenerateTeamRandom.place(x=200,y=400)
    StoredNamesAutomatch_Random = readfileAutomatch()
    for i in range(amountplayers):
        _y=350
        names_random_automatch = StringVar()
        players_entry_random_automatch = Entry(screen,textvariable=names_random_automatch)
        if StoredNamesAutomatch_Random:
            if i < len(StoredNamesAutomatch_Random):
                players_entry_random_automatch.insert(END,StoredNamesAutomatch_Random[i])  
        players_entry_random_automatch.place(x=50+(i*100),y=_y)
        names_entry_players_random_automatch.append(players_entry_random_automatch)



#######################################################################################################################################################################################################################################################################################################################################
####################      Delete TeamDisplay        ###################################################################################################################################################################################################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################################################################



def deleteTeamDisplay():
    global teampopup
    Namelist = []
    teampopup = canvas.delete("AxisTeamLabel","AxisPlayersLabel","AxisFactionsLabel","AxisCommandersLabel",
                "AlliedTeamLabel","AlliedPlayersLabel","AlliedFactionLabel","AlliedCommandersLabel",
                "AxisTeamLabelPremade","AxisPlayersLabelPremade","AxisFactionsLabelPremade","AxisCommandersPremade",
                "AlliedTeamLabelPremade","AlliedPlayersPremade","AlliedFactionPremade","AlliedCommandersPremade",
                "AxisPlayersLabelAutomatch","AxisFactionsLabelAutomatch","AxisCommandersAutomatch",
                "AlliedPlayersAutomatch","AlliedFactionAutomatch","AlliedCommandersAutomatch",
                "RandomPlayersAutomatch","RandomFactionAutomatch","RandomCommandersAutomatch")
def deletefactionimages():
    factionimages = canvas.delete('UK_Image', 'OKW_Image', 'Wehrmacht_Image', 'Sovjet_Image', 'USF_Image')


def deletecommanderimages():
    global commanderimages
    commanderimages = canvas.delete("Breakthrough_Doctrine_OKW","Elite_Armored_Doctrine","Feuersturm_Doctrine","Fortifications_Doctrine","Grand_Offensive_Doctrine","Luftwaffe_Ground_Forces_Doctrine","Overwatch_Doctrine","Scavenge_Doctrine","Special_Operations_Doctrine",
                "Assault_Support_Doctrine_OKW","Blitzkrieg_Doctrine","Close_Air_Support_Doctrine","Defensive_Doctrine","Elite_Troops_Doctrine","Encirclement_Doctrine","Festung_Armor_Doctrine","Festung_Support_Doctrine",'Fortified_Armor_Doctrine','German_Infantry_Doctrine','German_Mechanized_Doctrine','Jaeger_Armor_Doctrine','Jeager_Infantry_Doctrine','Joint_Operations_Doctrine','Lighting_War_Doctrine','Luftwaffe_Supply_Doctrine','Mechanized_Assault_Doctrine','Mobile_Defense_Doctrine','Osttruppen_Doctrine','Spearhead_Doctrine','Storm_Doctrine','Strategic_Reserves_Doctrine',
                'Advanced_Warfare_Tactics','Airborne_Troops_Tactics','Anti_Infantry_Tactics','Armored_Assault_Doctrine','Conscripts_Support_Tactics','Counterattack_Tactics','Defensive_Tactics','Guards_Motor_Coordination_Tactics','Guard_Rifle_Combined_Arms_Tactics','Lend_Lease_Tactics','Mechanized_Support_Tactics','NKVD_Disruption_Tactics','Partisan_Tactics','Shock_Motor_Heavy_Tactics','Shock_Rifle_Frontline_Tactics','Soviet_Combined_Army','Soviet_Industry_Tactics','Soviet_Reserve_Army','Tank_Hunter_Tactics','Terror_Tactics','Urban_Defense_Tactics', 'Soviet_Shock_Army',
                'Airborne_Company','Heavy_Cavalry_Company','Infantry_Company','Mechanized_Company','Recon_Support_Company','Rifle_Company','Urban_Assault_Company','Tactical_Support_Company',
                'Advanced_Emplacement_Regiment','Commando_Regiment','Mobile_Assault_Regiment','Royal_Artillery_Regiment','Royal_Engineer_Regiment','Special_Weapons_Regiment','Special_Weapons_Regiment','Vanguard_Operation',)

def deletemapimages():
    global mapimages
    mapimages = canvas.delete("map_4v4",'City17',"Essen_steelworks", 'Ettelbruck_station','General_mud',"hill400",'La_Gleize','Lienne_Forest','Lorch_Assault','Nordwind','Port_of_Hamburg','Red_Ball_Express','Road_to_Arnhem','Steppes','Vielsam')

def deleteall():
    deleteTeamDisplay()
    deletefactionimages()
    deletecommanderimages()
    deletemapimages()

#######################################################################################################################################################################################################################################################################################################################################
####################      TeamDisplay Hell Dont watch if you want to live        ###################################################################################################################################################################################################################################################################################################################################################################################################################################################
#######################################################################################################################################################################################################################################################################################################################################
#FactionFlags
OKW_Image = tk.PhotoImage(file=str(cwd)+ '\Images\OKW.png', name = 'OKW_Image')
GER_Image = tk.PhotoImage(file=str(cwd)+ '\Images\GER.png', name = 'GER_Image')
USSR_Image = tk.PhotoImage(file=str(cwd)+ '\Images\RUS.png', name = 'RUS_Image')
USF_Image = tk.PhotoImage(file=str(cwd)+ '\\Images\\US.png', name='USF_Image')
Brits_Image = tk.PhotoImage(file=str(cwd)+ '\\Images\\UK.png', name='UK_Image')
#OKWCommanders
Breakthrough_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OKWCommanders\\Breakthrough Doctrine.png', name='Breakthrough_Doctrine')
Elite_Armored_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OKWCommanders\\Elite Armored Doctrine.png', name='Elite Armored Doctrine')
Feuersturm_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OKWCommanders\\Feuersturm Doctrine.png', name='Feuersturm Doctrine')
Fortifications_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OKWCommanders\\Fortifications Doctrine.png', name='Fortifications Doctrine')
Grand_Offensive_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OKWCommanders\\Grand Offensive Doctrine.png', name='Grand Offensive Doctrine')
Luftwaffe_Ground_Forces_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OKWCommanders\\Luftwaffe Ground Forces Doctrine.png', name='Luftwaffe Ground Forces Doctrine')
Overwatch_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OKWCommanders\\Overwatch Doctrine.png', name='Overwatch Doctrine')
Scavenge_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OKWCommanders\\Scavenge Doctrine.png', name='Scavenge Doctrine')
Special_Operations_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OKWCommanders\\Special Operations Doctrine.png', name='Special Operations Doctrine')
#WehrmachtCommanders
Assault_Support_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Assault Support Doctrine.png', name='Assault_Support_Doctrine')
Blitzkrieg_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Blitzkrieg Doctrine.png', name='Blitzkrieg Doctrine')
Close_Air_Support_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Close Air Support Doctrine.png', name='Close Air Support Doctrine')
Defensive_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Defensive Doctrine.png', name='Defensive Doctrine')
Elite_Troops_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Elite Troops Doctrine.png', name='Elite Troops Doctrine')
Encirclement_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Encirclement Doctrine.png', name='Encirclement Doctrine')
Festung_Armor_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Festung Armor Doctrine.png', name='Festung Armor Doctrine')
Festung_Support_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Festung Support Doctrine.png', name='Festung Support Doctrine')
Fortified_Armor_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Fortified Armor Doctrine.png', name='Fortified Armor Doctrine')
German_Infantry_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\German Infantry Doctrine.png', name='German Infantry Doctrine')
German_Mechanized_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\German Mechanized Doctrine.png', name='German Mechanized Doctrine')
Jaeger_Armor_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Jaeger Armor Doctrine.png', name='Jaeger Armor Doctrine')
Jeager_Infantry_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Jeager Infantry Doctrine.png', name='Jeager Infantry Doctrine')
Joint_Operations_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Joint Operations Doctrine.png', name='Joint Operations Doctrine')
Lighting_War_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Lighting War Doctrine.png', name='Lighting War Doctrine')
Luftwaffe_Supply_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Luftwaffe Supply Doctrine.png', name='Luftwaffe Supply Doctrine')
Mechanized_Assault_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Mechanized Assault Doctrine.png', name='Mechanized Assault Doctrine')
Mobile_Defense_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Mobile Defense Doctrine.png', name='Mobile Defense Doctrine')
Osttruppen_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Osttruppen Doctrine.png', name='Osttruppen Doctrine')
Spearhead_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Spearhead Doctrine.png', name='Spearhead Doctrine')
Storm_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Storm Doctrine.png', name='Storm Doctrine')
Strategic_Reserves_Doctrine = tk.PhotoImage(file=str(cwd)+ '\\Images\\OstheerCommanders\\Strategic Reserves Doctrine.png', name='Strategic Reserves Doctrine')
#USSRCommanders
Advanced_Warfare_Tactics = tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Advanced Warfare Tactics.png', name='Advanced Warfare Tactics')
Airborne_Troops_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Airborne Troop Tactics.png', name='Airborne Troop Tactics')
Anti_Infantry_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Anti Infantry Tactics.png', name='Anti Infantry Tactics')
Armored_Assault_Doctrine= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Armored Assault Doctrine.png', name='Armored Assault Doctrine')
Conscripts_Support_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Conscripts Support Tactics.png', name='Conscripts Support Tactics')
Counterattack_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Counter Attack Tactics.png', name='Counter Attack Tactics')
Defensive_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Defensive Tactics.png', name='Defensive Tactics')
Guards_Motor_Coordination_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Guards Motor Coordination Tactics.png', name='Guards Motor Coordination Tactics')
Guard_Rifle_Combined_Arms_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Guards Rifle Combined Arms Tactics.png', name='Guards Rifle Combined Arms Tactics')
Lend_Lease_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Lend Lease Tactics.png', name='Lend Lease Tactics')
Mechanized_Support_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Mechanized Support tactics.png', name='Mechanized Support tactics')
NKVD_Disruption_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\NKVD Disruption Tactics.png', name='NKVD Disruption Tactics')
Partisan_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Partisan Tactics.png', name='Partisan Tactics')
Shock_Motor_Heavy_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Shock Motor Heavy Tactics.png', name='Shock Motor Heavy Tactics')
Shock_Rifle_Frontline_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Shock Rifle Frontline Tactics.png', name='Shock Rifle Frontline Tactics')
Soviet_Combined_Arms_Army= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Soviet Combined Arms Army.png', name='Soviet Combined Arms Army')
Soviet_Industry_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Soviet Industry Tactics.png', name='Soviet Industry Tactics')
Soviet_Reserve_Army= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Soviet Reserve Army.png', name='Soviet Reserve Army')
Soviet_Shock_Army= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Soviet Shock Army.png', name='Soviet Shock Army')
Tank_Hunter_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Tank Hunter tactics.png', name='Tank Hunter tactics')
Terror_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Terror Tactics.png', name='Terror Tactics')
Urban_Defense_Tactics= tk.PhotoImage(file=str(cwd)+ '\\Images\\USSRCommanders\\Urban Defense Tactics.png', name='Urban Defense Tactics')
#USFCommanders
Airborne_Company = tk.PhotoImage(file=str(cwd)+ '\\Images\\USFCommanders\\Airborne Company.png', name='Airborne Company')
Armor_Company = tk.PhotoImage(file=str(cwd)+ '\\Images\\USFCommanders\\Armor Company.png', name='Armor Company')
Heavy_Cavalry_Company = tk.PhotoImage(file=str(cwd)+ '\\Images\\USFCommanders\\Heavy Cavalry Company.png', name='Heavy Cavalry Company')
Infantry_Company = tk.PhotoImage(file=str(cwd)+ '\\Images\\USFCommanders\\Infantry Company.png', name='Infantry Company')
Mechanized_Company = tk.PhotoImage(file=str(cwd)+ '\\Images\\USFCommanders\\Mechanized Company.png', name='Mechanized Company')
Recon_Support_Company = tk.PhotoImage(file=str(cwd)+ '\\Images\\USFCommanders\\Recon Support Company.png', name='Recon Support Company')
Rifle_Company = tk.PhotoImage(file=str(cwd)+ '\\Images\\USFCommanders\\Rifle Company.png', name='Rifle Company')
Tactical_Support_Company = tk.PhotoImage(file=str(cwd)+ '\\Images\\USFCommanders\\Tactical Support Company.png', name='Tactical Support Company')
Urban_Assault_Company = tk.PhotoImage(file=str(cwd)+ '\\Images\\USFCommanders\\Urban Assault Company.png', name='Urban Assault Company')
#UKCommanders
Advanced_Emplacement_Regiment = tk.PhotoImage(file=str(cwd)+ '\\Images\\UKCommanders\\Advanced Emplacement Regiment.png', name='Advanced Emplacement Regiment')
Commando_Regiment = tk.PhotoImage(file=str(cwd)+ '\\Images\\UKCommanders\\Commando Regiment.png', name='Commando Regiment')
Mobile_Assault_Regiment = tk.PhotoImage(file=str(cwd)+ '\\Images\\UKCommanders\\Mobile Assault Regiment.png', name='Mobile Assault Regiment')
Royal_Artillery_Regiment = tk.PhotoImage(file=str(cwd)+ '\\Images\\UKCommanders\\Royal Artillery Regiment.png', name='Royal Artillery Regiment')
Royal_Engineer_Regiment = tk.PhotoImage(file=str(cwd)+ '\\Images\\UKCommanders\\Royal Engineer Regiment.png', name='Royal Engineer Regiment')
Special_Weapons_Regiment = tk.PhotoImage(file=str(cwd)+ '\\Images\\UKCommanders\\Special Weapons Regiment.png', name='Special Weapons Regiment')
Tactical_Support_Regiment = tk.PhotoImage(file=str(cwd)+ '\\Images\\UKCommanders\\Tactical Support Regiment.png', name='Tactical Support Regiment')
Vanguard_Operation = tk.PhotoImage(file=str(cwd)+ '\\Images\\UKCommanders\\Vanguard Operations Regiment.png', name='Vanguard Operation')
Lend_Lease_Assault_Regiment = tk.PhotoImage(file=str(cwd)+ '\\Images\\UKCommanders\\Lend Lease Assault Regiment.png', name='Lend Lease Assault Regiment')
#4v4maps
City17 = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\City 17.png', name='City17')
Essen_steelworks = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\Essen Steelworks.png', name='Essen Steelworks')
General_mud = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\General Mud.png', name='General Mud')
hill400 = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\Hill 400.png', name='Hill 400')
La_Gleize = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\La Gleize.png', name='La Gleize')
Lanzerath_Ambush = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\Lanzerath Ambush.png', name='Lanzerath Ambush')
Lienne_Forest = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\Lienne Forest.png', name='Lienne Forest')
Lorch_Assault = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\Lorch Assault.png', name='Lorch Assault')
Nordwind = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\Nordwind.png', name='Nordwind')
Port_of_Hamburg = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\Port of Hamburg.png', name='Port of Hamburg')
Red_Ball_Express = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\Red Ball Express.png', name='Red_Ball_Express')
Road_to_Arnhem = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\Road to Arnhem.png', name='Road to Arnhem')
Steppes = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\Steppes.png', name='Steppes')
Vielsam = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\Vielsam.png', name='Vielsam')
Whiteball_Express = tk.PhotoImage(file=str(cwd)+ '\\Images\\4v4 maps\\Whiteball Express.png', name='Whiteball Express')


#commander images location
x_axis = 100
x_axis_allied = 850
y_axis = 440

#playernames
names_x_axis_left = 155
names_x_axis_right = 845
names_y_axis = 460

#commanderNames
commanders_y_axis = 480

#flags
flag_right = 900
flag_left = 50
flag_y_axis = 447

i_distance = 60

#maplocation
map_x_text = 440
map_y_text = 440
map_x = 400
map_y = 450



def TeamResults(AxisPlayers,AlliedPlayers,AxisFactions,AlliedFactions,Axiscommanders,Alliedcommanders):#,Map_list_inhouse_4v4):#,Map_list_inhouse_3v3,Map_list_inhouse_2v2,Map_list_inhouse_1v1):
    # canvas.create_text(map_x_text,map_y_text,text=str(Map_list_inhouse_4v4[0]),fill = 'black', anchor = W, font=('times',12,'bold'),tag="map_4v4") 
    # if Map_list_inhouse_4v4[0] == 'City 17':
    #              canvas.create_image(map_x,map_y, image=City17 , anchor = NW , tag="City17 ")        
    # elif Map_list_inhouse_4v4[0] == 'Essen Steelworks':
    #             canvas.create_image(map_x,map_y, image=Essen_steelworks, anchor = NW , tag="Essen_steelworks")
    # elif Map_list_inhouse_4v4[0] == 'General Mud':
    #             canvas.create_image(map_x,map_y, image=General_mud , anchor = NW , tag="General_mud ")
    # elif Map_list_inhouse_4v4[0] == 'Hill 400':
    #             canvas.create_image(map_x,map_y, image=hill400, anchor = NW , tag="hill400")   
    # elif Map_list_inhouse_4v4[0] == 'La Gleize':
    #             canvas.create_image(map_x,map_y, image=La_Gleize , anchor = NW , tag="La_Gleize")   
    # elif Map_list_inhouse_4v4[0] == 'Lanzerath Ambush':
    #             canvas.create_image(map_x,map_y, image=Lanzerath_Ambush , anchor = NW , tag="Lanzerath_Ambush")   
    # elif Map_list_inhouse_4v4[0] == 'Lienne Forest':
    #             canvas.create_image(map_x,map_y, image=Lienne_Forest , anchor = NW , tag="Lienne_Forest")   
    # elif Map_list_inhouse_4v4[0] == 'Lorch Assault':
    #             canvas.create_image(map_x,map_y, image=Lorch_Assault , anchor = NW , tag="Lorch_Assault")   
    # elif Map_list_inhouse_4v4[0] == 'Nordwind':
    #             canvas.create_image(map_x,map_y, image=Nordwind, anchor = NW , tag="Nordwind")   
    # elif Map_list_inhouse_4v4[0] == 'Port of Hamburg':
    #             canvas.create_image(map_x,map_y, image=Port_of_Hamburg , anchor = NW , tag="Port_of_Hamburg")   
    # elif Map_list_inhouse_4v4[0] == 'Red Ball Express':
    #             canvas.create_image(map_x,map_y, image=Red_Ball_Express , anchor = NW , tag="Red_Ball_Express")
    # elif Map_list_inhouse_4v4[0] == 'Road to Arnhem':
    #             canvas.create_image(map_x,map_y, image=Road_to_Arnhem , anchor = NW , tag="Road_to_Arnhem")   
    # elif Map_list_inhouse_4v4[0] == 'Steppes':
    #             canvas.create_image(map_x,map_y, image=Steppes , anchor = NW , tag="Steppes")   
    # elif Map_list_inhouse_4v4[0] == 'Vielsam':
    #             canvas.create_image(map_x,map_y, image=Vielsam  , anchor = NW , tag="Vielsam")
    # else:              
    #             canvas.create_image(map_x,map_y, image=Whiteball_Express   , anchor = NW , tag="Whiteball_Express")


    for i in range(len(AxisPlayers)):
        canvas.create_text(names_x_axis_left,names_y_axis+(i*i_distance),text=str(AxisPlayers[i]),fill = 'black', font=('times',12,'bold'), anchor = W, tag="AxisPlayersLabel")
        canvas.create_text(names_x_axis_left,commanders_y_axis+(i*i_distance),text=str(Axiscommanders[i]),fill = 'black', font=('times',12,'bold'), anchor = W,tag="AxisCommandersLabel")

        if AxisFactions[i] == 'OKW':
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=OKW_Image, anchor=(NW), tag="OKW_Image")
            if Axiscommanders[i] == 'Breakthrough Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Breakthrough_Doctrine, anchor=(NW), tag="Breakthrough_Doctrine_OKW")
            elif Axiscommanders[i] == 'Elite Armored Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Elite_Armored_Doctrine, anchor=(NW), tag="Elite_Armored_Doctrine")
            elif Axiscommanders[i] == 'Feuersturm Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Feuersturm_Doctrine, anchor=(NW), tag="Feuersturm_Doctrine")
            elif Axiscommanders[i] == 'Fortifications Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Fortifications_Doctrine, anchor=(NW), tag="Fortifications_Doctrine")
            elif Axiscommanders[i] == 'Grand Offensive Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Grand_Offensive_Doctrine, anchor=(NW), tag="Grand_Offensive_Doctrine")
            elif Axiscommanders[i] == 'Luftwaffe Ground Forces Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Luftwaffe_Ground_Forces_Doctrine, anchor=(NW), tag="Luftwaffe_Ground_Forces_Doctrine")
            elif Axiscommanders[i] == 'Overwatch Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Overwatch_Doctrine, anchor=(NW), tag="Overwatch_Doctrine")
            elif Axiscommanders[i] == 'Scavenge Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Scavenge_Doctrine, anchor=(NW), tag="Scavenge_Doctrine")
            else:
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Special_Operations_Doctrine, anchor=(NW), tag="Special_Operations_Doctrine")

        else:  
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=GER_Image, anchor=(NW), tag="Wehrmacht_Image")
            if Axiscommanders[i] == 'Assault Support Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Assault_Support_Doctrine, anchor=(NW), tag="Assault_Support_Doctrine_OKW")  
            elif Axiscommanders[i] == 'Blitzkrieg Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Blitzkrieg_Doctrine, anchor=(NW), tag="Blitzkrieg_Doctrine")
            elif Axiscommanders[i] == 'Close Air Support Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Close_Air_Support_Doctrine, anchor=(NW), tag="Close_Air_Support_Doctrine")    
            elif Axiscommanders[i] == 'Defensive Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Defensive_Doctrine, anchor=(NW), tag="Defensive_Doctrine")
            elif Axiscommanders[i] == 'Elite Troops Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Elite_Troops_Doctrine, anchor=(NW), tag="Elite_Troops_Doctrine")                       
            elif Axiscommanders[i] == 'Encirclement Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Encirclement_Doctrine, anchor=(NW), tag="Encirclement_Doctrine")
            elif Axiscommanders[i] == 'Festung Armor Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Festung_Armor_Doctrine, anchor=(NW), tag="Festung_Armor_Doctrine")    
            elif Axiscommanders[i] == 'Festung Support Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Festung_Support_Doctrine, anchor=(NW), tag="Festung_Support_Doctrine")
            elif Axiscommanders[i] == 'Fortified Armor Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Fortified_Armor_Doctrine, anchor=(NW), tag="Fortified_Armor_Doctrine")  
            elif Axiscommanders[i] == 'German Infantry Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=German_Infantry_Doctrine, anchor=(NW), tag="German_Infantry_Doctrine")
            elif Axiscommanders[i] == 'German Mechanized Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=German_Mechanized_Doctrine, anchor=(NW), tag="German_Mechanized_Doctrine")    
            elif Axiscommanders[i] == 'Jaeger Armor Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Jaeger_Armor_Doctrine, anchor=(NW), tag="Jaeger_Armor_Doctrine")
            elif Axiscommanders[i] == 'Jeager Infantry Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Jeager_Infantry_Doctrine, anchor=(NW), tag="Jeager_Infantry_Doctrine")  
            elif Axiscommanders[i] == 'Lighting War Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Lighting_War_Doctrine, anchor=(NW), tag="Lighting_War_Doctrine")
            elif Axiscommanders[i] == 'Luftwaffe Supply Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Luftwaffe_Supply_Doctrine, anchor=(NW), tag="Luftwaffe_Supply_Doctrine")    
            elif Axiscommanders[i] == 'Mechanized Assault Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mechanized_Assault_Doctrine, anchor=(NW), tag="Mechanized_Assault_Doctrine")
            elif Axiscommanders[i] == 'Mobile Defense Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mobile_Defense_Doctrine, anchor=(NW), tag="Mobile_Defense_Doctrine")  
            elif Axiscommanders[i] == 'Osttruppen Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Osttruppen_Doctrine, anchor=(NW), tag="Osttruppen_Doctrine")
            elif Axiscommanders[i] == 'Spearhead Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Spearhead_Doctrine, anchor=(NW), tag="Spearhead_Doctrine")  
            elif Axiscommanders[i] == 'Storm Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Storm_Doctrine, anchor=(NW), tag="Storm_Doctrine")
            else:
                canvas.create_image(x_axis,440+(i*i_distance), image=Strategic_Reserves_Doctrine, anchor=(NW), tag="Strategic_Reserves_Doctrine")  



    for i in range(len(AlliedPlayers)):
        canvas.create_text(names_x_axis_right,names_y_axis+(i*i_distance),text=str(AlliedPlayers[i]),fill = 'black', font=('times',12,'bold'), anchor = E, tag="AlliedPlayersLabel")
        canvas.create_text(names_x_axis_right,commanders_y_axis+(i*i_distance),text=str(Alliedcommanders[i]),fill = 'black', font=('times',12,'bold'), anchor = E, tag="AlliedCommandersLabel")
        if AlliedFactions[i] == 'USSR':
            canvas.create_image(flag_right,flag_y_axis+(i*i_distance), image=USSR_Image, anchor=(NW), tag="Sovjet_Image")
            if Alliedcommanders[i] == 'Advanced Warfare Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Advanced_Warfare_Tactics, anchor=(NW), tag="Advanced_Warfare_Tactics ")
            elif Alliedcommanders[i] == 'Airborne Troops Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Airborne_Troops_Tactics, anchor=(NW), tag="Airborne_Troops_Tactics")
            elif Alliedcommanders[i] == 'Anti Infantry Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Anti_Infantry_Tactics, anchor=(NW), tag="Anti_Infantry_Tactics")
            elif Alliedcommanders[i] == 'Armored Assault Doctrine':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Armored_Assault_Doctrine, anchor=(NW), tag="Armored_Assault_Doctrine")           
            elif Alliedcommanders[i] == 'Conscripts Support Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Conscripts_Support_Tactics, anchor=(NW), tag="Conscripts_Support_Tactics")
            elif Alliedcommanders[i] == 'Counterattack Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Counterattack_Tactics, anchor=(NW), tag="Counterattack_Tactics")
            elif Alliedcommanders[i] == 'Defensive Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Defensive_Tactics, anchor=(NW), tag="Defensive_Tactics")
            elif Alliedcommanders[i] == 'Guards Motor Coordination Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Guards_Motor_Coordination_Tactics, anchor=(NW), tag="Guards_Motor_Coordination_Tactics")
            elif Alliedcommanders[i] == 'Guard Rifle Combined Arms Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Guard_Rifle_Combined_Arms_Tactics, anchor=(NW), tag="Guard_Rifle_Combined_Arms_Tactics")
            elif Alliedcommanders[i] == 'Lend Lease Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Lend_Lease_Tactics, anchor=(NW), tag="Lend_Lease_Tactics")
            elif Alliedcommanders[i] == 'Mechanized Support Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Mechanized_Support_Tactics, anchor=(NW), tag="Mechanized_Support_Tactics")
            elif Alliedcommanders[i] == 'NKVD Disruption Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=NKVD_Disruption_Tactics, anchor=(NW), tag="NKVD_Disruption_Tactics")
            elif Alliedcommanders[i] == 'Partisan Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Partisan_Tactics, anchor=(NW), tag="Partisan_Tactics")
            elif Alliedcommanders[i] == 'Shock Motor Heavy Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Shock_Motor_Heavy_Tactics, anchor=(NW), tag="Shock_Motor_Heavy_Tactics")
            elif Alliedcommanders[i] == 'Shock Rifle Frontline Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Shock_Rifle_Frontline_Tactics, anchor=(NW), tag="Shock_Rifle_Frontline_Tactics")
            elif Alliedcommanders[i] == 'Soviet Combined Arms Army':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Soviet_Combined_Arms_Army, anchor=(NW), tag="Soviet_Combined_Army")
            elif Alliedcommanders[i] == 'Soviet Industry Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Soviet_Industry_Tactics, anchor=(NW), tag="Soviet_Industry_Tactics")
            elif Alliedcommanders[i] == 'Soviet Reserve Army':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Soviet_Reserve_Army, anchor=(NW), tag="Soviet_Reserve_Army")
            elif Alliedcommanders[i] == 'Soviet Shock Army':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Soviet_Shock_Army, anchor=(NW), tag="Soviet_Shock_Army")
            elif Alliedcommanders[i] == 'Tank Hunter Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Tank_Hunter_Tactics, anchor=(NW), tag="Tank_Hunter_Tactics")
            elif Alliedcommanders[i] == 'Terror Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Terror_Tactics, anchor=(NW), tag="Terror_Tactics")
            else:
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Urban_Defense_Tactics, anchor=(NW), tag="Urban_Defense_Tactics")            
        elif AlliedFactions[i] == 'USF':
            canvas.create_image(flag_right,flag_y_axis+(i*i_distance), image=USF_Image, anchor=(NW), tag="USF_Image")
            if Alliedcommanders[i] == 'Airborne Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Airborne_Company, anchor=(NW), tag="Airborne_Company")
            elif Alliedcommanders[i] == 'Heavy Cavalry Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Heavy_Cavalry_Company, anchor=(NW), tag="Heavy_Cavalry_Company")
            elif Alliedcommanders[i] == 'Infantry Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Infantry_Company, anchor=(NW), tag="Infantry_Company")
            elif Alliedcommanders[i] == 'Mechanized Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Mechanized_Company, anchor=(NW), tag="Mechanized_Company")
            elif Alliedcommanders[i] == 'Recon Support Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Recon_Support_Company, anchor=(NW), tag="Recon_Support_Company")
            elif Alliedcommanders[i] == 'Rifle Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Rifle_Company, anchor=(NW), tag="Rifle_Company")
            elif Alliedcommanders[i] == 'Urban Assault Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Urban_Assault_Company, anchor=(NW), tag="Urban_Assault_Company")                
            else:
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Tactical_Support_Company, anchor=(NW), tag="Tactical_Support_Company")

        else:
            canvas.create_image(flag_right,flag_y_axis+(i*60), image=Brits_Image, anchor=(NW), tag="UK_Image")
            if Alliedcommanders[i] == 'Advanced Emplacement Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Advanced_Emplacement_Regiment  , anchor=(NW), tag="Advanced_Emplacement_Regiment")
            elif Alliedcommanders[i] == 'Commando Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Commando_Regiment, anchor=(NW), tag="Commando_Regiment")
            elif Alliedcommanders[i] == 'Mobile Assault Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Mobile_Assault_Regiment, anchor=(NW), tag="Mobile_Assault_Regiment")
            elif Alliedcommanders[i] == 'Royal Artillery Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Royal_Artillery_Regiment, anchor=(NW), tag="Royal_Artillery_Regiment")
            elif Alliedcommanders[i] == 'Royal Engineer Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Royal_Engineer_Regiment, anchor=(NW), tag="Royal_Engineer_Regiment")
            elif Alliedcommanders[i] == 'Special Weapons Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Special_Weapons_Regiment, anchor=(NW), tag="Special_Weapons_Regiment")
            elif Alliedcommanders[i] == 'Tactical Support Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Tactical_Support_Regiment, anchor=(NW), tag="Special_Weapons_Regiment")                
            elif Alliedcommanders[i] =='Vanguard Operations Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Vanguard_Operation  , anchor=(NW), tag="Vanguard_Operation")
            else:
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Lend_Lease_Assault_Regiment  , anchor=(NW), tag="Lend Lease Assault Regiment")




##################################### Inhouse Pre-Made Team ################################
def TeamResults_Premade_axis(Namelist_axis,AxisFactions_premade,Axiscommanders_premade):
    for i in range(len(Namelist_axis)):
        canvas.create_text(names_x_axis_left,names_y_axis+(i*i_distance),text=str(Namelist_axis[i]),fill = 'black', font=('times',12,'bold'), anchor = W, tag="AxisPlayersLabelPremade")
        canvas.create_text(names_x_axis_left,commanders_y_axis+(i*i_distance),text=str(Axiscommanders_premade[i]),fill = 'black', font=('times',12,'bold'), anchor = W, tag="AxisCommandersPremade")

        if AxisFactions_premade[i] == 'OKW':
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=OKW_Image, anchor=(NW), tag="OKW_Image")
            if Axiscommanders_premade[i] == 'Breakthrough Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Breakthrough_Doctrine, anchor=(NW), tag="Breakthrough_Doctrine_OKW")
            elif Axiscommanders_premade[i] == 'Elite Armored Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Elite_Armored_Doctrine, anchor=(NW), tag="Elite_Armored_Doctrine")
            elif Axiscommanders_premade[i] == 'Feuersturm Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Feuersturm_Doctrine, anchor=(NW), tag="Feuersturm_Doctrine")
            elif Axiscommanders_premade[i] == 'Fortifications Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Fortifications_Doctrine, anchor=(NW), tag="Fortifications_Doctrine")
            elif Axiscommanders_premade[i] == 'Grand Offensive Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Grand_Offensive_Doctrine, anchor=(NW), tag="Grand_Offensive_Doctrine")
            elif Axiscommanders_premade[i] == 'Luftwaffe Ground Forces Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Luftwaffe_Ground_Forces_Doctrine, anchor=(NW), tag="Luftwaffe_Ground_Forces_Doctrine")
            elif Axiscommanders_premade[i] == 'Overwatch Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Overwatch_Doctrine, anchor=(NW), tag="Overwatch_Doctrine")
            elif Axiscommanders_premade[i] == 'Scavenge Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Scavenge_Doctrine, anchor=(NW), tag="Scavenge_Doctrine")
            else:
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Special_Operations_Doctrine, anchor=(NW), tag="Special_Operations_Doctrine")
        else:  
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=GER_Image, anchor=(NW), tag="Wehrmacht_Image")
            if Axiscommanders_premade[i] == 'Assault Support Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Assault_Support_Doctrine, anchor=(NW), tag="Assault_Support_Doctrine_OKW")  
            elif Axiscommanders_premade[i] == 'Blitzkrieg Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Blitzkrieg_Doctrine, anchor=(NW), tag="Blitzkrieg_Doctrine")
            elif Axiscommanders_premade[i] == 'Close Air Support Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Close_Air_Support_Doctrine, anchor=(NW), tag="Close_Air_Support_Doctrine")    
            elif Axiscommanders_premade[i] == 'Defensive Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Defensive_Doctrine, anchor=(NW), tag="Defensive_Doctrine")
            elif Axiscommanders_premade[i] == 'Elite Troops Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Elite_Troops_Doctrine, anchor=(NW), tag="Elite_Troops_Doctrine")                       
            elif Axiscommanders_premade[i] == 'Encirclement Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Encirclement_Doctrine, anchor=(NW), tag="Encirclement_Doctrine")
            elif Axiscommanders_premade[i] == 'Festung Armor Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Festung_Armor_Doctrine, anchor=(NW), tag="Festung_Armor_Doctrine")    
            elif Axiscommanders_premade[i] == 'Festung Support Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Festung_Support_Doctrine, anchor=(NW), tag="Festung_Support_Doctrine")
            elif Axiscommanders_premade[i] == 'Fortified Armor Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Fortified_Armor_Doctrine, anchor=(NW), tag="Fortified Armor Doctrine")  
            elif Axiscommanders_premade[i] == 'German Infantry Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=German_Infantry_Doctrine, anchor=(NW), tag="German_Infantry_Doctrine")
            elif Axiscommanders_premade[i] == 'German Mechanized Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=German_Mechanized_Doctrine, anchor=(NW), tag="German_Mechanized_Doctrine")    
            elif Axiscommanders_premade[i] == 'Jaeger Armor Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Jaeger_Armor_Doctrine, anchor=(NW), tag="Jaeger_Armor_Doctrine")
            elif Axiscommanders_premade[i] == 'Jeager Infantry Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Jeager_Infantry_Doctrine, anchor=(NW), tag="Jeager_Infantry_Doctrine")  
            elif Axiscommanders_premade[i] == 'Lighting War Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Lighting_War_Doctrine, anchor=(NW), tag="Lighting_War_Doctrine")
            elif Axiscommanders_premade[i] == 'Luftwaffe Supply Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Luftwaffe_Supply_Doctrine, anchor=(NW), tag="Luftwaffe_Supply_Doctrine")    
            elif Axiscommanders_premade[i] == 'Mechanized Assault Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mechanized_Assault_Doctrine, anchor=(NW), tag="Mechanized_Assault_Doctrine")
            elif Axiscommanders_premade[i] == 'Mobile Defense Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mobile_Defense_Doctrine, anchor=(NW), tag="Mobile_Defense_Doctrine")  
            elif Axiscommanders_premade[i] == 'Osttruppen Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Osttruppen_Doctrine, anchor=(NW), tag="Osttruppen_Doctrine")
            elif Axiscommanders_premade[i] == 'Spearhead Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Spearhead_Doctrine, anchor=(NW), tag="Spearhead_Doctrine")  
            elif Axiscommanders_premade[i] == 'Storm Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Storm_Doctrine, anchor=(NW), tag="Storm_Doctrine")
            else:
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Strategic_Reserves_Doctrine, anchor=(NW), tag="Strategic_Reserves_Doctrine")

def TeamResults_Premade_allied(Namelist_allied,AlliedFactions_premade,Alliedcommanders_premade):#, Map_list_inhouse_4v4_premade):
    # canvas.create_text(map_x_text,map_y_text,text=str(Map_list_inhouse_4v4_premade[0]),fill = 'black', anchor = W, font=('times',12,'bold'),tag="map_4v4") 
    # if Map_list_inhouse_4v4_premade[0] == 'City 17':
    #             canvas.create_image(map_x,map_y, image=City17 , anchor = NW , tag="City17 ")        
    # elif Map_list_inhouse_4v4_premade[0] == 'Essen Steelworks':
    #             canvas.create_image(map_x,map_y, image=Essen_steelworks, anchor = NW , tag="Essen_steelworks")
    # elif Map_list_inhouse_4v4_premade[0] == 'General Mud':
    #             canvas.create_image(map_x,map_y, image=General_mud , anchor = NW , tag="General_mud ")
    # elif Map_list_inhouse_4v4_premade[0] == 'Hill 400':
    #             canvas.create_image(map_x,map_y, image=hill400, anchor = NW , tag="hill400")   
    # elif Map_list_inhouse_4v4_premade[0] == 'La Gleize':
    #             canvas.create_image(map_x,map_y, image=La_Gleize , anchor = NW , tag="La_Gleize")   
    # elif Map_list_inhouse_4v4_premade[0] == 'Lanzerath Ambush':
    #             canvas.create_image(map_x,map_y, image=Lanzerath_Ambush , anchor = NW , tag="Lanzerath_Ambush")   
    # elif Map_list_inhouse_4v4_premade[0] == 'Lienne Forest':
    #             canvas.create_image(map_x,map_y, image=Lienne_Forest , anchor = NW , tag="Lienne_Forest")   
    # elif Map_list_inhouse_4v4_premade[0] == 'Lorch Assault':
    #             canvas.create_image(map_x,map_y, image=Lorch_Assault , anchor = NW , tag="Lorch_Assault")   
    # elif Map_list_inhouse_4v4_premade[0] == 'Nordwind':
    #             canvas.create_image(map_x,map_y, image=Nordwind, anchor = NW , tag="Nordwind")   
    # elif Map_list_inhouse_4v4_premade[0] == 'Port of Hamburg':
    #             canvas.create_image(map_x,map_y, image=Port_of_Hamburg , anchor = NW , tag="Port_of_Hamburg")   
    # elif Map_list_inhouse_4v4_premade[0] == 'Red Ball Express':
    #             canvas.create_image(map_x,map_y, image=Red_Ball_Express , anchor = NW , tag="Red_Ball_Express")
    # elif Map_list_inhouse_4v4_premade[0] == 'Road to Arnhem':
    #             canvas.create_image(map_x,map_y, image=Road_to_Arnhem , anchor = NW , tag="Road_to_Arnhem")   
    # elif Map_list_inhouse_4v4_premade[0] == 'Steppes':
    #             canvas.create_image(map_x,map_y, image=Steppes , anchor = NW , tag="Steppes")   
    # elif Map_list_inhouse_4v4_premade[0] == 'Vielsam':
    #             canvas.create_image(map_x,map_y, image=Vielsam  , anchor = NW , tag="Vielsam")
    # else:              
    #             canvas.create_image(map_x,map_y, image=Whiteball_Express   , anchor = NW , tag="Whiteball_Express") 
    for i in range(len(Namelist_allied)):
        canvas.create_text(names_x_axis_right,names_y_axis+(i*i_distance),text=str(Namelist_allied[i]),fill = 'black', font=('times',12,'bold'), anchor = E, tag="AlliedPlayersPremade")
        canvas.create_text(names_x_axis_right,commanders_y_axis+(i*i_distance),text=str(Alliedcommanders_premade[i]),fill = 'black', font=('times',12,'bold'), anchor = E, tag="AlliedCommandersPremade")   
        if AlliedFactions_premade[i] == 'USSR':
            canvas.create_image(flag_right,flag_y_axis+(i*i_distance), image=USSR_Image, anchor=(NW), tag="Sovjet_Image")
            if Alliedcommanders_premade[i] == 'Advanced Warfare Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Advanced_Warfare_Tactics, anchor=(NW), tag="Advanced_Warfare_Tactics ")
            elif Alliedcommanders_premade[i] == 'Airborne Troops Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Airborne_Troops_Tactics, anchor=(NW), tag="Airborne_Troops_Tactics")
            elif Alliedcommanders_premade[i] == 'Anti Infantry Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Anti_Infantry_Tactics, anchor=(NW), tag="Anti_Infantry_Tactics")
            elif Alliedcommanders_premade[i] == 'Armored Assault Doctrine':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Armored_Assault_Doctrine, anchor=(NW), tag="Armored_Assault_Doctrine")     
            elif Alliedcommanders_premade[i] == 'Conscripts Support Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Conscripts_Support_Tactics, anchor=(NW), tag="Conscripts_Support_Tactics")
            elif Alliedcommanders_premade[i] == 'Counterattack Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Counterattack_Tactics, anchor=(NW), tag="Counterattack_Tactics")
            elif Alliedcommanders_premade[i] == 'Defensive Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Defensive_Tactics, anchor=(NW), tag="Defensive_Tactics")
            elif Alliedcommanders_premade[i] == 'Guards Motor Coordination Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Guards_Motor_Coordination_Tactics, anchor=(NW), tag="Guards_Motor_Coordination_Tactics")
            elif Alliedcommanders_premade[i] == 'Guard Rifle Combined Arms Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Guard_Rifle_Combined_Arms_Tactics, anchor=(NW), tag="Guard_Rifle_Combined_Arms_Tactics")
            elif Alliedcommanders_premade[i] == 'Lend Lease Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Lend_Lease_Tactics, anchor=(NW), tag="Lend_Lease_Tactics")
            elif Alliedcommanders_premade[i] == 'Mechanized Support Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Mechanized_Support_Tactics, anchor=(NW), tag="Mechanized_Support_Tactics")
            elif Alliedcommanders_premade[i] == 'NKVD Disruption Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=NKVD_Disruption_Tactics, anchor=(NW), tag="NKVD_Disruption_Tactics")
            elif Alliedcommanders_premade[i] == 'Partisan Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Partisan_Tactics, anchor=(NW), tag="Partisan_Tactics")
            elif Alliedcommanders_premade[i] == 'Shock Motor Heavy Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Shock_Motor_Heavy_Tactics, anchor=(NW), tag="Shock_Motor_Heavy_Tactics")
            elif Alliedcommanders_premade[i] == 'Shock Rifle Frontline Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Shock_Rifle_Frontline_Tactics, anchor=(NW), tag="Shock_Rifle_Frontline_Tactics")
            elif Alliedcommanders_premade[i] == 'Soviet Combined Arms Army':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Soviet_Combined_Arms_Army, anchor=(NW), tag="Soviet_Combined_Army")
            elif Alliedcommanders_premade[i] == 'Soviet Industry Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Soviet_Industry_Tactics, anchor=(NW), tag="Soviet_Industry_Tactics")
            elif Alliedcommanders_premade[i] == 'Soviet Reserve Army':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Soviet_Reserve_Army, anchor=(NW), tag="Soviet_Reserve_Army")
            elif Alliedcommanders_premade[i] == 'Soviet Shock Army':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Soviet_Shock_Army, anchor=(NW), tag="Soviet_Shock_Army")
            elif Alliedcommanders_premade[i] == 'Tank Hunter Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Tank_Hunter_Tactics, anchor=(NW), tag="Tank_Hunter_Tactics")
            elif Alliedcommanders_premade[i] == 'Terror Tactics':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Terror_Tactics, anchor=(NW), tag="Terror_Tactics")
            else:
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Urban_Defense_Tactics, anchor=(NW), tag="Urban_Defense_Tactics") 
        elif AlliedFactions_premade[i] == 'USF':
            canvas.create_image(flag_right,flag_y_axis+(i*i_distance), image=USF_Image, anchor=(NW), tag="USF_Image")
            if Alliedcommanders_premade[i] == 'Airborne Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Airborne_Company, anchor=(NW), tag="Airborne_Company")
            elif Alliedcommanders_premade[i] == 'Heavy Cavalry Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Heavy_Cavalry_Company, anchor=(NW), tag="Heavy_Cavalry_Company")
            elif Alliedcommanders_premade[i] == 'Infantry Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Infantry_Company, anchor=(NW), tag="Infantry_Company")
            elif Alliedcommanders_premade[i] == 'Mechanized Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Mechanized_Company, anchor=(NW), tag="Mechanized_Company")
            elif Alliedcommanders_premade[i] == 'Recon Support Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Recon_Support_Company, anchor=(NW), tag="Recon_Support_Company")
            elif Alliedcommanders_premade[i] == 'Rifle Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Rifle_Company, anchor=(NW), tag="Rifle_Company")
            elif Alliedcommanders_premade[i] == 'Urban Assault Company':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Urban_Assault_Company, anchor=(NW), tag="Urban_Assault_Company")     
            else:
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Tactical_Support_Company, anchor=(NW), tag="Tactical_Support_Company")
        else:
            canvas.create_image(flag_right,flag_y_axis+(i*i_distance), image=Brits_Image, anchor=(NW), tag="UK_Image")
            if Alliedcommanders_premade[i] == 'Advanced Emplacement Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Advanced_Emplacement_Regiment  , anchor=(NW), tag="Advanced_Emplacement_Regiment")
            elif Alliedcommanders_premade[i] == 'Commando Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Commando_Regiment, anchor=(NW), tag="Commando_Regiment")
            elif Alliedcommanders_premade[i] == 'Mobile Assault Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Mobile_Assault_Regiment, anchor=(NW), tag="Mobile_Assault_Regiment")
            elif Alliedcommanders_premade[i] == 'Royal Artillery Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Royal_Artillery_Regiment, anchor=(NW), tag="Royal_Artillery_Regiment")
            elif Alliedcommanders_premade[i] == 'Royal Engineer Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Royal_Engineer_Regiment, anchor=(NW), tag="Royal_Engineer_Regiment")
            elif Alliedcommanders_premade[i] == 'Special Weapons Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Special_Weapons_Regiment, anchor=(NW), tag="Special_Weapons_Regiment")
            elif Alliedcommanders_premade[i] == 'Tactical Support Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Tactical_Support_Regiment, anchor=(NW), tag="Special_Weapons_Regiment")                
            elif Alliedcommanders_premade[i] =='Vanguard Operations Regiment':
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Vanguard_Operation  , anchor=(NW), tag="Vanguard_Operation")
            else:
                canvas.create_image(x_axis_allied,y_axis+(i*i_distance), image=Lend_Lease_Assault_Regiment  , anchor=(NW), tag="Lend Lease Assault Regiment")






#################################### Automatch AxisTeam ################################
def TeamResults_Automatch_axis(Namelist_axis_automatch,AxisFactions_automatch,Axiscommanders_automatch):
    for i in range(len(Namelist_axis_automatch)):
        canvas.create_text(names_x_axis_left,names_y_axis+(i*i_distance),text=str(Namelist_axis_automatch[i]),fill = 'black', font=('times',12,'bold'), anchor = W, tag="AxisPlayersLabelAutomatch")
        canvas.create_text(names_x_axis_left,commanders_y_axis+(i*i_distance),text=str(Axiscommanders_automatch[i]),fill = 'black', font=('times',12,'bold'), anchor = W, tag="AxisCommandersAutomatch")
        if AxisFactions_automatch[i] == 'OKW':
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=OKW_Image, anchor=(NW), tag="OKW_Image")
            if Axiscommanders_automatch[i] == 'Breakthrough Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Breakthrough_Doctrine, anchor=(NW), tag="Breakthrough_Doctrine_OKW")
            elif Axiscommanders_automatch[i] == 'Elite Armored Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Elite_Armored_Doctrine, anchor=(NW), tag="Elite_Armored_Doctrine")
            elif Axiscommanders_automatch[i] == 'Feuersturm Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Feuersturm_Doctrine, anchor=(NW), tag="Feuersturm_Doctrine")
            elif Axiscommanders_automatch[i] == 'Fortifications Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Fortifications_Doctrine, anchor=(NW), tag="Fortifications_Doctrine")
            elif Axiscommanders_automatch[i] == 'Grand Offensive Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Grand_Offensive_Doctrine, anchor=(NW), tag="Grand_Offensive_Doctrine")
            elif Axiscommanders_automatch[i] == 'Luftwaffe Ground Forces Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Luftwaffe_Ground_Forces_Doctrine, anchor=(NW), tag="Luftwaffe_Ground_Forces_Doctrine")
            elif Axiscommanders_automatch[i] == 'Overwatch Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Overwatch_Doctrine, anchor=(NW), tag="Overwatch_Doctrine")
            elif Axiscommanders_automatch[i] == 'Scavenge Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Scavenge_Doctrine, anchor=(NW), tag="Scavenge_Doctrine")
            else:
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Special_Operations_Doctrine, anchor=(NW), tag="Special_Operations_Doctrine")
        else:  
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=GER_Image, anchor=(NW), tag="Wehrmacht_Image")
            if Axiscommanders_automatch[i] == 'Assault Support Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Assault_Support_Doctrine, anchor=(NW), tag="Assault_Support_Doctrine_OKW")  
            elif Axiscommanders_automatch[i] == 'Blitzkrieg Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Blitzkrieg_Doctrine, anchor=(NW), tag="Blitzkrieg_Doctrine")
            elif Axiscommanders_automatch[i] == 'Close Air Support Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Close_Air_Support_Doctrine, anchor=(NW), tag="Close_Air_Support_Doctrine")    
            elif Axiscommanders_automatch[i] == 'Defensive Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Defensive_Doctrine, anchor=(NW), tag="Defensive_Doctrine")
            elif Axiscommanders_automatch[i] == 'Elite Troops Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Elite_Troops_Doctrine, anchor=(NW), tag="Elite_Troops_Doctrine")                       
            elif Axiscommanders_automatch[i] == 'Encirclement Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Encirclement_Doctrine, anchor=(NW), tag="Encirclement_Doctrine")
            elif Axiscommanders_automatch[i] == 'Festung Armor Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Festung_Armor_Doctrine, anchor=(NW), tag="Festung_Armor_Doctrine")    
            elif Axiscommanders_automatch[i] == 'Festung Support Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Festung_Support_Doctrine, anchor=(NW), tag="Festung_Support_Doctrine")
            elif Axiscommanders_automatch[i] == 'Fortified Armor Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Fortified_Armor_Doctrine, anchor=(NW), tag="Fortified Armor Doctrine")  
            elif Axiscommanders_automatch[i] == 'German Infantry Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=German_Infantry_Doctrine, anchor=(NW), tag="German_Infantry_Doctrine")
            elif Axiscommanders_automatch[i] == 'German Mechanized Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=German_Mechanized_Doctrine, anchor=(NW), tag="German_Mechanized_Doctrine")    
            elif Axiscommanders_automatch[i] == 'Jaeger Armor Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Jaeger_Armor_Doctrine, anchor=(NW), tag="Jaeger_Armor_Doctrine")
            elif Axiscommanders_automatch[i] == 'Jeager Infantry Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Jeager_Infantry_Doctrine, anchor=(NW), tag="Jeager_Infantry_Doctrine")  
            elif Axiscommanders_automatch[i] == 'Lighting War Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Lighting_War_Doctrine, anchor=(NW), tag="Lighting_War_Doctrine")
            elif Axiscommanders_automatch[i] == 'Luftwaffe Supply Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Luftwaffe_Supply_Doctrine, anchor=(NW), tag="Luftwaffe_Supply_Doctrine")    
            elif Axiscommanders_automatch[i] == 'Mechanized Assault Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mechanized_Assault_Doctrine, anchor=(NW), tag="Mechanized_Assault_Doctrine")
            elif Axiscommanders_automatch[i] == 'Mobile Defense Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mobile_Defense_Doctrine, anchor=(NW), tag="Mobile_Defense_Doctrine")  
            elif Axiscommanders_automatch[i] == 'Osttruppen Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Osttruppen_Doctrine, anchor=(NW), tag="Osttruppen_Doctrine")
            elif Axiscommanders_automatch[i] == 'Spearhead Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Spearhead_Doctrine, anchor=(NW), tag="Spearhead_Doctrine")  
            elif Axiscommanders_automatch[i] == 'Storm Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Storm_Doctrine, anchor=(NW), tag="Storm_Doctrine")
            else:
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Strategic_Reserves_Doctrine, anchor=(NW), tag="Strategic_Reserves_Doctrine") 


################################### Automatch AlliedTeam ################################
def TeamResults_Automatch_allies(Namelist_allied_automatch,AlliedFactions_automatch,Alliedcommanders_Automatch): 
    for i in range(len(Namelist_allied_automatch)):
        canvas.create_text(names_x_axis_left,names_y_axis+(i*i_distance),text=str(Namelist_allied_automatch[i]),fill = 'black', font=('times',12,'bold'), anchor = W, tag="AlliedPlayersAutomatch")
        canvas.create_text(names_x_axis_left,commanders_y_axis+(i*i_distance),text=str(Alliedcommanders_Automatch[i]),fill = 'black', font=('times',12,'bold'), anchor = W, tag="AlliedCommandersAutomatch")
        if AlliedFactions_automatch[i] == 'USSR':
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=USSR_Image, anchor=(NW), tag="Sovjet_Image")
            if Alliedcommanders_Automatch[i] == 'Advanced Warfare Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Advanced_Warfare_Tactics, anchor=(NW), tag="Advanced_Warfare_Tactics ")
            elif Alliedcommanders_Automatch[i] == 'Airborne Troops Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Airborne_Troops_Tactics, anchor=(NW), tag="Airborne_Troops_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Anti Infantry Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Anti_Infantry_Tactics, anchor=(NW), tag="Anti_Infantry_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Armored Assault Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Armored_Assault_Doctrine, anchor=(NW), tag="Armored_Assault_Doctrine")     
            elif Alliedcommanders_Automatch[i] == 'Conscripts Support Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Conscripts_Support_Tactics, anchor=(NW), tag="Conscripts_Support_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Counterattack Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Counterattack_Tactics, anchor=(NW), tag="Counterattack_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Defensive Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Defensive_Tactics, anchor=(NW), tag="Defensive_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Guards Motor Coordination Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Guards_Motor_Coordination_Tactics, anchor=(NW), tag="Guards_Motor_Coordination_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Guard Rifle Combined Arms Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Guard_Rifle_Combined_Arms_Tactics, anchor=(NW), tag="Guard_Rifle_Combined_Arms_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Lend Lease Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Lend_Lease_Tactics, anchor=(NW), tag="Lend_Lease_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Mechanized Support Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mechanized_Support_Tactics, anchor=(NW), tag="Mechanized_Support_Tactics")
            elif Alliedcommanders_Automatch[i] == 'NKVD Disruption Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=NKVD_Disruption_Tactics, anchor=(NW), tag="NKVD_Disruption_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Partisan Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Partisan_Tactics, anchor=(NW), tag="Partisan_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Shock Motor Heavy Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Shock_Motor_Heavy_Tactics, anchor=(NW), tag="Shock_Motor_Heavy_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Shock Rifle Frontline Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Shock_Rifle_Frontline_Tactics, anchor=(NW), tag="Shock_Rifle_Frontline_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Soviet Combined Arms Army':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Soviet_Combined_Arms_Army, anchor=(NW), tag="Soviet_Combined_Army")
            elif Alliedcommanders_Automatch[i] == 'Soviet Industry Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Soviet_Industry_Tactics, anchor=(NW), tag="Soviet_Industry_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Soviet Reserve Army':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Soviet_Reserve_Army, anchor=(NW), tag="Soviet_Reserve_Army")
            elif Alliedcommanders_Automatch[i] == 'Soviet Shock Army':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Soviet_Shock_Army, anchor=(NW), tag="Soviet_Shock_Army")
            elif Alliedcommanders_Automatch[i] == 'Tank Hunter Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Tank_Hunter_Tactics, anchor=(NW), tag="Tank_Hunter_Tactics")
            elif Alliedcommanders_Automatch[i] == 'Terror Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Terror_Tactics, anchor=(NW), tag="Terror_Tactics")
            else:
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Urban_Defense_Tactics, anchor=(NW), tag="Urban_Defense_Tactics") 
        elif AlliedFactions_automatch[i] == 'USF':
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=USF_Image, anchor=(NW), tag="USF_Image")
            if Alliedcommanders_Automatch[i] == 'Airborne Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Airborne_Company, anchor=(NW), tag="Airborne_Company")
            elif Alliedcommanders_Automatch[i] == 'Heavy Cavalry Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Heavy_Cavalry_Company, anchor=(NW), tag="Heavy_Cavalry_Company")
            elif Alliedcommanders_Automatch[i] == 'Infantry Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Infantry_Company, anchor=(NW), tag="Infantry_Company")
            elif Alliedcommanders_Automatch[i] == 'Mechanized Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mechanized_Company, anchor=(NW), tag="Mechanized_Company")
            elif Alliedcommanders_Automatch[i] == 'Recon Support Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Recon_Support_Company, anchor=(NW), tag="Recon_Support_Company")
            elif Alliedcommanders_Automatch[i] == 'Rifle Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Rifle_Company, anchor=(NW), tag="Rifle_Company")
            elif Alliedcommanders_Automatch[i] == 'Urban Assault Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Urban_Assault_Company, anchor=(NW), tag="Urban_Assault_Company")     
            else:
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Tactical_Support_Company, anchor=(NW), tag="Tactical_Support_Company")
        else:
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=Brits_Image, anchor=(NW), tag="UK_Image")
            if Alliedcommanders_Automatch[i] == 'Advanced Emplacement Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Advanced_Emplacement_Regiment  , anchor=(NW), tag="Advanced_Emplacement_Regiment")
            elif Alliedcommanders_Automatch[i] == 'Commando Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Commando_Regiment, anchor=(NW), tag="Commando_Regiment")
            elif Alliedcommanders_Automatch[i] == 'Mobile Assault Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mobile_Assault_Regiment, anchor=(NW), tag="Mobile_Assault_Regiment")
            elif Alliedcommanders_Automatch[i] == 'Royal Artillery Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Royal_Artillery_Regiment, anchor=(NW), tag="Royal_Artillery_Regiment")
            elif Alliedcommanders_Automatch[i] == 'Royal Engineer Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Royal_Engineer_Regiment, anchor=(NW), tag="Royal_Engineer_Regiment")
            elif Alliedcommanders_Automatch[i] == 'Special Weapons Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Special_Weapons_Regiment, anchor=(NW), tag="Special_Weapons_Regiment")
            elif Alliedcommanders_Automatch[i] == 'Tactical Support Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Tactical_Support_Regiment, anchor=(NW), tag="Special_Weapons_Regiment")                
            elif Alliedcommanders_Automatch[i] =='Vanguard Operations Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Vanguard_Operation  , anchor=(NW), tag="Vanguard_Operation")
            else:
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Lend_Lease_Assault_Regiment  , anchor=(NW), tag="Lend Lease Assault Regiment")
################################### Automatch RANDOM ################################
def TeamResults_Automatch_RANDOM(Namelist_random_automatch,RandomFactions,Randomcommanders_Automatch): 
    for i in range(len(Namelist_random_automatch)):
        canvas.create_text(names_x_axis_left,names_y_axis+(i*i_distance),text=str(Namelist_random_automatch[i]),fill = 'black', font=('times',12,'bold'), anchor = W, tag="RandomPlayersAutomatch")
        canvas.create_text(names_x_axis_left,commanders_y_axis+(i*i_distance),text=str(Randomcommanders_Automatch[i]),fill = 'black', font=('times',12,'bold'), anchor = W, tag="RandomCommandersAutomatch")
        if RandomFactions[i] == 'OKW':
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=OKW_Image, anchor=(NW), tag="OKW_Image")
            if Randomcommanders_Automatch[i] == 'Breakthrough Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Breakthrough_Doctrine, anchor=(NW), tag="Breakthrough_Doctrine_OKW")
            elif Randomcommanders_Automatch[i] == 'Elite Armored Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Elite_Armored_Doctrine, anchor=(NW), tag="Elite_Armored_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Feuersturm Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Feuersturm_Doctrine, anchor=(NW), tag="Feuersturm_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Fortifications Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Fortifications_Doctrine, anchor=(NW), tag="Fortifications_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Grand Offensive Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Grand_Offensive_Doctrine, anchor=(NW), tag="Grand_Offensive_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Luftwaffe Ground Forces Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Luftwaffe_Ground_Forces_Doctrine, anchor=(NW), tag="Luftwaffe_Ground_Forces_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Overwatch Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Overwatch_Doctrine, anchor=(NW), tag="Overwatch_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Scavenge Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Scavenge_Doctrine, anchor=(NW), tag="Scavenge_Doctrine")
            else:
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Special_Operations_Doctrine, anchor=(NW), tag="Special_Operations_Doctrine")
        elif RandomFactions[i] == 'Wehrmacht':  
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=GER_Image, anchor=(NW), tag="Wehrmacht_Image")
            if Randomcommanders_Automatch[i] == 'Assault Support Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Assault_Support_Doctrine, anchor=(NW), tag="Assault_Support_Doctrine_OKW")  
            elif Randomcommanders_Automatch[i] == 'Blitzkrieg Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Blitzkrieg_Doctrine, anchor=(NW), tag="Blitzkrieg_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Close Air Support Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Close_Air_Support_Doctrine, anchor=(NW), tag="Close_Air_Support_Doctrine")    
            elif Randomcommanders_Automatch[i] == 'Defensive Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Defensive_Doctrine, anchor=(NW), tag="Defensive_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Elite Troops Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Elite_Troops_Doctrine, anchor=(NW), tag="Elite_Troops_Doctrine")                       
            elif Randomcommanders_Automatch[i] == 'Encirclement Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Encirclement_Doctrine, anchor=(NW), tag="Encirclement_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Festung Armor Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Festung_Armor_Doctrine, anchor=(NW), tag="Festung_Armor_Doctrine")    
            elif Randomcommanders_Automatch[i] == 'Festung Support Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Festung_Support_Doctrine, anchor=(NW), tag="Festung_Support_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Fortified Armor Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Fortified_Armor_Doctrine, anchor=(NW), tag="Fortified Armor Doctrine")  
            elif Randomcommanders_Automatch[i] == 'German Infantry Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=German_Infantry_Doctrine, anchor=(NW), tag="German_Infantry_Doctrine")
            elif Randomcommanders_Automatch[i] == 'German Mechanized Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=German_Mechanized_Doctrine, anchor=(NW), tag="German_Mechanized_Doctrine")    
            elif Randomcommanders_Automatch[i] == 'Jaeger Armor Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Jaeger_Armor_Doctrine, anchor=(NW), tag="Jaeger_Armor_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Jeager Infantry Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Jeager_Infantry_Doctrine, anchor=(NW), tag="Jeager_Infantry_Doctrine")  
            elif Randomcommanders_Automatch[i] == 'Lighting War Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Lighting_War_Doctrine, anchor=(NW), tag="Lighting_War_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Luftwaffe Supply Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Luftwaffe_Supply_Doctrine, anchor=(NW), tag="Luftwaffe_Supply_Doctrine")    
            elif Randomcommanders_Automatch[i] == 'Mechanized Assault Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mechanized_Assault_Doctrine, anchor=(NW), tag="Mechanized_Assault_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Mobile Defense Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mobile_Defense_Doctrine, anchor=(NW), tag="Mobile_Defense_Doctrine")  
            elif Randomcommanders_Automatch[i] == 'Osttruppen Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Osttruppen_Doctrine, anchor=(NW), tag="Osttruppen_Doctrine")
            elif Randomcommanders_Automatch[i] == 'Spearhead Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Spearhead_Doctrine, anchor=(NW), tag="Spearhead_Doctrine")  
            elif Randomcommanders_Automatch[i] == 'Storm Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Storm_Doctrine, anchor=(NW), tag="Storm_Doctrine")
            else:
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Strategic_Reserves_Doctrine, anchor=(NW), tag="Strategic_Reserves_Doctrine")  
        elif RandomFactions[i] == 'USSR':
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=USSR_Image, anchor=(NW), tag="Sovjet_Image")
            if Randomcommanders_Automatch[i] == 'Advanced Warfare Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Advanced_Warfare_Tactics, anchor=(NW), tag="Advanced_Warfare_Tactics ")
            elif Randomcommanders_Automatch[i] == 'Airborne Troops Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Airborne_Troops_Tactics, anchor=(NW), tag="Airborne_Troops_Tactics")
            elif Randomcommanders_Automatch[i] == 'Anti Infantry Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Anti_Infantry_Tactics, anchor=(NW), tag="Anti_Infantry_Tactics")
            elif Randomcommanders_Automatch[i] == 'Armored Assault Doctrine':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Armored_Assault_Doctrine, anchor=(NW), tag="Armored_Assault_Doctrine")     
            elif Randomcommanders_Automatch[i] == 'Conscripts Support Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Conscripts_Support_Tactics, anchor=(NW), tag="Conscripts_Support_Tactics")
            elif Randomcommanders_Automatch[i] == 'Counterattack Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Counterattack_Tactics, anchor=(NW), tag="Counterattack_Tactics")
            elif Randomcommanders_Automatch[i] == 'Defensive Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Defensive_Tactics, anchor=(NW), tag="Defensive_Tactics")
            elif Randomcommanders_Automatch[i] == 'Guards Motor Coordination Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Guards_Motor_Coordination_Tactics, anchor=(NW), tag="Guards_Motor_Coordination_Tactics")
            elif Randomcommanders_Automatch[i] == 'Guard Rifle Combined Arms Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Guard_Rifle_Combined_Arms_Tactics, anchor=(NW), tag="Guard_Rifle_Combined_Arms_Tactics")
            elif Randomcommanders_Automatch[i] == 'Lend Lease Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Lend_Lease_Tactics, anchor=(NW), tag="Lend_Lease_Tactics")
            elif Randomcommanders_Automatch[i] == 'Mechanized Support Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mechanized_Support_Tactics, anchor=(NW), tag="Mechanized_Support_Tactics")
            elif Randomcommanders_Automatch[i] == 'NKVD Disruption Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=NKVD_Disruption_Tactics, anchor=(NW), tag="NKVD_Disruption_Tactics")
            elif Randomcommanders_Automatch[i] == 'Partisan Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Partisan_Tactics, anchor=(NW), tag="Partisan_Tactics")
            elif Randomcommanders_Automatch[i] == 'Shock Motor Heavy Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Shock_Motor_Heavy_Tactics, anchor=(NW), tag="Shock_Motor_Heavy_Tactics")
            elif Randomcommanders_Automatch[i] == 'Shock Rifle Frontline Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Shock_Rifle_Frontline_Tactics, anchor=(NW), tag="Shock_Rifle_Frontline_Tactics")
            elif Randomcommanders_Automatch[i] == 'Soviet Combined Arms Army':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Soviet_Combined_Arms_Army, anchor=(NW), tag="Soviet_Combined_Army")
            elif Randomcommanders_Automatch[i] == 'Soviet Industry Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Soviet_Industry_Tactics, anchor=(NW), tag="Soviet_Industry_Tactics")
            elif Randomcommanders_Automatch[i] == 'Soviet Reserve Army':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Soviet_Reserve_Army, anchor=(NW), tag="Soviet_Reserve_Army")
            elif Randomcommanders_Automatch[i] == 'Soviet Shock Army':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Soviet_Shock_Army, anchor=(NW), tag="Soviet_Shock_Army")
            elif Randomcommanders_Automatch[i] == 'Tank Hunter Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Tank_Hunter_Tactics, anchor=(NW), tag="Tank_Hunter_Tactics")
            elif Randomcommanders_Automatch[i] == 'Terror Tactics':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Terror_Tactics, anchor=(NW), tag="Terror_Tactics")
            else:
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Urban_Defense_Tactics, anchor=(NW), tag="Urban_Defense_Tactics") 
        elif RandomFactions[i] == 'USF':
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=USF_Image, anchor=(NW), tag="USF_Image")
            if Randomcommanders_Automatch[i] == 'Airborne Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Airborne_Company, anchor=(NW), tag="Airborne_Company")
            elif Randomcommanders_Automatch[i] == 'Heavy Cavalry Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Heavy_Cavalry_Company, anchor=(NW), tag="Heavy_Cavalry_Company")
            elif Randomcommanders_Automatch[i] == 'Infantry Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Infantry_Company, anchor=(NW), tag="Infantry_Company")
            elif Randomcommanders_Automatch[i] == 'Mechanized Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mechanized_Company, anchor=(NW), tag="Mechanized_Company")
            elif Randomcommanders_Automatch[i] == 'Recon Support Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Recon_Support_Company, anchor=(NW), tag="Recon_Support_Company")
            elif Randomcommanders_Automatch[i] == 'Rifle Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Rifle_Company, anchor=(NW), tag="Rifle_Company")
            elif Randomcommanders_Automatch[i] == 'Urban Assault Company':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Urban_Assault_Company, anchor=(NW), tag="Urban_Assault_Company")     
            else:
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Tactical_Support_Company, anchor=(NW), tag="Tactical_Support_Company")
        else:
            canvas.create_image(flag_left,flag_y_axis+(i*i_distance), image=Brits_Image, anchor=(NW), tag="UK_Image")
            if Randomcommanders_Automatch[i] == 'Advanced Emplacement Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Advanced_Emplacement_Regiment  , anchor=(NW), tag="Advanced_Emplacement_Regiment")
            elif Randomcommanders_Automatch[i] == 'Commando Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Commando_Regiment, anchor=(NW), tag="Commando_Regiment")
            elif Randomcommanders_Automatch[i] == 'Mobile Assault Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Mobile_Assault_Regiment, anchor=(NW), tag="Mobile_Assault_Regiment")
            elif Randomcommanders_Automatch[i] == 'Royal Artillery Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Royal_Artillery_Regiment, anchor=(NW), tag="Royal_Artillery_Regiment")
            elif Randomcommanders_Automatch[i] == 'Royal Engineer Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Royal_Engineer_Regiment, anchor=(NW), tag="Royal_Engineer_Regiment")
            elif Randomcommanders_Automatch[i] == 'Special Weapons Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Special_Weapons_Regiment, anchor=(NW), tag="Special_Weapons_Regiment")
            elif Randomcommanders_Automatch[i] == 'Tactical Support Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Tactical_Support_Regiment, anchor=(NW), tag="Special_Weapons_Regiment")                
            elif Randomcommanders_Automatch[i] =='Vanguard Operations Regiment':
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Vanguard_Operation  , anchor=(NW), tag="Vanguard_Operation")
            else:
                canvas.create_image(x_axis,y_axis+(i*i_distance), image=Lend_Lease_Assault_Regiment  , anchor=(NW), tag="Lend Lease Assault Regiment")


screen.mainloop()