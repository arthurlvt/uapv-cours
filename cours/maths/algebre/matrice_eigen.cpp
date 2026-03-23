#include <iostream>
#include <Eigen/Dense>

using namespace Eigen;
using namespace std;

// DEBUG: g++ matrice_eigen.cpp -I /opt/homebrew/opt/eigen/include/eigen3 -o matrice
IOFormat matFmt(4, 0, "  ", "\n", "│ ", " │");

/* --------------- EXERCICE 1 --------------- */
void MatrixExo1() {
    cout << "------ EXERCICE 1 ------" << endl;
    // VERSION 1 DE LA MATRICE A
    MatrixXd A(3, 3);    
    A(0, 0) = 5;
    A(0, 1) = 3;
    A(0, 2) = 3;
    A(1, 0) = 3;
    A(1, 1) = 5;
    A(1, 2) = 3;
    A(2, 0) = 3;
    A(2, 1) = 3;
    A(2, 2) = 5;
    // VERSION 2 DE LA MATRICE A
    MatrixXd Abis = 3 * MatrixXd::Ones(3, 3) + 2 * MatrixXd::Identity(3, 3); // On commence par une matrice de 3, puis on ajoute 2 à la diagonale pour obtenir les 5

    // VERSION 1 DE LA MATRICE B
    MatrixXd B(3, 3);
    B(0, 0) = 1;
    B(0, 1) = 0;
    B(0, 2) = 0;
    B(1, 0) = 0;
    B(1, 1) = 1;
    B(1, 2) = 1;
    B(2, 0) = 1;
    B(2, 1) = 0;
    B(2, 2) = 1;
    // VERSION 2 DE LA MATRICE B
    MatrixXd Bbis = MatrixXd::Identity(3, 3); // On commence par la matrice identité
    Bbis.col(0) = VectorXd::Ones(3); // On remplace la première colonne par des 1

    // VERSION 1 DE LA MATRICE C
    MatrixXd C(4, 4);
    C(0, 0) = 1;
    C(0, 1) = 2;
    C(0, 2) = 3;
    C(0, 3) = 4;
    C(1, 0) = 5;
    C(1, 1) = 6;
    C(1, 2) = 7;
    C(1, 3) = 8;
    C(2, 0) = 9;
    C(2, 1) = 10;
    C(2, 2) = 11;
    C(2, 3) = 12;
    C(3, 0) = 13;
    C(3, 1) = 14;
    C(3, 2) = 15;
    C(3, 3) = 16;
    // VERSION AVEC EIGEN
    MatrixXd Cbis(4, 4);
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            Cbis(i, j) = i * 4 + j + 1;
        }
    }

    // VERSION 1 DE LA MATRICE D
    MatrixXd D(4,4);
    D(0, 0) = 1;
    D(0, 1) = 2;
    D(0, 2) = 3;
    D(0, 3) = 4;
    D(1, 0) = 1;
    D(1, 1) = 2;
    D(1, 2) = 3;
    D(1, 3) = 4;
    D(2, 0) = 1;
    D(2, 1) = 2;
    D(2, 2) = 3;
    D(2, 3) = 4;
    D(3, 0) = 1;
    D(3, 1) = 2;
    D(3, 2) = 3;
    D(3, 3) = 4;
    // VERSION 2 DE LA MATRICE D
    MatrixXd Dbis(4, 4);
    for(int i = 0; i < 4; i++) {
        int m = 1;
        for(int j = 0; j < 4; j++) {
            Dbis(i, j) = m;
            m++;
        }
    }

    cout << "Matrice A : " << endl << Abis.format(matFmt) << endl;
    cout << endl;
    cout << "Matrice B : " << endl << Bbis.format(matFmt) << endl;
    cout << endl;
    cout << "Matrice C : " << endl << Cbis.format(matFmt) << endl;
    cout << endl;
    cout << "Matrice D : " << endl << Dbis.format(matFmt) << endl;
    cout << endl;

}


