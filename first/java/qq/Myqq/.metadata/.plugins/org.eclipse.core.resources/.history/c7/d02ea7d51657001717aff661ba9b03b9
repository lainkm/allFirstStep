/*
 * 客户端连接服务器后台
 * */
package com.qq.client.model;

import java.util.*;

import javax.swing.JOptionPane;

import java.net.*;
import java.io.*;

import com.qq.client.tools.ManageNewUserConnectThread;
import com.qq.client.tools.NewUserThread;
import com.qq.common.*;

public class MyQqConnect {

	
	
	public Socket s;
	Object o;
	//第一次发送请求
	
	public MyQqConnect(Object o)
	{
		this.o = o;
		try {
			s = new Socket("127.0.0.1", 9999);
			ObjectOutputStream oos = new ObjectOutputStream
				(s.getOutputStream());
				oos.writeObject(o);
				System.out.println("服务器收到用户 id: " + ((User)o).getId() + " 密码：" + ((User)o).getPw());
				
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public String sendRegisterMessage()
	{
		Message m = new Message();
		try{
			ObjectInputStream ois = new ObjectInputStream(s.getInputStream());
			m = (Message)ois.readObject();
		}
		catch(Exception e1)
		{
			e1.printStackTrace();
		}
		finally{
			System.out.println("Client" + m.getCon());
			return m.getCon();
		}
		}
	public boolean sendLoginInfoToserver()
	{
		boolean b = false;
		try{
		//	s = new Socket("127.0.0.1", 9999);
			
			System.out.println("1");
			//发送user对象
	//		ObjectOutputStream oos = new ObjectOutputStream(s.getOutputStream());
		//	oos.writeObject(o);

			System.out.println("2");
			//接收
			ObjectInputStream ois = new ObjectInputStream(s.getInputStream());
			Message m = (Message)ois.readObject();

			System.out.println("3");
			//验证用户登陆的地方，把登陆成功的用户的socket（改成非静态的不共享），这样创建一个用户线程
			if(m.getMesType().equals("1"))
			{
				//创建一个该qq号和服务器的通讯连接的线程,并启动自己的线程，保持与服务器通讯 
				NewUserThread nut = new NewUserThread(s);
				nut.start();
				//为了管理这个qq号立马放进hashmap里
				ManageNewUserConnectThread.addNewUserThread(((User)o).getId(), nut);
				b = true;
				
			}
			else{
				s.close();
			}
			
		}catch(Exception e){
			e.printStackTrace();
		}finally{
			
		}
		return b;
	}
	
	
}


