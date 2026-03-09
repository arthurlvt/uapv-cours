#include <iostream>

using namespace std;
    
class Point {
    private:
        double x, y;
        friend class Col_Points;
    public:
        Point(double a=0, double b=0);
        bool identique(const Point &p) {
            int count = 0;
            if (x == p.x && y == p.y) {
                count++;  
                return true;
            }
            return false;
            }
            void afficher();
};

class Col_Points {
    friend class Point;
    Point *T;
    int nbp;
    int capacite;
    public:
        Col_Points(int cap=100);
        void add(const Point &p) {
            if(nbp < capacite) {
                T[nbp] = p;
                nbp++;
            } else {
                cout << "Capacité maximale atteinte. Impossible d'ajouter plus de points." << endl;
                // allouer un espace 2x plus grand et copier les éléments existants
                int newCap = capacite * 2;
                Point *newT = new Point[newCap];
                for (int i = 0; i < nbp; i++) {
                    newT[i] = T[i];
                }
                delete[] T;
                T = newT;
                capacite = newCap;
            }
        }
        bool inferieur(const Col_Points &p1, const Col_Points &p2) {
            for (int i = capacite; i < nbp; i++) {
                Point value1 = p1.T[i];
                Point value2 = p2.T[i];
                if (value1.x < value2.x || value1.y < value2.y) {
                    return true;
                }
            }
            return false;
        }
};

/*
1. Est-ce que les classes Point et Col_Points ont besoin d'un destructeur ? Justifiez votre réponse.
La classe Point n'a pas de ressources dynamiques, donc elle n'a pas besoin d'un destructeur. 
Cependant, la classe Col_Points utilise un tableau dynamique de Points (Point *T), ce qui nécessite un 
destructeur pour libérer la mémoire allouée lorsque l'objet Col_Points est détruit.
*/

