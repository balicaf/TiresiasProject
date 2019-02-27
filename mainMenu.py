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
gameStop=0
hack=0
def convertMap(motif,x,y):
	motif1=[[[0 for i in range(x)] for j in range(y)]for z in range(len(motif))]
	convertT=[[0,1,2,3],
			  [4,5,6,7],
			  [8,9,10,11],
			  [12,13,14,15]]
	for z in len(motif):
		for i in range(x):
			for j in range(y):
				xy=convertT[x][y]
				x1=int((xy-xy%x)/x)
				y1=xy%x
				motif1[z][x1][y1]=motif[z][x][y]
	return motif1 

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
				print(userName+", nous sommes heureux de votre retour sur l'application. Nous avons ajout??votre profil des informations.")
				indexS=i
				existUser=1
			contenu[i]=contenu[i].replace("\n","")
	if existUser==0:
		print(userName+" Nous avons cr? votre sauvegarde, elle permet de suivre votre ?olution pour am?iorer notre dispositif")
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
	stat=["","",""]
	statG=""
	statTime=["","",""]
	statGTime=""
	time.sleep(1)
def stopGame():
	global gameStop
	if gameStop==0:
		gameStop=1
		os.system('clear')
		print("Au revoir "+userName + " :)")
		saveGame()
		time.sleep(3)
		test1Scalable.destroy()
		exit()
	else:
		print("Bug possible")
def hackSetting():
	os.system('clear')
	print("Voulez vous afficher les r?ultats ?p???(triche)")
	print("0 pour oui(triche)")
	print("1 pour non")
	choice = key.queue.get()
	if(choice=='0'):
		hack=1
	else:
		hack=0
def login():
	hackSetting()
	print("Veuillez entrer la premiere lettre de votre pr?om")
	global userName
	userName= key.queue.get() #raw_input("")#raw input ne fonctionne pas avec les threads
	userName=userName.lower()
	os.system('clear')
	print("Merci "+userName)
	firstMenu()
def moreInformation():
	os.system('clear')
	print("Les differents jeux on pour objectif d'?aluer les limites du prototype, les am?iorations ?faire pour la prochaine version.")
	print("D'?aluer l'apprentissage de differents utilisateurs avec un outil de statistique. Suivre des utilisateurs sur differentes seance d'apprentissage.")
	print("De voir les limites sur les differents jeux repr?entant 3 perceptions differentes. La perception de la localisation, des mouvements et des motifs.")
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
			print("La pin "+str(j*x+i)+" se met ?clignoter")
			print("La pin aux coordonn?s: x="+str(i)+" y="+str(j))
			print(",",motif)
			sendDataToDisplay(motif,x,y,0)
			print("")
			print("0 pour la pin suivante")
			print("1 pour retourner au menu principal")
			choice = key.queue.get()
			motif[i][j]=0
			if(choice=='1'):
				firstMenu()
	os.system('clear')
	print("Vous etes arriv??la fin de l'installation.")
	print("Appuyer sur 0 pour retourner au menu principal")
	choice = key.queue.get() 
	firstMenu()
def installation():
	os.system('clear')
	print("Bienvenue au programme d'installation du syst?e")
	print("Il permet de faciliter le branchement des cables")
	print("Veuillez donner la largeur x de l'?ran?")
	x=int(key.queue.get())
	os.system('clear')
	print("Ok, l'?ran fait "+str(x)+" de large.")
	print("Quelle est la hauteur y de l'?ran?")
	y=int(key.queue.get())
	os.system('clear')
	print("L'?ran fait "+str(x)+" de large et "+str(y)+" de hauteur.")
	print("Pour faciliter le branchement, chacune des sorties vont alterner entre 1 et 0 les unes apr? les autres.")
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
	print("0 pour d?ineur")
	print("1 pour guitar hero")
	print("2 pour des chiffres et pas de lettre")
	print("3 pour retourner au menu principal")
	print("4 pour enregistrer")
	print("5 pour quitter")
	choice=key.queue.get()
	if(choice=='0'):
		initGame(0)
	elif(choice=='1'):
		initGame(1)
	elif(choice=='2'):
		initGame(2)
	elif(choice=='3'):
		firstMenu()
	elif(choice=='4') :
		saveGame()
		gameMenu()
	else:
		stopGame()
