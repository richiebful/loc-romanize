import csv
import sys

if len(sys.argv) < 2:
    print("Please pass a string argument into the script")
    exit(1)
else:
    rustring = ' '.join(sys.argv[1:])

with open('ru-mapping.csv', 'r+', encoding='utf-8-sig') as csv_fp:
    mapreader = csv.reader(csv_fp)
    mappairs = [r for r in mapreader]
    mappairs = [(r[0].strip(), r[1]) for r in mappairs]
    
ru_en_map = str.maketrans(dict(mappairs))
print(rustring.translate(ru_en_map))
exit(0)
