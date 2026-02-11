# 🐍 Fiche de Révision : Python pour les Mathématiques (L1)

Ce guide est conçu pour réviser les fondamentaux de Python appliqués à l'algorithmique et aux mathématiques.

---

## 1. Types de Données et Syntaxe
En Python, le typage est dynamique, mais la distinction entre les types est cruciale pour les calculs.

| Concept | Syntaxe / Exemple | Note |
| :--- | :--- | :--- |
| **Entier** | `n = 10` | Type `int` |
| **Flottant** | `x = 3.14` | Type `float` |
| **Division réelle** | `7 / 2` | Donne `3.5` |
| **Division entière**| `7 // 2` | Donne `3` |
| **Modulo** | `7 % 2` | Reste de la division (ici `1`) |
| **Puissance** | `x**2` | Attention : ne pas utiliser `^` |

---

## 2. Structures de Données (Listes & Tuples)

Les listes sont au cœur de l'algorithmique en L1.

* **Accès :** `L[0]` (premier), `L[-1]` (dernier).
* **Slicing :** `L[start:stop]` (le `stop` est exclu).
* **Méthodes utiles :**
    * `L.append(x)` : Ajoute `x` à la fin.
    * `len(L)` : Taille de la liste.
    * `sum(L)` / `max(L)` / `min(L)` : Fonctions natives mathématiques.

---

## 3. Structures de Contrôle

### Boucles (Loops)


* **Boucle `for`** : Pour itérer un nombre de fois connu.
  ```python
  for i in range(n): # de 0 à n-1
      # instructions