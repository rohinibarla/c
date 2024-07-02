## July 2nd 2024: Experimentations done
Exeperiments:
- single input
- double input
- dounle input checks with files

## Observations
1. **There is no mechanism for validating prompt message.**

### TODO: Fork check50 repo and add functionality to validate prompt message
Validation of prompt in check50 library as part of stdin function
https://github.com/cs50/check50/blob/f6aa5de4164fd427a46aa28f7754a84b8be9a609/check50/_api.py#L195C12-L195C18  

It just consumes the prompt message here.  

As part of function  
 def stdin(self, line, str_line=None, prompt=True, timeout=3):  
https://github.com/cs50/check50/blob/f6aa5de4164fd427a46aa28f7754a84b8be9a609/check50/_api.py#L169C4-L169C66  