def firstMenu():
	os.system('clear')
	print (userName.capitalize()+", bienvenue sur le menu principal")
	print ("choisisez :")
	print ("0 pour en savoir plus sur le but des jeux")
	print ("1 pour jouer")
	print ("2 pour le programme d'installation")
	print ("3 pour sauvegarder")
	print ("4 pour les parametres")
	print ("5 pour quitter")
	choice = key.queue.get()
	if(choice=='0'):
		moreInformation()
	elif(choice=='1'):
		gameMenu()
	elif(choice=='2'):
		installation()
	elif(choice=='3') :
		saveGame()
		gameMenu()
	elif(choice=='4'):
		hackSetting()
	else :
		stopGame()

def initGame(game):
	os.system('clear')
	if(game==0):
		print("Bienvenue au jeu de d?ineur")
		print("10 bombes vont apparaitre les unes ?apr? les autres.")
		print("Vous devrez dire ?quelles coordonne?s elles se trouvent avec le pav?num?ique")
		print("Vous serez not?sur le temps pour localiser les 10 bombes et le nombre de bombe d?in?)
	elif(game==1):
		print("Bienvenue au jeu de guitar h?o (jeu non officiel inspirant le jeu Guitar Hero")
		print("Vous allez avoir 10 motifs qui vont etre dessin?sur votre peau.")
		print("Si vous sentez un balayage vers la gauche appuyer sur 6(touche de gauche du pav?num?ique")
		print("Pour la droite 4, pour le haut 8, pour le bas 2")
		print("Vous serez not?sur le temps pour suivre la partition et le nombre de note respect?)
	elif(game==2):
		print("Bienvenue au jeu des chiffres et pas de lettre")
		print("L'objectif du jeu et de reconnaitre les chiffres qui seront dessin?sur votre bras")
		print("Les chiffres seront afficher au hasard et vous le saisirez sur le pav?num?ique")
		print("Vous serez not?sur le temps pour reconnaitre les 10 chiffres et le nombre de r?ssite")

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
def sendDataToDisplay(motif1,x,y,motifMult=1,frequence=0.5,sleeptime=0.5):
	#print("motifL220",motif1)
	if motifMult==1:
		motifMult=len(motif1)
		#print("MotifMult",motifMult)
	else:
		motifMult=1
	motifF=[[[0 for i in range(x)] for j in range(y)]for z in range(motifMult+1)]
	for z in range(motifMult+1):
		for i in range(x):
			for j in range(y):
				if z<motifMult:
					if motifMult==1:
						motifF[z][i][j]=motif1[i][j]
					else:
						motifF[z][i][j]=motif1[z][i][j]
				else:
					motifF[z][i][j]=0
	#print(motifF)
	motifF=convertMap(motifF,x,y)
	test1Scalable.convertToHexa(motifF,x,y,frequence,sleeptime)#ici les commentaires pour marcher sans rasberry
def displayNone():
	x=4
	y=4
	motif1=[[0 for i in range(x)] for j in range(y)]
	sendDataToDisplay(motif1,x,y,0)
def mineDisplay(value):
	x=4 #3
	y=4 #3
	motif=[[0 for i in range(x)] for j in range(y)]
	value=value-1
	val1=int((value-value%3)/3)
	motif[val1][value%3]=1
	sendDataToDisplay(motif,x,y,0)
def guitarDisplay(value):
	x=4
	y=4
	nbMotif=4
	motifS=[[[0 for i in range(x)] for j in range(y)]for z in range(nbMotif)] 
	if value==2:
		motifS[0]=[[1, 1, 1, 0], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0]]
		motifS[1]=[[0, 0, 0, 0], 
		 [1, 1, 1, 0], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0]]
		motifS[2]=[[0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [1, 1, 1, 0], 
		 [0, 0, 0, 0]]
		motifS[3]=[[0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [1, 1, 1, 0]]
	elif value==6:
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
	elif value==4:
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
		 [1, 1, 1, 0]]
		motifS[1]=[[0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [1, 1, 1, 0], 
		 [0, 0, 0, 0]]
		motifS[2]=[[0, 0, 0, 0], 
		 [1, 1, 1, 0], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0]]
		motifS[3]=[[1, 1, 1, 0], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0]]
	#print("motifS",motifS)
	sendDataToDisplay(motifS,x,y,1,0.1,0.5)
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
		motifS=[[0, 1, 0, 0], 
		 [1, 1, 0, 0], 
		 [0, 0, 1, 1], 
		 [0, 0, 1, 0]]
	elif value==2 :
		motifS=[[1, 0, 0, 1], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [1, 0, 0, 1]]
	elif value==3 :
		motifS=[[0, 1, 0, 0], 
		 [1, 0, 0, 0], 
		 [0, 0, 0, 1], 
		 [0, 0, 1, 0]]
	elif value==4 :
		motifS=[[1, 0, 0, 1], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [0, 0, 1, 0]]
	elif value==5 :
		motifS=[[1, 0, 0, 1], 
		 [0, 1, 1, 0], 
		 [0, 1, 1, 0], 
		 [1, 0, 0, 1]]
	elif value==6 :
		motifS=[[1, 1, 1, 1], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0], 
		 [1, 1, 1, 1]]
	elif value==7 :
		motifS=[[1, 0, 0, 1], 
		 [1, 0, 0, 1], 
		 [1, 0, 0, 1], 
		 [1, 0, 0, 1]]
	elif value==8 :
		motifS=[[0, 0, 0, 0], 
		 [0, 1, 1, 0], 
		 [0, 1, 1, 0], 
		 [0, 0, 0, 0]]
	else :
		motifS=[[0, 0, 0, 0], 
		 [1, 1, 1, 1], 
		 [0, 0, 0, 0], 
		 [0, 0, 0, 0]] 
	sendDataToDisplay(motifS,x,y,0)
