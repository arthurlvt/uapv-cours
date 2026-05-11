# ----------------- EXERCICE 1 ----------------- #
# Commande cat, head, tail, cut, sort, join, paste, grep…

head -n 9 etudiant.txt | tail -n 1 etudiant.txt
tail -n 1 etudiant.txt
les deux affichent UAPV30908:L3:SIMON:Julien:27/12/1990:Montfavet

tail -n 1 etudiant.txt | cut -c 14-25 -> "SIMON:Julien"
sed "s/:/ /g" etudiant.txt -> remplace tous les ":" par des espaces
grep L1 etudiant.txt -> affiche toute les lignes avec "L1"
grep -e "L1" -e "L2" -e "L3" etudiant.txt -> affiche toute les lignes avec "L1", "L2" et "L3"
cat etudiant.txt | cut -f3 -d":" | grep "R"
cat etudiant.txt | cut -f3 -d":" | grep "^[B-R]"
cat etudiant.txt | cut -f3 -d":" | grep "^R"
cat etudiant.txt | cut -f3 -d":" | grep "^.A"
cat etudiant.txt | grep -c "L1"
cat etudiant.txt | grep -c "1990"

join -1 1 -2 1 -t':' etudiant.txt notes.txt > result.txt"
cat result.txt | grep "Anglais" | cut -f3 -d":"
cat result.txt | grep "Anglais" | cut -f8 -d":" | sort -n | tail -1
or
cat result.txt | grep "Anglais" | sort -k8 -t":" -n | tail -1 | cut -f8 -d":"

cat result.txt | cut -f3 -d":" | sort
cat result.txt | cut -f5 -d":" | grep -e "^...12" -e "^...01"
cat result.txt | cut -f5 -d":" | grep -e "^......" | sort -n | head -1
or
cat result.txt | grep -E "^([^:]*:){4}.{6,}" | sort -t":" -k5,5 -n | head -1
cat result.txt | cut -f5 -d":" | grep -e "^......" | sort -n | tail -1
or
cat result.txt | grep -E "^([^:]*:){4}.{6,}" | sort -t":" -k5,5 -n | tail -1
cat result.txt | sort -k6,6 -t":" | cut -f3,4,6 -d":" | sed "s/:/ /g"
cat result.txt | cut -f6 -d":" | sed "s/:/ /g" | grep "e.*e" | sort -u
or
grep -f<(cat result.txt)

# ----------------- EXERCICE 2 ----------------- #
# Commande find
2. find . -name "*.cc"
3. find . -name "san*"
4. find . -iname "san*"
5. find -type f
6. find -type d
7. find . -size +300k
8. find . -iname "san*" | find . -size -300k | copy san_francisco/small_images
9. find . -iname "san*" -size -300k -exec cp {} san_francisco/small_images/ \;
10. find . -iname "*.pdf" -exec cp {} pdf/ \;

# ----------------- EXERCICE 3 ----------------- #
# Redirections des flux d'entrée/sortie