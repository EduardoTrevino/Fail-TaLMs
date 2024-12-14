#!/bin/bash

# Set the output directory
OUTPUT_DIR="outputs/{data_setting}/{model_name}"

# Read the OpenAI key from the file and set it as a variable
if [[ -f "your_api_key.txt" ]]; then
  OPENAI_KEY=$(<your_api_key.txt)
else
  echo "Error: your_api_key.txt not found!"
  exit 1
fi

# Set PYTHONPATH
export PYTHONPATH=.

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Run the Python script with the necessary arguments
python inference/pipeline_{model_name}.py \
  --tool_root_dir tools/ \
  --model {model_name} \
  --api_key "$OPENAI_KEY" \
  --input_query_file benchmark/{data_setting}/all_{data_setting}_queries.json \
  --output_answer_file "$OUTPUT_DIR/answers.json" \
  --use_human_interact false
