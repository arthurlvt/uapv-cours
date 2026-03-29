# FUNCTION TO CALCULATE DISCRIMINANT AND ROOTS OF A POLYNOMIAL OF DEGREE 2
def calculate_discriminant(a, b, c):
    """
    Calculates the discriminant (delta) and the real roots of a quadratic equation (ax^2 + bx + c = 0).
    """
    delta = b**2 - 4*a*c
    if delta > 0:
        root1 = (-b + delta**0.5) / (2*a)
        root2 = (-b - delta**0.5) / (2*a)
        return "The discriminant is positive and there are two distinct real roots: " + str(delta), (root1, root2)
    elif delta == 0:
        root = -b / (2*a)
        return "The discriminant is zero and there is only one real root: " + str(delta), (root,)
    else:
        return "The discriminant is negative and there are no real roots"
        
def solve_quadratic():
    """
    Prompts the user for coefficients a, b, c and returns the roots result.
    """
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    result = calculate_discriminant(a, b, c)
    return result

def display_result():
    """
    Solves the quadratic equation and displays the result.
    """
    result = solve_quadratic()
    print("Result:", result)

def main():
    display_result()

if __name__ == "__main__":
    main()


# FUNCTION TO CALCULATE THE NUMBER OF MONTHS NEEDED FOR A STOCK TO REACH A CERTAIN VALUE
def months_to_reach_value():
    """
    Calculates the number of months required for a stock, starting at 57.0 with a 3% monthly growth rate, 
    to reach or exceed 200.0.
    """
    valeur_initiale = 57.0  # Initial price
    taux_croissance = 0.03 # 3%
    valeur_cible = 200.0  # Target value
    
    valeur_actuelle = valeur_initiale
    nombre_mois = 0
    
    # Continue as long as the current value is strictly less than the target
    while valeur_actuelle < valeur_cible:
        valeur_actuelle *= (1 + taux_croissance) # 3% increase
        nombre_mois += 1
        
    return nombre_mois

def months_to_reach_value_general(prix_initial, taux_mensuel, valeur_cible):
    """
    Calculates the number of months required for a stock with a given initial price and 
    monthly rate to reach or exceed a target value.
    """
    # Basic checks (positive price, positive rate)
    if prix_initial <= 0 or taux_mensuel <= 0 or valeur_cible <= prix_initial:
        # If the target is already reached or if the rates are invalid
        return 0 
        
    valeur_actuelle = prix_initial
    nombre_mois = 0
    
    while valeur_actuelle < valeur_cible:
        valeur_actuelle *= (1 + taux_mensuel)
        nombre_mois += 1
        
    return nombre_mois


# FUNCTION TO CALCULATE THE SUM OF THE DIGITS OF A POSITIVE INTEGER
def sum_digits(n):
    """
    Calculates the sum of the digits that make up the positive integer n.
    """
    if n < 0:
        n = abs(n) # Ensure we are working with a positive number
        
    somme = 0
    
    # Conversion to a string to iterate over the digits
    chaine_n = str(n)
    
    for chiffre_char in chaine_n:
        # Convert the digit character to an integer
        somme += int(chiffre_char)
        
    return somme


# FUNCTION TO DETERMINE IF A YEAR IS A LEAP YEAR
def is_leap_year(annee):
    """
    Checks if a given year is a leap year.
    """
    # Rule 3: divisible by 400 (takes precedence)
    if annee % 400 == 0:
        return True
    
    # Rule 2: divisible by 100 (but not 400)
    if annee % 100 == 0:
        return False
        
    # Rule 1: divisible by 4 (and not 100)
    if annee % 4 == 0:
        return True
        
    return False


# FUNCTION TO CHECK IF TWO FLOATING-POINT NUMBERS ARE IDENTICAL WITHIN A CERTAIN EPSILON
def are_identical_epsilon(a, b, epsilon=1e-9): # Changed default epsilon for better float comparison
    """
    Determines if two numbers a and b are identical within a given tolerance (epsilon).
    """
    # Numbers are identical within epsilon if the absolute value of their difference
    # is less than or equal to epsilon.
    return abs(a - b) <= epsilon


# FUNCTION TO DETERMINE IF THREE SQUARES OF LENGTHS CAN FORM A RIGHT TRIANGLE
def are_squares_of_right_triangle(c1, c2, c3):
    """
    Checks if the three values (c1, c2, c3) can represent the squares of the
    side lengths of a right triangle (Pythagorean theorem).
    """
    # The squares of the lengths must be positive
    if c1 <= 0 or c2 <= 0 or c3 <= 0:
        return False

    # Using a small tolerance (epsilon) for float comparison
    epsilon = 1e-9 
    
    # We check the three possible combinations for the hypotenuse (the largest square)
    
    # Case 1: c3 is the hypotenuse
    if are_identical_epsilon(c1 + c2, c3, epsilon):
        return True
        
    # Case 2: c2 is the hypotenuse
    if are_identical_epsilon(c1 + c3, c2, epsilon):
        return True
        
    # Case 3: c1 is the hypotenuse
    if are_identical_epsilon(c2 + c3, c1, epsilon):
        return True
        
    return False


# FUNCTION TO DETERMINE IF A NUMBER IS PRIME
def is_prime(n):
    """
    Checks if the integer n (greater than 1) is a prime number.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    # A prime number is only divisible by 1 and itself.
    # We check divisibility up to the square root of n.
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False # Found a divisor
        i += 1
        
    return True


# FUNCTION TO FIND THE SMALLEST PRIME DIVISOR OF A NUMBER
def smallest_prime_divisor(n):
    """
    Returns the smallest prime divisor of the integer n (greater than 1).
    """
    if n <= 1:
        return None
        
    i = 2
    while i * i <= n:
        if n % i == 0:
            # We check if i is prime (optional but safer)
            if is_prime(i):
                return i
        i += 1
        
    # If the loop finishes without a divisor found, n itself is prime
    return n 


# FUNCTION TO DECOMPOSE A NUMBER INTO ITS PRIME FACTORS
def decompose_prime_factors(n):
    """
    Decomposes the integer n (n > 1) into its prime factors.
    """
    if n <= 1:
        return str(n)
        
    temp_n = n
    
    # The 'chaine' variable to store the text format as requested
    chaine = ""
    
    while temp_n > 1:
        d = smallest_prime_divisor(temp_n) # Find the smallest prime divisor
        
        if chaine != "":
            chaine += " x " # Add the " x " separator
            
        chaine += str(d) # Add the divisor to the string
        
        # Update temp_n using integer division
        temp_n //= d
        
    # The prompt asks to return a string.
    return chaine