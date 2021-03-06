/*
 * 客户端和服务器端保持通信 的线程
 * 
 * 允许一台机器上登陆的多个qq，多个线程，进行管理，再写一个管理的
 * 也实现聊天的线程类
 * */

package com.qq.client.tools;

import java.io.*;
import java.net.*;

import com.qq.client.view.QqChat;
import com.qq.client.view.QqList;
import com.qq.common.*;

public class NewUserThread extends Thread{

	private Socket s;
	public NewUserThread(Socket s) {
		this.s = s;
		
	}
	
	public void run(){
		while(true){
			//不停的读取从服务器端发来的消息
			try{
				ObjectInputStream ois = new ObjectInputStream(s.getInputStream());
				Message m = (Message)ois.readObject();
				
				if(m.getMesType().equals(MessageType.Message_com)){
					//如果是普通信息包，把从服务器获得的消息（不停地）显示到聊天界面
					System.out.println("读取到从服务器发来的消息  " + m.getSender() + "给 " +
				m.getGetter() + "发送内容：" + m.getCon());
				
				QqChat qc = ManageQqChat.getQqChat(m.getGetter() + " " + m.getSender());
				qc.ShowMessage(m);
				}
				else if(m.getMesType().equals(MessageType.Message_return_online)){
					//如果是请求返回好友列表的包
					
					//修改好友列表
					QqList ql = ManageQqList.getQqList(m.getGetter());
					System.out.println("客户端收到" + m.getGetter());
					
					if(ql!=null)
					{
						ql.updateQqList(m);
					}
				}
				
				
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}

	public Socket getS() {
		return s;
	}

	public void setS(Socket s) {
		this.s = s;
	}
}
