# -*- coding:utf-8 -*-

from flask import Flask, render_template
import pandas as pd
import pandas as pd_15
import pymssql
import re
import os
import cx_Oracle
import matplotlib.pyplot as plt 
import matplotlib.pyplot as plt2
# from app import app
import pandas as pd 
import numpy as np
import numpy as np_15

import random
from io import BytesIO
# from StringIO import StringIO  # python 2.7x
import matplotlib.pyplot as plt
from flask import make_response, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import base64
# Visible rows limit
rows_limit = 5000
from tkinter import messagebox

# MS SQL server configuration
server = 'JIOGENSQLDB01'
base = 'ListDB'
user = 'Genesys_Report'
password = 'Genesys@1234'


app = Flask(__name__)

@app.route("/BlasterLast5Min")
def BlasterLast5Min():
	conn = pymssql.connect(server, user, password, base)
	df = pd.read_sql("Select (case when b.name = 'SIPSwitch01' then 'AHM' when b.name = 'SIPSwitch02' then 'BLR' when b.name = 'SIPSwitch03' then 'MOH' when b.name = 'SIPSwitch04' then 'HYD' when b.name = 'SIPSwitch05' then 'KOL' when b.name = 'SIPSwitch06' then 'MUM' when b.name = 'SIPSwitch07' then 'NOI' else b.name end) Circle ,count(1)[Total], sum(case when call_result=13 then 1 else 0 end )[Dial_Error], sum(case when Call_Result=35 then 1 else 0 end )[No_DialTone], sum(case when call_result=37 then 1 else 0 end )[No_Ring Back Tone], sum(case when call_result=7 then 1 else 0 end )[No Answer],sum(case when call_result=6 then 1 else 0 end )[Busy], sum(case when call_result=33 then 1 else 0 end )[Answered], sum(case when call_result=14 then 1 else 0 end )[SIT Unknown], sum(case when  call_result=3 then 1 else 0 end )[General Error], sum(case when call_result=4 then 1 else 0 end )[System Error], sum(case when call_result=11 then 1 else 0 end )[Invalid Number] from  TRG_JIO_CALLHISTORY(nolock) a inner join ConfigDB..cfg_switch(Nolock) b on a.switch_id = b.dbid where  Call_date >= DATEADD(MINUTE, -5, CONVERT(DATETIME, CONVERT(VARCHAR(16), GETDATE(), 120) + ':00:00'))  group by  (case when b.name = 'SIPSwitch01' then 'AHM' when b.name = 'SIPSwitch02' then 'BLR' when b.name = 'SIPSwitch03' then 'MOH' when b.name = 'SIPSwitch04' then 'HYD' when b.name = 'SIPSwitch05' then 'KOL' when b.name = 'SIPSwitch06' then 'MUM' when b.name = 'SIPSwitch07' then 'NOI' else b.name end)  order by 1;", con = conn)
	conn.close()
    # Prepare html code for the table
	html = df.head(rows_limit).to_html(classes = 'example', border = 1, index = False)
	html = re.sub(' example', '" id = "example', html)
	return render_template('5Min.html', table = html)
	
