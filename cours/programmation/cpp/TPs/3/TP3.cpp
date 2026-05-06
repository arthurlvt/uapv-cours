#include <iostream>
#include <string>


using namespace std;

// ==================== CLASSE MOT ====================

class mot {
    private:
        string mots;
        string def;
        string* synonymes;
        int nbs;     // nombre actuel de synonymes
        int max_nbs; // capacité maximale

    public:
        // Constructeur par défaut
        mot(string m = "") {
            mots = m;
            def = "";
            nbs = 0;
            max_nbs = 10;
            synonymes = new string[max_nbs];
        }
    
        // Constructeur avec tableau de synonymes
        mot(string m, string syns[], int nb_syns) {
            mots = m;
            def = "";
            nbs = nb_syns;
            max_nbs = (nb_syns > 10) ? nb_syns * 2 : 10;
            synonymes = new string[max_nbs];
        
            for (int i = 0; i < nbs; i++) {
                synonymes[i] = syns[i];
            }   
        }
    
        // Constructeur par copie (IMPORTANT pour éviter les bugs)
        mot(const mot &m) {
            mots = m.mots;
            def = m.def;
            nbs = m.nbs;
            max_nbs = m.max_nbs;
            synonymes = new string[max_nbs];
        
            for (int i = 0; i < nbs; i++) {
                synonymes[i] = m.synonymes[i];
            }   
        }
    
        // Opérateur d'affectation
        mot& operator=(const mot &m) {
            if (this != &m) {
                // Libérer l'ancienne mémoire
                delete[] synonymes;
                // Copier les nouvelles valeurs
                mots = m.mots;
                def = m.def;
                nbs = m.nbs;
                max_nbs = m.max_nbs;
                synonymes = new string[max_nbs];
                for (int i = 0; i < nbs; i++) {
                    synonymes[i] = m.synonymes[i];
                }
            }
        return *this;
        }

        // Destructeur
        ~mot() { delete[] synonymes; }

        void ajout_synonyme(string syn) {
            if (nbs >= max_nbs) {
                int new_max = max_nbs * 2;
                string* new_synonymes = new string[new_max];
                for (int i = 0; i < nbs; i++) {
                    new_synonymes[i] = synonymes[i];
                }
                delete[] synonymes;
                synonymes = new_synonymes;
                max_nbs = new_max;
            }
        
            synonymes[nbs] = syn;
            nbs++;
        }
    
        bool isSynonyme(const string &s) const {
            for (int i = 0; i < nbs; i++) {
                if (synonymes[i] == s) {
                    return true;
                }
            }
            return false;
        }
    
        void saisir() {
            cout << "Entrez le mot: ";
            cin >> mots;
            cout << "Entrez la définition: ";
            cin.ignore();
            getline(cin, def);
            cout << "Combien de synonymes? ";
            int nb;
            cin >> nb;
            // Réallouer si nécessaire
            if (nb > max_nbs) {
                delete[] synonymes;
                max_nbs = nb;
                synonymes = new string[max_nbs];
            }
            nbs = 0;
            for (int i = 0; i < nb; i++) {
                string syn;
                cout << "Synonyme " << (i + 1) << ": ";
                cin >> syn;
                synonymes[nbs++] = syn;
            }
        }

        void afficher() const {
            cout << "Mot: " << mots << endl;
            cout << "Définition: " << def << endl;
            cout << "Synonymes (" << nbs << "): ";
            for (int i = 0; i < nbs; i++) {
                cout << synonymes[i];
                if (i < nbs - 1) cout << ", ";
            }
            cout << endl;
        }
    
        string getMot() const { return mots; }
    
        int getNbSynonymes() const { return nbs; }
    
        string* getSynonymes() const { return synonymes; }
};

// ==================== CLASSE DICTIONNAIRE ====================

class dictionnaire {
    private:
        mot** D;     // Tableau de pointeurs vers des mots
        int nbm;     // nombre actuel de mots
        int max_nbm; // capacité maximale

