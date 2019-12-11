import itertools

# https://rosettacode.org/wiki/Universal_Turing_machine#Python
def run(state=None, blank=None, rules=[], tape=[], halt=None, pos=0):
    st = state
    if not tape:
        tape = [blank]
    if pos < 0:
        pos += len(tape)
    if pos >= len(tape) or pos < 0:
        raise ValueError("bad init position")
    rules = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in rules)

    while True:
        print(st, "\t", end=" ")
        for i, v in enumerate(tape):
            if i == pos:
                print("[%s]" % (v,), end=" ")
            else:
                print(v, end=" ")
        print()

        if st == halt:
            break
        if (st, tape[pos]) not in rules:
            break

        (v1, dr, s1) = rules[(st, tape[pos])]
        tape[pos] = v1
        if dr == "left":
            if pos > 0:
                pos -= 1
            else:
                tape.insert(0, blank)
        if dr == "right":
            pos += 1
            if pos >= len(tape):
                tape.append(blank)
        st = s1
    return tape

def batch_run():
    """Runner for batches of tasks, taken from the cpp implementation: https://www.algorithmicdynamics.net/software.html"""

def binary_machines(n):
    """The number of possible n-state, binary Turing machines."""
    return (4 * n + 2) ** (2 * n)


def enumerate_instructions(states):
    """Yields all possible transitions for an n-state machine."""
    for state in reversed(["Z"] + list(range(states))):
        for symbol in [0, 1]:
            for move in [-1, 1]:
                yield (symbol, move, state)


def enumerate_transitions(states):
    """Generate all possible transition functions."""
    for i in itertools.product(enumerate_instructions(states), repeat=states * 2):
        trans = {}
        n = 0
        if len(i) > states:
            for state in range(states):
                for symbol in [0, 1]:
                    trans[(state, symbol)] = i[n]
                    n += 1
        return trans


def enumerate_utms(n=1):
    total = (4 * n + 2) ** (2 * n)
    print(
        "Total number of unique rulesets for {n} state, 2 symbol TM: {total} \n".format(
            n=n, total=total
        )
    )

    # Define positional arguments for ruleset string
    halt = "halt"
    state = "a"
    blank = "0"
    rules = ""
    for i in range(total):
        print("The {i} UTM has parameters: \n".format(i=i))


if __name__ == "__main__":

    # EXAMPLES

    print("incr machine\n")
    run(
        halt="qf",
        state="q0",
        tape=list("111"),
        blank="B",
        rules=map(tuple, ["q0 1 1 right q0".split(), "q0 B 1 stay  qf".split()]),
    )

    print("\nbusy beaver\n")
    run(
        halt="halt",
        state="a",
        blank="0",
        rules=map(
            tuple,
            [
                "a 0 1 right b".split(),
                "a 1 1 left  c".split(),
                "b 0 1 left  a".split(),
                "b 1 1 right b".split(),
                "c 0 1 left  b".split(),
                "c 1 1 stay  halt".split(),
            ],
        ),
    )

    print("\nsorting test\n")
    run(
        halt="STOP",
        state="A",
        blank="0",
        tape="2 2 2 1 2 2 1 2 1 2 1 2 1 2".split(),
        rules=map(
            tuple,
            [
                "A 1 1 right A".split(),
                "A 2 3 right B".split(),
                "A 0 0 left  E".split(),
                "B 1 1 right B".split(),
                "B 2 2 right B".split(),
                "B 0 0 left  C".split(),
                "C 1 2 left  D".split(),
                "C 2 2 left  C".split(),
                "C 3 2 left  E".split(),
                "D 1 1 left  D".split(),
                "D 2 2 left  D".split(),
                "D 3 1 right A".split(),
                "E 1 1 left  E".split(),
                "E 0 0 right STOP".split(),
            ],
        ),
    )
    print(enumerate_transitions(2))

