-> Systèmes d'Equations Linéaires - L1 informatique 2025
1. Systèmes simples: Résoudre les systèmes suivants:
    a) x + y + 2z = 3
       x + 2y + z = 1
       2x + y + z = 0
    -> Résolution:
       x + y + 2z = 3   (1)
       y - z = -2       (2) (en soustrayant (1) de (2))
       -y -3z = -6      (3) (en soustrayant (1) de (3))

       x + y + 2z = 3   (1)
       y - z = -2       (2)
       -4z = -8         (3) (en ajoutant (2) à (3))
    -> Solution: z = 2, y = 0, x = -1

    b) x + 2z = 1
       -y + z = 2
       x - 2y = 1
    -> Résolution:
       x + 2z = 1       (1)
       -y + z = 2       (2) (en sous)
       -2y - 2z = 0     (3) (en soustrayant (1) de (3))

       x + 2z = 1       (1)
       -y + z = 2       (2)
       -4z = -4         (3) (en soustrayant (3) de 2*(2))
    -> Solution: z = 1, y = 1, x = -1

2. + inconnues ou équations: Résoudre les systèmes suivants:
    a) x + y + z - 3t = 1
       2x + y - z + t = 1
    -> Résolution:
       x + y + z - 3t = 1 (1)
       -y -3z + 7t = -1   (2) (en soustrayant 2*(1) de (2))
      
       x = -y -z +3t + 1  (3) (en isolant x dans (1))
       y = -3z + 7t + 1   (4) (en isolant y dans (2))
       z = z              (5) (z est une variable libre)
       t = t              (6) (t est une variable libre)
    S = {(-y - z + 3t + 1, -3z + 7t + 1, z, t) | z, t ∈ ℝ^2}


