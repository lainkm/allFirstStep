package com.qq.common;

public interface MessageType {

	//登陆成功失败
	String Message_success = "1";
	String Message_failed = "2";
	
	//普通信息包
	String Message_com = "3";
	
	//要求在线好友的包
	String Message_get_online = "4";
	
	//返回在线好友的包
	String Message_return_online = "5";
}
