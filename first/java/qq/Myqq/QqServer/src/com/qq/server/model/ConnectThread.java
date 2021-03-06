/**
 * 服务器与某个客户端通信线程
 */

package com.qq.server.model;

import java.net.*;
import java.util.HashMap;
import java.util.Iterator;

import com.qq.common.Message;
import com.qq.common.MessageType;
import com.qq.server.tools.ManageClientThread;

import java.io.*;

public class ConnectThread extends Thread{
	
	Socket s;//得到一个Socket
	
	public ConnectThread(Socket s)
	{
		//把服务器与客户端的连接赋给s,让线程有一个Socket
		this.s = s;
	}
	
	
	//用户上线信息通知给其他人，传入用户
	public void notifyThread(String myId){
		HashMap hm = ManageClientThread.hm;
		Iterator it = hm.keySet().iterator(); 
		while(it.hasNext())
		{
			Message m = new Message();
			m.setCon(myId);//把con传给其他人
			m.setMesType(MessageType.Message_return_online);//返回给其他好友在线的消息
			
			String onlineId = it.next().toString();
			try{
			ObjectOutputStream oos = new ObjectOutputStream
					(ManageClientThread.getClientThread(onlineId).s.getOutputStream());
			
			m.setGetter(onlineId);//onlineId的好友会收到该用户上线的消息
			oos.writeObject(m);
			}
			catch(Exception e)
			{
				e.printStackTrace();
			}
		}
	}
	
	public void run()
	{
		while(true)
		{
			//这里这个线程就可以接收客户端的信息
			
			try{
				ObjectInputStream ois = new ObjectInputStream(s.getInputStream());
				Message m = (Message)ois.readObject();
			
				//消息判断，普通消息和更新好友列表
				if(m.getMesType().equals(MessageType.Message_com))
				{
					//测试一下服务器拿到了客户端1
				System.out.println(m.getSender() + "给" + m.getGetter()+" 说了 " + m.getCon());
				
				//完成转发
				
				//取得接收人的通讯线程
				ConnectThread ct = ManageClientThread.getClientThread(m.getGetter());//找到接收人的Socket
				ObjectOutputStream oos = new ObjectOutputStream(ct.s.getOutputStream());//接收人的Socket和服务器的连接
				oos.writeObject(m);//服务器给他发出去
				}
				else if(m.getMesType().equals(MessageType.Message_get_online))
				{
					//把在服务器的好友给这个请求的用户返回回去
					//遍历hashmap得到在线的人
					
					
					String res = ManageClientThread.getAllOnline();
					Message return_m = new Message();
					return_m.setMesType(MessageType.Message_return_online);
					return_m.setCon(res);
					return_m.setGetter(m.getSender());
					
					//这个是在回送给请求端的，不是转发
					ObjectOutputStream oos = new ObjectOutputStream(s.getOutputStream());//接收人的Socket和服务器的连接
					oos.writeObject(return_m);//服务器给他发出去
					
				}
				
				
			}catch(Exception e){
				
			}
		}
		
	}
}
