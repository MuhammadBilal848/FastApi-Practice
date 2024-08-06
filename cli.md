* To run the app so that others can use APIs using "ip'.
```
uvicorn app:app --host 0.0.0.0 --port any_port --reload
```


* The --workers option is used to specify the number of workers that can hit API concurrently. 
```
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4 --reload
```

