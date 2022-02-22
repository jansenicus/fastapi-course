Known Current Limitation on Mac:
https://docs.docker.com/desktop/mac/networking/


For example:
```yaml
    ports:
      - "5050:80"
    expose:
      - "80"
```

In this case:
On Linux, open browser to the exposed port http://localhost:80/
Will fail when trying to connect with Mac to http://localhost:80/

Workaround:
On Mac, open browser to the original http://localhost:5050/ 
instead of the intended exposed port http://localhost:80/

