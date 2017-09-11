from locust import HttpLocust,TaskSet
from locust_CONFIG import *

def login(l):
    l.client.post("/vektordata/authenticate/local", json=CONFIG["local"])
    l.client.get("/vektordata/authenticate/user")

def kc_page9(l):
    result = l.client.get("/vektordata/solutions")
    result = result.json()
    project_Id=" "
    for resp in result:
        if resp["displayName"] == CONFIG["solution_name"]:
                project_Id=resp["kcProject"]["id"]
                break
    #print project_Id
    l.client.get("/vektordata/projects/"+project_Id)
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/dashboards")
    l.client.get("/vektordata/projects/"+project_Id+"/stats")
    result=l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    result=result.json()
    result_list=result["filterMenu"]["data_layer"]
    for resp in result_list:
        if resp["name"] == inputs9["datalayer_name"]:
            data_layer = resp["id"]
    #print data_layer
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/signalsets?projectId="+project_Id)
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id)
    result=l.client.get("/vektordata/workflows?projectId="+project_Id)
    result=result.json()
    definition_Id=""
    for key in result:
        if key["name"] == CONFIG["definition"]:
            definition_Id = key["id"]
    #print definition_Id
    l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+definition_Id)

    #1a
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&data_layer="+data_layer+"&data_layer_mode=any")
    l.client.get("/vektordata/diagrams/kitchenlevel?data_layer="+data_layer+"&data_layer_mode=any&output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id)

    #1b
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&data_layer="+data_layer+"&search="+inputs9["search1"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&data_layer_mode=any")
    result=l.client.get("/vektordata/diagrams/kitchenlevel?data_layer="+data_layer+"&data_layer_mode=any&output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&search="+inputs9["search1"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
    result=result.json()
    result_list=result["signals"]
    id1=id2=id3=id4=id5=id6=id7=id8=id9=id10=""
    id11=id12=id13=id14=id15=""
    for key in result_list:
        if key["signalSourceFQN"] == inputs9["signal_name3"]:
            signalId3=key["id"]
        if key["signalSourceFQN"] == inputs9["signal_name4"]:
            signalId4=key["id"]
        if key["signalSourceFQN"] == inputs9["signal_name5"]:
            signalId5=key["id"]
    #print signalId3
    #print signalId4
    #print signalId5
    for resp in result_list:
        if resp["description"] == inputs9["description_name"]:
            resp_key1=resp["propagation"]
        if resp["fqn"] == inputs9["fqn_value1"]:
            resp_key2=resp["propagation"]
        if resp["fqn"] == inputs9["fqn_value2"]:
            resp_key3=resp["propagation"]
    for list in resp_key1:
        if list["view"]["fqn"] == inputs9["id1_name"]:
            id1=list["view"]["id"]
        if list["view"]["fqn"] == inputs9["id2_name"]:
            id2=list["view"]["id"]
        if list["view"]["fqn"] == inputs9["id3_name"]:
            id3=list["view"]["id"]
        if list["view"]["fqn"] == inputs9["id4_name"]:
            id4=list["view"]["id"]
        if list["view"]["fqn"] == inputs9["id5_name"]:
            id5=list["view"]["id"]
    #print id1
    #print id2
    #print id3
    #print id4
    #print id5
    for list in resp_key2:
        if list["view"]["fqn"] == inputs9["id6_name"]:
            id6=list["view"]["id"]
        if list["view"]["fqn"] == inputs9["id7_name"]:
            id7=list["view"]["id"]
        if list["view"]["fqn"] == inputs9["id8_name"]:
            id8=list["view"]["id"]
        if list["view"]["fqn"] == inputs9["id9_name"]:
            id9=list["view"]["id"]
        if list["view"]["fqn"] == inputs9["id10_name"]:
            id10=list["view"]["id"]
    #print id6
    #print id7
    #print id8
    #print id9
    #print id10
    for list in resp_key3:
        if list["view"]["fqn"] == inputs9["id11_name"]:
            id11=list["view"]["id"]
        if list["view"]["fqn"] == inputs9["id12_name"]:
            id12=list["view"]["id"]
        if list["view"]["fqn"] == inputs9["id13_name"]:
            id13=list["view"]["id"]
        if list["view"]["fqn"] == inputs9["id14_name"]:
            id14=list["view"]["id"]
        if list["view"]["fqn"] == inputs9["id15_name"]:
            id15=list["view"]["id"]
    #print id11
    #print id12
    #print id13
    #print id14
    #print id15

    #1c
    l.client.post("/vektordata/signals/list/signalstable", json={"id": [signalId5]})
    #l.client.get("/vektordata/views/list?id="+id1+"&id="+id2+"&id="+id3+"&id="+id4+"&id="+id5)

    #1d
    l.client.post("/vektordata/signals/list/signalstable", json={"id": [signalId3]})
    #l.client.get("/vektordata/views/list?id="+id6+"&id="+id7+"&id="+id8+"&id="+id9+"&id="+id10)
    l.client.post("/vektordata/signals/list/signalstable", json={"id": [signalId4]})
    #l.client.get("/vektordata/views/list?id="+id11+"&id="+id12+"&id="+id13+"&id="+id14+"&id="+id15)

    #1e
    result=l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
    result=result.json()
    result_list=result["filterMenu"]["relationship"]
    for dict in result_list:
        if dict["displayName"] == inputs9["displayName1"]:
            relationship_id=dict["id"]
    #print relationship_id
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")

    #1f
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&search="+inputs9["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&search="+inputs9["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")

    #1g
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&relationship="+relationship_id+"&search="+inputs9["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&relationship_mode=any")
    result=l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&relationship="+relationship_id+"&relationship_mode=any&search="+inputs9["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
    result=result.json()
    subject_Id=""
    result_list=result["signals"]
    for resp in result_list:
        if resp["fqn"] == inputs9["id16_name"]:
            id16=resp["signalSetId"]
            signalId1=resp["id"]
        if resp["fqn"] == inputs9["signal_name1"]:
            signalId1=resp["id"]
        if resp["fqn"] == inputs9["signal_name2"]:
            signalId2=resp["id"]

    result_list=result["filterMenu"]["subject"]
    for key in result_list:
        if key["displayName"] == inputs9["displayName2"]:
            subject_Id=key["id"]
    #print id16
    #print signalId1
    #print signalId2
    #print subject_Id

    #1h
    l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&relationship="+relationship_id+"&subject="+subject_Id+"&search="+inputs9["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&relationship_mode=any&subject_mode=any")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&relationship="+relationship_id+"&relationship_mode=any&search="+inputs9["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&subject="+subject_Id+"&subject_mode=any")

    #1i
    l.client.post("/vektordata/signals/list/signalstable", json={"id": [signalId1]})
    #l.client.get("/vektordata/views/list?id="+id16)

    #1j
    l.client.post("/vektordata/signals/list/signalstable", json={"id": [signalId2]})

    #2a
    l.client.get("/vektordata/schemas/definitions/list?id="+id16+"&id="+id8+"&id="+id12+"&id="+id5)
    #l.client.get("/vektordata/views/list?id="+id16+"&id="+id8+"&id="+id12+"&id="+id5)
    l.client.get("/vektordata/signals/signalstable?signalId="+signalId1+"&signalId="+signalId2+"&signalId="+signalId3+"&signalId="+signalId4+"&signalId="+signalId5)
    l.client.get("/vektordata/schemas/definitions/list?id="+id16+"&id="+id8+"&id="+id12+"&id="+id5)
    #l.client.get("/vektordata/views/list?id="+id16+"&id="+id8+"&id="+id12+"&id="+id5)
    l.client.get("/vektordata/signals/signalstable?signalId="+signalId1+"&signalId="+signalId2+"&signalId="+signalId3+"&signalId="+signalId4+"&signalId="+signalId5)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)

    #2b
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs9["data"]["view"]+"/labels")
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs9["data"]["view"]+"/variants")

    #2c
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports")
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports/"+inputs9["data"]["reportName"]+"/executions")
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs9["data"]["view"]+"/labels")
    l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs9["data"]["view"]+"/variants")
    l.client.get("/vektordata/schemas?definitionId="+id16)
    l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)

    print "********************************************************************"

class Task9(TaskSet):
        tasks = {kc_page9 : 1}
        def on_start(self):
            login(self)

class WebsiteUser(HttpLocust):
    task_set = Task9
