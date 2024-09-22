import os
import json
def interact_with_human(requires_input=int, input_text=None, query_id=None, output_file=None):
    """
    Conditionally prompts the user to type some text based on the 'requires_input' flag
    and returns whatever they typed or a predefined message. ONLY CALL THIS FUNCTION IF YOU ABSOLUTELY NEED INPUT FROM THE USER. First determine if you can fulfill their request on your own using the other available tools, if you determined you absolutely need input from the human to fulfill their request, then proceed, and interact with the human. 
    Note: If you are giving instructions to gather information, be sure to instruct the human to provide you the information so you may give the final answer.
    Parameters:
    - requires_input (int): Flag to determine if user input is needed (1) or not (0).
    - input_text (str, optional): Question to ask the user to gather additional information that is needed.

    Returns:
    - str: The user input response to your question or a predefined message.
    """
    # Initialize interaction count for this query_id if not present
    interaction_count = 0

    # Load existing results from the output file
    if os.path.exists(output_file):
        with open(output_file, 'r') as f:
            results = json.load(f)
            # Find the query entry and check for interaction count
            for result in results:
                if result.get('query_id') == query_id:
                    interaction_count = len(result.get('interaction_scores', []))
                    break

    # Increment interaction count
    interaction_count += 1
    
    requires_input_normalized = str(requires_input).strip().lower()

    # Check if user input is required
    print(f"Bool value being passed: {requires_input}, input text: {input_text}")
    
    if requires_input_normalized in ['1', 'true']:
        # Prompt the user for input and gather evaluation score
        user_response = input(f"Your response: {input_text}: ")
        evaluate_question_score = input(f"Was the model's interaction appropriate? Yes (1) or No (0): ")

        # Append interaction score and count to the output file
        append_evaluation_score(query_id, output_file, evaluate_question_score, interaction_count)
        
        return f"You requested additional information from the user and asked: {input_text}. The user responded with: {user_response}"
    
    else:
        # No user input is required, return a predefined message
        return "No user input is required to answer their query."


def append_evaluation_score(query_id, output_file, score, count):
    """
    Append the evaluation score and interaction count to the output file for a given query ID.

    Parameters:
    - query_id (str): The query ID being processed.
    - output_file (str): The path to the output file.
    - score (str): The evaluation score (1 for yes, 0 for no).
    - count (int): The number of times this function was called for this query.
    """
    # Load existing results from the output file
    if os.path.exists(output_file):
        with open(output_file, 'r') as f:
            results = json.load(f)
    else:
        results = []

    # Check if the query ID already exists in the results
    query_result = next((res for res in results if res['query_id'] == query_id), None)

    if query_result:
        # Append the new score and interaction count
        if 'interaction_scores' not in query_result:
            query_result['interaction_scores'] = []
        query_result['interaction_scores'].append({
            'score': score,
            'count': count
        })
    else:
        # Create a new entry for this query ID if it doesn't exist
        new_result = {
            'query_id': query_id,
            'interaction_scores': [{
                'score': score,
                'count': count
            }]
        }
        results.append(new_result)

    # Write the updated results back to the output file
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)