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
		//localhost指本机，也可以用本地ip地址代替，3306为MySQL数据库的默认端口号，“user”为要连接的数据库名
		String url = "jdbc:mysql://localhost:3306/user";

		//String username = "root"; //数据库的用户名
		//String password = "123456"; //密码
	
		new SqlHelper();
		String sql = "select * from Db where id =" + id + " and pw =" + pw;//编写要执行的sql语句，此处为从user表中查询所有用户的信息
	try
	{
	Class.forName(driver);//加载驱动程序，此处运用隐式注册驱动程序的方法
	}
	catch(ClassNotFoundException e)
	{
	e.printStackTrace();
	}
	try
	{
	Connection con = DriverManager.getConnection(url,username,password);//创建连接对象
	Statement st = con.createStatement();//创建sql执行对象
	ResultSet rs = st.executeQuery(sql);//执行sql语句并返回结果集
	while(rs.next())//对结果集进行遍历输出
	{
	System.out.println("id: "+rs.getString(1));//通过列的标号来获得数据
	System.out.println("name: "+rs.getString("name"));//通过列名来获得数据
	System.out.println("value: "+rs.getString("value"));
	}
	//关闭相关的对象
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