@app.route("/BlasterLast15Min")
def BlasterLast15Min():
	conn = pymssql.connect(server, user, password, base)
	df = pd.read_sql("Select (case when b.name = 'SIPSwitch01' then 'AHM' when b.name = 'SIPSwitch02' then 'BLR' when b.name = 'SIPSwitch03' then 'MOH' when b.name = 'SIPSwitch04' then 'HYD' when b.name = 'SIPSwitch05' then 'KOL' when b.name = 'SIPSwitch06' then 'MUM' when b.name = 'SIPSwitch07' then 'NOI' else b.name end) Circle ,count(1)[Total], sum(case when call_result=13 then 1 else 0 end )[Dial_Error], sum(case when Call_Result=35 then 1 else 0 end )[No_DialTone], sum(case when call_result=37 then 1 else 0 end )[No_Ring Back Tone], sum(case when call_result=7 then 1 else 0 end )[No Answer],sum(case when call_result=6 then 1 else 0 end )[Busy], sum(case when call_result=33 then 1 else 0 end )[Answered], sum(case when call_result=14 then 1 else 0 end )[SIT Unknown], sum(case when  call_result=3 then 1 else 0 end )[General Error], sum(case when call_result=4 then 1 else 0 end )[System Error], sum(case when call_result=11 then 1 else 0 end )[Invalid Number] from  TRG_JIO_CALLHISTORY(nolock) a inner join ConfigDB..cfg_switch(Nolock) b on a.switch_id = b.dbid where  Call_date >= DATEADD(MINUTE, -15, CONVERT(DATETIME, CONVERT(VARCHAR(16), GETDATE(), 120) + ':00:00'))  group by  (case when b.name = 'SIPSwitch01' then 'AHM' when b.name = 'SIPSwitch02' then 'BLR' when b.name = 'SIPSwitch03' then 'MOH' when b.name = 'SIPSwitch04' then 'HYD' when b.name = 'SIPSwitch05' then 'KOL' when b.name = 'SIPSwitch06' then 'MUM' when b.name = 'SIPSwitch07' then 'NOI' else b.name end)  order by 1;", con = conn)
	conn.close()
    # Prepare html code for the table
	html = df.head(rows_limit).to_html(classes = 'example', border = 1, index = False)
	html = re.sub(' example', '" id = "example', html)
	return render_template('15Min.html', table = html)

@app.route("/BlasterLastHrs")
def BlasterLastHrs():
	conn = pymssql.connect(server, user, password, base)
	df = pd.read_sql("Select (case when b.name = 'SIPSwitch01' then 'AHM' when b.name = 'SIPSwitch02' then 'BLR' when b.name = 'SIPSwitch03' then 'MOH' when b.name = 'SIPSwitch04' then 'HYD' when b.name = 'SIPSwitch05' then 'KOL' when b.name = 'SIPSwitch06' then 'MUM' when b.name = 'SIPSwitch07' then 'NOI' else b.name end) Circle ,count(1)[Total], sum(case when call_result=13 then 1 else 0 end )[Dial_Error], sum(case when Call_Result=35 then 1 else 0 end )[No_DialTone], sum(case when call_result=37 then 1 else 0 end )[No_Ring Back Tone], sum(case when call_result=7 then 1 else 0 end )[No Answer],sum(case when call_result=6 then 1 else 0 end )[Busy], sum(case when call_result=33 then 1 else 0 end )[Answered], sum(case when call_result=14 then 1 else 0 end )[SIT Unknown], sum(case when  call_result=3 then 1 else 0 end )[General Error], sum(case when call_result=4 then 1 else 0 end )[System Error], sum(case when call_result=11 then 1 else 0 end )[Invalid Number] from  TRG_JIO_CALLHISTORY(nolock) a inner join ConfigDB..cfg_switch(Nolock) b on a.switch_id = b.dbid where  Call_date >= DATEADD(MINUTE, - 60, CONVERT(DATETIME, CONVERT(VARCHAR(16), GETDATE(), 120) + ':00:00'))  group by  (case when b.name = 'SIPSwitch01' then 'AHM' when b.name = 'SIPSwitch02' then 'BLR' when b.name = 'SIPSwitch03' then 'MOH' when b.name = 'SIPSwitch04' then 'HYD' when b.name = 'SIPSwitch05' then 'KOL' when b.name = 'SIPSwitch06' then 'MUM' when b.name = 'SIPSwitch07' then 'NOI' else b.name end)  order by 1;", con = conn)
	conn.close()
    # Prepare html code for the table
	html = df.head(rows_limit).to_html(classes = 'example', border = 1, index = False)
	html = re.sub(' example', '" id = "example', html)
	return render_template('Hrs.html', table = html)

