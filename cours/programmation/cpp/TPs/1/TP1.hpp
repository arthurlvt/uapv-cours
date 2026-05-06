#ifndef TD1_HPP
#define TD1_HPP
#include <cmath>

class Point {
    private:
        double x;
        double y;
    public:
        void afficher(); 
        void saisir();
        
        Point(double abs = 0.0, double ord = 0.0);
        
        double distance(const Point& P) const;    
        double getX() const;
        double getY() const;
        void setNewX(double abs);
        void setNewY(double ord);
};

bool equal(const Point &P1, const Point &P2);
int PointIntoCircle(Point tab[], int sizeOfTab, Point &center, double R);

class Cercle {
    private:
        Point centre;
        double rayon;
        
    public:
        Cercle(Point c, double r) : centre(c), rayon(r) {
            if (r <= 0) {
                cout << "Erreur: rayon doit etre positif!" << endl;
                rayon = 1.0; // valeur par défaut
            }
        }
        
        Point getCentre() const { return centre; }
        double getRayon() const { return rayon; }
        
        void setRayon(double r) {
            if (r > 0) {
                rayon = r;
            } else {
                cout << "Erreur: rayon invalide!" << endl;
            }
        }
};
#endif