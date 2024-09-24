@echo off
REM Set the output directory
set OUTPUT_DIR=outputs\Replaceable\llama_70B_auto_eval

REM Read the OpenAI key from the file and set it as a variable
for /f %%i in (proxy_key.txt) do set OPENAI_KEY=%%i

REM Set PYTHONPATH
set PYTHONPATH=.

REM Create the output directory if it doesn't exist
if not exist %OUTPUT_DIR% mkdir %OUTPUT_DIR%

REM Run the Python script with the necessary arguments
python inference\pipeline_llama_auto_eval.py ^
    --tool_root_dir tools\ ^
    --model neulab/meta-llama/Meta-Llama-3.1-70B-Instruct ^
    --openai_key %OPENAI_KEY% ^
    --input_query_file benchmark\subset_Replaceable_queries_21-100.json ^
    --output_answer_file %OUTPUT_DIR%\answers.json ^
    --use_human_interact false

