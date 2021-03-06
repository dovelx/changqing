#作业任务删除
from globalpkg.global_var import work_appoint_id
from tools import tool
from globalpkg.global_var import tsi
from globalpkg.global_var import workticketid
from globalpkg.global_var import worktaskid
from globalpkg.global_var import jsaid
from globalpkg.global_var import safeclarid
from globalpkg.global_var import sql_query_work_appointid

case = '作业任务删除'
#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now
#mendtime = tool.mendtime
#作业预约名称
name = tool.ran_name_with_str()
print(name)
#用例信息变量定义
testsuit9 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''
#work_appoint_id_plus1=  work_appoint_id+1
work_appoint_id_plus1 = sql_query_work_appointid+1
#作业预约创建使用ID
yuyueid = work_appoint_id_plus1
count =0
#用例信息
caseinfo['id'] = 1
caseinfo['name'] = '作业预约'
caseinfo['isactive'] = 1
#拼写预约URL
url2='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_APPOINT&0.5564922508434509&contentType=json&ajax=true&tid=1'
caseinfo['url'] = url2
#作业许可大票数据
data = {
	"tableName": "hse_work_appoint",
	"iscontractor": "0",
	"workunitname_no": "",
	"territorialunitid": 2000000003339,
	"worktaskid_no": 0,
	"isreport": "0",
	"territorialunitname": "运行一部",
	"territorialunitcode": "CS8082020",
	"wf_audit_state": "6",
	"status": "draft",
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"isspecialcondition": "0",
	"specialenvironment": "ALLNOT",
	"task_worktype_code": "GCN",
	"task_worktype_name": "储罐浮舱内",
	"cywlqfyxzz": "0",
	"isdzdh": "0",
	"projecttype": "rcjx",
	"isupgradedh": "0",
	"persistent_type": "newoperation",
	"issjtssxzy": "0",
	"worklevel_dh": "",
	"worklevel_sx": "",
	"worklevel_gc": "",
	"worklevel_dz": "",
	"worklevel_gx": "",
	"sourcetype": "",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",
	"work_position_id": 2000000002019,
	"work_position_name": "制氢北区",
	"worksite": "作业地点",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workname": name,
	"workcontent": "作业内容",
	"worktypename": "作业许可证",
	"worktype": "xkz",
	"appointstarttime": starttime,
	"appointendtime": endtime,
	"material_medium": "物料介质",
	"risksmeasures": "重点防控的风险"
}
caseinfo['data'] =data
testsuit9.append(caseinfo.copy())

#送交用例信息

caseinfo['id'] = 2
caseinfo['name'] = '作业预约送交'
#送交接口地址
url3='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.30092471197648707&contentType=json&ajax=true&tid=1'%(yuyueid,yuyueid)
caseinfo['url'] = url3
formdata2={
	"opinion": "申请审批",
	"nodeStr": "2000000009070",
	"2000000009070": "测试用户",
	"2000000009070_id": 1000
}
caseinfo['data'] =formdata2
print(caseinfo['id'] )
testsuit9.append(caseinfo.copy())

#作业预约审批用例信息
caseinfo['id'] = 3
caseinfo['name'] = '作业预约审批'
#审批接口地址
url4='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfFinish?parentEntityId=&parentFuncCode=&topEntityId=+&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.027850408425730055&contentType=json&ajax=true&tid=1'%(yuyueid)
caseinfo['url'] = url4
#参数
formdata ={
	"opinion": "同意",
	"cC": "1000",
	"cCName": "测试用户",
	"nickName": "用户",
	"is_normal_finish": "true",
	"nodeStr": ""
}
caseinfo['data'] =formdata
testsuit9.append(caseinfo.copy())

#安全分析第一个保存用例信息
#caseid = 5
casename = '安全分析及交底保存'
count =count+1
caseid = count
caseinfo['id'] = 4
caseinfo['name'] = casename

urlfenxi ='http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_SAFETY_TASK_RISK&0.6529845051499572&contentType=json&ajax=true&tid=1'
formdatafenxi ={
	"tableName": "hse_safety_task",
	"wf_create_user": 1000,
	"iscontractor": "0",
	"analyze_type": "jsa,aqjd",
	"work_appoint_name": name,
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"workstatus": "draft",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"projecttype": "rcjx",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",

	"work_appoint_id": yuyueid,
	"workcontent": "作业内容123",
	"workname": name,
	"worktickettype": "xkz,dh",
	"worktickettype_name": "作业许可证,动火作业",
	"workunitname": "长庆石化分公司",
	"workunit": 1688712,
	"planstarttime":starttime,
	"planendtime": endtime,
	"site": "作业地点123",
	"equipmentname": "",
	"work_position_name": "制氢北区",
	"work_position_id": 2000000002019,
	"equipmentnumber": "",
	"equipmentcode": "",
	"constructionscheme": "",
	"standardmaintenance": ""
}
caseinfo['url'] = urlfenxi
caseinfo['data'] =formdatafenxi
testsuit9.append(caseinfo.copy())

