from mpmath import mp
mp.dps = 1000000
pi_str = mp.nstr(mp.pi, 1000000, strip_zeros=False).replace('3.', '3')
pos = pi_str.find('230107', 1)  # skip the leading 3
print(f'Motif trouvé à la position (décimale) : {pos}')
print(f'Contexte : ...{pi_str[pos-3:pos+10]}...')