@app.route("/BlasterDayReport")
def BlasterDayReport():
	conn = pymssql.connect(server, user, password, base)
	df = pd.read_sql("Select (case when b.name = 'SIPSwitch01' then 'AHM' when b.name = 'SIPSwitch02' then 'BLR' when b.name = 'SIPSwitch03' then 'MOH' when b.name = 'SIPSwitch04' then 'HYD' when b.name = 'SIPSwitch05' then 'KOL' when b.name = 'SIPSwitch06' then 'MUM' when b.name = 'SIPSwitch07' then 'NOI' else b.name end) Circle ,count(1)[Total], sum(case when call_result=13 then 1 else 0 end )[Dial_Error], sum(case when Call_Result=35 then 1 else 0 end )[No_DialTone], sum(case when call_result=37 then 1 else 0 end )[No_Ring Back Tone], sum(case when call_result=7 then 1 else 0 end )[No Answer],sum(case when call_result=6 then 1 else 0 end )[Busy], sum(case when call_result=33 then 1 else 0 end )[Answered], sum(case when call_result=14 then 1 else 0 end )[SIT Unknown], sum(case when  call_result=3 then 1 else 0 end )[General Error], sum(case when call_result=4 then 1 else 0 end )[System Error], sum(case when call_result=11 then 1 else 0 end )[Invalid Number] from  TRG_JIO_CALLHISTORY(nolock) a inner join ConfigDB..cfg_switch(Nolock) b on a.switch_id = b.dbid where  Call_date >=  CONVERT(VARCHAR(11), GETDATE(), 101)   group by  (case when b.name = 'SIPSwitch01' then 'AHM' when b.name = 'SIPSwitch02' then 'BLR' when b.name = 'SIPSwitch03' then 'MOH' when b.name = 'SIPSwitch04' then 'HYD' when b.name = 'SIPSwitch05' then 'KOL' when b.name = 'SIPSwitch06' then 'MUM' when b.name = 'SIPSwitch07' then 'NOI' else b.name end)  order by 1;", con = conn)
	conn.close()
    # Prepare html code for the table
	html = df.head(rows_limit).to_html(classes = 'example', border = 1, index = False)
	html = re.sub(' example', '" id = "example', html)
	return render_template('DayReport.html', table = html)
	

	
