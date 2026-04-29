#include <stdio.h>
#include <stdlib.h>

void addExpense(int *tableExpensesByDay, int monthLength) {
    int day, spendings;

    printf("For which day do you want to enter your spendings? ");
    scanf("%d", &day);

    printf("How much did you spend that day? ");
    scanf("%d", &spendings);

    tableExpensesByDay[day - 1] += spendings;
}

void manageExpenses(int monthLength, int *tableExpensesByDay) {
    int n;
    printf("How many expenses do you want to enter? ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        addExpense(tableExpensesByDay, monthLength);
    }
}

int main() {
    int monthLength;

    printf("What is the length of the month? ");
    scanf("%d", &monthLength);
    int *tableExpensesByDay = malloc(monthLength * sizeof(int));

    manageExpenses(monthLength, tableExpensesByDay);
    printf("\nFinal expenses by day:\n");
    for (int i = 0; i < monthLength; i++) {
        printf("Day %d: %d\n", i + 1, tableExpensesByDay[i]);
    }

    free(tableExpensesByDay);
}
