#Le menu principal avec les differents jeux. On choisi tout en console. Pas de bibliotheque graphique pour l'instant
# -*- coding: latin-1 -*-

import os
from multiprocessing import Pool
import time
import datetime
import random
import sys
import threading
import os.path
import test1Scalable #mettre des commentaires ici pour que ca marche sans rasberry
# enlever le commentaire de convert to hexa
import key

#clear = lambda: os.system('cls') #windows
os.system('clear')
test1Scalable.mainFunction()
userName=""
stat=["","",""]
statG=""
statTime=["","",""]
statGTime=""
def saveGame():
	global stat
	global statG
	global statTime
	global statGTime
	global userName
	indexS=0
	contenu=[]
	fileName="statFile.txt"
	existUser=0
	if os.path.isfile(fileName):
		theFile=open(fileName,"r") 
		contenu=theFile.readlines()
		theFile.close()
		for i in range(len(contenu)):
			if userName in contenu[i]:
				print(userName+", nous sommes heureux de votre retour sur l'application. Nous avons ajouté à votre profil des informations.")
				indexS=i
				existUser=1
			contenu[i]=contenu[i].replace("\n","")
	if existUser==0:
		print(userName+" Nous avons créé votre sauvegarde, elle permet de suivre votre évolution pour améliorer notre dispositif")
		indexS=len(contenu)
		contenu.extend([userName,"0","0","0","0","0","0","0","0"])
	for i in range(3):
		contenu[indexS+1+i]=contenu[indexS+1+i]+stat[i]
	for i in range(3):
		contenu[indexS+1+3+i]=contenu[indexS+1+3+i]+statTime[i]
	contenu[indexS+1+6]=contenu[indexS+1+6]+statG
	contenu[indexS+1+6+1]=contenu[indexS+1+6+1]+statGTime

	theFile=open(fileName,"w")
	theFile.write('\n'.join(contenu))
def stopGame():
	os.system('clear')
	print("Au revoir "+userName + " :)")
	saveGame()
	test1Scalable.destroy()
	exit()
def login():
	print("Veuillez entrer la premiere lettre de votre prénom")
	global userName
	userName= key.queue.get() #raw_input("")#raw input ne fonctionne pas avec les threads
	userName=userName.lower()
	print("Merci "+userName)
	firstMenu()
def moreInformation():
	os.system('clear')
	print("Les differents jeux on pour objectif d'évaluer les limites du prototype, les améliorations à faire pour la prochaine version.")
	print("D'évaluer l'apprentissage de differents utilisateurs avec un outil de statistique. Suivre des utilisateurs sur differentes seance d'apprentissage.")
	print("De voir les limites sur les differents jeux représentant 3 perceptions differentes. La perception de la localisation, des mouvements et des motifs.")
	print("")
	print("0 pour retourner au menu principal")
	print("1 pour quitter")
	choice = key.queue.get()
	if(choice=='0'):
		firstMenu()
	else :
		stopGame()
def installationSuite(x,y):
	motif=[[0 for i in range(x)] for j in range(y)]
	for j in range(0,y):
		for i in range(0,x):
			motif[i][j]=1
			os.system('clear')
			print("La pin "+str(j*x+i)+" se met à clignoter")
			print("La pin aux coordonnées: x="+str(i)+" y="+str(j))
			print(motif)
			sendDataToDisplay(motif,x,y,1)
			print("")
			print("0 pour la pin suivante")
			print("1 pour retourner au menu principal")
			choice = key.queue.get()
			motif[i][j]=0
			if(choice=='1'):
				firstMenu()
	os.system('clear')
	print("Vous etes arrivé à la fin de l'installation.")
	print("Appuyer sur 0 pour retourner au menu principal")
	choice = key.queue.get() 
	firstMenu()
def installation():
	os.system('clear')
	print("Bienvenue au programme d'installation du système")
	print("Il permet de faciliter le branchement des cables")
	print("Veuillez donner la largeur x de l'écran?")
	x=int(key.queue.get())
	os.system('clear')
	print("Ok, l'écran fait "+str(x)+" de large.")
	print("Quelle est la hauteur y de l'écran?")
	y=int(key.queue.get())
	os.system('clear')
	print("L'écran fait "+str(x)+" de large et "+str(y)+" de hauteur.")
	print("Pour faciliter le branchement, chacune des sorties vont alterner entre 1 et 0 les unes après les autres.")
	print("Choisisez :")
	print("0 pour commencer")
	print("1 pour retourner au menu principal")
	print("2 pour quitter")
	choice = key.queue.get()
	if(choice=='0'):
		installationSuite(x,y)
	elif(choice=='1'):
		firstMenu()
	else :
		stopGame()