/* --------------- EXERCICE 2 --------------- */
void MatrixExo2() {
    cout << "------ EXERCICE 2 ------" << endl;
    // VERSION 1 DE LA MATRICE B2
    MatrixXd B2(3, 3);
    B2(0, 0) = 1;
    B2(0, 1) = 1;
    B2(0, 2) = 0;
    B2(1, 0) = 1;
    B2(1, 1) = -1;
    B2(1, 2) = 1;
    B2(2, 0) = 1;
    B2(2, 1) = 0;
    B2(2, 2) = 1;
    // VERSION 2 DE LA MATRICE B2
    MatrixXd B2bis(3, 3);
    B2bis << 1, 1, 0,
             1, -1, 1,
             1, 0, 1;
    // verifier que B est inversible
    if (B2.determinant() != 0) {
        cout << "La matrice B2 est inversible." << endl;
        MatrixXd B2_inv = B2.inverse();
        cout << "L'inverse de B2 : " << endl << B2_inv.format(matFmt) << endl;
    } else {
        cout << "La matrice B2 n'est pas inversible." << endl;
    }
    // résoudre le système linéaire B2 * x = [1, 3, -2]
    VectorXd b(3);
    b << 1, 3, -2;
    VectorXd x = B2.colPivHouseholderQr().solve(b);
    cout << "La solution du système B2 * x = [1, 3, -2] est : " << endl << x.format(matFmt) << endl;
    // vérifier que la solution est correcte
    VectorXd b_check = B2 * x;
    cout << "Vérification : B2 * x = " << endl << b_check.format(matFmt) << endl;
    cout << "Matrice B2 : " << endl << B2.format(matFmt) << endl;
    cout << "Matrice B2bis : " << endl << B2bis.format(matFmt) << endl;

}


/* --------------- EXERCICE 3 --------------- */
void MatrixExo3() {
    cout << "------ EXERCICE 3 ------" << endl;
    MatrixXd A3(3, 3);
    A3 << 1, 1, 1,
          1, -2, 1,
          2, -1, 1;
    MatrixXd B3(1, 3);
    B3 << 1, 0, 2;
    // résoudre le système linéaire A3 * x = B3
    cout << "Matrice A3 : " << endl << A3.format(matFmt) << endl;
    cout << endl;
    cout << "Matrice B3 : " << endl << B3.format(matFmt) << endl;
    VectorXd x = A3.colPivHouseholderQr().solve(B3.transpose());
    cout << "La solution du système A3 * x = B3 est : " << endl << x.format(matFmt) << endl;
    
    MatrixXd A3bis(3, 3);
    A3bis << 3, 1, -1,
             1, 1, 1,
             1, -2, 2;
    MatrixXd B3bis(1, 3);
    B3bis << 3, 3, 1;
    // résoudre le système linéaire A3bis * x = B3bis
    cout << "Matrice A3bis : " << endl << A3bis.format(matFmt) << endl;
    cout << "Matrice B3bis : " << endl << B3bis.format(matFmt) << endl;
    VectorXd xbis = A3bis.colPivHouseholderQr().solve(B3bis.transpose());
    cout << "La solution du système A3bis * x = B3bis est : " << endl << xbis.format(matFmt) << endl;
    cout << endl;
}


/* --------------- EXERCICE 4 --------------- */
void MatrixExo4() {
    cout << "------ EXERCICE 4 ------" << endl;
    MatrixXd A4(10, 10);
    int m = 1;
    for (int i = 0; i < 10; i++) {
        m = 1;
        for (int j = 0; j < 10; j++) {
            A4(i, j) = m;
            m++;
        }
    }
    cout << "Matrice A4 : " << endl << A4.format(matFmt) << endl;
    cout << endl;
}


void MatrixExo5() {
    cout << "------ EXERCICE 5 ------" << endl;
    int n, m;
    cout << "Entrez n : ";
    cin >> n;
    cout << "Entrez m : ";
    cin >> m;
    MatrixXd A5(n, m);
    // mesurer le temps de construction de la matrice A5
    clock_t start = clock();
    int val = 1;
    for (int i = 0; i < n; i++) {
        val = 1;
        for (int j = 0; j < m; j++) {
            A5(i, j) = val;
            val++;
        }
    }
    clock_t end = clock();
    double elapsed = double(end - start) / CLOCKS_PER_SEC;
    cout << "Matrice A5 : " << endl << A5.format(matFmt) << endl;
    cout << "Temps de construction de la matrice A5 : " << elapsed << " secondes" << endl;
    cout << endl;
}


