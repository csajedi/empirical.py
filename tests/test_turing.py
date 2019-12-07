import compute.turing as utm


def test_incr_machine():
    print("incr machine\n")
    tape = utm.run(
        halt="qf",
        state="q0",
        tape=list("111"),
        blank="B",
        rules=map(tuple, ["q0 1 1 right q0".split(), "q0 B 1 stay  qf".split()]),
    )
    assert tape == ["qf", 1, 1, 1, [1]]

def test_busy_beaver():
    print("\nbusy beaver\n")
    tape = utm.run(
        halt = 'halt',
        state = 'a',
        blank = '0',
        rules = map(tuple,
            ["a 0 1 right b".split(),
            "a 1 1 left  c".split(),
            "b 0 1 left  a".split(),
            "b 1 1 right b".split(),
            "c 0 1 left  b".split(),
            "c 1 1 stay  halt".split()]
            )
        )
    assert(tape == [TODO])

def test_nsorting():
    print("\nsorting test\n")
    utm.run(halt = 'STOP',
        state = 'A',
        blank = '0',
        tape = "2 2 2 1 2 2 1 2 1 2 1 2 1 2".split(),
        rules = map(tuple,
        ["A 1 1 right A".split(),
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
            "E 0 0 right STOP".split()]
            )
        )
    assert(tape == [TODO])