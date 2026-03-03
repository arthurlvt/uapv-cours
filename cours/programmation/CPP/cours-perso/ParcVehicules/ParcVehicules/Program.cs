using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ParcVehicules
{
    class Program
    {
        static List<Vehicule> listeVehicules; // Liste des véhicules du parc

        static void Main(string[] args)
        {
            // Initialisation des variables
            listeVehicules = new List<Vehicule>();
            int choix = AfficherMenu(); 
            
            // Boucle principale
            // Choix 5 : quitter
            while (choix != 5)
            {
                switch (choix)
                {
                    case 1 :
                        // Afficher la liste
                        AfficherListe();
                        break;
                    case 2 :
                        // Ajouter une voiture
                        AjouterVoiture();
                        break;
                    case 3: 
                        // Ajouter un utilitaire
                        AjouterUtilitaire();
                        break;
                    case 4: 
                        // Supprimer un véhicule
                        SupprimerVehicule();
                        break;
                }
                // On reboucle
                choix = AfficherMenu();
            }
        }

        /// <summary>
        /// Supprime un véhicule à partir de son immatriculation
        /// </summary>
        private static void SupprimerVehicule()
        {
            Console.WriteLine("Suppression d'un véhicule à partir de son immatriculation");

            // On demande l'immatriculation
            Console.Write(" Immatriculation ? ");
            String immatriculation = Console.ReadLine();

            // On cherche l'indice du véhicule dans la liste
            int index = ChercherVehicule(immatriculation);

            if (index >= 0)
            {
                // Suppression
                listeVehicules.RemoveAt(index);
                Console.WriteLine("Véhicule supprimé ! \n");
            }
            else
            {
                Console.WriteLine("Désolé, pas de véhicule correspondant");
            }
        }

        /// <summary>
        /// Cherche l'indice d'un véhicule dans la liste
        /// </summary>
        /// <param name="immatriculation">L'immatriculation voulue</param>
        /// <returns>L'indice du véhicule si trouvé, -1 sinon</returns>
        private static int ChercherVehicule(string immatriculation)
        {
            foreach (Vehicule v in listeVehicules)
            {
                if (v.Immatriculation.Equals(immatriculation)) {
                    // On a trouvé !
                    return listeVehicules.IndexOf(v);
                }
            }
            // Pas de véhicules correspondant
            return -1;
        }

        /// <summary>
        /// Ajout d'un utilitaire à la liste
        /// </summary>
        private static void AjouterUtilitaire()
        {
            Console.WriteLine("Ajouter un utilitaire :");

            Console.Write(" Immatriculation ? ");
            String imm = Console.ReadLine();

            Console.Write(" Couleur ? ");
            String coul = Console.ReadLine();

            Console.Write(" Marque ? ");
            String marque = Console.ReadLine();

            Console.Write(" Volume utile ? ");
            int volume = LireEntier();

            Utilitaire util = new Utilitaire(imm, marque, coul, volume);
            listeVehicules.Add(util);

            Console.WriteLine("\n");
        }

        /// <summary>
        /// Ajout d'une voiture à la liste
        /// </summary>
        private static void AjouterVoiture()
        {
            Console.WriteLine("Ajouter une voiture :");

            Console.Write(" Immatriculation ? ");
            String imm = Console.ReadLine();

            Console.Write(" Couleur ? ");
            String coul = Console.ReadLine();

            Console.Write(" Marque ? ");
            String marque = Console.ReadLine();

            Console.Write(" Nombre de portes ? ");
            int nbPortes = LireEntier();

            Voiture voiture = new Voiture(imm, marque, coul, nbPortes);
            listeVehicules.Add(voiture);

            Console.WriteLine("\n");
        }


        /// <summary>
        /// Méthode utilitaire permettant de lire un entier sur la console. Reboucle tant que ce n'est pas valide
        /// </summary>
        /// <returns>L'entier tapé par l'utilisateur</returns>
        private static int LireEntier()
        {
            // On boucle jusqu'à ce que l'entier soit correct
            while (true)
            {
                int entier;
                if (int.TryParse(Console.ReadLine(), out entier))
                {
                    // C'est bon
                    return entier;
                }
            }
        }

        /// <summary>
        /// Affiche la liste des véhicules
        /// </summary>
        private static void AfficherListe()
        {
            Console.WriteLine("Liste des véhicules :");
            foreach (Vehicule v in listeVehicules)
            {
                Console.WriteLine(v);
            }
            Console.WriteLine("\n");
        }

        /// <summary>
        /// Affiche le menu et renvoi le choix utilisateur
        /// </summary>
        /// <returns>L'entrée entre 1 et 5 choisie par l'utilisateur</returns>
        private static int AfficherMenu()
        {
            while (true)
            {
                Console.WriteLine("Gestion d'un parc de véhicules");
                Console.WriteLine("Actuellement, il y a " + listeVehicules.Count + " véhicules dans le parc");

                Console.WriteLine("1 : afficher la liste des véhicules");
                Console.WriteLine("2 : ajouter une voiture");
                Console.WriteLine("3 : ajouter un utilitaire");
                Console.WriteLine("4 : supprimer un véhicule");
                Console.WriteLine("5 : quitter");

                String reponse = Console.ReadLine();
                int choix;

                if (int.TryParse(reponse, out choix))
                {
                    if (choix > 0 && choix <= 5)
                    {
                        return choix;
                    }
                }

                Console.WriteLine("\n");
            }
        }
    }
}
