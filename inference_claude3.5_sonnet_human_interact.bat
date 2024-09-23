@echo off
REM Set the output directory
set OUTPUT_DIR=outputs\Original\claude3.5_sonnet_auto_eval_mod_test

REM Read the OpenAI key from the file and set it as a variable
for /f %%i in (proxy_key.txt) do set OPENAI_KEY=%%i

REM Set PYTHONPATH
set PYTHONPATH=.

REM Create the output directory if it doesn't exist
if not exist %OUTPUT_DIR% mkdir %OUTPUT_DIR%

REM Run the Python script with the necessary arguments
python inference\pipeline_claude_auto_eval_mod.py ^
    --tool_root_dir tools\ ^
    --model neulab/claude-3-5-sonnet-20240620 ^
    --openai_key %OPENAI_KEY% ^
    --input_query_file benchmark\one_Original_queries.json ^
    --output_answer_file %OUTPUT_DIR%\answers.json ^
    --use_human_interact true
