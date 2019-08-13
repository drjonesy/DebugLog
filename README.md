# Debug Log 
An alternative to the default Python logging

## Overview

The DebugLog file contains the main Log class and two functions for debugging: TEST and PAUSE.

### Log (class)
The **Log** class has five levels of debug messages.
```log
INFO = 0
DEBUG = 1
WARNING = 2
ERROR = 3
CRITICAL = 4
```

#### Initalizing
```python
log = Log(logPath="logs/Debug/2019-08-13.log", level=Log.DEBUG)
```
#### Debug Functions
All functions, excluding Lvl, take a string message.

| Function  | Data Type | Description |
| ------------- | ------------- | ------------- |
| msg      | string | log a message|
| info     | string | log a messsage with **INFO** followed by the message |
| debug    | string | log a messsage with **DEBUG** followed by the message |
| warning  | string | log a messsage with **WARNING** followed by the message |
| error    | string | log a messsage with **ERROR** followed by the message |
| critial  | string | log a messsage with **CRITIAL** followed by the message |
| Lvl      | int    | changes the level of debug message that can write to the log file |

#### Optional Functions

- TEST
- PAUSE

## Sample Code

```python
if __name__ == "__main__":
    log = Log(logPath="logs/Debug/2019-08-13.log", level=Log.INFO)
    log.info(msg="This is a test")
    log.Lvl(level=Log.ERROR)
    log.warning(msg="This is warning message")
    log.error(msg="This is an error message")
```