def gameMenu():
	displayNone()
	os.system('clear')
	print("choisisez votre jeu :")
	print("0 pour démineur")
	print("1 pour guitar hero")
	print("2 pour des chiffres et pas de lettre")
	print("3 pour retourner au menu principal")
	print("4 pour quitter")
	choice=key.queue.get()
	if(choice=='0'):
		initGame(0)
	elif(choice=='1'):
		initGame(1)
	elif(choice=='2'):
		initGame(2)
	elif(choice=='3'):
		firstMenu()
	else :
		stopGame()
def firstMenu():
	print (userName.capitalize()+", bienvenue sur le menu principal")
	print ("choisisez :")
	print ("0 pour en savoir plus sur le but des jeux")
	print ("1 pour jouer")
	print ("2 pour le programme d'installation")
	print ("3 pour quitter")
	choice = key.queue.get()
	if(choice=='0'):
		moreInformation()
	elif(choice=='1'):
		gameMenu()
	elif(choice=='2'):
		installation()
	else :
		stopGame()

def initGame(game):
	os.system('clear')
	if(game==0):
		print("Bienvenue au jeu de démineur")
		print("10 bombes vont apparaitre les unes à après les autres.")
		print("Vous devrez dire à quelles coordonneées elles se trouvent avec le pavé numérique")
		print("Vous serez noté sur le temps pour localiser les 10 bombes et le nombre de bombe déminé")
	elif(game==1):
		print("Bienvenue au jeu de guitar héro (jeu non officiel inspirant le jeu Guitar Hero")
		print("Vous allez avoir 10 motifs qui vont etre dessiné sur votre peau.")
		print("Si vous sentez un balayage vers la gauche appuyer sur 4(touche de gauche du pavé numérique")
		print("Pour la droite 6, pour le haut 8, pour le bas 2")
		print("Vous serez noté sur le temps pour suivre la partition et le nombre de note respecté")
	elif(game==2):
		print("Bienvenue au jeu des chiffres et pas de lettre")
		print("L'objectif du jeu et de reconnaitre les chiffres qui seront dessiné sur votre bras")
		print("Les chiffres seront afficher au hasard et vous le saisirez sur le pavé numérique")
		print("Vous serez noté sur le temps pour reconnaitre les 10 chiffres et le nombre de réussite")

	print("")
	print("Etes vous pret?")
	print("0 pour oui")
	print("1 pour retourner au menu principal")
	print("2 pour quitter")
	choice = key.queue.get()
	if(choice=='0'):
		gameLaunch(game)
	elif(choice=='1'):
		firstMenu()
	else :
		stopGame()
def sendDataToDisplay(motif,x,y,motifNb,frequence=0.5,sleeptime=0.5):
	motifF=[[[0 for i in range(x)] for j in range(y)]for z in range(motifNb+1)]
	for z in range(motifNb+1):
		for i in range(x):
			for j in range(y):
				if z<motifNb:
					if motifNb==1:
						motifF[z][i][j]=motif[i][j]
					else:
						motifF[z][i][j]=motif[z][i][j]
				else:
					motifF[z][i][j]=0
	#print(motifF)
	test1Scalable.convertToHexa(motifF,x,y,motifNb+1,frequence,sleeptime)#ici les commentaires pour marcher sans rasberry
def displayNone():
	x=4
	y=4
	motif=[[0 for i in range(x)] for j in range(y)]
	sendDataToDisplay(motif,x,y,1)
def mineDisplay(value):
	x=3
	y=3
	motif=[[0 for i in range(x)] for j in range(y)]
	value=value-1
	val1=int((value-value%3)/3)
	motif[val1][value%3]=1
	sendDataToDisplay(motif,x,y,1)
