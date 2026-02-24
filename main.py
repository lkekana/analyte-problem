from itertools import permutations
import time

ALLOW_LEADING_ZERO = False

def solve():
    solutions = []
    iterations = 0
    start_time = time.time()

    for S in (0, 5):
        for R in (0, 2, 4, 6, 8):
            if R == S:
                continue

            remaining_digits = [d for d in range(10) if d not in (S, R)]
            # T, V, E cannot be zero (leading letters)
            for perm in permutations(remaining_digits, 7):
                T, H, I, V, E, Y, A = perm  # noqa: E741
                # print(f"Iteration {iterations}: T={T}, H={H}, I={I}, S={S}, V={V}, E={E}, R={R}, Y={Y}, A={A}")

                if not ALLOW_LEADING_ZERO:
                    if T == 0 or V == 0 or E == 0:
                        continue

                if I == 5:
                    continue

                if T == 9 or V == 9:
                    continue

                THIS = 1000*T + 100*H + 10*I + S
                IS   = 10*I + S
                VERY = 1000*V + 100*E + 10*R + Y
                EASY = 1000*E + 100*A + 10*S + Y

                if THIS > 9999:
                    continue

                if IS > 99:
                    continue

                if VERY > 9999:
                    continue

                if EASY > 9999:
                    continue

                if THIS + IS + VERY == EASY:
                    solutions.append({
                        'T': T, 'H': H, 'I': I, 'S': S,
                        'V': V, 'E': E, 'R': R, 'Y': Y, 'A': A
                    })
                iterations += 1

    end_time = time.time()
    duration = end_time - start_time

    print()
    if ALLOW_LEADING_ZERO:
        print("\033[1mWith leading zeros allowed:\033[0m")
    else:
        print("\033[1mWithout leading zeros allowed:\033[0m")

    print(f"> Solved in {duration:.2f} seconds\n")
    
    print(f"Total iterations: {iterations}")
    print(f"Total solutions: {len(solutions)}")
    
    print("\n\033[1mValid Solutions:\033[0m\n")
    for sol in solutions:
        THIS = 1000*sol['T'] + 100*sol['H'] + 10*sol['I'] + sol['S']
        IS   = 10*sol['I'] + sol['S']
        VERY = 1000*sol['V'] + 100*sol['E'] + 10*sol['R'] + sol['Y']
        EASY = 1000*sol['E'] + 100*sol['A'] + 10*sol['S'] + sol['Y']
        print(f"T={sol['T']} H={sol['H']} I={sol['I']} S={sol['S']} V={sol['V']} E={sol['E']} R={sol['R']} Y={sol['Y']} A={sol['A']}")
        print(f"{THIS:04d} + {IS:02d} + {VERY:04d} = {EASY:04d}")
        print()

    # print the available solutions for each letter
    # print("\nAcross all valid solutions, the following values were used for each letter:")
    # for letter in ['T', 'H', 'I', 'S', 'V', 'E', 'R', 'Y', 'A']:
    #     available_values = set(sol[letter] for sol in solutions)
    #     print(f"Values used for {letter}: {', '.join(str(v) for v in sorted(available_values))}")
    # print()


if __name__ == "__main__":
    solve()