#获取安全分析接口用例信息
#预约安全分析接口地址
url11 = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/getMetaData?0.26386458099914045&contentType=json&ajax=true&tid=1'


#jsaidxx = work_appoint_id-33
jsaidxx = jsaid+1
print ("安全分析列表使用ID:",jsaidxx)


#安全分析步骤添加接口用例信息
#caseid = 7
casename = '安全分析步骤添加'
count =count+1
caseid = count
caseinfo['id'] = 5
caseinfo['name'] = casename
#url ='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_STEP_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_ANALYSIS_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&0.5426692795870303&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx)
url ='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_STEP_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_ANALYSIS_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&0.8939960513657317&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx)
data = {
	"tableName": "hse_safety_analysis_step",
	"qualify_level": "no_qualify",
	"duty_name": "",
	"jsaid": jsaidxx,
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"step_type": "02",
	"evaluate_type": "",
	"risk_level": "02",
	"remain_risk_accept": "",
	"risk_value": 0,
	"risk_harm": "风险及危害123",
	"gravity": "1",
	"consequence": "后果123",
	"accident_possibility": "2",
	"step_name": "步骤活动123"
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit9.append(caseinfo.copy())

#安全分析步保存加接口用例信息

casename = '安全分析保存'
count =count+1
caseid = count
caseinfo['id'] = 6
caseinfo['name'] = casename

url='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.09494809285755568&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx,jsaidxx)
data = {
	"tableName": "hse_safety_analysis",

	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"jsaid": jsaidxx,
	"jsa_templete_name": "",
	"jsa_templete_id": "",
	"temp_type": "newWorkTask",
	"jsa_monitor_userid": 1000,
	"jsa_monitor_name": "测试用户",
	"jsa_menber_userids": "1000",
	"jsa_menber_username": "测试用户",
	"analyze_time": now,
	"worktickettype": "",
	"equip_stuff": "",
	"worktaskid": jsaidxx,
	"workstatus": "",
	"worktype": "jsa",
	"revampandadvide": "",
	"inspection_name": "",
	"work_position_id": 2000000002019,
	"projecttype": "",
	"workname": "",
	"workunitname": "",
	"reference": "",
	"iscontractor": "",
	"territorialunitid": "",
	"territorialunitname": "",
	"planendtime": "",
	"reviewer": "",
	"site": "",
	"worknumber": "",
	"workunit": "",
	"craftprocess": "",
	"planstarttime": "",
	"workcontent": "",
	"isnew": "",
	"wf_instance": "",
	"wf_current_user": "",
	"wf_audit_time": "",
	"wf_current_nodeid": "",
	"wf_type": "",
	"wf_create_user": "",
	"wf_audit_state": "",
	"sourcejsaid": "",
	"remainsrisk_level": "",
	"risk_level": "04"
}

caseinfo['url'] = url
caseinfo['data'] =data
testsuit9.append(caseinfo.copy())
#安全分析修改


casename = '安全分析修改'

caseinfo['id'] = 7
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.2463658272702205&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx)
data = {
	"tableName": "hse_safety_task",
	"standardmaintenance_name": "",
	"territorialdeviceid": 2000000003454,
	"constructionscheme": 0,
	"work_appoint_name": name,
	"teampost": "",
	"contractor_analyst_id": "",
	"territorialdevicename": "制氢装置",
	"work_position_name": "制氢北区",
	"contractor_analyst": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"projecttype": "rcjx",
	"worktaskid": 2000000001880,
	"recordnumber": "",
	"worknumber": "gzfx20200608022",
	"workname": name,
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"workcontent": "作业内容123",
	"site": "作业地点1234444",
	"analyze_type": "jsa,aqjd",
	"workstatus": "draft",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"iscontractor": "0",
	"submitdate": "",
	"planstarttime": starttime,
	"planendtime": endtime,
	"wf_current_user": "",
	"wf_audit_state": "0",
	"wf_create_user": 1000,
	"wf_instance": "",
	"wf_current_nodeid": "",
	"wf_audit_time": "",
	"wf_type": "",
	"created_by_name": "测试用户",
	"work_position_id": 2000000002019,
	"work_appoint_id": 2000000001792,
	"invalidreason": ""
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit9.append(caseinfo.copy())

#安全交底
#安全交底接口用例信息

casename = '安全交底'
count =count+1
caseid = count
caseinfo['id'] = 8
caseinfo['name'] = casename
#worktaskidxx = jsaidxx+17
anquansongjiaoid = safeclarid+1
safeclaridxx = safeclarid+1
print ("送交ID:",safeclaridxx)
url='http://192.168.6.27:6030/hse/HSE_SAFETY_DISCLOSURE/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.7447101068947941&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx,safeclaridxx)


data = {
	"tableName": "hse_safety_disclosure",
	"additional_content": "",
	"confirm_content": "1、已清楚作业区域及周边生产作业情况\r\n2、已清楚本次作业的安全风险（JSA）\r\n3、已清楚本次作业的具体安全要求（作业许可证中的控制措施）\r\n4、已对本次作业现场安全措施进行了检查确认\r\n5、已清楚本次作业涉及的作业许可证的有限期限 \r\n6、已掌握个人防护用具正确佩戴使用方法\r\n7、已清楚突发情况下的应急避险方法",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"safeclarid": safeclaridxx,
	"projecttype": "",
	"safe_name": "长庆石化安全交底",
	"worktype": "aqjd",
	"workstatus": "draft",
	"scopeandenv": "",
	"workrisk": "",
	"preventmeasure": "",
	"emermeasure": "",
	"othermatter": "",
	"safe_content": "长庆石化安全交底",
	"safe_clar_temp_id": 2000000001040,
	"safe_clar_temp_name": "",
	"worktaskid": jsaid,
	"work_position_id": 2000000002019
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit9.append(caseinfo.copy())


#安全送交接口用例信息

casename = '安全送交'
count =count+1
caseid = count
caseinfo['id'] = 9
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.9498759321537273&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx)
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit9.append(caseinfo.copy())

#安全分析撤回

caseinfo['id'] = 10
caseinfo['name'] = '安全分析撤回'
url = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/withdraw?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.8385515971602189&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx)
data = {
	"tableName": "hse_safety_task",
	"standardmaintenance_name": "",
	"territorialdeviceid": 2000000003454,
	"constructionscheme": 0,
	"work_appoint_name": name,
	"teampost": "",
	"contractor_analyst_id": "",
	"territorialdevicename": "制氢装置",
	"work_position_name": "制氢北区",
	"contractor_analyst": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"projecttype": "rcjx",
	"worktaskid": jsaidxx,
	"recordnumber": "",
	"worknumber": "gzfx20200608021",
	"workname": name,
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"workcontent": "作业内容123",
	"site": "作业地点123",
	"analyze_type": "jsa,aqjd",
	"workstatus": "analyzeFinish",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"iscontractor": "0",
	"submitdate": now,
	"planstarttime": starttime,
	"planendtime": endtime,
	"wf_current_user": "",
	"wf_audit_state": "2",
	"wf_create_user": 1000,
	"wf_instance": "",
	"wf_current_nodeid": "",
	"wf_audit_time": now,
	"wf_type": "",
	"created_by_name": "测试用户",
	"work_position_id": 2000000002019,
	"work_appoint_id": 2000000001786,
	"invalidreason": ""
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit9.append(caseinfo.copy())

#安全分析撤回再送交

casename = '安全分析撤回再送交'

caseinfo['id'] = 11
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.9498759321537273&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx)
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit9.append(caseinfo.copy())
#作业任务添加接口用例信息

