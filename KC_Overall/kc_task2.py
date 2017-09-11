from locust import TaskSet, task
from kc_CONFIG import *

class Task2(TaskSet):
    @task
    def kc_page2(l):
        result = l.client.get("/vektordata/solutions")
        result = result.json()
        project_id=""
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
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id)
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

        #1b
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id)
        result = l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
        result = result.json()
        data_layer = ""
        resp_list = result["filterMenu"]["data_layer"]
        for resp in resp_list:
            if resp["name"] == inputs2['datalayer_name']:
                data_layer = resp["id"]
                break
        #print data_layer
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id+"&data_layer="+data_layer+"&data_layer_mode=any")
        l.client.get("/vektordata/diagrams/kitchenlevel?data_layer="+data_layer+"&data_layer_mode=any&output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id)

        #1c
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_id+"&data_layer="+data_layer+"&search="+inputs2['search_text']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&data_layer_mode=any")
        result = l.client.get("/vektordata/diagrams/kitchenlevel?data_layer="+data_layer+"&data_layer_mode=any&output=table&outputLimitSize=25&outputOffset=0&projectId="+project_id+"&search="+inputs2['search_text']+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
        result = result.json()
        resp_list = result["signals"]
        definition_id_2 = ""
        column_id = ""
        for resp in resp_list:
            if resp["signalSetName"] == inputs2['definition_id2_name']:
                definition_id_2 = resp["signalSetId"]
            if resp["name"] == inputs2['signal_name']:
                column_id = resp["id"]
                break
        #print definition_id_2
        #print column_id

        #1d
        l.client.get("/vektordata/views/"+definition_id_2+"?projectId="+project_id)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)
        l.client.get("/vektordata/schemas?definitionId="+definition_id_2+"&formulaType=definition")
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_2)
        l.client.get("/vektordata/signalsets/"+definition_id_2+"/signalstable?outputLimitSize=25&outputOffset=0")
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_2)
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&columnId="+column_id)
        l.client.get("/vektordata/diagrams/columnlevel?projectId="+project_id+"&columnId="+column_id)

        #1g
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_2)
        l.client.get("/vektordata/columns/"+column_id+"/formula")
        l.client.get("/vektordata/columns/"+column_id+"/formula?type=predecessor")
        l.client.get("/vektordata/columns/"+column_id+"/formula?type=consumer")

        #1h
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&definitionId="+definition_id_2)
        l.client.get("/vektordata/columns/"+column_id+"/formula")
        l.client.get("/vektordata/columns/"+column_id+"/formula?type=predecessor")
        l.client.get("/vektordata/columns/"+column_id+"/formula?type=consumer")

        #1j
        l.client.get("/vektordata/workflows?definitionId="+definition_id_2+"&projectId="+project_id)
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&columnId="+column_id)
        l.client.get("/vektordata/diagrams/columnlevel?projectId="+project_id+"&columnId="+column_id)
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_id+"&columnId="+column_id)
        l.client.get("/vektordata/diagrams/columnlevel?projectId="+project_id+"&columnId="+column_id)

        #1k
        l.client.get("/vektordata/schemas?definitionId="+definition_id_2+"&formulaType=definition")

        #1l
        l.client.get("/vektordata/views/"+definition_id_2+"/source?projectId="+project_id+"&moduleName=undefined")

        #1m
        l.client.get("/vektordata/views/"+definition_id_2+"/source?projectId="+project_id+"&moduleName=undefined")

        #1n
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_id)

        print "TASK-2
        print "\n******************************************************************"
