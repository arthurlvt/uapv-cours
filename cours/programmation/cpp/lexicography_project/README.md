# Projet POO L1 — Dictionnaire intelligent et correcteur orthographique

**Auteur** : Arthur Louvet
**Formation** : L1 CMI Informatique, CERI Avignon Université (UAPV)
**Année** : 2025–2026, Semestre 2
**Dépôt** : 15 mai 2026

---

## 1. Présentation

Le projet implémente un dictionnaire de mots stocké sous deux formes
différentes, à des fins de comparaison :

- un **arbre lexicographique** en représentation fils–frère (classe `Arbre`) ;
- un **tableau dynamique trié** avec recherche dichotomique (classe `Tab`).

Les deux structures sont chargées depuis le même fichier dictionnaire, puis
on compare leurs temps de chargement et de recherche.

## 2. Compilation et exécution

```bash
make            # compile -> ./lexico
./lexico        # tests sur test.dic
./lexico mon_dico.txt   # tests + benchmark sur le dictionnaire passé en argument
make clean      # nettoie obj/ et le binaire
make rebuild    # clean puis make
make rendu      # produit Louvet-Arthur.tgz pour le dépôt
```

Le projet doit compiler avec `g++` (version C++17 ou plus récente) sur les
machines Linux du CERI.

## 3. Organisation des fichiers

```
lexicography_project/
├── include/
│   ├── APC/apc.hpp     # classe Arbre + classe Noeud
│   └── TAB/tab.hpp     # classe Tab
├── src/
│   ├── APC/apc.cpp     # implémentation de l'arbre lexicographique
│   ├── TAB/tab.cpp     # implémentation du tableau dynamique
│   └── principal.cpp   # main : tests fonctionnels + benchmark
├── obj/                # créé automatiquement par make
├── makefile            # compilation principale (structure include/src)
├── makefile.rendu      # makefile « à plat » utilisé pour le dépôt
├── test.dic            # petit dictionnaire de test
└── README.md
```

J'ai choisi une organisation en sous-dossiers (`include/`, `src/`, `obj/`)
plutôt qu'à plat, parce que je trouve ça plus propre et plus extensible si
le projet grossit. Pour le dépôt qui demande une structure plate, la cible
`make rendu` se charge d'aplatir l'arborescence et d'adapter les `#include`.

## 4. État d'avancement

### Partie 1 — Arbre lexicographique (10 fonctionnalités obligatoires)

| # | Méthode                   | Statut |
|---|---------------------------|--------|
| 1 | `Arbre()`                 | ✓      |
| 2 | `Arbre(const char*)`      | ✓      |
| 3 | `~Arbre()`                | ✓      |
| 4 | `Arbre(const Arbre&)`     | ✓      |
| 5 | `insert(const char*)`     | ✓      |
| 6 | `search(const char*)`     | ✓      |
| 7 | `remove(const char*)`     | ✓      |
| 8 | `countWord()`             | ✓      |
| 9 | `lengthOfLongestWord()`   | ✓      |
| 10| `save(const char*)`       | ✓      |

### Partie 2 — Tableau dynamique trié

- Constructeur sans argument, depuis fichier, par recopie, destructeur ✓
- Recherche dichotomique ✓
- `countWord()` ✓

### Partie 3 — Comparaison des deux structures

`principal.cpp` mesure :
- le temps de chargement du dictionnaire dans chaque structure ;
- le temps de recherche de tous les mots du dictionnaire dans chaque structure.

### Fonctionnalités avancées (11–16)

À implémenter après ce dépôt.

## 5. Progression depuis le dépôt du 30 avril

Au dépôt précédent, j'avais :
- l'arborescence du projet (`include/`, `src/`, `obj/`) ;
- les classes `Noeud` et `Arbre` avec toutes leurs déclarations dans
  `apc.hpp` ;
- l'implémentation des deux constructeurs de `Arbre` (sans argument et
  depuis fichier) ;
- un makefile incomplet.

Pour ce dépôt, j'ai :
- corrigé un problème de chemin d'inclusion qui aurait empêché la
  compilation sur les machines Linux du CERI (chemin sensible à la casse) ;
- corrigé deux fautes de frappe dans les noms de méthodes (`coutWord`,
  `lenghtOfLongestWord`) ;
- implémenté les **8 fonctionnalités obligatoires manquantes** de la classe
  `Arbre` (3, 4, 5, 6, 7, 8, 9, 10) ainsi que leurs helpers récursifs ;
- créé la classe `Tab` (Partie 2) : header, implémentation, tests ;
- écrit `principal.cpp` avec une suite de tests fonctionnels pour les deux
  classes et un benchmark pour la Partie 3 ;
- réécrit le `makefile` (gestion automatique de l'arborescence
  `src/.../X.cpp` → `obj/.../X.o`, options de warnings strictes) ;
- ajouté une cible `make rendu` pour automatiser la création du tarball.

## 6. Choix techniques notables

**Représentation fils–frère pour l'arbre.** Le marqueur de fin de mot est
un nœud spécial portant `'\0'`. Comme `'\0'` a la valeur ASCII 0, il se
range naturellement en première position dans la chaîne triée des frères,
ce qui permet de stocker simultanément un mot et l'un de ses préfixes
(par exemple `"ma"` et `"mais"`).

**Suppression récursive avec référence sur pointeur.** La fonction
`removeWordByRec` reçoit un `Noeud*&` plutôt qu'un `Noeud*` : ainsi, quand
on supprime un nœud, on peut directement mettre à jour le pointeur du
parent qui référençait ce nœud, sans avoir à gérer un cas particulier
pour le premier élément de la chaîne de frères.

**Tableau dynamique en deux blocs (`buf` continu + `tab` de pointeurs).**
Une seule grosse allocation pour stocker tous les mots, plus un tableau
de pointeurs qu'on trie. Les chaînes elles-mêmes ne bougent jamais, on
ne réordonne que les pointeurs (de simples copies de 8 octets).

**Constructeur par recopie de `Tab` par offsets.** Plutôt que de
rechercher chaque mot dans le nouveau buffer, je calcule l'offset de
chaque pointeur dans l'ancien `buf` et je l'applique au nouveau :
`nouveau_tab[i] = nouveau_buf + (ancien_tab[i] - ancien_buf)`.

## 7. Limitations connues

- `fscanf("%255s", ...)` tronque silencieusement les mots de plus de
  255 caractères. Suffisant pour un dictionnaire de français courant.
- La gestion des caractères accentués n'est pas spécialement traitée :
  selon l'encodage du fichier, un caractère multi-octets sera traité
  comme plusieurs « lettres » dans l'arbre, ce qui marche mais consomme
  un peu plus de mémoire.

## 8. À faire pour les prochains rendus

- Fonctionnalité 11 : autocomplétion par préfixe (toutes les complétions
  d'un préfixe donné).
- Fonctionnalité 13 : distance de Levenshtein (programmation dynamique).
- Fonctionnalité 14 : correction orthographique via descente dans l'arbre
  avec maintien d'une ligne de la matrice de Levenshtein et élagage
  (`pruning`) quand `min(D)` dépasse le seuil.
- Fonctionnalités 12, 15, 16 : interfaces interactives.
