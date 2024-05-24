1. add file .env in ./ with SPEECHACE_API_KEY = "put the key here" if .env does not exist
2. put the task context in folder ./context as txt files (one file for one task rubric using a distinct file name, no more than 1024 characters each)
3. run command "python ./demo_record.py" for task score test by recording directly, or run "python ./demo_score_task.py" with recorded files.
4. press space to start recording and press space again to stop
5. check the latest json in ./results to see the scoring details
