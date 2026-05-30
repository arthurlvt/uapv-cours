#include <cstdio>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include "APC/apc.hpp"
#include "TAB/tab.hpp"
#include "levenshtein.hpp"

using namespace std;

static void sortFile(const char* fileName) {
    FILE* f = fopen(fileName, "r");
    if (f == nullptr) return;

    std::vector<std::string> mots;
    char buf[256];
    while (fscanf(f, "%255s", buf) == 1)
        mots.push_back(buf);
    fclose(f);

    std::sort(mots.begin(), mots.end());

    f = fopen(fileName, "w");
    if (f == nullptr) return;
    for (const std::string& m : mots)
        fprintf(f, "%s\n", m.c_str());
    fclose(f);
    std::cout << "Fichier trié : " << fileName << " (" << mots.size() << " mots)\n";
}

static void afficheTest(const char* libelle, bool ok) {
    printf("  [%s] %s\n", ok ? "OK" : "KO", libelle);
}

static double seconds(clock_t debut, clock_t fin) {
    return (double)(fin - debut) / CLOCKS_PER_SEC;
}

// test de l'arbre lexicographique
static void testArbre() {
    printf("---- TESTS ARBRE LEXICOGRAPHIQUE ----\n\n");

    printf("[1] Constructeur sans argument + insertions :\n");
    Arbre a;
    const char* mots[] = {"main", "mais", "mal", "male",
                          "mon", "son", "sono", "sons", "sont"};
    for (const char* m : mots) a.insert(m);
    afficheTest("countWord == 9", a.countWord() == 9);

    printf("\n[6] search :\n");
    afficheTest("search(\"main\")  == true",  a.search("main")  == true);
    afficheTest("search(\"so\")    == false (préfixe seulement)",
                a.search("so") == false);
    afficheTest("search(\"chat\")  == false", a.search("chat")  == false);

    printf("\n[9] lengthOfLongestWord :\n");
    afficheTest("lengthOfLongestWord == 4", a.lengthOfLongestWord() == 4);

    printf("\n[7] remove :\n");
    afficheTest("remove(\"main\") == true",  a.remove("main") == true);
    afficheTest("search(\"main\") == false", a.search("main") == false);
    afficheTest("search(\"mais\") == true",  a.search("mais") == true);
    afficheTest("remove(\"chat\") == false (mot absent)",
                a.remove("chat") == false);
    afficheTest("countWord == 8", a.countWord() == 8);

    printf("\n[4] Constructeur par recopie :\n");
    Arbre b(a);
    a.remove("mal");
    afficheTest("a.search(mal) == false (a modifié)", a.search("mal") == false);
    afficheTest("b.search(mal) == true  (b intact)",  b.search("mal") == true);

    printf("\n[10] save :\n");
    b.save("dico_sauvegarde.txt");
    printf("  -> b sauvegardé dans dico_sauvegarde.txt\n");

    printf("\n[2] Constructeur depuis fichier :\n");
    Arbre c("dico_sauvegarde.txt");
    afficheTest("c.countWord == 8 (rechargement)", c.countWord() == 8);
}

// test du tableau dynamique
static void testTab() {
    printf("\n---- TESTS TABLEAU DYNAMIQUE ----\n\n");
    Tab t("dico.dic");
    printf("[Tab] %d mots chargés depuis dico.dic\n", t.countWord());
    afficheTest("countWord == 9",            t.countWord() == 9);
    afficheTest("search(\"main\") == true",  t.search("main") == true);
    afficheTest("search(\"sont\") == true",  t.search("sont") == true);
    afficheTest("search(\"chat\") == false", t.search("chat") == false);
    afficheTest("search(\"so\")   == false (pas un mot complet)",
                t.search("so") == false);

    Tab t2(t);
    afficheTest("Tab recopié : search(\"main\") == true",
                t2.search("main") == true);
    afficheTest("Tab recopié : countWord identique",
                t2.countWord() == t.countWord());
}

