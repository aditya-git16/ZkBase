from py_ecc.bn128 import G1, multiply, add, eq

# 5 = 2 + 3
assert eq(multiply(G1, 5), add(multiply(G1, 2), multiply(G1, 3)));
