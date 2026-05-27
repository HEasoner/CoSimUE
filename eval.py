import json

def load_data(file_path):
    with open(file_path, 'r') as f:
        data = [json.loads(line) for line in f]
    return data


def calculate_accuracy(data):

    N_L = sum(1 for d in data if d['category'] == 'L')
    N_V = sum(1 for d in data if d['category'] == 'V')
    N_total = len(data)

    # T-H Pair Accuracy
    T_H_correct = sum(1 for d in data if d['answer_original'] == d['true_answer_original'] and 
                                          d['answer_hallucination'] == d['true_answer_hallucination'])
    Consistent_answers = sum(1 for d in data if d['answer_original'] == d['answer_hallucination'])

    T_H_accuracy = T_H_correct / N_total
    Consistentcy = Consistent_answers / N_total
    

    # Co-occurrence Pair Accuracy (for category L)
    L_correct = sum(1 for d in data if d['category'] == 'L' and 
                                         d['answer_original'] == d['true_answer_original'] and
                                         d['answer_hallucination'] == d['true_answer_hallucination'])
    Co_occurrence_accuracy = L_correct / N_L if N_L > 0 else 0

    # Similarity Pair Accuracy (for category V)
    V_correct = sum(1 for d in data if d['category'] == 'V' and 
                                         d['answer_original'] == d['true_answer_original'] and
                                         d['answer_hallucination'] == d['true_answer_hallucination'])
    Similarity_accuracy = V_correct / N_V if N_V > 0 else 0

    # All Accuracy
    all_correct = sum(1 for d in data if d['answer_original'] == d['true_answer_original']) + sum(1 for d in data if d['answer_hallucination'] == d['true_answer_hallucination'])
    Yes_answers = sum(1 for d in data if d['answer_original'] == "yes") + sum(1 for d in data if d['answer_hallucination'] == "yes")
    N_total = 2 * N_total
    All_accuracy = all_correct / N_total
    Yes_bias = Yes_answers / N_total

    return {
        "T-H Pair Accuracy": T_H_accuracy,
        "Co-occurrence Pair Accuracy": Co_occurrence_accuracy,
        "Similarity Pair Accuracy": Similarity_accuracy,
        "All Accuracy": All_accuracy,
        "Yes Bias": Yes_bias,
        "Pair Consistency": Consistentcy
    }


data = load_data('./output_results_qwen3-vl-235b-a22b-thinking.jsonl')
result = calculate_accuracy(data)
print(result)