// l'autocomplétion par prefixe : descend dans l'arbre jusqu'à la fin du préfixe, puis collecte tous les mots du sous-arbre restant. 
// Si une lettre du préfixe est absente, renvoie un vector vide.
static void testAutocompletion() {
    printf("\n---- TESTS AUTOCOMPLÉTION (fonctionnalité 11) ----\n\n");
    Arbre a;
    const char* mots[] = {"main", "mais", "mal", "male",
                          "mon", "son", "sono", "sons", "sont"};
    for (const char* m : mots) a.insert(m);

    // Préfixe qui matche plusieurs mots à différents niveaux
    std::vector<std::string> c1 = a.getCompletions("ma");
    printf("getCompletions(\"ma\") -> %zu résultats :\n", c1.size());
    for (const std::string& w : c1) printf("   %s\n", w.c_str());
    afficheTest("count == 4 (main, mais, mal, male)", c1.size() == 4);

    // Préfixe qui est lui-même un mot complet
    std::vector<std::string> c2 = a.getCompletions("son");
    printf("\ngetCompletions(\"son\") -> %zu résultats :\n", c2.size());
    for (const std::string& w : c2) printf("   %s\n", w.c_str());
    afficheTest("count == 4 (son, sono, sons, sont)", c2.size() == 4);

    // Préfixe absent
    std::vector<std::string> c3 = a.getCompletions("xyz");
    afficheTest("getCompletions(\"xyz\") -> vide", c3.empty());

    // Préfixe vide : doit renvoyer tous les mots
    std::vector<std::string> c4 = a.getCompletions("");
    afficheTest("getCompletions(\"\") -> tous les mots (9)", c4.size() == 9);

    // Vérifie aussi l'ordre alphabétique (parcours en profondeur sur frères triés)
    bool ordreOK = true;
    for (size_t i = 1; i < c4.size(); i++) {
        if (c4[i-1] >= c4[i]) { ordreOK = false; break; }
    }
    afficheTest("ordre alphabétique garanti par la structure", ordreOK);
}

// test de la distance de Levenshtein
static void testLevenshtein() {
    printf("\n---- TESTS LEVENSHTEIN (fonctionnalité 13) ----\n\n");

    // Cas dégénérés
    afficheTest("distance(\"\", \"\")           == 0",
                levenshtein("", "") == 0);
    afficheTest("distance(\"chat\", \"chat\")   == 0 (identiques)",
                levenshtein("chat", "chat") == 0);
    afficheTest("distance(\"\", \"chat\")       == 4 (vide vs 4 lettres)",
                levenshtein("", "chat") == 4);
    afficheTest("distance(\"chat\", \"\")       == 4 (4 lettres vs vide)",
                levenshtein("chat", "") == 4);

    // Opérations unitaires
    afficheTest("distance(\"chien\", \"chen\")  == 1 (suppression du i)",
                levenshtein("chien", "chen") == 1);
    afficheTest("distance(\"chen\", \"chien\")  == 1 (insertion du i)",
                levenshtein("chen", "chien") == 1);
    afficheTest("distance(\"chuen\", \"chien\") == 1 (substitution u->i)",
                levenshtein("chuen", "chien") == 1);

    // Avec Levenshtein STANDARD (3 opérations : insertion / suppression /
    // substitution), la distance correcte est 3 :
    //   "chien" -> "shien" (sub c->s)        : 1 op
    //   "shien" -> "shien" sub i->e          : 2 op
    //                       sub e->i          : 3 op  (swap = 2 sub)
    // La valeur 2 du sujet correspondrait à Damerau-Levenshtein (qui ajoute
    // la transposition comme 4e opération de coût 1), pas à la formule
    // décrite dans le sujet.
    int d = levenshtein("chien", "shein");
    printf("\ndistance(\"chien\", \"shein\")   = %d "
           "(Levenshtein standard ; le sujet annonce 2 par erreur)\n", d);
    afficheTest("Levenshtein standard donne 3", d == 3);

    // Symétrie
    afficheTest("symétrie : d(a,b) == d(b,a)",
                levenshtein("bonjour", "bonsoir") ==
                levenshtein("bonsoir", "bonjour"));

    // Cas plus salés
    afficheTest("distance(\"kitten\", \"sitting\") == 3 (classique)",
                levenshtein("kitten", "sitting") == 3);
    afficheTest("distance(\"saturday\", \"sunday\") == 3 (classique)",
                levenshtein("saturday", "sunday") == 3);
}

