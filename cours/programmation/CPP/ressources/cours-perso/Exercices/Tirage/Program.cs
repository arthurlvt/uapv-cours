using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tirage
{
    class Program
    {
        static void Main(string[] args)
        {
            // Message d'accueil
            Console.WriteLine("Voici le programme de tirage au sort");

            // Boucler
            bool continuer = true;
            Random rand = new Random();
            while (continuer) {
                // tirage aléatoire
                int aleatoire = rand.Next(1, 7);
                Console.WriteLine("J'ai fait un " + aleatoire);

                // demander à l'utilisateur s'il continue
                Console.WriteLine("Un autre ? (oui / non)");
                String reponse = Console.ReadLine();
                if (reponse.Equals("non"))
                {
                    continuer = false;
                }
            }


            // Fin du programme
            Console.ReadKey();
        }
    }
}