@app.route("/BlasterDayReportGraph")
def BlasterDayReportGraph():
	conn = pymssql.connect(server, user, password, base)
	df = pd.read_sql("Select (case when b.name = 'SIPSwitch01' then 'AHM' when b.name = 'SIPSwitch02' then 'BLR' when b.name = 'SIPSwitch03' then 'MOH' when b.name = 'SIPSwitch04' then 'HYD' when b.name = 'SIPSwitch05' then 'KOL' when b.name = 'SIPSwitch06' then 'MUM' when b.name = 'SIPSwitch07' then 'NOI' else b.name end) Circle ,count(1)[Total], sum(case when call_result=13 then 1 else 0 end )[Dial_Error], sum(case when Call_Result=35 then 1 else 0 end )[No_DialTone], sum(case when call_result=37 then 1 else 0 end )[No_Ring_Back_Tone], sum(case when call_result=7 then 1 else 0 end )[No Answer],sum(case when call_result=6 then 1 else 0 end )[Busy], sum(case when call_result=33 then 1 else 0 end )[Answered], sum(case when call_result=14 then 1 else 0 end )[SIT Unknown], sum(case when  call_result=3 then 1 else 0 end )[General Error], sum(case when call_result=4 then 1 else 0 end )[System Error], sum(case when call_result=11 then 1 else 0 end )[Invalid Number] from  TRG_JIO_CALLHISTORY(nolock) a inner join ConfigDB..cfg_switch(Nolock) b on a.switch_id = b.dbid where  Call_date >=  CONVERT(VARCHAR(11), GETDATE(), 101)   group by  (case when b.name = 'SIPSwitch01' then 'AHM' when b.name = 'SIPSwitch02' then 'BLR' when b.name = 'SIPSwitch03' then 'MOH' when b.name = 'SIPSwitch04' then 'HYD' when b.name = 'SIPSwitch05' then 'KOL' when b.name = 'SIPSwitch06' then 'MUM' when b.name = 'SIPSwitch07' then 'NOI' else b.name end)  order by 1;", con = conn)
	conn.close()
    # Prepare html code for the table
	category_group = df.groupby(['Total','Dial_Error','No_DialTone','No_Ring_Back_Tone']).sum()
	category_group.head()
	category_group.unstack().head()
	plt = category_group.unstack().plot(kind='bar',stacked=True,title="Total Sales by Customer",figsize=(9, 7))
	x_labels = df['Circle'].values
	x_coordinates = np.arange(len(x_labels))
	bar_heights = df['Total'].values

	plt.legend(["Total","Dial_Error","No_DialTone","No_Ring_Back_Tone"], loc=9,ncol=4)
	plt.bar(x_coordinates, bar_heights, align='center', color=['AliceBlue','AntiqueWhite','Aqua','Aquamarine','Beige','BlueViolet','Brown','BurlyWood','CadetBlue','Chocolate','Coral','Crimson','DarkCyan'], edgecolor=['red'])
	plt.xticks(x_coordinates, x_labels, rotation='vertical')
	plt.ylabel('Total')
	plt.title('Mojo Onnet RealtimeCallDetails')
	plt.tight_layout()
	plt.savefig('pic.png')
	figfile = BytesIO()
	plt.savefig(figfile, format='png')
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	result = str(figdata_png)[2:-1]
	#return render_template('TEST1.html', result=result)
	html = df.head(rows_limit).to_html(classes = 'example', border = 1, index = False)
	html = re.sub(' example', '" id = "example', html)
	return render_template('MojoOnnetRealtimeView.html', table = html, result=result)
	
	
@app.route("/IVR")
def IVR():
	#dsn_tns = cx_Oracle.makedsn('genivr-scan-bss.jio.com', '1521', 'PJIVRDB')
	#conns = cx_Oracle.connect('prod_ivr_config', 'Szyvr7#u', dsn_tns)
	conns = 'prod_ivr_config/Szyvr7#u@PJIVRDB'
	conns = cx_Oracle.connect('prod_ivr_config/Szyvr7#u@genivr-scan-bss.jio.com/PJIVRDB')
	query =  "select FLDCIRCLE Circle, count(*) TotalCall from TBLCALLDETAIL where FLDCALLSTARTTIME between '20-Nov-18 12:00:00.858000000 AM' and '20-Nov-18 11:59:59.858000000 PM' and FLDAPPNAME like '%SCT_MOJO_ONNET%' group by FLDCIRCLE "
	df = pd.read_sql(query, con = conns)
	conns.close()
    # Prepare html code for the table
	html = df.head(rows_limit).to_html(classes = 'example', border = 1, index = False)
	html = re.sub(' example', '" id = "example', html)
	return render_template('MojoOnet.html', table = html)

	

	
