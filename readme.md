1. add file .env in ./ with SPEECHACE_API_KEY = #key
2. run ./demo.py
3. press space to start recording and press space again to stop
4. check the latest json in ./results to see the scoring details

Note: 
If you want to test the Score Task feature, please put the task context (no more than 1024 characters) in ./task_context.txt;
Otherwise, please set task_assigned = False in ./demo.py