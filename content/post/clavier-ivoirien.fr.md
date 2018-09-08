+++
author = "Boyd Kelly"
date = "2018-07-01T00:00:00.000+00:00"
description = "Tappez sur Linux en langues ivoiriennes !"
featured_image = "/images/clavier_ivoirien.png"
marques = ["langue", "tech", "afrique"]
sujets = ["Technologie"]
title = "Clavier Ivoirien"

+++
Je suis très heureux de publier le 'Clavier Ivoirien' sur un repo publique.  Ce clavier qui permet de tapper aisément (sans faire de gymnastiques avec les doigts) les langues ivoriennes.   On peut l'installer sur les systems 'rpm':  Fedora, Suse, Mageia etc.  Simplement ajouter le repo approprié disponible ici:

[https://copr.fedorainfracloud.org/coprs/boydkelly/xkeyboard-config-ci/](https://copr.fedorainfracloud.org/coprs/boydkelly/xkeyboard-config-ci/ "Fedora Copr")

\** Installation

Fedora:   

> sudo dnf copr enable boydkelly/xkeyboard-config-ci
>
> sudo dnf update xkeyboard-config

Suse et Mageia:  Voir votre distribution pour ajouter repo et mettre à jour xkeyboard-config

Si vous avez des patchs ou contributions, voir le source sur [github.com](https://github.com/boydkelly/xkeyboard-config-ci "Github")

Pardon pour les usagers de distributions debian je vais mettre publier un deb très bientôt!

Le clavier français de Côte d'Ivoire est identique au clavier national français azerty.

Le clavier multilingue de Côte d'Ivoire (civ) est basé sur le clavier français azerty, mais inclut des symboles unicode supplémentaires pour les langues localesde la Côte d'Ivoire. On a consulté les claviers de Togo, Nigeria, Mali et en particulier le Cameroon pour faire le faire. Il peut être utlisé pour écrire l'Attié, Abé, Baoulé, Français, Gueré, Jula, Senoufo, Yacouba, et d'autres langues locales.

Les charactères unicode sont disponible de deux façons:

1. Appuyer et tenir la touche AltGr et ensuite la touche appropriée de la table ci dessous.
2. Appuyer la touch exclamation (!, sur le clavier azerty), relache, et ensuite appuyer la touche appropriée de la table ci dessous.

La première méthode peut être difficile surtout avec les majuscules et quand la touche en question se trouve sur la droite du clavier. La deuxième méthod permet de tapper avec plus de fluidité. Appuyer la touch exclamation (!) deux fois pour insérer la mark d'exclamation.::

      ____                                    
     | 1 3| 1 = Maj,  3 = AltGr + Maj    (AltGr est du côte droit)
     | 2 4| 2 = normal, 4 = AltGr
      ¯¯¯¯                                  
      ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ _______
     |    | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 0  | °  | +  | <--   |
     | ²  | &  | é ~| " #| ' {| ( [| - || è `| _ \| ç ^| à @| ) ]| = }|       |
      ========================================================================
     | |<-  | A  | Z Ʒ| E Ɛ| R  | T  | Y Ƴ| U Ʋ| I Ɩ| O Ɔ| P  | ¨  | $  |   , |
     |  ->| | a  | z ʒ| e ɛ| r  | t  | y ƴ| u ʋ| i ɩ| o ɔ| p  | ^  ̌| £ ¤| <-' |
      ===================================================================¬    |
     |       | Q  | S  | D Ɗ | F  | G Ŋ| H  | J  | K  | L  | M  | %  | µ  |   |
     | MAJ   | q  | s  | d ɗ | f  | g ŋ| h  | j  | k  | l  | m  | ù `| *  ́|   |
      ========================================================================
     | ^   | >  | W  | X  | C  | V Ʋ| B Ɓ| N Ŋ| ?  | .  | /  | §  |     |     |
     | |   | <  | w  | x  | c  | v ʋ| b ɓ| n ŋ| ,  | ;  | : ¯| ! ~|     |     |
      ========================================================================
     |      |      |      |                       |       |      |     |      |
     | Ctrl | Super| Alt  | Espace   Nobreakspace | AltGr | Super|Menu | Ctrl |
      ¯¯¯¯¯¯ ¯¯¯¯¯¯ ¯¯¯¯¯¯ ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ ¯¯¯¯¯¯¯ ¯¯¯¯¯¯ ¯¯¯¯¯ ¯¯¯¯¯