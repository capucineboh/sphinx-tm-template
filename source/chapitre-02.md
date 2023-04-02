# Documentation développeur

## Mise en Route 

1.	Pour mettre en route le site internet, il nécessaire de se rendre sur [ce lien](https://github.com/capucineboh/site-candide "lien pour accéder sur le dépôt du projet") en passant par chrome, puis y ajouter la particule `gitpod.io#` au début. [^1]    
2.	À la suite de cette manipulation, le projet s’ouvre dans GitPod, une plateforme de développement en ligne permettant de travailler sur les projets sans installer d'environnement de développement. Ceci permet la non-nécessité d’installer quelque application de développement.      
3.	Une fois le projet ouvert dans GitPod, il faut le démarrer. Pour ce faire, il faut inscrire la commande `python -m http.server 8000` dans le terminal, puis sélectionner le bouton « open in browser » de la fenêtre ouverte à l’occasion de la commande effectuée.       

Enfin, une page où il est possible de naviguer sur le site s’est ouverte. 

## Installation

{cite:p}`documentation-github`
[Documentation GitHub]({{cite:p}}documentation-github) [^2]



S’il est souhaité d’installer le projet localement, il est nécessaire de procéder de la manière suivante :

1.	Il faut ouvrir un terminal sur l’ordinateur où l’installation locale est souhaitée. 

2.	Par le biais de la commande `git clone https://github.com/capucineboh/site-candide.git`, il est rendu possible de cloner le dépôt Git et cela créera une copie locale du dépôt sur l’ordinateur. 

3.	Il sera nécessaire de naviguer jusqu’au répertoire du projet à l’aide de la commande `cd site-candide`. 

4.	Il est important de vérifier si npm est installé sur l’ordinateur en inscrivant `npm -v` dans terminal local. Ainsi, le serveur de développement peut être démarré par la commande `npm start` et ouvrir automatiquement le site chargé dans votre navigateur web. Pour arrêter le serveur, il suffit d’entrer Ctrl+C dans le terminal.

De cette manière, le site peut être ouvert à n’importe quel moment, directement depuis l’ordinateur en question.

## Contributions  

{cite:p}`documentation-gitclone` 
[Documentation Git clone]({{cite:p}}documentation-gitclone) [^3]

Il est possible pour tous développeur d’apporter des modifications à ce projet, elles sont d’ailleurs les bienvenues. Ce site demande d’ailleurs à être mis-à-jour de manière régulière, afin qu’il reste actif et utile pour le comité. Plusieurs manipulations sont nécessaires à la contribution au site web de Candide.       
 
1.	Il faut forker [ce lien](https://github.com/capucineboh/site-candide "lien pour accéder sur le dépôt du projet"), en passant par chrome, puis y ajouter la particule `gitpod.io#` au début.   [^1] 
« Forker » signifie créer une copie indépendante sur son propre compte GitHub. Cette copie vous permet de travailler sur le code sans affecter l'original, ce qui est voulu ici. 

2.	Maintenant le fork effectué il est nécessaire de clôner le dépôt forké sur GitPod. Ceci est faisable grâce à la commande `git clone https://github.com/capucineboh/site-candide.git`, l’effet de celle-ci est de pouvoir récupérer l’entièreté des documents et fichiers d’un dépôt pour se l’approprier directement.

3.	Ainsi, il faut créer une branche pour la nouvelle contribution en inscrivant la commande suivante dans le terminal : `git checkout -b [nom-de-la-nouvelle-fonctionnalité] `. Cette nouvelle branche créée, il est rendu possible d’apporter les modifications souhaitées sans altéré le projet initial.           

4.	Une fois tous les changements effectués, il faut enregistrer ces éditions grâce aux commandes `git add .` suivie de `git commit -m [nom du commit]`, puis push les nouvelles fonctionnalités avec `git push origin [nom-de-la-nouvelle-fonctionnalité]`.        


5.	Dans le but que ces modifications soient ajoutées au projet initial, une dernière manipulation est nécessaire. Celle-ci est d’effectuer une pull request, elle doit être accompagnée d’une description détailler de la contribution. Pour ce faire, il est nécessaire de cliquer sur le bouton « Compare & pull resquest » disponible à côté de la nouvelle branche créée. De cette manière l’auteur majeur du site Web de Candide, peut choisir d’accepter ou de rejeter la demande et, au cas où elle serait acceptée, le nom de contributeur apparaîtra dans la liste des auteurs du projet. 

## Structure du code et rôle des différents fichiers

### Structure du code

#### HTML

{cite:p}`documentation-meta`
[Documentation Métadonnées]({{cite:p}}documentation-meta) [^4]

Le code du site web de Candide est structuré conformément aux règles d’usage. Il est composé de quatre fichiers HTML correspondant aux quatre pages du site. Ceux-ci forment le squelette du site internet, car le langage de programmation HTML est un langage de balisage, ce qui signifie qu’il permet d’organiser les éléments d’une page par leur type. Ces quatre fichiers déterminent la façon dont les différents éléments de la page, tels que les titres, les paragraphes, les images, les liens, les boutons et les formulaires, sont organisés et disposés sur celle-ci. C’est à l’intérieur de ces différents types de balises que se trouvent également les textes et les images qui forment le contenu du site.       

##### Métadonnées

Les métadonnées sont des informations qui ne sont pas affichées directement sur le site web, mais qui sont stockées dans le code HTML de la page et sont utilisées par les moteurs de recherches pour comprendre le contenu de la page et pour effectuer des opérations de référencement. En effet, elles aident les navigateurs à savoir à quelle position le site web doit figurer lorsque des recherches sont effectuées.      

Les métadonnées sont communément définies dans l’entête de code HTML contenue dans les balises `head`. 
La balise `charset` est l’une des plus commune. Il s’agit de celle définissant les jeux des caractères utilisés dans le site. Le charset de ce site est le UTF-8, un format d’encodage de caractères permettant de représenter tous les caractères de toutes les langues du monde. Cela permet également au navigateur de savoir comment interpréter les caractères spéciaux et les accents utilisés, pour les afficher correctement aux utilisateurs. 
`description` est une autre balise essentielle à un site internet, puisqu’elle contient une courte description du contenu du site internet. Celle-ci s’affichera d’ailleurs directement en dessous du titre du site lors d’une recherche internet.         
La métadonnée `content=“width=1200px , initial-scale=1.0“ ` est importante dans une page web, car elle permet de définir la largeur de la fenêtre d'affichage initiale. On s'assure alors que la page sera affichée de manière cohérente sur des écrans de taille différente. Aussi, l'attribut `initial-scale=1.0` permet de définir le niveau de zoom initial pour la page web. Elle permet donc de s'assurer que la page s'affichera dans sa taille originale sans être agrandie ou réduite automatiquement par le navigateur. Ces deux paramètres sont particulièrement importants pour offrir une expérience utilisateur cohérente et agréable, sans avoir à faire défiler horizontalement ou à zoomer. Ceci permet donc une bonne responsivité du site.     
Cette partie du code est également souvent complétée par la balise `title`. Celle-ci contient le titre de la page, celui inscrit sur l’onglet du site web, une fois le site ouvert.    

#### CSS

Le code de ce projet contient également un fichier CSS. Il est utilisé pour définir la présentation visuelle de la page web, plus communément appelé le « style » de la page. Il permet donc de préciser les différentes caractéristiques des éléments du HTML, comme les couleurs, les polices, les tailles et les dispositions.        
Le langage de programmation CSS permet également la création de mises en page plus complexes grâce à des techniques telles que les types de positions, les ` z-index `, les `grid` et les `Flex-box`, qui permettent une bonne organisation du contenu.      

##### Responsivity

Le document CSS de ce projet est séparé en deux parties distinctes : une pour les écrans de plus de 1000 pixels de largeur (ordinateurs), et la seconde pour les appareils dotés d’un plus petit écran (smartphones). Cette distinction est possible grâce à la fonctionnalité `@media screen and (min/max-width: 1000px)`, alors l’affichage sera différent sur ces deux types d’écrans différents. Cette fonctionnalité s’appelle le « responsive design ». L’organisation interne de ces sections est similaire. En effet, elles commencent toutes deux par des « class » générales, puis se précisent avec d’autres `class` complémentaires. L’ordre dépend de l’ordre chronologique de la visite du site web, en commençant par la page d’accueil et en terminant par la page contact.    

Le `Flex-box` susnommé s’est également montré très utile pour rendre le site responsive. La technologie CSS `Flex-box` permet de créer des mises-en-page flexibles et adaptables. Elle aide les développeurs à créer des mises en page facilement modifiables sans avoir à utiliser des outils plus complexe ou à devoirs utiliser des frameworks externes.            
L’outil `Flex-box` offre une grande flexibilité dans l’organisation des différents éléments d’une page en permettant de contrôler l'alignement, la taille et l'ordre des éléments à l'intérieur d'un conteneur (ici banner). Il est également possible de facilement spécifier comment les éléments à l'intérieur d'un conteneur doivent être positionnés et comment ils doivent s'adapter à différentes tailles d'écran. Par exemple, il est possible de spécifier que les éléments doivent être alignés verticalement et horizontalement au centre, ou que les éléments doivent s'adapter à la largeur disponible, …       
L'un des avantages majeurs des `Flex-box` est sa capacité à simplifier la création de designs responsives. Avant l’existence d’une telle technologie, les développeurs devaient utiliser des techniques moins directes comme les tableaux pour créer des mises en page responsives. Cependant, ces méthodes étaient souvent maladroites, difficiles à mettre en œuvre et engendraient d'un grand nombre de problèmes.       
Avec les `Flex-box`, la création d'une mise en page responsive est grandement simplifiée. Les éléments peuvent être disposés en rangées ou en colonnes et le conteneur flex s'adapte automatiquement à la largeur de l'écran. 

1.	En utilisant la propriété `flex-direction`, il est possible de spécifier comment les éléments doivent se positionner en fonction de l'espace disponible.       

2.	La propriété `align-content` spécifie comment les éléments doivent se comporter lorsqu'ils sont répartis sur plusieurs lignes et permet d’organiser l’alignement des éléments sur l'axe vertical.    

3.	L’élément `grid` en parallèle à Flex-box est également très utile.


## Instructions pour tester le projet

1.	Pour mettre en route le site internet, il nécessaire de se rendre sur [ce lien](https://github.com/capucineboh/site-candide "lien pour accéder sur le dépôt du projet") en passant par chrome, puis y ajouter la particule `gitpod.io#` au début.   [^1] 
2.	À la suite de cette manipulation, le projet s’ouvre dans GitPod, une plateforme de développement en ligne permettant de travailler sur les projets sans installer d'environnement de développement. Ceci permet la non-nécessité d’installer quelque application de développement.        
3.	Une fois le projet ouvert dans GitPod, il faut le démarrer. Pour ce faire, il faut inscrire la commande `python -m http.server 8000` dans le terminal, puis sélectionner le bouton « open in browser » de la fenêtre ouverte à l’occasion de la commande effectuée.          
4.	Pour finir, une page où il est possible de naviguer sur le site internet crée dans le cadre d’un Travail de Maturité s’est ouverte.         

## Présentation des outils sous-jacents au projet 

###Technologies spécifiques  

Le logiciel Adobe XD a été utilisé pour l’élaboration des maquettes de ce projet. C’est un logiciel de prototypage d'interfaces de sites web et d’applications mobiles / de bureau permettant de créer des maquettes interactives pour tester l'expérience utilisateur au mieux.          
Ce logiciel offre de nombreux outils pour faciliter le processus de conception comme : la possibilité de créer des grid, des layout et des modèles pour garder une certaine cohérence dans le design. Parmi les avantages d'Adobe XD, on peut citer sa fonctionnalité de partage de prototypes permettant de présenter le design à des collaborateurs pour obtenir des retours rapidement. Il offre aussi la possibilité de créer des prototypes interactifs qui peuvent être utilisés pour tester l'expérience utilisateur et recueillir des commentaires et critiques. Cela permet d'optimiser le design avant le développement du site et de s'assurer que l'expérience utilisateur est optimale.        
Dans le cadre de la création du site web du comité étudiant humanitaire du Collège du Sud, Adobe XD est un outil très utile dans la conception et le prototypage de l'interface, dans le but de s'assurer que le design réponde aux besoins de l'utilisateur et de Candide avant de commencer le développement du site. En effet, cette fonctionnalité est un majeur de ce logiciel, puisque les longues discussions au sujet de l’interface sont souvent genèse de nombreuses modifications.         
De plus, la première prise en main de ce logiciel, bien que nécessitant l’aide de plusieurs tutoriels et de la documentation en ligne d’Adobe XD, reste assez intuitive. Plusieurs raccourcis sont d’ailleurs similaires à d’autres logiciels de la suite Adobe, notamment à In Design. Il est alors très agréable de travailler avec ce logiciel et il est facile d’obtenir les bases très rapidement.       
 


### Principes de conception / de programmation  

Plusieurs techniques et bonnes pratiques sont appliquées dans la création du site web de Candide, afin d'améliorer sa qualité, son efficacité et sa maintenabilité.        
Tout d’abord, ce site est accessible à tous. Le design est pensé pour rendre la navigation intuitive et naturelle. De plus, chaque image contient un texte de remplacement, qui rend leur présence possible pour les personnes malvoyantes. Aussi, les couleurs sont plutôt contrastées, ce qui permet une meilleure analyse des différents éléments de la page.        
Ensuite, le design du site web est responsive. La mise-en-page s’adapte donc à tous type d’écrans. Il est important de concevoir un design utilisable sur différents supports. À l’aide de techniques telles que les `media queries` et les `Flex-box` le site correspond à toutes les tailles d’appareils.        
Aussi, le CSS pouvant être très répétitif, il est défini par groupes. En effet, les classes de certains éléments de mêmes types ne se différencient que par quelques caractéristiques, il est alors intéressant de créer une classe générale et que les précisions stylistiques soient apportées dans d’autres classes. Ce biais permet d’éviter les nombreuses répétitions qui peuvent souvent être trouvées dans un fichier CSS lorsque les bonnes pratiques de programmations ne sont pas appliquées.          
 
 
[^1]: https://github.com/capucineboh/site-candide 
[^2]: https://docs.github.com/en 
[^3]: https://github.com/git-guides/git-clone
[^4]: https://developer.mozilla.org/fr/docs/Web/HTML/Element/meta