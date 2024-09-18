@echo off
REM Set the output directory
set OUTPUT_DIR=outputs\benchmark\GPT4o_original_test

REM Read the OpenAI key from the file and set it as a variable
for /f %%i in (proxy_key.txt) do set OPENAI_KEY=%%i

REM Set PYTHONPATH
set PYTHONPATH=.

REM Create the output directory if it doesn't exist
if not exist %OUTPUT_DIR% mkdir %OUTPUT_DIR%

REM Run the Python script with the necessary arguments
python inference\pipeline.py ^
    --tool_root_dir tools\ ^
    --model openai/neulab/gpt-4o-2024-05-13 ^
    --openai_key %OPENAI_KEY% ^
    --input_query_file benchmark\Original\Art\query_1.json ^
    --output_answer_file %OUTPUT_DIR%\answers.json