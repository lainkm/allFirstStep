package com.qq.server.tools;

import java.util.*;

import com.qq.server.model.ConnectThread;

public class ManageClientThread {
	
	public static HashMap hm= new HashMap<String, ConnectThread>();//只能有一个hm，可用静态
	
	
	//向hm中添加一个客户端通讯线程
	public static void addClientThread(String userId, ConnectThread ct){
		hm.put(userId, ct);//把用户id和线程放进去
	}
	
	//返回一个线程，因为要通过这个线程转发
	public static ConnectThread getClientThread(String userId)
	{
		return (ConnectThread)hm.get(userId);
	}
	
	//返回当前在线的人的情况
	public static String getAllOnline()
	{
		//hashMap得到key值，用迭代器
		String res = "";
		Iterator it=hm.keySet().iterator();
		while(it.hasNext())
		{
			res += it.next().toString() + " ";
		}
		return res;
	}
}
