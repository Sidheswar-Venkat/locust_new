from locust import HttpLocust,TaskSet
from locust_CONFIG import *

def login(l):
    l.client.post("/vektordata/authenticate/local", json=CONFIG["local"])
    l.client.get("/vektordata/authenticate/user")

def kc_page1(l):
    result = l.client.get("/vektordata/solutions")
    result = result.json()
    project_Id=""
    for resp in result:
        if resp["displayName"] == CONFIG["solution_name"]:
                project_Id=resp["kcProject"]["id"]
                break
    #print project_Id
    l.client.get("/vektordata/projects/"+project_Id)
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/dashboards")
    l.client.get("/vektordata/projects/"+project_Id+"/stats")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/signalsets?projectId="+project_Id)
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports")
    result=l.client.get("/vektordata/workflows?projectId="+project_Id)
    result=result.json()
    definition_id1=""
    for resp in result:
        if resp["name"] == CONFIG["definition"]:
            definition_id1 = resp["id"]
            break
    #print definition_id1
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+definition_id1)

    result=l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id)
    result=  result.json()
    result_list = result["filterMenu"]["subject"]
    sub = ""
    for resp in result_list:
        if resp["name"] == inputs1["name_value2"]:
            sub = resp["id"]
            break
    #print sub

    #1b
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id+"&subject="+sub)
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&subject="+sub)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    result = l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&subject="+sub)
    result=result.json()
    result_list = result["filterMenu"]["relationship"]
    relationship = ""
    for resp in result_list:
        if resp["name"] == inputs1["name_value1"]:
            relationship = resp["id"]
            break
    #print relationship

    #1c
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&subject="+sub+"&relationship="+relationship+"&relationship_mode=any")
    result = l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&relationship="+relationship+"&relationship_mode=any&subject="+sub)
    result = result.json()
    result_list= result["signals"]
    signal_id = ""
    number = ""
    for res in result_list:
        if res["name"] == inputs1["name_value8"]:
            signal_id = res["signalSetId"]
            number = res["id"]
    #print number
    #print signal_id

    #1d
    result = l.client.post("/vektordata/signals/list/signalstable", json={"id": [number]})
    result = result.json()
    id_1=id_2=id_3=id_4=""
    result_list = result[number]["propagation"]
    for resp in result_list:
        if resp["view"]["fqn"] == inputs1["fqn_1"] and id_1 == "":
            id_1 = resp["view"]["id"]
        if resp["view"]["fqn"] == inputs1["fqn_2"] and id_2 == "":
            id_2 = resp["view"]["id"]
        if resp["view"]["fqn"] == inputs1["fqn_3"] and id_3 == "":
            id_3 = resp["view"]["id"]
        if resp["view"]["fqn"] == inputs1["fqn_4"] and id_4 == "":
            id_4 = resp["view"]["id"]
    #print id_1
    #print id_2
    #print id_3
    #print id_4
    l.client.get("/vektordata/collections/list?id="+signal_id)
    #l.client.get("/vektordata/views/list?id="+id_1+"&id="+id_2+"&id="+id_3+"&id="+id_4)

    #1e
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&subject="+sub)
    result = l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&subject="+sub)
    result=result.json()
    result_list = result["filterMenu"]["window"]
    window1 = ""
    for resp in result_list:
        if resp["displayName"] == inputs1["name_value7"]:
            window1 = resp["id"]
            break
    #print window1

    #1f
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&subject="+sub+"&window="+window1+"&window_mode=any")
    result = l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&subject="+sub+"&window="+window1+"&window_mode=any")
    result=result.json()
    result_list = result["filterMenu"]["relationship"]
    relationship2 = ""
    for resp in result_list:
        if resp["name"] == inputs1["name_value6"]:
            relationship2 = resp["id"]
            break
    #print relationship2

    #1g
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&subject="+sub+"&window="+window1+"&relationship="+relationship2+"&window_mode=any&relationship_mode=any")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&relationship="+relationship2+"&relationship_mode=any&subject="+sub+"&window="+window1+"&window_mode=any")

    #1h
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&subject="+sub+"&window="+window1+"&relationship="+relationship2+"&search=front%20store%20trip&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&window_mode=any&relationship_mode=any")
    result = l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&relationship="+relationship2+"&relationship_mode=any&search=front+store+trip&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&subject="+sub+"&window="+window1+"&window_mode=any")
    result = result.json()
    result_list= result["signals"]
    number1 = ""
    signal_id_2=""
    for res in result_list:
        if res["name"] == inputs1["name_value9"]:
            signal_id_2 = res["signalSetId"]
            number1 = res["id"]
    #print number1
    #print signal_id_2

    #1i
    l.client.post("/vektordata/signals/list/signalstable", json={"id": [number1]})
    #l.client.get("/vektordata/views/list?id="+signal_id_2)

    #1j
    l.client.get("/vektordata/views/"+signal_id_2+"?projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/schemas?definitionId="+signal_id_2+"&formulaType=definition")
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+signal_id_2)
    l.client.get("/vektordata/signalsets/"+signal_id_2+"/signalstable?outputLimitSize=25&outputOffset=0")
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+signal_id_2)
    l.client.get("/vektordata/diagrams/columnlevel?projectId="+project_Id+"&columnId="+number1)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&columnId="+number1)
    l.client.get("/vektordata/diagrams/columnlevel?projectId="+project_Id+"&columnId="+number1)
    l.client.get("/vektordata/workflows?definitionId="+signal_id_2+"&projectId="+project_Id)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&columnId="+number1)
    l.client.get("/vektordata/diagrams/columnlevel?projectId="+project_Id+"&columnId="+number1)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&columnId="+number1)
    l.client.get("/vektordata/diagrams/columnlevel?projectId="+project_Id+"&columnId="+number1)

    #2a
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)

    #2b
    l.client.get("/vektordata/projects/"+project_Id+"/stats")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+definition_id1)

    #2c
    result = l.client.get("/vektordata/signalsets?projectId="+project_Id)
    result = result.json()
    signal_set_id = ""
    for resp in result:
        if resp["name"] == inputs1["signal_set_name"]:
            signal_set_id = resp["id"]
            break
    #print signal_set_id
    l.client.get("/vektordata/views/"+signal_set_id+"?projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/schemas?definitionId="+signal_set_id+"&formulaType=definition")
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs1["value_1"]+"/results/measuresLatest")
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+signal_set_id)
    result = l.client.get("/vektordata/signalsets/"+signal_set_id+"/signalstable?outputLimitSize=25&outputOffset=0")
    result = result.json()
    result_list = result["signals"]
    id_99 = ""
    for res in result_list:
        if res["name"] == inputs1["name_value11"]:
            id_99 = res["id"]
            break
    #print "id_99 : 359633", id_99
    result = l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+signal_set_id)
    result = result.json()
    result_list= result["nodes"]
    id_100 = ""
    for res in result_list:
        if res["properties"]["fqn"] == inputs1["fqn_value8"]:
            id_100 = res["id"]
            break
    #print id_100

    #2d
    l.client.get("/vektordata/views/"+signal_set_id+"?projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/schemas?definitionId="+signal_set_id+"&formulaType=definition")
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs1["value_1"]+"/results/measuresLatest")
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+signal_set_id)
    l.client.get("/vektordata/signalsets/"+signal_set_id+"/signalstable?outputLimitSize=25&outputOffset=0")
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+signal_set_id)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&columnId="+id_99)
    l.client.get("/vektordata/diagrams/columnlevel?projectId="+project_Id+"&columnId="+id_99)

    #2e
    l.client.post("/vektordata/signals/list/signalstable", json={"id": [id_99]})
    #l.client.get("/vektordata/views/list?id="+signal_set_id)

    #2f
    l.client.get("/vektordata/schemas/definitions/list?id="+id_100+"&id="+signal_set_id)
    #l.client.get("/vektordata/views/list?id="+id_100+"&id="+signal_set_id)
    l.client.get("/vektordata/signals/signalstable?signalId="+number+"&signalId="+number1+"&signalId="+id_99)
    l.client.get("/vektordata/schemas/definitions/list?id="+id_100+"&id="+signal_set_id)
    #l.client.get("/vektordata/views/list?id="+id_100+"&id="+signal_set_id)
    l.client.get("/vektordata/signals/signalstable?signalId="+number+"&signalId="+number1+"&signalId="+id_99)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)

    #2g
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs1["value_1"]+"/labels")
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs1["value_1"]+"/variants")

    #2h
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports")
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports/"+inputs1["report"]+"/executions")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs1["value_1"]+"/labels")
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs1["value_1"]+"/variants")
    l.client.get("/vektordata/schemas?definitionId="+signal_set_id)
    result = l.client.post("/vektordata/sample", json=inputs1["sample"])
    result = result.json()
    sample_id = ""
    try:
        sample_id = result["sampleId"]
    except:
        sample_id = None

    if sample_id != None:
        l.client.post("/vektordata/sample/"+sample_id, json=inputs1["sample2"])
        #2i
        l.client.post("/vektordata/sample/"+sample_id, json=inputs1["sample3"])
        #2j
        l.client.post("/vektordata/sample/"+sample_id, json=inputs1["sample4"])
        #2k
        #l.client.get("/vektordata/sample/"+sample_id+"/csv", json=inputs1["download"])

    #3a
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)

    #3b
    l.client.get("/vektordata/projects/"+project_Id+"/stats")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports")
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports/executions")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id)
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+definition_id1)

    #3c
    l.client.get("/vektordata/projects/"+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    if sample_id != None:
        l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports/"+inputs1["script"])
        l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports/"+inputs1["script"]+"/executions")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)

    #3d
    if sample_id != None:
        l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports/"+inputs1["script"]+"/executions")
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports")
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports/executions")

    #3e
    l.client.get("/vektordata/projects/"+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    if sample_id != None:
        l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports/"+inputs1["script"])
        l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports/"+inputs1["script"]+"/executions")

    #3g
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)

    #4a
    l.client.get("/vektordata/schemas/definitions/list?id="+id_100+"&id="+signal_set_id)
    #l.client.get("/vektordata/views/list?id="+id_100+"&id="+signal_set_id)
    l.client.get("/vektordata/signals/signalstable?signalId="+number+"&signalId="+number1+"&signalId="+id_99)
    l.client.get("/vektordata/schemas/definitions/list?id="+id_100+"&id="+signal_set_id)
    #l.client.get("/vektordata/views/list?id="+id_100+"&id="+signal_set_id)
    l.client.get("/vektordata/signals/signalstable?signalId="+number+"&signalId="+number1+"&signalId="+id_99)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)

    #4c
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)

    print "********************************************************************"

class Task1(TaskSet):
        tasks = {kc_page1 : 1}
        def on_start(self):
            login(self)

class WebsiteUser(HttpLocust):
    task_set = Task1