@app.route("/EmailPeakAgent")
def EmailPeakAgent():
	#dsn_tns = cx_Oracle.makedsn('genivr-scan-bss.jio.com', '1521', 'PJIVRDB')
	#conns = cx_Oracle.connect('prod_ivr_config', 'Szyvr7#u', dsn_tns)
	conns = 'prod_gim/prod_gim@PJAAR'
	conns = cx_Oracle.connect('prod_gim/prod_gim@gkcrept-scan.bss.jio.com/PJAAR')
	query =  "SELECT CALLDATE,TENANT_NAME,FIFTEENMIN,AGENT_COUNT FROM ( SELECT  DT.LABEL_YYYY_MM_DD AS CALLDATE ,TN.TENANT_NAME ,DT.LABEL_YYYY_MM_DD_HH24_15INT AS FIFTEENMIN ,COUNT(DISTINCT A.RESOURCE_KEY) AS AGENT_COUNT ,RANK()OVER (PARTITION BY DT.LABEL_YYYY_MM_DD,TN.TENANT_NAME ORDER BY COUNT(DISTINCT A.RESOURCE_KEY)DESC ,DT.LABEL_YYYY_MM_DD_HH24_15INT) RNK FROM SM_RES_SESSION_FACT A   INNER JOIN TENANT TN ON TN.TENANT_KEY = a.TENANT_KEY INNER JOIN RESOURCE_  RS ON RS.RESOURCE_KEY=A.RESOURCE_KEY JOIN DATE_TIME DT ON (DT.LABEL_YYYY_MM_DD =TO_CHAR(TO_DATE('01.01.1970 00:00:00','DD.MM.YYYY HH24:MI:SS') + ( A.START_DATE_TIME_KEY+19800)/86400,'YYYY-MM-DD') AND DT.DATE_TIME_KEY BETWEEN A.START_DATE_TIME_KEY AND A.END_DATE_TIME_KEY) JOIN DATE_TIME DTT ON DTT.DATE_TIME_KEY = A.START_DATE_TIME_KEY  WHERE DTT.LABEL_YYYY_MM_DD  >= to_char(sysdate-15,'YYYY-MM-DD') GROUP BY   DT.LABEL_YYYY_MM_DD ,TN.TENANT_NAME  ,DT.LABEL_YYYY_MM_DD_HH24_15INT ) WHERE RNK = 1"
	df = pd.read_sql(query, con = conns)
	conns.close()
    # Prepare html code for the table
	html = df.head(rows_limit).to_html(classes = 'example', border = 1, index = False)
	html = re.sub(' example', '" id = "example', html)
	return render_template('Peak Agent Report.html', table = html)

@app.route("/EmailCountLast10Day")
def EmailCountLast10Day():
	#dsn_tns = cx_Oracle.makedsn('genivr-scan-bss.jio.com', '1521', 'PJIVRDB')
	#conns = cx_Oracle.connect('prod_ivr_config', 'Szyvr7#u', dsn_tns)
	conns = 'prod_gim/prod_gim@PJAAR'
	conns = cx_Oracle.connect('prod_gim/prod_gim@gkcrept-scan.bss.jio.com/PJAAR')
	query =  "select EMAIL_DATE,count(*) total_Email  from V_EMAIL_SUMMARY WHERE EMAIL_DATE   >= to_char(sysdate-10,'YYYY-MM-DD')  group by EMAIL_DATE"
	df = pd.read_sql(query, con = conns)
	conns.close()
    # Prepare html code for the table
	html = df.head(rows_limit).to_html(classes = 'example', border = 1, index = False)
	html = re.sub(' example', '" id = "example', html)
	return render_template('EmailCountLast10Day.html', table = html)



