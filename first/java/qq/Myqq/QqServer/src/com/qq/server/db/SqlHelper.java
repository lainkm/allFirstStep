/*
 * 
 * */

package com.qq.server.db;

import java.sql.*;


public class SqlHelper {
}
	/*
	public static void main(String[] args)
	{
		String driver = "com.mysql.jdbc.Driver";  
		//localhostָ������Ҳ�����ñ���ip��ַ���棬3306ΪMySQL���ݿ��Ĭ�϶˿ںţ���user��ΪҪ���ӵ����ݿ���
		String url = "jdbc:mysql://localhost:3306/user";

		//String username = "root"; //���ݿ���û���
		//String password = "123456"; //����
	
		new SqlHelper();
		String sql = "select * from Db where id =" + id + " and pw =" + pw;//��дҪִ�е�sql��䣬�˴�Ϊ��user���в�ѯ�����û�����Ϣ
	try
	{
	Class.forName(driver);//�����������򣬴˴�������ʽע����������ķ���
	}
	catch(ClassNotFoundException e)
	{
	e.printStackTrace();
	}
	try
	{
	Connection con = DriverManager.getConnection(url,username,password);//�������Ӷ���
	Statement st = con.createStatement();//����sqlִ�ж���
	ResultSet rs = st.executeQuery(sql);//ִ��sql��䲢���ؽ����
	while(rs.next())//�Խ�������б������
	{
	System.out.println("id: "+rs.getString(1));//ͨ���еı�����������
	System.out.println("name: "+rs.getString("name"));//ͨ���������������
	System.out.println("value: "+rs.getString("value"));
	}
	//�ر���صĶ���
	if(rs != null)
	{
	try
	{
	rs.close();
	}
	catch(SQLException e)
	{
	e.printStackTrace();
	}
	}
	if(st != null)
	{
	try
	{
	st.close();
	}
	catch(SQLException e)
	{
	e.printStackTrace();
	}
	}
	if(con !=null)
	{
	try
	{
	con.close();
	}
	catch(SQLException e)
	{
	e.printStackTrace();
	}
	}
	}
	catch(SQLException e)
	{
	e.printStackTrace();
	}
	}
}
*/