/* --------------- EXERCICE 8 --------------- */
void MatrixExo8() {
    cout << "------ EXERCICE 8 ------" << endl;
    int n, m;
    cout << "Entrez n : ";
    cin >> n;
    cout << "Entrez m : ";
    cin >> m;
    MatrixXd A8 = MatrixXd::Random(n, m);
    MatrixXd A8_copy = A8;
    for (int i = 0; i < A8_copy.rows(); i++) {
        for (int j = 0; j < A8_copy.cols(); j++) {
            A8_copy(i, j) = abs(A8_copy(i, j));
        }
    }
    cout << "Matrice A8 : " << endl << A8.format(matFmt) << endl;
    cout << endl;
    cout << "Matrice A8_copy : " << endl << A8_copy.format(matFmt) << endl;
    cout << endl;
}


/* --------------- EXERCICE 9 --------------- */
void MatrixExo9() {
    cout << "------ EXERCICE 9 ------" << endl;
    int n, m;
    cout << "Entrez n : ";
    cin >> n;
    cout << "Entrez m : ";
    cin >> m;
    MatrixXi A9(n, m);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            A9(i, j) = rand() % 10;
        }
    }
    int compteur = 0;
    for(int i = 0; i < n - 1; i++) {
        for(int j = 0; j < m - 1; j++) {
            if(A9(i, j) == A9(i + 1, j + 1)) compteur++;
        }
    }
    int total = (n - 1) * (m - 1);
    double pOccurences = (double)compteur / total * 100;
    cout << "Matrice A9 : " << endl << A9.format(matFmt) << endl;
    cout << endl;
    cout << "Pourcentage d'occurences dans cette Matrice " << n << "*" << m << ": " << pOccurences << "%" << endl;
    cout << endl;
}


/* --------------- EXERCICE 11 --------------- */
void MatrixExo11() {
    cout << "------ EXERCICE 11 ------" << endl;
    int n, m;
    cout << "Entrez n : ";
    cin >> n;
    cout << "Entrez m : ";
    cin >> m;
    MatrixXd A11(n, m);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            A11(i, j) = rand() % 10;
        }
    }
    int OddNumbersCounter, EvenNumbersCounter = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if((int)A11(i, j) % 2 == 0) EvenNumbersCounter++;
            else OddNumbersCounter++; 
        }
    }
    cout << "Matrice A11 : " << endl << A11.format(matFmt) << endl;
    cout << endl;
    cout << "|> Nombre de nombres impairs : " << OddNumbersCounter << endl;
    cout << "|> Nombre de nombres pairs : " << EvenNumbersCounter << endl;
}


/* ------------------------------------------ */
/* ------------- MENU --- CHOIX ------------- */
/* ------------------------------------------ */
int main() {
    cout << "/* ------ ALGEBRE ET PROGRAMME - TP1 ------ */" << endl;
    int choice;
    do {
        cout << "1. Exercice 1" << endl;
        cout << "2. Exercice 2" << endl;
        cout << "3. Exercice 3" << endl;
        cout << "4. Exercice 4" << endl;
        cout << "5. Exercice 5" << endl;
        cout << "8. Exercice 8" << endl;
        cout << "9. Exercice 9" << endl;
        cout << "11. Exercice 11" << endl;
        cout << "0. Quitter" << endl;
        cout << "Votre choix : ";
        cin >> choice;
        switch (choice) {
            case 1:
                MatrixExo1();
                break;
            case 2:
                MatrixExo2();
                break;
            case 3:
                MatrixExo3();
                break;
            case 4:
                MatrixExo4();
                break;
            case 5:
                MatrixExo5();
                break;
            case 8:
                MatrixExo8();
                break;
            case 9:
                MatrixExo9();
                break;
            case 11:
                MatrixExo11();
                break;
            case 0:
                cout << "Au revoir !" << endl;
                break;
            default:
                cout << "Choix invalide, veuillez réessayer." << endl;  

                    }            
                } while (choice != 0);
    return 0;
}