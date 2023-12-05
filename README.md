# ZkBase

TBD LATER:

1. We do not want attackers to be able to take an elliptic curve point and compute the field element that generated it. If the order of our cyclic group is too small, then the attacker can just brute force it.

2. It is an exercise for the reader to do something more sophisticated, like prove knowledge of a solution to a linear system of equations.


As a (very important) hint, multiplying a number by a constant is the same thing as repeated addition. Repeated addition is the same thing as elliptic curve scalar multiplication. Thus, if x is an elliptic curve point, we can multiply it by a scalar 9 as multiply(x, 9). This is consistent with our statement that we cannot multiply elliptic curve points – we are actually multiplying an elliptic curve point by a scalar, not another point.


Can you prove you know x such that 23x = 161? Can you generalize this to more variables?


As another hint: you (the prover) and the verifier need to agree on the formula in advance, as the verifier will be running the same “structure” of the original formula you claim to know the solution for.

3. https://en.wikipedia.org/wiki/Baby-step_giant-step

4. Example: Proving integer division was done properly
Proving finite field division was done properly is easy, we saw that in the first example. But if we want to prove a / b = c for integer division this is trickier than just saying a * b = c.


Consider the example of 7 / 2. The solution is 3 in integer division, but 2 * 3 ≠ 7. We need to verify two claims: 3 is the quotient of 7 / 2, and 1 is the remainder. So the first entry in our proof is quotient * divisor + remainder == numerator. This is not a sufficient constraint because a malicious prover could provide 2 * 2 + 3 == 7 — they would be proving 7 / 2 = 2 and the quotient is 3. Additional constraints are needed to ensure the division was done properly. The implementation details of this are left as an exercise for the reader.


Example: Proving a list was sorted
Suppose I give you two arrays, A and B, and I claim that B is the sorted version of A. In this section, we will learn about auxiliary computations. That is, we ask the prover to do additional work to back up their claim.


One way you can verify this is to sort A yourself, but carrying out merge sort or quick sort as a set of multiplications is rather challenging.


Let’s think about this in reverse. Suppose B is a sorted version of A. Then the following set of facts must be true:

A and B have the same length

B is itself sorted

A and B have the same elements

We already know how to accomplish the first two checks using the sections above, but what about the last one? Computing the mapping ourselves, especially only with addition and multiplication will be rather challenging. Thankfully we don’t need to compute the mapping ourselves. We ask the prover to give us the mapping from the unsorted list to the sorted one and then we verify the mapping is a valid one.

For example, one way to permute vectors is to do matrix multiplication in the following manner:

circuit permutation validation
Such a sparse matrix can have an efficient representation, but let’s not concern ourselves with that. To verify the “transformation matrix” is valid, we need to ensure each element is zero or one, and each row and column contains exactly one “1” with the rest being zeros. If these constraints are not in place, then the prover could prove that the “sorted” list contains elements that are not in the original array.


How a malicious prover could accomplish this, and determining what the proper constraints are, are an exercise for the reader.
