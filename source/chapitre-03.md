# Regard Critique 

## Pistes d’améliorations
       
La création du site Web du Comité étudiant humanitaire du Collège du Sud est un projet mené dans le cadre d’un Travail de Maturité. Ainsi son objectif est avant tout l’apprentissage. C’est pourquoi chaque étape prend un temps non-négligeable et que plusieurs points demandent encore à être corrigés. Il est d’ailleurs prévu que les points d’améliorations identifiés seront résolus pour l'oral du moi de mai.        
      
1.	Le premier est la nav-bar (barre de navigation). Certe elle semble tout à fait correcte lorsqu’on l’utilise sur un écran de bureau, mais dès que la surface de l’écran se réduit, elle n’est plus facilement utilisable. En effet, les boutons servant à accéder aux différentes pages du site Web deviennent trop petits et les inscriptions sont illisibles. Il serait alors nécessaire de transformer cette barre de navigation en bouton "menu". Il rendrait le site bien plus accessible et permettrait une large amélioration de l’expérience utilisateur mobile.          

2.	Les media queries du CSS sont uniquement pensés pour les écrans de bureaux et les smartphone. Cependant, l’utilisation du site internet sur des tablettes ne doit pas être négligée. Il serait donc intéressant d’ajouter une troisième `media query`, celle-ci se trouvant entre les deux déjà existantes. De plus, sur ce type de taille d’écran, l’image de fond de chaque titre ne se met pas bien en place. Un cadre blanc se forme autour d’elle. Il faudrait alors trouver une solution pour que cette image se mette correctement en place. Ainsi, le site Web de Candide serait plus agréable à visiter sur des appareils de ce format.         

3.	Toujours au niveau de la responsivité du design, il faudrait probablement utiliser la caractéristique `float` pour les « chapter » du site, car des éléments ont effectivement tendance à se coincer en dessous des « chapter » rendant l’affichage désordonné et la lecture des différents éléments compliquée. 

4.	Finalement, le site Web du comité étudiant humanitaire du Collège du Sud, ayant été programmé sur Google chrome, ne s’adapte pas correctement aux autres navigateurs internet. Le « progressive enhancement » consiste à concevoir et à développer une base fonctionnelle solide pour un site web, en se concentrant sur les fonctionnalités essentielles. Ensuite, des améliorations et des fonctionnalités plus avancées sont ajoutées de manière progressive, en tenant compte des capacités du navigateur ou de l'appareil utilisé par l'utilisateur. Ainsi, tous les utilisateurs bénéficient d'une expérience de base, tandis que ceux disposant de technologies plus avancées peuvent profiter d'une expérience optimisée.

## Objectifs initiaux non réalisés 

### Objectif non remplis 

Les membres de Candide ne sont pas spécialisés en informatique. C’est pourquoi le moyen de changement du contenu du site doit être simple. Ainsi, un des objectifs fixés au début de ce Travail de Maturité est de créer une manière de changer les éléments du site simplement pour n’importe qui. Cependant, cette tâche, n’ayant pas été considérée comme étant une priorité immédiate, n’a pas été complétée au profit d’autres éléments.

### Solutions possibles 

Afin de créer ce moyen simple de modification pour les membres du comité, il est possible de passer par le biais d’un CMS en ligne. Un CMS est un système de gestion de contenu en ligne qui permet à un utilisateur de gérer les publications de contenu sur un site Web, sans avoir à connaître de langages de programmation. Il s’agit alors exactement de ce dont les membres de l’association ont besoin pour tenir ce site à jour. Ces services sont disponibles en open source. Cependant, cette adaptation n’a pas pu être effectuée dans le cadre de ce travail.

## Difficultés rencontrées

Les difficultés majeures de l’élaboration de ce projet résident dans l’apprentissage du logiciel Adobe XD, de GitHub et GitPod, ainsi que des langages de programmation et la correction de bugs. 

1.	Dans le but de créer les maquettes du site, il faut s’initier à Adobe XD, un logiciel de prototypage d'interfaces web, les applications mobiles et les applications de bureau. Les maquettes prennent entre 3 h et 5 h à être faites, sans compter les nombreuses modifications apportées au cours de multiples discussions avec Candide. 

2.	Une fois la maquette finale obtenue, de nouvelles difficultés arrivent, mais celles-ci résident dans la programmation en elle-même. En effet, le développement web étant une discipline qui n’avait pas été abordée avant ce Travail de Maturité, l’apprentissage s’est fait pendant l’été et directement lors de l’implémentation du site. C’est pourquoi, de nombreux problèmes tels que des difficultés à mettre en avant certains éléments, à télécharger des polices, à utiliser les `Flex box`, à placer correctement les éléments, à rendre le site responsive et tant d’autres voient le jour tout au long de sa programmation.

3.	Un problème récurrent est rencontré en lien avec l'utilisation du CSS et le manque d'expérience dans l'utilisation de Git. À chaque nouvelle session de travail, il est nécessaire de créer un nouveau fichier CSS et de le lier à toutes les pages HTML, car les modifications apportées ne sont pas reflétées. Bien que la résolution de ce problème soit relativement simple une fois comprise, il n'a pas été possible de déterminer si cela est dû à un manque de connaissances pratiques ou à des problèmes inhérents à GitPod. Par conséquent, une solution définitive n'a pas été trouvée.

Beaucoup de temps a été investi dans l’apprentissage et dans la résolution de bugs. Ce premier projet de développement web a alors été très enrichissant.

## Fonctionnalités supplémentaires

L’activité du comité étudiant humanitaire du Collège du Sud réside autour de la collecte de dons pour des associations externes. Ainsi, il serait bon de développer une fonctionnalité permettant de faire des dons directement à partir du site, comme un formulaire à remplir afin de donner cinq, dix, ou même cent francs à la collecte en cours.       
Cet ajout rendrait les dons beaucoup plus simples et rapides. Il n’y aurait plus besoin de se déplacer, de se souvenir de prendre de l’argent et tout se ferait en quelques clics. Il est remarquable que lorsque les dons sont plus faciles à réaliser, ils conduisent inévitablement à une augmentation du nombre de dons effectués. Il est effectivement souvent observé que la contrainte « cash » d’une collecte peut dissuader certaines personnes. De plus, ce biais permettrait d’atteindre une audience plus large et potentiellement extérieure au Collège du Sud.      
Aussi, dans l’air digitale dans laquelle nous vivons, il ne faut pas négliger le fait que de plus en plus de collectes se feront uniquement en ligne. Cette fonctionnalité moderniserait alors aussi l’organisation du comité et son image en soi.       
 
