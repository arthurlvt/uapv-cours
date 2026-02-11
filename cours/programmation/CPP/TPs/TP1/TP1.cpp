#include <iostream>
#include <cmath>
#include "TP1.hpp"
using namespace std;

// TD1 + TP1

// Constructeur
Point::Point(double abs, double ord) {
    x = abs;
    y = ord;
}

// Affichage
void Point::afficher() {
    cout << "(" << x << "," << y << ")" << endl;
}

// Saisie
void Point::saisir() {
    cout << "Enter x: ";
    cin >> x;
    cout << "Enter y: ";
    cin >> y;
}

// Getters
double Point::getX() const {
    return x;
}

double Point::getY() const {
    return y;
}

// Setters
void Point::setNewX(double abs) {
    x = abs;
}

void Point::setNewY(double ord) {
    y = ord;
}

// Distance
double Point::distance(const Point& P) const {
    double dx = x - P.x;
    double dy = y - P.y;
    return sqrt(dx*dx + dy*dy);
}

// Égalité
bool equal(const Point &P1, const Point &P2) {
    double d = P1.distance(P2);
    return (d < 0.00001);
}

// Points dans un cercle
int PointIntoCircle(Point tab[], int sizeOfTab, Point &center, double R) {
    int count = 0;
    for (int i = 0; i < sizeOfTab; i++) {
        double d = tab[i].distance(center);
        if (d <= R) {
            count++;
        }
    }
    return count;
}

// Affichage caracteristiques cercle
void displayCercle(const Cercle& C) {
    cout << "Centre: ";
    C.getCentre().afficher();
    cout << "Rayon: " << C.getRayon() << endl;
}

// Calcul perimetre cercle
double perimeterCircle(const Cercle& C) {
    return 2 * M_PI * C.getRayon(); // M_PI est defini dans <cmath>
}

// Calcul surface cercle par méthode Monte Carlo

// Calcul point dans un cercle ou non
bool isPointInCircle(const Point& P, const Cercle& C) {
    double d = P.distance(C.getCentre());
    return (d <= C.getRayon());
}

// Calcul intersection entre deux cercles
bool doCirclesIntersect(const Cercle& C1, const Cercle& C2) {
    double d = C1.getCentre().distance(C2.getCentre());
    double r1 = C1.getRayon();
    double r2 = C2.getRayon();
    return (d <= (r1 + r2)) && (d >= fabs(r1 - r2));
}
    
int main() {
    // Test simple
    Point P1(2.0, 3.0);
    cout << "Point P1: ";
    P1.afficher();
    
    Point P2(5.0, 7.0);
    cout << "Point P2: ";
    P2.afficher();
    
    cout << "Distance entre P1 et P2: " << P1.distance(P2) << endl;
    
    cout << "P1 et P2 sont egaux? " << (equal(P1, P2) ? "Oui" : "Non") << endl;
    
    // Test avec tableau
    Point tab[3] = {Point(1,1), Point(2,2), Point(10,10)};
    Point center(0, 0);
    double R = 5.0;
    
    int nbPoints = PointIntoCircle(tab, 3, center, R);
    cout << "Nombre de points dans le cercle: " << nbPoints << endl;
    
    return 0;

    // PARTIE CERCLE (TP)
    // constructeur sans parametres
    Cercle C();
    // constructeur avec parametres
    Cercle C1(Point(0,0), 5.0);
    // afficher caracteristiques cercle
    displayCercle(C1);
    // calcul perimetre cercle
    double perim = perimeterCircle(C1);
    cout << "Perimetre du cercle C1: " << perim << endl;
    // test point dans cercle
    Point P3(3,4);
    cout << "Le point P3 est dans le cercle C1? " << (isPointInCircle(P3, C1) ? "Oui" : "Non") << endl;
    // test intersection entre deux cercles
    Cercle C2(Point(4,0), 3.0);
    cout << "Les cercles C1 et C2 s'intersectent-ils? " << (doCirclesIntersect(C1, C2) ? "Oui" : "Non") << endl;
}