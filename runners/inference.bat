@echo off
REM Set the output directory
set OUTPUT_DIR=outputs\{data_setting}\{model_name}

REM Read the api key from the file and set it as a variable
for /f %%i in (your_api_key.txt) do set OPENAI_KEY=%%i

REM Set PYTHONPATH
set PYTHONPATH=.

REM Create the output directory if it doesn't exist
if not exist %OUTPUT_DIR% mkdir %OUTPUT_DIR%

REM Run the Python script with the necessary arguments
python inference\pipeline_{model_name}.py ^
    --tool_root_dir tools\ ^
    --model {model_name} ^
    --api_key %OPENAI_KEY% ^
    --input_query_file benchmark\{data_setting}\all_{data_setting}_queries.json ^
    --output_answer_file %OUTPUT_DIR%\answers.json
    --use_human_interact false