    public:
        // Constructeur
        dictionnaire(int max = 10) {
            max_nbm = max;
            nbm = 0;
            D = new mot*[max_nbm];
        
            // Initialiser les pointeurs à nullptr
            for (int i = 0; i < max_nbm; i++) {
                D[i] = nullptr;
            }
        }
    
        // Destructeur
        ~dictionnaire() {
            // Libérer chaque mot
            for (int i = 0; i < nbm; i++) {
                delete D[i];
            }
            // Libérer le tableau de pointeurs
            delete[] D;
        }
    
        void ajouterMot(const mot &m) {
            if (nbm < max_nbm) {
                D[nbm] = new mot(m);  // Crée une copie du mot
                nbm++;
                cout << "'" << m.getMot() << "' ajouté." << endl;
            } else {
            cout << "Dictionnaire plein ! Impossible d'ajouter '" << m.getMot() << "'" << endl;
            }
        }
    
        bool isInDictionnaire(const string &s) const {
            for (int i = 0; i < nbm; i++) {
                if (D[i]->getMot() == s || D[i]->isSynonyme(s)) {
                    cout << "'" << s << "' trouvé (mot: " << D[i]->getMot() << ")" << endl;
                    return true;
                }
            }
            cout << "'" << s << "' non trouvé." << endl;
            return false;
        }

        void alphaSort() {
            // Tri à bulles
            for (int i = 0; i < nbm - 1; i++) {
                for (int j = 0; j < nbm - i - 1; j++) {
                    if (D[j]->getMot() > D[j + 1]->getMot()) {
                        // Échanger les pointeurs
                        mot* temp = D[j];
                        D[j] = D[j + 1];
                        D[j + 1] = temp;
                    }
                }
            }
        
            cout << "\nMots triés:" << endl;
            for (int i = 0; i < nbm; i++) {
            cout << "- " << D[i]->getMot() << endl;
            }
        }
    
        void afficher() const {
            cout << "\n=== DICTIONNAIRE (" << nbm << " mots) ===" << endl;
            for (int i = 0; i < nbm; i++) {
                D[i]->afficher();
                cout << "---" << endl;
            }
        }
};

// ==================== MAIN ====================

int main() {
    cout << "=== Programme Dictionnaire (version tableaux dynamiques) ===\n" << endl;
    
    // Création de mots
    string syns1[] = {"vite", "prompt", "agile"};
    mot m1("rapide", syns1, 3);
    
    string syns2[] = {"paresseux", "calme", "tranquille"};
    mot m2("lent", syns2, 3);
    
    string syns3[] = {"joyeux", "content", "gai"};
    mot m3("heureux", syns3, 3);
    
    // Affichage
    m1.afficher();
    cout << endl;
    
    // Test ajout synonyme
    cout << "--- Ajout d'un synonyme à 'rapide' ---" << endl;
    m1.ajout_synonyme("fulgurant");
    m1.afficher();
    cout << endl;
    
    // Test isSynonyme
    if (m1.isSynonyme("vite")) {
        cout << "'vite' est un synonyme de 'rapide' ✓" << endl;
    }

    cout << "Voulez-vous saisir un nouveau mot ? (o/n) ";
    char choice;
    cin >> choice;
    while (choice == 'o' || choice == 'O') {
        m1.saisir();
        cout << "\nMot saisi:" << endl;
        cout << "Voulez-vous saisir un autre mot ? (o/n) ";
        cin >> choice;
    }
    m1.afficher();
    
    // Dictionnaire
    cout << "\n--- Création du dictionnaire ---" << endl;
    dictionnaire d(10);
    
    d.ajouterMot(m1);
    d.ajouterMot(m2);
    d.ajouterMot(m3);
    
    // Recherche
    cout << "\n--- Recherches ---" << endl;
    d.isInDictionnaire("vite");
    d.isInDictionnaire("calme");
    d.isInDictionnaire("triste");

    cout << "\n--- Tri ---" << endl;
    d.alphaSort();

    d.afficher();
}