// test de la correction orthographique via descente dans l'arbre
static void testCorrection() {
    printf("\n---- TESTS CORRECTION VIA L'ARBRE (fonctionnalité 14) ----\n\n");
    Arbre a;
    const char* mots[] = {"main", "mais", "mal", "male",
                          "mon", "son", "sono", "sons", "sont"};
    for (const char* m : mots) a.insert(m);

    auto afficheCorrections = [](const char* mot,
            const std::vector<std::pair<int, std::string>>& res) {
        printf("findClosest(\"%s\") -> %zu propositions :\n", mot, res.size());
        for (const auto& p : res) {
            printf("   distance=%d  %s\n", p.first, p.second.c_str());
        }
    };

    // Faute classique : substitution d'une lettre. "sonr" doit suggérer
    // "son", "sont", "sons", "sono" (tous à distance 1).
    auto r1 = a.findClosest("sonr", 5, 1);
    afficheCorrections("sonr", r1);
    afficheTest("au moins 1 candidat à distance <= 1", r1.size() >= 1);
    afficheTest("tous à distance <= 1",
                std::all_of(r1.begin(), r1.end(),
                            [](const auto& p){ return p.first <= 1; }));

    // Mot exact dans le dico : distance 0, doit être proposé en premier.
    auto r2 = a.findClosest("main", 3, 2);
    printf("\n");
    afficheCorrections("main", r2);
    afficheTest("main retrouvé à distance 0",
                !r2.empty() && r2[0].first == 0 && r2[0].second == "main");

    // Mot un peu plus loin : seuil 2, faute "mauon" -> "mon" (dist 2 : drop a, sub u->m... wait)
    auto r3 = a.findClosest("maon", 5, 2);
    printf("\n");
    afficheCorrections("maon", r3);
    afficheTest("au moins une proposition à seuil 2", r3.size() >= 1);

    // Seuil 0 sur un mot exact : doit renvoyer exactement ce mot.
    auto r4 = a.findClosest("son", 5, 0);
    afficheTest("seuil 0 sur mot exact -> 1 résultat (son lui-même)",
                r4.size() == 1 && r4[0].first == 0);

    // Seuil 0 sur un mot absent : aucune proposition.
    auto r5 = a.findClosest("chien", 5, 0);
    afficheTest("seuil 0 sur mot absent -> vide", r5.empty());

    // Vérifier le k : on limite à 2 mêmes si plus de candidats existent.
    auto r6 = a.findClosest("son", 2, 2);
    afficheTest("k=2 limite bien la taille du résultat", r6.size() <= 2);
}


// Benchmark : on charge le dico dans les deux structures, puis on cherche
// tous les mots du fichier dans chaque structure et on chronomètre. C'est la situation 
// où Arbre et Tab comparent leur vitesse en "best effort" sur leur propre contenu.
static void benchmark(const char* dico) {
    printf("\n---- BENCHMARK SUR \"%s\" ----\n\n", dico);

    clock_t t0 = clock();
    Arbre arbre(dico);
    clock_t t1 = clock();
    Tab tab(dico);
    clock_t t2 = clock();

    if (arbre.countWord() == 0) {
        fprintf(stderr, "Dictionnaire vide ou introuvable : %s\n", dico);
        return;
    }

    printf("Chargement Arbre : %.6f s (%d mots)\n",
           seconds(t0, t1), arbre.countWord());
    printf("Chargement Tab   : %.6f s (%d mots)\n",
           seconds(t1, t2), tab.countWord());

    char buf[256];
    int trouvesArbre = 0, trouvesTab = 0;

    FILE* f = fopen(dico, "r");
    if (f == nullptr) return;
    clock_t r0 = clock();
    while (fscanf(f, "%255s", buf) == 1) {
        if (arbre.search(buf)) trouvesArbre++;
    }
    clock_t r1 = clock();
    fclose(f);

    f = fopen(dico, "r");
    if (f == nullptr) return;
    clock_t r2 = clock();
    while (fscanf(f, "%255s", buf) == 1) {
        if (tab.search(buf)) trouvesTab++;
    }
    clock_t r3 = clock();
    fclose(f);

    printf("Recherche Arbre  : %.6f s (%d trouvés)\n",
           seconds(r0, r1), trouvesArbre);
    printf("Recherche Tab    : %.6f s (%d trouvés)\n",
           seconds(r2, r3), trouvesTab);
}

// mode interactif // chargement du dico dans un Arbre;
static void afficheAide() {
    printf("Commandes disponibles :\n"
           "  insert <mot>             ajouter un mot\n"
           "  search <mot>             chercher un mot exact (oui/non)\n"
           "  remove <mot>             supprimer un mot\n"
           "  complete <prefixe>       lister les mots commençant par <prefixe>\n"
           "  distance <m1> <m2>       distance de Levenshtein\n"
           "  correct <mot> [k] [s]    suggestions de correction (k=5, s=2 par défaut)\n"
           "  count                    nombre de mots\n"
           "  longest                  longueur du plus long mot\n"
           "  save <fichier>           sauvegarder le dico\n"
           "  help                     cette aide\n"
           "  quit | exit              sortir\n");
}

