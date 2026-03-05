using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ParcVehicules
{
    /// <summary>
    /// Représente les utilitaires, hérite de Vehicule
    /// </summary>
    public class Utilitaire : Vehicule
    {
        // Attribut volume
        protected int volume;

        /// <summary>
        /// Constructeur
        /// </summary>
        /// <param name="_imm">Immatriculation</param>
        /// <param name="_marque">Marque</param>
        /// <param name="_coul">Couleur</param>
        /// <param name="_volume">Volume utile en m3</param>
        public Utilitaire(String _imm, String _marque, String _coul, int _volume)
            : base(_imm, _marque, _coul)
        {
            volume = _volume;
        }

        /// <summary>
        /// Complète ToString de la classe mère
        /// </summary>
        /// <returns>Véhicule imm (marque, couleur) : utilitaire de xm3</returns>
        public override string ToString()
        {
            return base.ToString() + " : utilitaire de " + volume + "m3";
        }
    }
}
