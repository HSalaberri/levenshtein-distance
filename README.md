# levenshtein-distance
Levenshtein distance calculator

### Running the name finder

```bash
python3 levenshtein.py -i data/20210103_hundenamen.csv -n Luca -d 1
```

### User interface

```bash
usage: levenshtein [-h] -i INPUT_DATA -n NAME -d DISTANCE

Calculate levenshtein distance

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_DATA, --input INPUT_DATA
                        Path to file containing data [.csv]
  -n SEARCH_NAME, --name NAME
                        name
  -d DISTANCE, --distance DISTANCE
                        distance
```