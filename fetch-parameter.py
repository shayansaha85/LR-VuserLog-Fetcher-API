from flask import *
import re
import os

app = Flask(__name__)



@app.route("/generateParams", methods = ["POST"])
def generateParams():
    apiOutput = {}
    input_json = request.get_json(force=True) 

    log_file_folder_path = ""
    parameter_name = ""
    path = ""
    
    log_file_folder_path = str(input_json["log_folder"])
    parameter_name = str(input_json["parameter"])
    path = str(input_json["output_path"])
    count = 0
    if len(log_file_folder_path) != 0 and len(parameter_name) != 0 and len(path) != 0:
        try:
            logFileList = list(os.listdir(log_file_folder_path))
            def readLogfile(file_path):
                    file = open(file_path, "r")
                    raw_data = file.read()
                    file.close()
                    return raw_data

            parameters = []
            k = 1
            for file in logFileList:
                file_path = os.path.join(log_file_folder_path, file)
                content = readLogfile(file_path)
                paramList = re.findall(f"\"{parameter_name}\" = \"(.+?)\"", content)
                # print(f"{k}. {paramList}")
                # k = k+1
                if len(paramList) != 0:
                    for param in paramList:
                        parameters.append(param)
                else:
                        count += 1
            # print(count)
            if count != len(logFileList):
                paramFileContent = ""
                paramFileContent += parameter_name + "\n"
                for parameter in parameters:
                    paramFileContent += parameter + "\n"

                parameter_file_name = str(parameter_name) + "_filtered.txt"
                outputFile = open(os.path.join(path, parameter_file_name), "w")
                outputFile.write(paramFileContent)
                outputFile.close()
                apiOutput["message"] = "Parameter generated successfully"
                apiOutput["output_file_path"] = str(os.path.join(path, parameter_file_name))

            else:
                    apiOutput["error_message"] = "The parameter does not exists in the log files"
        except:
             apiOutput["error_message"] = "Could not generate due to some internal server error"
    else:
         apiOutput["error_message"] = "Either payload is empty or provided wrong information"

    return apiOutput

app.run(port=3333)