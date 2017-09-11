from locust import TaskSet, task
from kc_CONFIG import *

class Task8(TaskSet):
    @task
    def kc_page8(l):
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
        result=l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        result=result.json()
        result_list=result["filterMenu"]["data_layer"]
        for resp in result_list:
            if resp["name"] == inputs8["datalayer_name"]:
                data_layer = resp["id"]
        #print data_layer
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        l.client.get("/vektordata/signalsets?projectId="+project_Id)
        l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports")
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id)
        result = l.client.get("/vektordata/workflows?projectId="+project_Id)
        result = result.json()
        definition_Id = ""
        for resp in result:
            if resp["name"] == CONFIG['definition']:
                definition_Id = resp["id"]
                break
        #print definition_Id
        l.client.get("/vektordata/diagrams/definitionlevel?projectId="+project_Id+"&definitionId="+definition_Id)

        #1a
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&data_layer=341126&data_layer_mode=any")
        l.client.get("/vektordata/diagrams/kitchenlevel?data_layer="+data_layer+"&data_layer_mode=any&output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id)

        #1c
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&data_layer="+data_layer+"&search=segm&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&data_layer_mode=any")
        result=l.client.get("/vektordata/diagrams/kitchenlevel?data_layer="+data_layer+"&data_layer_mode=any&output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&search=segm&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
        result=result.json()
        result_list=result["signals"]
        id1=id2=id3=id4=id5=id6=id7=id8=id9=id10=""
        id11=id12=id13=id14=id15=""
        for key in result_list:
            if key["signalSourceFQN"] == inputs8["signal_name1"]:
                signalId1=key["id"]
            if key["signalSourceFQN"] == inputs8["signal_name2"]:
                signalId2=key["id"]
            if key["signalSourceFQN"] == inputs8["signal_name5"]:
                signalId5=key["id"]
        #print signalId1
        #print signalId2
        #print signalId5
        for resp in result_list:
            if resp["description"] == inputs8["description_name"]:
                resp_key1=resp["propagation"]
            if resp["fqn"] == inputs8["fqn_value1"]:
                resp_key2=resp["propagation"]
            if resp["fqn"] == inputs8["fqn_value2"]:
                resp_key3=resp["propagation"]
        for list in resp_key1:
            if list["view"]["fqn"] == inputs8["id1_name"]:
                id1=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id2_name"]:
                id2=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id3_name"]:
                id3=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id4_name"]:
                id4=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id5_name"]:
                id5=list["view"]["id"]
        #print id1
        #print id2
        #print id3
        #print id4
        #print id5
        for list in resp_key2:
            if list["view"]["fqn"] == inputs8["id6_name"]:
                id6=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id7_name"]:
                id7=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id8_name"]:
                id8=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id9_name"]:
                id9=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id10_name"]:
                id10=list["view"]["id"]
        #print id6
        #print id7
        #print id8
        #print id9
        #print id10
        for list in resp_key3:
            if list["view"]["fqn"] == inputs8["id11_name"]:
                id11=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id12_name"]:
                id12=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id13_name"]:
                id13=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id14_name"]:
                id14=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id15_name"]:
                id15=list["view"]["id"]
        #print id11
        #print id12
        #print id13
        #print id14
        #print id15
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&data_layer="+data_layer+"&search="+inputs8["search1"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&data_layer_mode=any")
        l.client.get("/vektordata/diagrams/kitchenlevel?data_layer="+data_layer+"&data_layer_mode=any&output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&search="+inputs8["search1"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")

        #1d
        l.client.post("/vektordata/signals/list/signalstable", json={"id": [signalId5]})
        #l.client.get("/vektordata/views/list?id="+id1+"&id="+id2+"&id="+id3+"&id="+id4+"&id="+id5)

        #1e
        l.client.post("/vektordata/signals/list/signalstable", json={"id": [signalId1]})
        #l.client.get("/vektordata/views/list?id="+id6+"&id="+id7+"&id="+id8+"&id="+id9+"&id="+id10)
        l.client.post("/vektordata/signals/list/signalstable", json={"id": [signalId2]})
        #l.client.get("/vektordata/views/list?id="+id11+"&id="+id12+"&id="+id13+"&id="+id14+"&id="+id15)

        #1f
        result=l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
        subject_id=""
        result=result.json()
        result_list=result["filterMenu"]["relationship"]
        for dict in result_list:
            if dict["displayName"] == inputs8["displayName1"]:
                relationship_id=dict["id"]

        result_list=result["filterMenu"]["subject"]
        for dict in result_list:
            if dict["displayName"] == inputs8["displayName2"]:
                subject_id=dict["id"]

        result_list=result["filterMenu"]["data_layer"]
        for dict in result_list:
            if dict["displayName"] == inputs8["displayName3"]:
                datalayer_id=dict["id"]
        #print relationship_id
        #print subject_id
        #print datalayer_id

        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
        #1g
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&search="+inputs8["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&search="+inputs8["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")

        #1h
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&relationship="+relationship_id+"&search="+inputs8["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&relationship_mode=any")
        result=l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&relationship="+relationship_id+"&relationship_mode=any&search="+inputs8["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
        result=result.json()
        result_list=result["signals"]
        id16=id17=id18=id19=id20=""
        for key in result_list:
            if key["signalSourceFQN"] == inputs8["signal_name3"]:
                signalId3=key["id"]
        #print signalId3
        for resp in result_list:
            if resp["fqn"] == inputs8["fqn_value3"]:
                resp_key=resp["propagation"]
                id20=resp["signalSetId"]
            if resp["fqn"] == inputs8["fqn_value4"]:
                resp_key1=resp["propagation"]
                id22=resp["signalSetId"]
        for list in resp_key:
            if list["view"]["fqn"] == inputs8["id16_name"]:
                id16=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id17_name"]:
                id17=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id18_name"]:
                id18=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id19_name"]:
                id19=list["view"]["id"]
        #print id16
        #print id17
        #print id18
        #print id19
        #print id20
        for list in resp_key1:
            if list["view"]["fqn"] == inputs8["id21_name"]:
                id21=list["view"]["id"]
            if list["view"]["fqn"] == inputs8["id23_name"]:
                id23=list["view"]["id"]
        #print id21
        #print id22
        #print id23

        #1i
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&relationship="+relationship_id+"&subject="+subject_id+"&search="+inputs8["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&relationship_mode=any&subject_mode=any")
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&relationship="+relationship_id+"&relationship_mode=any&search="+inputs8["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&subject="+subject_id+"&subject_mode=any")

        #1j
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&relationship="+relationship_id+"&subject="+subject_id+"&data_layer="+datalayer_id+"&search="+inputs8["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&relationship_mode=any&subject_mode=any&data_layer_mode=any")
        l.client.get("/vektordata/diagrams/kitchenlevel?data_layer="+datalayer_id+"&data_layer_mode=any&output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&relationship="+relationship_id+"&relationship_mode=any&search="+inputs8["search2"]+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&subject="+subject_id+"&subject_mode=any")

        #1k
        l.client.post("/vektordata/signals/list/signalstable", json={"id": [signalId3]})
        #l.client.get("/vektordata/views/list?id="+id16+"&id="+id17+"&id="+id18+"&id="+id19+"&id="+id20)

        #1l
        result=l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")
        result=result.json()
        result_list=result["filterMenu"]["window"]
        for key in result_list:
            if key["displayName"] == inputs8["displayName4"]:
                window_id=key["id"]
        #print window_id
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName")

        #1m
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&window="+window_id+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&window_mode=any")
        result=l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&window="+window_id+"&window_mode=any")
        result=result.json()
        result_list=result["signals"]
        for key in result_list:
            if key["signalSourceFQN"] == inputs8["signal_name4"]:
                signalId4=key["id"]
        #print signalId4

        #1n
        l.client.get("/vektordata/diagrams/kitchenlevel?projectId="+project_Id+"&window="+window_id+"&subject="+subject_id+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&window_mode=any&subject_mode=any")
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=25&outputOffset=0&projectId="+project_Id+"&searchColumn=name&searchColumn=description&searchColumn=function&searchColumn=tags&searchColumn=displayName&subject="+subject_id+"&subject_mode=any&window="+window_id+"&window_mode=any")

        #1o
        l.client.post("/vektordata/signals/list/signalstable", json={"id": [signalId4]})
        #l.client.get("/vektordata/views/list?id="+id21+"&id="+id22+"&id="+id23)

        #2a
        l.client.get("/vektordata/schemas/definitions/list?id="+id8+"&id="+id12+"&id="+id19+"&id="+id5)
        #l.client.get("/vektordata/views/list?id="+id8+"&id="+id12+"&id="+id19+"&id="+id5)
        l.client.get("/vektordata/signals/signalstable?signalId="+signalId1+"&signalId="+signalId2+"&signalId="+signalId3+"&signalId="+signalId4+"&signalId="+signalId5)
        l.client.get("/vektordata/schemas/definitions/list?id="+id8+"&id="+id12+"&id="+id19+"&id="+id5)
        #l.client.get("/vektordata/views/list?id="+id8+"&id="+id12+"&id="+id19+"&id="+id5)
        l.client.get("/vektordata/signals/signalstable?signalId="+signalId1+"&signalId="+signalId2+"&signalId="+signalId3+"&signalId="+signalId4+"&signalId="+signalId5)
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)

        #2b
        l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs8["id19_name"]+"/labels")
        l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs8["id19_name"]+"/variants")

        #2c
        l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports")
        l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/reports/"+inputs8["reportName"]+"/executions")
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)
        l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs8["id19_name"]+"/labels")
        l.client.get("/vektordata/solutions/"+CONFIG["solution"]+"/views/"+inputs8["id19_name"]+"/variants")
        l.client.get("/vektordata/views?projectId="+project_Id)
        l.client.get("/vektordata/collections?projectId="+project_Id)
        l.client.get("/vektordata/models?projectId="+project_Id)
        l.client.get("/vektordata/views?projectId="+project_Id+"&type=scoring")
        l.client.get("/vektordata/referencedata?projectId="+project_Id)

        #3c
        l.client.get("/vektordata/diagrams/kitchenlevel?output=table&outputLimitSize=1&projectId="+project_Id)

        print "TASK-8"
        print "********************************************************************"