def guitarDisplay(value):
	x=4
	y=4
	nbMotif=7
	motifS=[[[0 for i in range(x)] for j in range(y)]for z in range(nbMotif)] 
	if value==2:
		motifS[0]=[[1, 1, 1, 1], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0]]
		motifS[1]=[[0, 0, 0, 0], 
		 [1, 1, 1, 1], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0]]
		motifS[2]=[[0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [1, 1, 1, 1], 
		 [0, 0, 0, 0]]
		motifS[3]=[[0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [1, 1, 1, 1]]
	elif value==4:
		motifS[0]=[[0, 0, 0, 1], 
		 [0, 0, 0, 1], 
		 [0, 0, 0, 1], 
		 [0, 0, 0, 1]]
		motifS[1]=[[0, 0, 1, 0], 
		 [0, 0, 1, 0], 
		 [0, 0, 1, 0], 
		 [0, 0, 1, 0]]
		motifS[2]=[[0, 1, 0, 0], 
		 [0, 1, 0, 0], 
		 [0, 1, 0, 0], 
		 [0, 1, 0, 0]]
		motifS[3]=[[1, 0, 0, 0], 
		 [1, 0, 0, 0], 
		 [1, 0, 0, 0], 
		 [1, 0, 0, 0]]
	elif value==6:
		motifS[0]=[[1, 0, 0, 0], 
		 [1, 0, 0, 0], 
		 [1, 0, 0, 0], 
		 [1, 0, 0, 0]]
		motifS[1]=[[0, 1, 0, 0], 
		 [0, 1, 0, 0], 
		 [0, 1, 0, 0], 
		 [0, 1, 0, 0]]
		motifS[2]=[[0, 0, 1, 0], 
		 [0, 0, 1, 0], 
		 [0, 0, 1, 0], 
		 [0, 0, 1, 0]]
		motifS[3]=[[0, 0, 0, 1], 
		 [0, 0, 0, 1], 
		 [0, 0, 0, 1], 
		 [0, 0, 0, 1]]
	else :
		motifS[0]=[[0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [1, 1, 1, 1]]
		motifS[1]=[[0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [1, 1, 1, 1], 
		 [0, 0, 0, 0]]
		motifS[2]=[[0, 0, 0, 0], 
		 [1, 1, 1, 1], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0]]
		motifS[3]=[[1, 1, 1, 1], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0]]
	sendDataToDisplay(motifS,x,y,nbMotif,0.1,0.5)
def digitDisplay(value):
	x=4
	y=4
	motifS=[[0 for i in range(x)] for j in range(y)]
	if value==0 :
		motifS=[[0, 1, 1, 0], 
		 [1, 0, 0, 1], 
		 [1, 0, 0, 1], 
		 [0, 1, 1, 0]]
	elif value==1 :
		motifS=[[0, 0, 1, 0], 
		 [0, 0, 1, 0], 
		 [0, 0, 1, 0], 
		 [0, 0, 1, 0]]
	elif value==2 :
		motifS=[[1, 1, 1, 0], 
		 [0, 0, 0, 1], 
		 [1, 0, 0, 0], 
		 [1, 1, 1, 1]]
	elif value==3 :
		motifS=[[1, 1, 1, 1], 
		 [0, 0, 0, 1], 
		 [0, 1, 1, 1], 
		 [1, 1, 1, 1]]
	elif value==4 :
		motifS=[[1, 0, 0, 1], 
		 [1, 1, 1, 1], 
		 [0, 0, 0, 1], 
		 [0, 0, 0, 1]]
	elif value==5 :
		motifS=[[1, 1, 1, 1], 
		 [1, 0, 0, 0], 
		 [0, 1, 1, 1], 
		 [1, 1, 1, 1]]
	elif value==6 :
		motifS=[[1, 0, 0, 0], 
		 [1, 0, 0, 0], 
		 [1, 1, 1, 1], 
		 [1, 0, 0, 1]]
	elif value==7 :
		motifS=[[1, 1, 1, 1], 
		 [0, 0, 0, 1], 
		 [0, 0, 0, 1], 
		 [0, 0, 0, 1]]
	elif value==8 :
		motifS=[[1, 0, 0, 1], 
		 [1, 1, 1, 1], 
		 [1, 1, 1, 1], 
		 [1, 0, 0, 1]]
	else :
		motifS=[[1, 0, 0, 1], 
		 [1, 1, 1, 1], 
		 [0, 0, 0, 1], 
		 [0, 0, 0, 1]] 
	sendDataToDisplay(motifS,x,y,1)
def gameLaunch(game):
	global stat
	global statG
	global statTime
	global statGTime
	score=0
	debut=time.time()
	oldTime=time.time()
	for i in range(0,10):
		os.system('clear')
		oldTime=time.time()
		timeSpend=int(oldTime-debut)
		print("Score = "+str(score)+"/10 Temps ecoulé : "+str(timeSpend))
		if(game==0):
			print("Où se trouve la bombe?")
			digit=random.randint(1,9)
			mineDisplay(digit)
		elif(game==1):
			print("Que dit la partition?")
			digit=random.randint(0,3)
			if(digit==0):
				digit=2
			elif(digit==1):
				digit=4
			elif(digit==2):
				digit=6
			else:
				digit=8
			guitarDisplay(digit)
		elif(game==2):
			print("Quel chiffre sens tu?")
			digit=random.randint(0,9)
			digitDisplay(digit)
		print(digit)
		guess=key.queue.get()
		result=0
		if(guess==str(digit)):
			print("Well done")
			score=score+1
			result=1
		else:
			print("you failed")
		stat[game]=stat[game]+","+str(result)
		statG=statG+","+str(result)
		VstatTime=int((time.time()-oldTime)*10)
		statTime[game]=statTime[game]+","+str(VstatTime)
		statGTime=statGTime+","+str(VstatTime)
	os.system('clear')
	displayNone()
	print("Vous avez "+str(score)+" bonne(s) réponse(s) sur 10")
	timeSpend=int(time.time()-debut)
	print("Vous avez pris "+str(timeSpend)+" secondes pour finir la partie")
	print("")
	print("0 pour recommencer")
	print("1 pour retourner au menu principal")
	print("2 pour quitter")
	choice = key.queue.get()
	if(choice=='0'):
		gameLaunch(game)
	elif(choice=='1'):
		firstMenu()
	else :
		stopGame()
login()

