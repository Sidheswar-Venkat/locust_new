from locust import TaskSet, task
from kc_config import *

class Task7(TaskSet):
    @task
    def kc_page7(l):
        result = l.client.get("/vektordata/solutions")
        result = result.json()
        project_id=""
        for resp in result:
            if resp["displayName"] == CONFIG['solution_name']:
                    project_id=resp["kcProject"]["id"]
                    break
        #print project_id
        l.client.get("/vektordata/projects/"+project_id)
        l.client.get("/vektordata/solutions/"+CONFIG['solution']+"/dashboards")
        l.client.get("/vektordata/projects/"+project_id+"/stats")
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
        l.client.get("/vektordata/signalsets?projectId="+project_id)
        l.client.get("/vektordata/solutions/"+CONFIG['solution']+"/reports")
        result = l.client.get("/vektordata/workflows?projectId="+project_id)
        result = result.json()
        definition_id = ""
        for resp in result:
            if resp["name"] == CONFIG['definition']:
                definition_id = resp["id"]
                break
        #print definition_id
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id)
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id)

        #1b
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id)
        result = l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
        result = result.json()
        data_layer=""
        resp_list = result["filterMenu"]["data_layer"]
        for resp in resp_list:
            if resp["name"] == inputs7['datalayer_name']:
                data_layer = resp["id"]
                break
        #print data_layer
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id+"&data_layer="+data_layer+"&data_layer_mode=any")
        l.client.get("/vektordata/diagrams/kitchenlevel?data_layer="+data_layer+"&data_layer_mode=any&output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id)

        #1c
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id+"&data_layer="+data_layer+"&search="+inputs7['search_text_1']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&data_layer_mode=any")
        result = l.client.get("/vektordata/diagrams/kitchenlevel?data_layer="+data_layer+"&data_layer_mode=any&output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id+"&search="+inputs7['search_text_1']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
        result = result.json()
        result_list = result["signals"]
        signal_id_1 = ""
        signal_id_2 = ""
        fqn_id = ""
        for resp in result_list:
            if resp["name"] == inputs7['signal_name_1'] and signal_id_1 == "":
                signal_id_1 = resp["id"]
            if resp["name"] == inputs7['signal_name_2'] and signal_id_2 == "":
                signal_id_2 = resp["id"]
            if fqn_id == "":
                result_list2 = resp["propagation"]
                for resp2 in result_list2:
                    if resp2["view"]["fqn"] == inputs7["fqn"]:
                        fqn_id = resp2["view"]["id"]
                        break
        #print signal_id_1
        #print signal_id_2
        #print fqn_id

        #1d
        result = l.client.post("/vektordata/signals/list/signalstable", json={"id": [signal_id_1]})
        result = result.json()
        id_1 = ""
        id_2 = ""
        id_3 = ""
        id_14 =""
        result_list = result[signal_id_1]["propagation"]
        for resp in result_list:
            if resp["view"]["fqn"] == inputs7["fqn_1"] and id_1 == "":
                id_1 = resp["view"]["id"]
            if resp["view"]["fqn"] == inputs7["fqn_2"] and id_2 == "":
                id_2 = resp["view"]["id"]
            if resp["view"]["fqn"] == inputs7["fqn_3"] and id_3 == "":
                id_3 = resp["view"]["id"]
            if resp["view"]["fqn"] == inputs7["fqn_13"] and id_14 == "":
                id_14 = resp["view"]["id"]
        #print id_1
        #print id_2
        #print id_3
        #print id_14
        #l.client.get("/vektordata/views/list?id="+id_1+"&id="+id_2+"&id="+id_14+"&id="+id_3+"&id="+fqn_id)

        #1e
        result = l.client.post("/vektordata/signals/list/signalstable", json={"id": [signal_id_2]})
        result = result.json()
        id_4 = ""
        id_5 = ""
        id_6 = ""
        id_7 = ""
        id_8 = ""
        result_list = result[signal_id_2]["propagation"]
        for resp in result_list:
            if resp["view"]["fqn"] == inputs7["fqn_4"] and id_4 == "":
                id_4 = resp["view"]["id"]
            if resp["view"]["fqn"] == inputs7["fqn_5"] and id_5 == "":
                id_5 = resp["view"]["id"]
            if resp["view"]["fqn"] == inputs7["fqn_6"] and id_6 == "":
                id_6 = resp["view"]["id"]
            if resp["view"]["fqn"] == inputs7["fqn_7"] and id_7 == "":
                id_7 = resp["view"]["id"]
            if resp["view"]["fqn"] == inputs7["fqn_8"] and id_8 == "":
                id_8 = resp["view"]["id"]
        #print id_4
        #print id_5
        #print id_6
        #print id_7
        #print id_8
        #l.client.get("/vektordata/views/list?id="+id_4+"&id="+id_5+"&id="+id_6+"&id="+id_7+"&id="+id_8)

        #1f
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")

        #1h
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id+"&search="+inputs7['search_text_2']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
        result = l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id+"&search="+inputs7['search_text_2']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
        result = result.json()
        result_list = result["filterMenu"]["relationship"]
        relationship_id = ""
        for resp in result_list:
            if resp["name"] == inputs7["relationship_name"]:
                relationship_id = resp["id"]
                break
        #print relationship_id

        #1i
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id+"&relationship="+relationship_id+"&search="+inputs7['search_text_2']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&relationship_mode=any")
        result = l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id+"&relationship="+relationship_id+"&relationship_mode=any&search="+inputs7['search_text_2']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
        result = result.json()
        result_list = result["filterMenu"]["subject"]
        subject_id = ""
        for resp in result_list:
            if resp["name"] == inputs7["subject_name"]:
                subject_id = resp["id"]
                break
        #print subject_id

        #1j
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id+"&relationship="+relationship_id+"&subject="+subject_id+"&search="+inputs7['search_text_2']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&relationship_mode=any&subject_mode=any")
        result = l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id+"&relationship="+relationship_id+"&relationship_mode=any&search="+inputs7['search_text_2']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&subject="+subject_id+"&subject_mode=any")
        result = result.json()
        result_list = result["filterMenu"]["data_layer"]
        data_layer_2 = ""
        for resp in result_list:
            if resp["name"] == inputs7["datalayer_name_2"]:
                data_layer_2 = resp["id"]
                break
        #print data_layer_2

        #1k
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id+"&relationship="+relationship_id+"&subject="+subject_id+"&data_layer="+data_layer_2+"&search="+inputs7['search_text_2']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&relationship_mode=any&subject_mode=any&data_layer_mode=any")
        result = l.client.get("/vektordata/diagrams/kitchenlevel?data_layer="+data_layer_2+"&data_layer_mode=any&output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id+"&relationship="+relationship_id+"&relationship_mode=any&search="+inputs7['search_text_2']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&subject="+subject_id+"&subject_mode=any")
        result = result.json()
        result_list = result["signals"]
        signal_id_3 = ""
        for resp in result_list:
            if resp["name"] == inputs7['signal_name_3'] and signal_id_3 == "":
                signal_id_3 = resp["id"]
        #print signal_id_3

        #1l
        result = l.client.post("/vektordata/signals/list/signalstable", json={"id": [signal_id_3]})
        result = result.json()
        id_9 = ""
        id_10 = ""
        id_11 = ""
        id_12 = ""
        id_13 = ""
        result_list = result[signal_id_3]["propagation"]
        for resp in result_list:
            if resp["view"]["fqn"] == inputs7["fqn_9"] and id_9 == "":
                id_9 = resp["view"]["id"]
            if resp["view"]["fqn"] == inputs7["fqn_10"] and id_10 == "":
                id_10 = resp["view"]["id"]
            if resp["view"]["fqn"] == inputs7["fqn_11"] and id_11 == "":
                id_11 = resp["view"]["id"]
            if resp["view"]["fqn"] == inputs7["fqn_12"] and id_12 == "":
                id_12 = resp["view"]["id"]
        if result[signal_id_3]["signalSetName"] == inputs7["signal_set_name"]:
            id_13 = result[signal_id_3]["signalSetId"]
        #print id_9
        #print id_10
        #print id_11
        #print id_12
        #print id_13
        #l.client.get("/vektordata/views/list?id="+id_9+"&id="+id_10+"&id="+id_11+"&id="+id_12+"&id="+id_13)

        #2a
        #l.client.get("/vektordata/schemas/definitions/list?id="+id_6+"&id="+fqn_id+"&id="+id_13)
        #l.client.get("/vektordata/views/list?id="+id_6+"&id="+fqn_id+"&id="+id_13)
        l.client.get("/vektordata/signals/signalstable?signalId="+signal_id_2+"&signalId="+signal_id_1+"&signalId="+signal_id_3)
        #l.client.get("/vektordata/schemas/definitions/list?id="+id_6+"&id="+fqn_id+"&id="+id_13)
        #l.client.get("/vektordata/views/list?id="+id_6+"&id="+fqn_id+"&id="+id_13)
        l.client.get("/vektordata/signals/signalstable?signalId="+signal_id_2+"&signalId="+signal_id_1+"&signalId="+signal_id_3)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)

        #2b
        l.client.get("/vektordata/solutions/"+CONFIG['solution']+"/views/"+inputs7['signal_name']+"/labels")
        l.client.get("/vektordata/solutions/"+CONFIG['solution']+"/views/"+inputs7['signal_name']+"/variants")

        #2c
        l.client.get("/vektordata/solutions/"+CONFIG['solution']+"/reports")
        l.client.get("/vektordata/solutions/"+CONFIG['solution']+"/reports/"+inputs7['reportName']+"/executions")
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
        l.client.get("/vektordata/solutions/"+CONFIG['solution']+"/views/"+inputs7['signal_name']+"/labels")
        l.client.get("/vektordata/solutions/"+CONFIG['solution']+"/views/"+inputs7['signal_name']+"/variants")
        l.client.get("/vektordata/schemas?definitionId="+id_13)

        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)

        print "TASK-7"
        print "\n******************************************************************"
