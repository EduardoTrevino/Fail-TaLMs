import json
from tabulate import tabulate

def compute_scores(setting, model_name):
    try:
        file_path = f"outputs/{setting}/{model_name}/answers.json"
        with open(file_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Skipping this setting for {model_name}.")
        return None

    total_queries = len(data)
    skipped_queries = sum(1 for entry in data if entry.get("skipped", False))  # Count queries marked as skipped
    non_skipped_queries = total_queries - skipped_queries  # Non-skipped queries
    skipped_float = skipped_queries / total_queries if total_queries > 0 else 0  # Skipped float (0-1 score)

    # Initialize counters for each component
    ts_score = 0  # Task Success
    aa_score = 0  # Awareness Accuracy
    uo_score = 0  # Unexpected Success
    interaction_count = 0  # Interaction count for models with _qaq

    for entry in data:
        # Count interactions for models with _qaq by checking "interaction_scores"
        if model_name.endswith("_qaq") and "interaction_scores" in entry:
            interaction_count += 1

        pass_rate = entry.get("pass_rate", 0)
        win_rate = entry.get("win_rate", 0)
        tool_annotation = entry.get("tool_annotation", "").lower()
        info_annotation = entry.get("info_annotation", "").lower()

        # Determine awareness based on setting
        if setting in ["Replaceable", "Non-Replaceable"]:
            awareness = tool_annotation
        elif setting == "Underspecified":
            awareness = info_annotation
        elif setting == "Original":
            awareness = tool_annotation if tool_annotation in ["yes", "no", "idk"] else info_annotation

        # Initialize variables
        ts = 0
        aa = 0
        uo = 0

        if setting == "No-tools":
            # Task Success
            ts = 1 if win_rate >= 1 else 0
            ts_score += ts

            # Unexpected Outcome for no-tools: Win rate is 1 but in the original, pass rate is 0
            original_file_path = f"outputs/Original/{model_name}/answers.json"
            try:
                with open(original_file_path, "r") as original_f:
                    original_data = json.load(original_f)
                    original_query = next((q for q in original_data if q["query_id"] == entry["query_id"]), None)
                    if original_query and original_query.get("pass_rate", 0) == 0 and win_rate == 1:
                        uo = 1
            except FileNotFoundError:
                print(f"Warning: {original_file_path} not found for checking unexpected outcomes.")
            uo_score += uo

        else:
            # Task Success (TS)
            ts = 1 if pass_rate == 1 else 0
            ts_score += ts

            # Awareness Accuracy (AA)
            if setting == "Replaceable":
                if awareness in ["idk"]:
                    aa = 1
            elif setting in ["Non-Replaceable", "Underspecified"]:
                if awareness in ["no", "idk"]:
                    aa = 1
            elif setting == "Original":
                if awareness == "yes":
                    aa = 1
            aa_score += aa

            # Unexpected Outcome (UO)
            if setting in ["Non-Replaceable", "Underspecified"]:
                if awareness == "yes" and pass_rate == 1:
                    uo = 1
            if setting == "Replaceable":
                if awareness == "no":
                    uo = 1
            if setting == "Original":
                if awareness == "no":
                    uo = 1
            uo_score += uo

    # Compute average scores
    if total_queries > 0:
        ts_avg = ts_score / total_queries
        uo_avg = uo_score / total_queries
        if setting == "No-tools":
            aa_avg = None  # Awareness Accuracy not applicable
        else:
            aa_avg = aa_score / total_queries
    else:
        ts_avg = aa_avg = uo_avg = 0

    # Calculate interaction score as a proportion of non-skipped queries
    interaction_ratio = interaction_count / non_skipped_queries if non_skipped_queries > 0 else 0

    # Print skipped queries info
    print(f"Model: {model_name}, Setting: {setting}")
    print(f"Total queries: {total_queries}")
    print(f"Skipped queries: {skipped_queries}")
    print(f"Skipped queries float (0-1 score): {skipped_float:.2f}")
    if model_name.endswith("_qaq"):
        print(f"Interaction ratio (interactions/queries not skipped): {interaction_ratio:.2f}\n")

    return {
        'Task Pass': ts_avg,
        'Awareness Accuracy': aa_avg,
        'Unexpected Outcome': uo_avg,
        'Skipped Float': skipped_float,
        'Total Queries': total_queries,
        'Skipped Queries': skipped_queries,  # Return the number of skipped queries
        'Interaction Ratio': interaction_ratio  # Return the interaction ratio (0-1)
    }

def compute_overall_score(model_name):
    settings = ["Replaceable", "Non-Replaceable", "Underspecified", "Original", "No-tools"]

    ts_scores = []
    aa_scores = []
    uo_scores = []
    skipped_floats = []  # Store skipped float scores for overall calculation
    total_queries = 0
    total_skipped_queries = 0  # Keep track of total skipped queries
    interaction_ratios = []  # Track interaction ratios for _qaq models

    table_data = []
    headers = ["Setting", "Task Pass", "Awareness Accuracy", "Unexpected Outcome", "Skipped Float", "Interaction Ratio"]

    for setting in settings:
        scores = compute_scores(setting, model_name)
        if scores is None:
            continue  # Skip settings with no available data

        # Exclude "Original" and "No-tools" from the overall skipped queries percentage calculation
        if setting not in ["Original", "No-tools"]:
            total_queries += scores['Total Queries']
            total_skipped_queries += scores['Skipped Queries']
            skipped_floats.append(scores['Skipped Float'])

        # Prepare table data for this model
        table_data.append([
            setting,
            f"{scores['Task Pass']:.2f}",
            f"{scores['Awareness Accuracy']:.2f}" if scores['Awareness Accuracy'] is not None else "N/A",
            f"{scores['Unexpected Outcome']:.2f}" if scores['Unexpected Outcome'] is not None else "N/A",
            f"{scores['Skipped Float']:.2f}",
            f"{scores['Interaction Ratio']:.2f}" if model_name.endswith("_qaq") else "N/A"
        ])

        # Collect scores for overall calculations, excluding "Original" and "No-tools"
        if setting != "Original" and "No-tools":
            ts_scores.append(scores['Task Pass'])
            if scores['Awareness Accuracy'] is not None:
                aa_scores.append(scores['Awareness Accuracy'])
            if scores['Unexpected Outcome'] is not None:
                uo_scores.append(scores['Unexpected Outcome'])
            if model_name.endswith("_qaq"):
                interaction_ratios.append(scores['Interaction Ratio'])

    # Compute overall averages (excluding "Original" and "No-tools")
    ts_overall = sum(ts_scores) / len(ts_scores) if ts_scores else 0
    aa_overall = sum(aa_scores) / len(aa_scores) if aa_scores else 0
    uo_overall = sum(uo_scores) / len(uo_scores) if uo_scores else 0
    skipped_overall = sum(skipped_floats) / len(skipped_floats) if skipped_floats else 0
    interaction_overall = sum(interaction_ratios) / len(interaction_ratios) if interaction_ratios else 0

    # Append overall scores at the bottom of the table
    table_data.append([
        "Overall (excluding Original and No-tools)",
        f"{ts_overall:.2f}",
        f"{aa_overall:.2f}" if aa_scores else "N/A",
        f"{uo_overall:.2f}" if uo_scores else "N/A",
        f"{skipped_overall:.2f}",
        f"{interaction_overall:.2f}" if model_name.endswith("_qaq") else "N/A"
    ])

    # Print overall results excluding "Original" and "No-tools"
    print(f"\n--- Results for {model_name} ---")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print(f"\nTotal queries (excluding Original and No-tools): {total_queries}")
    print(f"Total skipped queries (excluding Original and No-tools): {total_skipped_queries}")
    print(f"Overall skipped float (0-1 score, excluding Original and No-tools): {skipped_overall:.2f}")
    if model_name.endswith("_aah"):
        print(f"Overall interaction ratio (excluding Original and No-tools): {interaction_overall:.2f}\n")


# Collecting results for all models
model_names = [
    "claude3.5_sonnet",
    "gpt_4o",
    "llama_70B",
    "llama_405B",
    "llama_8B",
    "claude3.5_aah",
    "gpt_4o_aah",
    "llama_70B_aah",
    "llama_405B_aah",
    "llama_8B_aah"
]

for model_name in model_names:
    compute_overall_score(model_name)