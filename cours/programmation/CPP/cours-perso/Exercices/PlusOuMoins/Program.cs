using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PlusOuMoins
{
    class Program
    {
        static void Main(string[] args)
        {
            // Message d'accueil
            Console.WriteLine("Jouons au plus ou moins. Essaie de trouver à quel chiffre je pense (entre 1 et 100)");

            // Le programme choisit un nombre aléatoire
            Random rand = new Random();
            int cible = rand.Next(1, 101);

            bool trouve = false;
            int nbEssais = 0;
            // Tant que l'utilisateur n'a pas trouvé
            while (!trouve)
            {
                // On lui demande un nombre
                Console.WriteLine("Propose un nombre");
                int proposition;

                // si c'est un nombre correct
                if (int.TryParse(Console.ReadLine(), out proposition))
                {
                    // On incrémente son nombre d'essai
                    nbEssais++;

                    // On lui dit si c'est plus ou moins
                    if (proposition > cible)
                    {
                        Console.WriteLine("C'est moins !");
                    }
                    else if (proposition < cible)
                    {
                        Console.WriteLine("C'est plus !");
                    }
                    else
                    {
                        // s'il a trouvé : on lui affiche un message et on s'arrête
                        Console.WriteLine("Bravo ! Tu as trouvé en " + nbEssais + " coups !");
                        trouve = true;
                    }
                }
            }

            // Fin du programme
            Console.ReadKey();
        }
    }
}
