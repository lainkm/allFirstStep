/*
 * 管理客户端与服务器通讯的线程类
 * 多个用户的线程
 * */

package com.qq.client.tools;

import java.util.*;

public class ManageNewUserConnectThread {

	//可以静态，一个服务器只需要一个hashmap
	static HashMap hm = new HashMap<String, NewUserThread>();
	
	//把创建好的新用户线程和对应的id号放进创建好的线程
	public static void addNewUserThread(String userId, NewUserThread nut){
		hm.put(userId, nut);//把用户id和线程放进去
	}
	
	//返回一个线程，因为要通过这个线程转发
	public static NewUserThread getNewUserThread(String userId)
	{
		return (NewUserThread)hm.get(userId);
	}
	
}
