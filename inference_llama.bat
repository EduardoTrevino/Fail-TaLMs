@echo off
REM Set the output directory
set OUTPUT_DIR=outputs\Original\llama_70b

REM Read the OpenAI key from the file and set it as a variable
for /f %%i in (proxy_key.txt) do set OPENAI_KEY=%%i

REM Set PYTHONPATH
set PYTHONPATH=.

REM Create the output directory if it doesn't exist
if not exist %OUTPUT_DIR% mkdir %OUTPUT_DIR%

REM Run the Python script with the necessary arguments
python inference\pipeline_llama.py ^
    --tool_root_dir tools\ ^
    --model neulab/meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo ^
    --openai_key %OPENAI_KEY% ^
    --input_query_file benchmark\all_Original_queries.json ^
    --output_answer_file %OUTPUT_DIR%\answers.json
