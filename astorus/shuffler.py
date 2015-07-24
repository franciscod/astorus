import os
import sys
import astor
import difflib

from etc import nsplit, scorediff

# this is a cool thing that lets you import walk.py on local dir
sys.path.append(os.getcwd())
from walk import LightWalk, BoomWalk  #E402

TESTS = 'test.py'
ORIGINAL = 'main.py'

test_source = open(TESTS).read()
original_source = open(ORIGINAL).read()
a = astor.parsefile(ORIGINAL)
normalized_source = astor.to_source(a)

print("### TEST SUITE ###:", TESTS)
print('')
print(test_source)
print('')

print("### IMPLEMENTATION CODE ###:", ORIGINAL)
print('')
print(original_source)
print('')

print("### NORMALIZED CODE (after AST library round trip) ###")
print('')
print(normalized_source)
print('')

print("crunching some numbers just for you, hang on...")

path_count = LightWalk(a).count + 1
bw = BoomWalk()

candidate_programs = set()

# get some candidates

for n in range(2 ** path_count):
    a = astor.parsefile(ORIGINAL)

    bw.path = n
    bw.count = 0

    bw.walk(a)

    candidate_programs.add(astor.to_source(a))

# lets try them!
candidate_id = 0
best_diff, best_score = None, None

for candidate_source in candidate_programs:
    #print(candidate_source)
    #print("")
    #print("")
    exec(candidate_source)

    try:
        exec(test_source)
    except AssertionError:
        continue

    print("")
    print("found a good diff!")
    candidate_id += 1

    d = list(difflib.unified_diff(
            nsplit(normalized_source),
            nsplit(candidate_source),
            fromfile=ORIGINAL,
            tofile='pretty_cool_diff_' + str(candidate_id) + '.py'))

    for line in d:
        sys.stdout.write(line)

    sc = scorediff(d)
    print("it has a score of", sc)

    if best_diff is None or best_score < sc:
        best_diff = d
        best_score = sc

    print('')

if best_diff is None:
    print ("Booo, no diff found")
else:
    print("THE WINNER DIFF IS")
    for line in best_diff:
        sys.stdout.write(line)
    print("IT HAS A MAGNIFICENT SCORE OF", best_score)
