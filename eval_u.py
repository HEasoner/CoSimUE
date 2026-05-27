import json

def load_data(file_path):
    with open(file_path, 'r') as f:
        data = [json.loads(line) for line in f]
    return data

def calculate_accuracy(data):
    uncertainty = 0
    for d in data:
        uncertainty = uncertainty + float(d['uncertainty'])
    uncertainty_1 = 0
    for d in data:
        if d['category'] == 1:
            uncertainty_1 = uncertainty_1 + float(d['uncertainty'])
    uncertainty_2 = 0
    for d in data:
        if d['category'] == 2:
            uncertainty_2 = uncertainty_2 + float(d['uncertainty'])
    uncertainty_3 = 0
    for d in data:
        if d['category'] == 3:
            uncertainty_3 = uncertainty_3 + float(d['uncertainty'])
    print(f'all uncertainty:{uncertainty}')
    print(f'I uncertainty:{uncertainty_1}')
    print(f'II uncertainty:{uncertainty_2}')
    print(f'III uncertainty:{uncertainty_3}')


data = load_data('./output_results_mplug-owl3-7b.jsonl')
result = calculate_accuracy(data)
