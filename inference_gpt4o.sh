export OUTPUT_DIR="outputs/benchmark/GPT4o_original_test"
export OPENAI_KEY=$(cat proxy_key.txt)
export PYTHONPATH=./

mkdir -p $OUTPUT_DIR
python inference/pipeline.py \
    --tool_root_dir tools/ \
    --model openai/neulab/gpt-4o-2024-05-13 \
    --openai_key $OPENAI_KEY \
    --input_query_file benchmark/Original/Art/query_1.json \
    --output_answer_file $OUTPUT_DIR/answers.json
