from main import rangesum  # , newtonsum

for n in range(4, 20):
    ref = sum(range(n))
    assert rangesum(n) == ref
    # assert newtonsum(n) == ref
