# ZkBase

TBD LATER:

1. We do not want attackers to be able to take an elliptic curve point and compute the field element that generated it. If the order of our cyclic group is too small, then the attacker can just brute force it.

2. It is an exercise for the reader to do something more sophisticated, like prove knowledge of a solution to a linear system of equations.


As a (very important) hint, multiplying a number by a constant is the same thing as repeated addition. Repeated addition is the same thing as elliptic curve scalar multiplication. Thus, if x is an elliptic curve point, we can multiply it by a scalar 9 as multiply(x, 9). This is consistent with our statement that we cannot multiply elliptic curve points – we are actually multiplying an elliptic curve point by a scalar, not another point.


Can you prove you know x such that 23x = 161? Can you generalize this to more variables?


As another hint: you (the prover) and the verifier need to agree on the formula in advance, as the verifier will be running the same “structure” of the original formula you claim to know the solution for.

3. https://en.wikipedia.org/wiki/Baby-step_giant-step
