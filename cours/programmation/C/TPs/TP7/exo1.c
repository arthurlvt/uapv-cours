#include <stdio.h>
#include <stdlib.h>
int addDonation(int *total, int newDonation);
void processDonors(int *totalDonations)
{
    int newDonation;
    int numDonations;
    printf("Entrez le nombre de dons : ");
    scanf("%d", &numDonations);
    for (int i = 0; i < numDonations ; i++) 
    {
        printf("Donation #%d : ", i + 1);
        scanf("%d", &newDonation);
        addDonation(totalDonations, newDonation);
    }
}
int addDonation(int *total, int newDonation) 
{
    *total += newDonation;
    return *total;
}
int main() 
{
    int totalDonations = 0;
    processDonors(&totalDonations);
    printf("Total des dons : %d\n", totalDonations);
    return 0;
}