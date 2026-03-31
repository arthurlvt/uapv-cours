using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ParcVehicules
{
    /// <summary>
    /// Classe de base aux voitures et aux utilitaires. Ne peut être instanciée directement (abstraite)
    /// </summary>
    public abstract class Vehicule
    {
        // Attributs et propriétés
        protected String immatriculation;
        public String Immatriculation
        {
            get { return immatriculation; }
        }

        protected String marque;
        protected String couleur;

        /// <summary>
        /// Constructeur de véhicule (attention, classe abstraite)
        /// </summary>
        /// <param name="_imm">Immatriculation</param>
        /// <param name="_marque">Marque</param>
        /// <param name="_coul">Couleur</param>
        public Vehicule(String _imm, String _marque, String _coul)
        {
            immatriculation = _imm;
            marque = _marque;
            couleur = _coul;
        }

        /// <summary>
        /// Redéfinition de ToString()
        /// </summary>
        /// <returns>de la forme : Véhicule imm (marque, couleur)</returns>
        public override string ToString()
        {
            return "Véhicule " + immatriculation + " (" + marque + ", " + couleur + ")";
        }
    }
}
