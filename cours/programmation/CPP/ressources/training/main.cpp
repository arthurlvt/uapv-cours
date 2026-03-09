#include <iostream>

using namespace std;
    
class Point {
    private:
        double x, y;
        public:
            Point(double a=0, double b=0);
            bool identique(const Point &p);
            void afficher();
            bool inferieur(const Point &p);


};