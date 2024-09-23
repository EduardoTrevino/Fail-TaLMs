import os
import json
def interact_with_human(requires_input=int, input_text=None):
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
    
    requires_input_normalized = str(requires_input).strip().lower()

    # Initialize interaction data
    interaction_data = None

    # Check if user input is required
    print(f"Bool value: {requires_input}, Model's Interaction text:\n {input_text}")
    
    if requires_input_normalized in ['1', 'true']:
        # Prompt the user for input and gather evaluation score
        user_response = input(f"Your response: {input_text}: ")
        evaluate_question_score = input(f"Was the model's interaction appropriate? Yes (1) or No (0): ")
        print("Evaluation Score: ", evaluate_question_score)
         # Increment interaction count
        interaction_data = {
            'score': evaluate_question_score,
            'question': input_text,
            'user_response': user_response
        }

        function_response = f"You requested additional information from the user and asked: {input_text}. The user responded with: {user_response}"
        
    else:
        # No user input is required, return a predefined message
        function_response = "No user input is required to answer their query."
        interaction_data = None

    return function_response, interaction_data