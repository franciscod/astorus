import astor

ORIGINAL = 'main.py'

a = astor.parsefile(ORIGINAL)

print(astor.dump(a))
