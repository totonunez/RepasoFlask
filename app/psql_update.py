from configuraciones import *
import psycopg2
conn=psycopg2.connect("dbname=%s user=%s password=%s"%(database, user, passwd))



cur=conn.cursor()







sql="""select * from  autos where patente='CKTJ76' for update;"""
cur.execute(sql)
data=cur.fetchall()
print(data)
if data:
	print('TRUE')
	try:
		sql="""update autos set rut='19114077';"""
		response=cur.execute(sql)
		data=cur.fetchall()
		print(response)
		print(data)
	except:
		print('error, debe ingresar el usuario o fue mal escrito')
else:
	print('error el auto no se registra en la bases de datos')



conn.commit()
cur.close()
conn.close()
print 'ok'


