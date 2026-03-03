using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ParcVehicules
{
    /// <summary>
    /// Représente les voitures, hérite de Vehicule
    /// </summary>
    public class Voiture : Vehicule
    {
        // Attribut : nombre de portes
        protected int nbPortes;

        /// <summary>
        /// Constructeur
        /// </summary>
        /// <param name="_imm">Immatriculation</param>
        /// <param name="_marque">Marque</param>
        /// <param name="_coul">Couleur</param>
        /// <param name="_nbPortes">Nombre de portes</param>
        public Voiture(String _imm, String _marque, String _couleur, int _nbPortes)
            : base(_imm, _marque, _couleur)
        {
            nbPortes = _nbPortes;
        }

        /// <summary>
        /// Complète ToString de la classe mère
        /// </summary>
        /// <returns>Véhicule imm (marque, couleur) : voiture avec x portes</returns>
        public override string ToString()
        {
            return base.ToString() + " : voiture avec " + nbPortes + " portes";
        }
    }
}
