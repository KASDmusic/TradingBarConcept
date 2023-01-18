# TradingBarConcept

![GUI](https://github.com/KASDmusic/TradingBarConcept/blob/main/doc/img/chart.png)

## Résumé

La naissance de ce projet de test de réalisation d'un cours de trading vient du fait que, dans les bars de trading (bars où le prix des produits évoluent au cours du temps), les prix n'évoluent pas en fonction de l'offre et de la demande mais aléatoirement ou pseudo aléatoirement avec une borne inférieur et supérieur.  
De ce fait, je me suis dis qu'il serait une bonne idée de faire un système de trading qui, contrairement à l'aléatoire, pourrait influer en fonction du consommateur, dans le but de l'inciter à la consommation.  
En effet, ce système pourrait par exemple valoriser les effets de groupe en permettant à un grand groupe de payer moins chère par exemple (dans le cas d'un système de trading inversé où plus la demande est grande et plus le prix baisse).  

## Architecture 

* Le repertoire *doc* contient tout ce qui est relatif à la documentation (images, videos, ressources ...).
* Le repertoire *src* contient le code source de l'application.
* Le repertoire *src/web* contient les pages web générés à intervalles réguliers.

## Environnement

Ce projet en Python3.  
Il utilise la bibliothèque javascript *chart.js* pour les graphiques et les diagrammes.  

### Exécution

Récupération du projet:
~~~
git clone https://github.com/KASDmusic/TradingBarConcept
~~~

Execution du projet
~~~
    cd TradingBarConcept/src
    python3 Main.py
~~~

Lancement de la visualisation:  
*rendez-vous dans le repertoire /web et lancez l'un des fichiers indexi.html où i est un nombre (ex: index1.html).*