casename = '作业任务添加'
count =count+1
caseid = count
caseinfo['id'] = 12
caseinfo['name'] = casename

url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TASK_MCQ&0.9079012038155838&contentType=json&ajax=true&tid=1'
jsaidxxx = jsaid+1

data = {
	"tableName": "hse_work_task",
	"iscontractor": "0",
	"isupgrade": "0",
	"work_appoint_name": "",
	"territorialunitid": 2000000003339,
	"applyunitname": "长庆石化分公司",
	"task_pause": "0",
	"territorialunitname": "运行一部",
	"territorialunitcode": "CS8082020",
	"applyunitid": "1688712",
	"workstatus": "draft",
	"autorisklevel": 1,
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"projecttype": "",
	"isrecord": "",
	"eq_position": "",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",
	"jsaid": jsaidxxx,
	"work_appoint_id": "",
	"jsa_code": name,
	"site": "作业地点123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"work_position_id": 2000000002019,
	"work_position_name": "制氢北区",
	"workcontent": "作业内容123",
	"planstarttime": starttime,
	"planendtime": endtime,
	"standardmaintenance_name": "",
	"constructionscheme": 0,
	"worktickettype": "xkz",
	"worktickettype_name": "作业许可证",
	"standardmaintenance": "",
	"equipmentname": "",
	"equipmentnumber": "",
	"equipmentcode": "",
	"workname": name
}
data = {
	"tableName": "hse_work_task",
	"iscontractor": "0",
	"isupgrade": "0",
	"work_appoint_name": name,
	"territorialunitid": "2000000003339",
	"applyunitname": "运行一部",
	"task_pause": "0",
	"territorialunitname": "运行一部",
	"territorialunitcode": "CS8082020",
	"applyunitid": "2000000003339",
	"workstatus": "draft",
	"autorisklevel": 1,
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"projecttype": "rcjx",
	"isrecord": "",
	"eq_position": "",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",
	"jsaid": jsaidxxx,
	"work_appoint_id": 2000000001921,
	"jsa_code": name,
	"site": "作业地点123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"work_position_id": 2000000002019,
	"work_position_name": "制氢北区",
	"workcontent": "作业内容123",
	"planstarttime": starttime,
	"planendtime": endtime,
	"standardmaintenance_name": "",
	"constructionscheme": 0,
	"worktickettype": "xkz",
	"worktickettype_name": "作业许可证",
	"standardmaintenance": "",
	"equipmentname": "",
	"equipmentnumber": "",
	"equipmentcode": "",
	"workname": name,
	#"safety_task_img": "[{\"dfs_file_name\":\"map.jpg\",\"isicon\":false,\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000003551,\"dataStatus\":0,\"ver\":1,\"created_by\":"",\"created_dt\":\"2020-06-17 16:50:28\",\"updated_by\":"",\"updated_dt\":\"2020-06-17 16:50:28\",\"df\":0,\"tenantid\":1,\"ts\":"",\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/01/17/wKgGGl7p2VSAJxy9AAIemjI3PH8782.jpg\",\"dfs_file_size\":138906,\"dfs_preview_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p2VSAJxy9AAIemjI3PH8782.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p2VSAWc-oAAHKnlsRKiE156.png\"}]"
	#"safety_task_img": "[ {\n  \"dfs_file_name\" : \"map.jpg\",\n  \"dfs_file_group_name\" : "",\n  \"dfs_file_key\" : \"M00/01/17/wKgGGl7p3M2AeAP5AAIemjI3PH8065.jpg\",\n  \"dfs_file_size\" : 138906,\n  \"dfs_preview_url\" : \"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p3M2AeAP5AAIemjI3PH8065.jpg\",\n  \"dfs_thumbnail_url\" : \"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p3M2ADS2BAAHKnlsRKiE726.png\"\n} ]"
    "safety_task_img": "[{\"dfs_file_name\":\"微信图片_20200617160345.jpg\",\"isicon\":false,\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000003652,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-06-17 17:22:42\",\"updated_by\":null,\"updated_dt\":\"2020-06-17 17:22:42\",\"df\":0,\"tenantid\":1,\"ts\":null,\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/01/17/wKgGGl7p4OKAaPXcAAExXFSqfEE896.jpg\",\"dfs_file_size\":78172,\"dfs_preview_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p4OKAaPXcAAExXFSqfEE896.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p4OWAFqCrAAIKVnDfoY0466.png\"}]"
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit9.append(caseinfo.copy())

worktaskidxx = worktaskid+1
print("作业任务列表ID-worktaskid:",worktaskidxx)

#作业任务删除
casename = '作业任务删除'
count =count+1
caseid = count
caseinfo['id'] = 13
caseinfo['name'] = casename
#url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/hse_work_task_submit?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&0.412998005925274&contentType=json&ajax=true&tid=1'%(worktaskidxx,worktaskidxx)
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/listDeleteBatch?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&0.15056918041866485&contentType=json&ajax=true&tid=1'%(worktaskidxx,worktaskidxx-1)
data = [worktaskidxx]
caseinfo['url'] = url
caseinfo['data'] =data
testsuit9.append(caseinfo.copy())