def gameLaunch(game):
	global stat
	global statG
	global statTime
	global statGTime
	score=0
	debut=time.time()
	oldTime=time.time()
	olddigit=-1
	os.system('clear')
	for i in range(0,10):
		oldTime=time.time()
		timeSpend=int(oldTime-debut)
		print("Score = "+str(score)+"/"+str(i)+" Temps ecoul?: "+str(timeSpend))
		if(game==0):
			print("O? se trouve la bombe?")
			digit=random.randint(1,9)
			if digit==olddigit:
				digit=random.randint(1,9)
				olddigit=digit
			mineDisplay(digit)
		elif(game==1):
			print("Que dit la partition?")
			digit=random.randint(0,3)
			if digit==olddigit:
				digit=random.randint(0,3)
				olddigit=digit
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
			print("0 est : \u007C  1      \u007C   2     \u007C   3     \u007C  4     ")
			print("  \u2588 \u2588   \u007C   \u2588     \u007C \u2588     \u2588 \u007C   \u2588     \u007C \u2588     \u2588")
			print("\u2588     \u2588 \u007C \u2588 \u2588     \u007C         \u007C \u2588       \u007C        ")
			print("\u2588     \u2588 \u007C     \u2588 \u2588 \u007C         \u007C       \u2588 \u007C        ")
			print("  \u2588 \u2588   \u007C     \u2588   \u007C \u2588     \u2588 \u007C     \u2588   \u007C     \u2588  ")
			print("                                                                   ")
			print("5       \u007C 6       \u007C 7       \u007C 8       \u007C 9      ")
			print("\u2588     \u2588 \u007C \u2588 \u2588 \u2588 \u2588 \u007C \u2588     \u2588 \u007C         \u007C        ")
			print("  \u2588 \u2588   \u007C         \u007C \u2588     \u2588 \u007C   \u2588 \u2588   \u007C \u2588 \u2588 \u2588 \u2588")
			print("  \u2588 \u2588   \u007C         \u007C \u2588     \u2588 \u007C   \u2588 \u2588   \u007C        ")
			print("\u2588     \u2588 \u007C \u2588 \u2588 \u2588 \u2588 \u007C \u2588     \u2588 \u007C         \u007C        ")
			digit=random.randint(0,9)
			if digit==olddigit:
				digit=random.randint(0,9)
				olddigit=digit
			digitDisplay(digit)
		if(hack==1):
			print("un peu de triche:",digit)
		guess=key.queue.get()
		os.system('clear')
		result=0
		if(guess==str(digit)):
			print("Bien jou? le resultat ?ait bien",digit)
			score=score+1
			result=1
		else:
			print("Loup? le resultat ?ait",digit)
		stat[game]=stat[game]+","+str(result)
		statG=statG+","+str(result)
		VstatTime=int((time.time()-oldTime)*10)
		statTime[game]=statTime[game]+","+str(VstatTime)
		statGTime=statGTime+","+str(VstatTime)
	os.system('clear')
	displayNone()
	print("Vous avez "+str(score)+" bonne(s) r?onse(s) sur 10")
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
