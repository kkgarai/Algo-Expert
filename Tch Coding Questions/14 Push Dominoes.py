"""
Push Dominoes

There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.



After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state.

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Note:

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.'
"""


# O(N) time / O(N) space
class Solution:
    def pushDominoes(self, d: str) -> str:
        N = len(d)
        force = [0] * N

        # Populate Rs
        f = 0
        for i in range(N):
            if d[i] == "R":
                f = N
            elif d[i] == "L":
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] += f

        # Populate Ls
        for i in range(N - 1, -1, -1):
            if d[i] == "L":
                f = N
            elif d[i] == "R":
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] -= f

        for i in range(N):
            if force[i] == 0:
                force[i] = "."
            elif force[i] < 0:
                force[i] = "L"
            else:
                force[i] = "R"
        return "".join(force)
