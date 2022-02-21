Known Current Limitation on Mac:
cannot connect to exposed port on Mac, use original (inner) port instead.

For example:
```yaml
    ports:
      - "5050:80"
    expose:
      - "80"
```
On Mac, open browser to the original http://localhost:5050/ 
instead of the intended exposed port http://localhost:80/

On Linux, open browser to the exposed port http://localhost:80/
