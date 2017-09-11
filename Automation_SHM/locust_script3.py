from locust import HttpLocust, TaskSet
from locust_CONFIG import *

def login(l):
    l.client.post("/vektordata/authenticate/local", json=CONFIG["local"])
    l.client.get("/vektordata/authenticate/user")

def kc_page3(l):
    result = l.client.get("/vektordata/solutions")
    result = result.json()
    project_id = ""
    for resp in result:
        if resp["displayName"] == CONFIG["solution_name"]:
                project_id=resp["kcProject"]["id"]
                break
    #print project_id
    l.client.get("/vektordata/projects/"+project_id)
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/dashboards")
    l.client.get("/vektordata/projects/"+project_id+"/stats")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    result=l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id)
    result = result.json()
    result_list=result["collections"]
    definition_id_3 = ""
    for resp in result_list:
        if resp["name"] == inputs3["definition_id3_name"]:
            definition_id_3 = resp["vertexId"]
            break
    #print definition_id_3
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/signalsets?projectId="+project_id)
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports")
    result = l.client.get("/vektordata/workflows?projectId="+project_id)
    result = result.json()
    definition_id = ""
    for resp in result:
        if resp["name"] == CONFIG["definition"]:
            definition_id = resp["id"]
            break
    #print definition_id
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id)

    #1a
    l.client.get("/vektordata/projects/"+project_id+"/stats")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports")
    l.client.get("/vektordata/collections?projectId="+project_id)
    result = l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id)
    result = result.json()
    result_list=result["nodes"]
    definition_id_2 = ""
    for resp in result_list:
        if resp["properties"]["fqn"] == inputs3["definition_id2_name"]:
            definition_id_2 = resp["id"]
    #print definition_id_2
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id)

    #1c
    l.client.get("/vektordata/collections/"+definition_id_2+"?projectId="+project_id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/schemas?definitionId="+definition_id_2+"&formulaType=definition")
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_2)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_2)

    #1f
    l.client.get("/vektordata/collections/"+definition_id_2+"/source")

    #1g
    l.client.get("/vektordata/workflows?definitionId="+definition_id_2+"&projectId="+project_id)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_2)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_2)

    #1i
    l.client.get("/vektordata/currentFiles?collectionFQN="+inputs3['definition_id2_name']+"&solutionName="+CONFIG["solution"])

    #1j
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_2)

    #2a
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/collections/"+definition_id_2+"?projectId="+project_id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/schemas?definitionId="+definition_id_2+"&formulaType=definition")
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_3)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_3)

    #2c
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)

    #2d
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)

    print "********************************************************************"

class Task3(TaskSet):
    tasks = {kc_page3 : 1}
    def on_start(self):
        login(self)

class WebsiteUser(HttpLocust):
    task_set = Task3