static void modeInteractif(Arbre& a) {
    printf("Mode interactif. %d mot(s) en mémoire. "
           "Tapez 'help' pour la liste, 'quit' pour sortir.\n",
           a.countWord());

    char line[1024];
    char cmd[64], arg1[256], arg2[256];

    while (true) {
        printf("> ");
        fflush(stdout);
        if (!fgets(line, sizeof(line), stdin)) { printf("\n"); break; }
        line[strcspn(line, "\n")] = '\0'; // strip trailing \n

        cmd[0] = arg1[0] = arg2[0] = '\0';
        int n = sscanf(line, "%63s %255s %255s", cmd, arg1, arg2);
        if (n < 1) continue;  // ligne vide

        if (strcmp(cmd, "quit") == 0 || strcmp(cmd, "exit") == 0) {
            break;
        }
        else if (strcmp(cmd, "help") == 0 || strcmp(cmd, "?") == 0) {
            afficheAide();
        }
        else if (strcmp(cmd, "insert") == 0 && n >= 2) {
            a.insert(arg1);
            printf("inséré : %s (total : %d mots)\n", arg1, a.countWord());
        }
        else if (strcmp(cmd, "search") == 0 && n >= 2) {
            printf("%s\n", a.search(arg1) ? "oui" : "non");
        }
        else if (strcmp(cmd, "remove") == 0 && n >= 2) {
            bool ok = a.remove(arg1);
            printf("%s (total : %d mots)\n", ok ? "supprimé" : "absent",
                                              a.countWord());
        }
        else if (strcmp(cmd, "complete") == 0) {
            const char* pref = (n >= 2) ? arg1 : "";
            std::vector<std::string> cs = a.getCompletions(pref);
            printf("%zu complétion(s) pour \"%s\" :\n", cs.size(), pref);
            for (const std::string& s : cs) printf("   %s\n", s.c_str());
        }
        else if (strcmp(cmd, "distance") == 0 && n >= 3) {
            printf("%d\n", levenshtein(arg1, arg2));
        }
        else if (strcmp(cmd, "correct") == 0 && n >= 2) {
            // Valeurs par défaut, surchargeables via les arguments restants.
            int k = 5, seuil = 2;
            sscanf(line, "%*s %*s %d %d", &k, &seuil);
            std::vector<std::pair<int, std::string>> rs =
                a.findClosest(arg1, k, seuil);
            printf("%zu suggestion(s) pour \"%s\" (k=%d, seuil=%d) :\n",
                   rs.size(), arg1, k, seuil);
            for (const std::pair<int, std::string>& p : rs) {
                printf("   distance=%d  %s\n", p.first, p.second.c_str());
            }
        }
        else if (strcmp(cmd, "count") == 0) {
            printf("%d mot(s)\n", a.countWord());
        }
        else if (strcmp(cmd, "longest") == 0) {
            printf("%d caractères\n", a.lengthOfLongestWord());
        }
        else if (strcmp(cmd, "save") == 0 && n >= 2) {
            a.save(arg1);
            printf("sauvegardé dans %s\n", arg1);
        }
        else {
            printf("Commande inconnue (ou arguments manquants). "
                   "Tapez 'help'.\n");
        }
    }
    printf("Au revoir.\n");
}

int main(int argc, char* argv[]) {
    // Tri alphabétique du dictionnaire principal au démarrage
    const char* dicoPrincipal = (argc > 1 && strcmp(argv[1], "-i") == 0)
                                ? (argc > 2 ? argv[2] : "dico.dic")
                                : (argc > 1 ? argv[1] : "dico.dic");
    sortFile(dicoPrincipal);

    // Mode interactif : ./lexico -i [dico]
    if (argc > 1 && strcmp(argv[1], "-i") == 0) {
        const char* dico = (argc > 2) ? argv[2] : "dico.dic";
        printf("Chargement de %s ...\n", dico);
        Arbre a(dico);
        modeInteractif(a);
        return 0;
    }

    // Mode tests (par défaut) : ./lexico [dico]
    const char* dico = (argc > 1) ? argv[1] : "dico.dic";
    testArbre();
    testTab();
    testAutocompletion();
    testLevenshtein();
    testCorrection();
    benchmark(dico);

    printf("\n=== Fin des tests ===\n");
    printf("(Astuce : lance \"./lexico -i [dico]\" pour le mode interactif.)\n");
    return 0;
}
