
# LR-VuserLog-Fetcher


- Imagine you have a LoadRunner script which has n number of users and you want to check for which user it is failing
- Of course, you can run in vugen itself with n iterations to fetch that, but let me tell you one amazing way to fetch the same
- Clone this repository running below command
```
git clone https://github.com/shayansaha85/LR-VuserLog-Fetcher.git
```
- Install python from this link : [Python](https://www.python.org/downloads/)
- Our this code uses three libraries : **flask**, **re**, and **os**
- **re** and **os** will be pre-installed with Python
- For downloading **flask** run below command in your terminal
```
pip install flask
```
_**Note** : pip will be installed automatically when you will install Python_
- Go to the cloned repository folder and run below command to run the application
```
python fetch-parameter.py
```
- Launch any API testing client (e.g. Postman, ThunderClient)
- User below configurations to run the API
    - URL : **http://localhost:3333/generateParams**
    - Method : **POST**
    - Paylod :
    ```json
    {
        "log_folder" : "<Enter the path of the log foler where all VuserLog files are present>",
        "parameter" : "<Enter the name of the parameter>",
        "output_path" : "<Enter the output folder path>"
    }
    ```
    Example :
    ```json
    {
        "log_folder" : "/Users/shayan/Documents/code/LR-VUSERLOG-Fetcher/Logs",
        "parameter" : "p_Username",
        "output_path" : "/Users/shayan/Desktop"
    }
    ```
- The API will read all log files present in the defined Log folder location in paylod ("log_folder")
- Find out the exact parameter value defined in parameter in payload ("parameter")
- Save the output with only the parameter values in the output folder location defined in payload ("output_path")

**Web UI Version** : https://github.com/shayansaha85/LR-VuserLog-Fetcher-WebUI
