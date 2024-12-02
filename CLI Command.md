* To run the app so that others can use APIs using "ip'. Also `--reload` helps reload terminal automatically once u change code.
```
uvicorn app:app --host 0.0.0.0 --port any_port --reload
```

* The --workers option is used to specify the number of workers that can hit API concurrently. In other words **workers** sets how many times we can hit api simultaneously to check if it is breaking or not due to load.
```
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4  
```

* To run it on other machines, you can give them your **ip** and assign that ip a port and you are good to go.
```
your_ip:port
192.168.10.2:8000
```