@app.route("/EmailPeakAgentGraph")
def EmailPeakAgentGraph():
	#dsn_tns = cx_Oracle.makedsn('genivr-scan-bss.jio.com', '1521', 'PJIVRDB')
	#conns = cx_Oracle.connect('prod_ivr_config', 'Szyvr7#u', dsn_tns)
	conns = 'prod_gim/prod_gim@PJAAR'
	conns = cx_Oracle.connect('prod_gim/prod_gim@gkcrept-scan.bss.jio.com/PJAAR')
	query =  "SELECT CALLDATE,TENANT_NAME,FIFTEENMIN,AGENT_COUNT FROM ( SELECT  DT.LABEL_YYYY_MM_DD AS CALLDATE ,TN.TENANT_NAME ,DT.LABEL_YYYY_MM_DD_HH24_15INT AS FIFTEENMIN ,COUNT(DISTINCT A.RESOURCE_KEY) AS AGENT_COUNT ,RANK()OVER (PARTITION BY DT.LABEL_YYYY_MM_DD,TN.TENANT_NAME ORDER BY COUNT(DISTINCT A.RESOURCE_KEY)DESC ,DT.LABEL_YYYY_MM_DD_HH24_15INT) RNK FROM SM_RES_SESSION_FACT A   INNER JOIN TENANT TN ON TN.TENANT_KEY = a.TENANT_KEY INNER JOIN RESOURCE_  RS ON RS.RESOURCE_KEY=A.RESOURCE_KEY JOIN DATE_TIME DT ON (DT.LABEL_YYYY_MM_DD =TO_CHAR(TO_DATE('01.01.1970 00:00:00','DD.MM.YYYY HH24:MI:SS') + ( A.START_DATE_TIME_KEY+19800)/86400,'YYYY-MM-DD') AND DT.DATE_TIME_KEY BETWEEN A.START_DATE_TIME_KEY AND A.END_DATE_TIME_KEY) JOIN DATE_TIME DTT ON DTT.DATE_TIME_KEY = A.START_DATE_TIME_KEY  WHERE DTT.LABEL_YYYY_MM_DD  >= to_char(sysdate-15,'YYYY-MM-DD') GROUP BY   DT.LABEL_YYYY_MM_DD ,TN.TENANT_NAME  ,DT.LABEL_YYYY_MM_DD_HH24_15INT ) WHERE RNK = 1"
	df = pd.DataFrame(pd.read_sql(query, con = conns))
	conns.close()
	df.plot.bar(x='CALLDATE', y='AGENT_COUNT')
    # Prepare html code for the table
	html = df.head(rows_limit).to_html(classes = 'example', border = 1, index = False)
	html = re.sub(' example', '" id = "example', html)
	return render_template('Peak Agent Report.html', table = html)
	
@app.route("/IVRMojoOnnetDay")
def IVRMojoOnnetDay():
	#dsn_tns = cx_Oracle.makedsn('genivr-scan-bss.jio.com', '1521', 'PJIVRDB')
	#conns = cx_Oracle.connect('prod_ivr_config', 'Szyvr7#u', dsn_tns)
	conns = 'prod_ivr_config/Szyvr7#u@PJIVRDB'
	conns = cx_Oracle.connect('prod_ivr_config/Szyvr7#u@genivr-scan-bss.jio.com/PJIVRDB')
	query =  "select FLDCIRCLE Circle, count(*) TotalCall from TBLCALLDETAIL where FLDCALLSTARTTIME >= to_char(sysdate,'DD-MON-YY') and  FLDAPPNAME like '%SCT_MOJO_ONNET%' group by FLDCIRCLE"
	df = pd.DataFrame(pd.read_sql(query, con = conns))
	conns.close()	
	
    # Prepare html code for the table
	#x_labels = df['CIRCLE'].values
	#x_coordinates = np.arange(len(x_labels))
	#bar_heights = df['TOTALCALL'].values
	#plt.bar(x_coordinates, bar_heights, align='center', #color=['AliceBlue','AntiqueWhite','Aqua','Aquamarine','Beige','BlueViolet','Brown','BurlyWood','CadetBlue','Chocolate','Coral','Crimson','DarkCyan'], #edgecolor=['red'])
	#plt.xticks(x_coordinates, x_labels, rotation='vertical')
	#plt.ylabel('TOTALCALL')
	#plt.title('Mojo Onnet RealtimeCallDetails')
	#plt.tight_layout()
	#plt.savefig('pic.png')
	#figfile = BytesIO()
	#plt.savefig(figfile, format='png')
	#figfile.seek(0)
	#figdata_png = base64.b64encode(figfile.getvalue())
	#result = str(figdata_png)[2:-1]
	#return render_template('TEST1.html', result=result)
	html = df.head(rows_limit).to_html(classes = 'example', border = 1, index = False)
	html = re.sub(' example', '" id = "example', html)
	return render_template('MojoOnnetRealtimeView.html', table = html)

