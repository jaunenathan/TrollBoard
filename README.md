
## TrollBoard  🧌 : Soundboard
![](https://i.imgur.com/E3xroB9.png)![](https://i.imgur.com/E3xroB9.png)![](https://i.imgur.com/E3xroB9.png)![](https://i.imgur.com/E3xroB9.png)![](https://i.imgur.com/E3xroB9.png)![](https://i.imgur.com/E3xroB9.png)![](https://i.imgur.com/E3xroB9.png)![](https://i.imgur.com/E3xroB9.png)![](https://i.imgur.com/E3xroB9.png)![](https://i.imgur.com/E3xroB9.png)![](https://i.imgur.com/E3xroB9.png)![](https://i.imgur.com/E3xroB9.png)
![enter image description here](https://i.imgur.com/A8r0FrI.png)

**TrollBoard c'est quoi ?**

Comme chaque année depuis 2023, j'essaie de publier sur mon Github des applications drôles avec un petit défi technique pour moi-même. De plus, cela me motive à coder en Python. Par exemple, l'année dernière, j'ai créé un semi-langage de programmation révolutionnaire (lol) appelé [BoaScript](https://github.com/jaunenathan/BoaScript). Pour ce premier avril 2024, j'avais envie de vous proposer mon logiciel de Soundboard que j'ai créé pour mon utilisation personnelle et pour troll mes amis sur Discord. Créer un logiciel de Soundboard n'est pas particulièrement révolutionnaire, étant donné qu'il en existe déjà beaucoup sur Internet, mais mon programme a l'avantage d'avoir quelques fonctionnalités que je n'ai pas trouvées dans les autres Soundboards.

## Téléchargez vos Soundboards directement depuis YouTube sur TrollBoard

Allez sur l'onglet "Download" de TrollBoard, récupérez l'URL de la vidéo que vous souhaitez télécharger et collez-la dans le champ "Enter YouTube URL here". Ensuite, appuyez sur le bouton "Download". Cela aura pour conséquence de télécharger votre vidéo au format **MP3**, afin qu'elle puisse être utilisée dans la Soundboard depuis l'onglet "Sounds". 

![enter image description here](https://i.imgur.com/114bQos.gif)

## Comment utiliser TrollBoard sur Discord, Teamspeak ou Skype ?
Une fois que vous avez téléchargé votre Soundboard, vous la retrouverez dans l'onglet "Sounds". Double-cliquez sur l'échantillon en question pour lancer la musique que vous avez sélectionnée.






https://github.com/jaunenathan/TrollBoard/assets/38536450/15ccef8c-07bc-4b7b-8333-aa2ffd51f644




TrollBoard ne possède pas de gestion de périphérique audio, car cela était trop compliqué à réaliser en Python. Cependant, il est tout à fait possible de diffuser vos Soundboards sur vos plateformes de communication préférées assez simplement à l'aide de [VB-Cable](https://vb-audio.com/Cable/) et de [Voicemeeter](https://vb-audio.com/Voicemeeter/banana.htm).

1. Tout d'abord, vous allez créer une ligne virtuelle avec [VB-Cable](https://www.youtube.com/watch?v=bl0NQAjHbws&t=203s), puis l'assigner comme entré audio principale sur votre Windows ou Mac

![enter image description here](https://i.imgur.com/Rx1mioM.jpeg)![enter image description here](https://i.imgur.com/7uZNf7R.png)
Ensuite, vous allez configurer une entrée Micro et une entrée VB-Cable sur Voicemeeter. Votre configuration devrait ressembler à ceci. Je vous mets également un [tutoriel ici](https://www.youtube.com/watch?v=5jG3OGJ68cs) pour ceux et celles qui n'ont jamais utilisé Voicemeeter.

![enter image description here](https://i.imgur.com/OpUacMH.png)

> Dans la colonne VB-Cable ici, les boutons A2 et B2 sont activés. A2 me
> permet dans ma configuration d'avoir le retour du bureau sur mes
> enceintes, et B2 de le diffuser sur Discord, par exemple. Ainsi, on
> peut utiliser cette configuration pour diffuser nos Soundboards depuis
> TrollBoard vers Discord.

2. Maintenant, vous n'avez plus qu'à aller dans vos paramètres audio de Discord, Teamspeak ou Skype et mettre en entrée **VoiceMeeter Aux Output**' et en sortie **VoiceMeeter Input**.

![enter image description here](https://i.imgur.com/g7nVbGz.png)

## Comment télécharger TrollBoard sur mon ordinateur ?
Vous pouvez télécharger l'exécutable ici ou décompiler le code source du projet pour le lancer sur d'autres systèmes d'exploitation comme macOS ou Linux. Voici la commande pour installer toutes les dépendances Python d'un coup

    pip install PyQt5 yt-dlp

Le code source de TrollBoard est libre tant qu'il n'est pas utilisé à des fins commerciales ou de manière malveillante. Si vous utilisez du code de TrollBoard pour votre projet, merci de bien vouloir citer le projet comme source.  [Apache-2.0 license](https://www.apache.org/licenses/LICENSE-2.0#) 
