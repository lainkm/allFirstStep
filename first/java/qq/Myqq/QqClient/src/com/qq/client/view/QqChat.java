/*
 * qq好友聊天界面
 * 客户端要处于一直读取的状态，所以要把他做成一个线程
 * */
package com.qq.client.view;

import javax.swing.*;

import com.qq.common.Message;
import com.qq.common.MessageType;

import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.text.ParsePosition;
import java.text.SimpleDateFormat;
import java.util.Date;

import com.qq.client.model.*;
import com.qq.client.tools.*;
public class QqChat extends JFrame implements ActionListener{

	JTextArea jta1, jta2;
	JButton jb1, jb2;
	JPanel jp;
	
	String myId;
	String friendId;
	
	Message my_m;
	public QqChat(String myId, String friendId)
	{
		this.myId = myId;
		this.friendId = friendId;
		
		jta1 = new JTextArea(25,40);
		jta2 = new JTextArea(15,25);
		jb1 = new JButton("发送");
		jb1.addActionListener(this);
		jb2 = new JButton("关闭");
		jp = new JPanel();
		
		jp.add(jb1);
		jp.add(jb2);
		setLayout(new BorderLayout(5,5));
		this.add(jta1,"North");
		this.add(jta2,"Center");
		this.add(jp, "South");
		
		
		this.setSize(800,700);
		this.setIconImage(new ImageIcon("image/qq.gif").getImage());
		this.setTitle(myId+" 正在和 " + friendId + " 聊天");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setVisible(true);
		
	}
	
	
	public static void main(String[] args)
	{
		//QqChat qqChat = new QqChat("name");
	}


	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() == jb1)
		{
			//如果用户点击了发送按钮
			my_m = new Message();
			my_m.setMesType(MessageType.Message_com);
			my_m.setSender(myId);
			my_m.setGetter(friendId);
			my_m.setCon(jta2.getText());
			my_m.setTime(new java.util.Date().toString());
			
			//发送给服务器
			try{
				ObjectOutputStream oos = new ObjectOutputStream(
						 ManageNewUserConnectThread.getNewUserThread(myId).getS().getOutputStream());
				
				oos.writeObject(my_m);//发送
				String my_info = my_m.getSender() + " ("+my_m.getTime()+")\r\n    "
							   + my_m.getCon() +"\n\n";
				this.jta1.append(my_info);
			}catch(Exception e0){
				e0.printStackTrace();
			}
			
			//应该处于一个一直读取的状态，用线程或while
			
		}
	}

	//让QqChat在线程显示收到的信息
	public void ShowMessage(Message fr_m)
	{
		String fr_info = fr_m.getSender()+" ("+fr_m.getTime()+")\r\n    "+fr_m.getCon()+"\n\n";
		this.jta1.append(fr_info);
	}
	
	
	
	
	/*
	public void run() {
		// TODO Auto-generated method stub
		while(true){
			
			try{
			//读取（读取不到就等待
			ObjectInputStream ois = new ObjectInputStream(MyQqConnect.s.getInputStream());
			fr_m = (Message)ois.readObject();
			
			//显示
			String fr_info = fr_m.getSender()+" ("+fr_m.getTime()+")\r\n    "+fr_m.getCon()+"\n\n";
			this.jta1.append(fr_info);//追加放到上面的textarea
			
			}
			catch(Exception e){
				e.printStackTrace();
			}
		}
	}
	*/
		
}