@app.route("/IVRMojoOnnetLast15Min")
def IVRMojoOnnetLast15Min():
	#dsn_tns = cx_Oracle.makedsn('genivr-scan-bss.jio.com', '1521', 'PJIVRDB')
	#conns = cx_Oracle.connect('prod_ivr_config', 'Szyvr7#u', dsn_tns)
	conns = 'prod_ivr_config/Szyvr7#u@PJIVRDB'
	conns = cx_Oracle.connect('prod_ivr_config/Szyvr7#u@genivr-scan-bss.jio.com/PJIVRDB')
	query_15 =  "select FLDCIRCLE Circle, count(*) TotalCall from TBLCALLDETAIL where FLDCALLSTARTTIME >= systimestamp - numtodsinterval(15,'MINUTE')	and  FLDAPPNAME like '%SCT_MOJO_ONNET%' group by FLDCIRCLE"
	df_15 = pd_15.DataFrame(pd_15.read_sql(query_15, con = conns))
	conns.close()	
	
    # Prepare html code for the table
	x_labels_15 = df_15['CIRCLE'].values
	x_coordinates_15 = np_15.arange(len(x_labels_15))
	bar_heights_15 = df_15['TOTALCALL'].values
	plt2.bar(x_coordinates_15, bar_heights_15, align='center', color=['AliceBlue','AntiqueWhite','Aqua','Aquamarine','Beige','BlueViolet','Brown','BurlyWood','CadetBlue','Chocolate','Coral','Crimson','DarkCyan'], edgecolor=['yellow'])
	plt2.xticks(x_coordinates_15, x_labels_15, rotation='vertical')
	plt2.ylabel('TOTALCALL')
	plt2.title('Mojo Onnet Last 15 Mins Call Report')
	plt2.tight_layout()
	plt2.savefig('MojoOnnetRealtimeView_Last15Min.png')
	figfile_15 = BytesIO()
	plt2.savefig(figfile_15, format='png')
	figfile_15.seek(0)
	figdata_png2 = base64.b64encode(figfile_15.getvalue())
	result_15 = str(figdata_png2)[2:-1]
	#return render_template('TEST1.html', result=result)
	html = df_15.head(rows_limit).to_html(classes = 'example', border = 1, index = False)
	html = re.sub(' example', '" id = "example', html)
	return render_template('MojoOnnetRealtimeView_Last15Min.html', table = html, result = result_15)
	
	
@app.route("/IVRMojoOnnetData")
def IVRMojoOnnetData():
	#dsn_tns = cx_Oracle.makedsn('genivr-scan-bss.jio.com', '1521', 'PJIVRDB')
	#conns = cx_Oracle.connect('prod_ivr_config', 'Szyvr7#u', dsn_tns)
	conns = 'prod_ivr_config/Szyvr7#u@PJIVRDB'
	conns = cx_Oracle.connect('prod_ivr_config/Szyvr7#u@genivr-scan-bss.jio.com/PJIVRDB')
	query =  "select FLDCIRCLE Circle, count(*) TotalCall from TBLCALLDETAIL where FLDCALLSTARTTIME >= to_char(sysdate,'DD-MON-YY') and  FLDAPPNAME like '%SCT_MOJO_ONNET%' group by FLDCIRCLE"
	df = pd.read_sql(query, con = conns)
	conns.close()
    # Prepare html code for the table
	html = df.head(rows_limit).to_html(classes = 'example', border = 1, index = False)
	html = re.sub(' example', '" id = "example', html)
	return render_template('MojoOnet.html', table = html)
	
	
if __name__ == "__main__":
    
    # Retreive MS SQL data
      
    
    # Remove empty or equal filled columns
    #df.drop('consumer_complaint_narrative', axis = 1, inplace = True)
    #df.drop('company_public_response', axis = 1, inplace = True)
    #df.drop('consumer_consent_provided', axis = 1, inplace = True)
    
    # Run the app with enabled debug
    app.run(host='0.0.0.0', port=80, debug = True)