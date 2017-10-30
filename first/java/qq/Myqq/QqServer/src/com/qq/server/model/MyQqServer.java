/**
 *qq服务器 
 *监听某个qq客户端连接 
 */

package com.qq.server.model;
import java.net.*;
import java.io.*;
import java.util.*;

import javax.swing.tree.ExpandVetoException;

import com.qq.common.Message;
import com.qq.common.User;
import com.qq.server.tools.ManageClientThread;


public class MyQqServer {

	final int std = 906486132;
	public static int random = 1;
	public MyQqServer()
	{
		try{
			System.out.println("服务器在监听");
			//在9999监听
			ServerSocket ss = new ServerSocket(9999);//就在本机服务器启动监听，不用ip啊
			//阻塞，等待连接
			
			while(true)
			{
				Socket s = ss.accept();
				
				//直接用对象流接收客户端发来的信息
				ObjectInputStream ois = new ObjectInputStream(s.getInputStream());
				
				User u = (User)ois.readObject();
				System.out.println("服务器收到用户 id: " + u.getId() + " 密码：" + u.getPw());
				
				if(u.getId().equals(""))
				{
					Message m = new Message();
					try{
						File file = new File("Register.txt");
						Writer w = new FileWriter(file, true);
						Reader r = new FileReader(file);
						
						//FileWriter file = new FileWriter("S.txt","aw");
						BufferedWriter bw = new BufferedWriter(w);
						BufferedReader br = new BufferedReader(r);
						String string;
						String string1 = new String("");
						while((string = br.readLine())!=null)
						{
							//StringTokenizer temp = new StringTokenizer(string, " ");
							//string1 = temp.nextToken();
							
							Scanner in = new Scanner(string);
							Long id = in.nextLong() + 1;
							string1 = id + "";
						}
						m.setCon(string1);
						
						String str = m.getCon() + " " + u.getPw();
						System.out.println((String.valueOf(string1) + 1) + "");
						int n = str.length();
						bw.write(str, 0, n);
						bw.newLine();
						
						
						bw.close();
						w.close();
						r.close();
						}
						catch(Exception e)
						{
							e.printStackTrace();
						}
					
					
					//用户名不存在，要注册
					//m.setCon((random++) + "");
					System.out.println(u.getPw());

					System.out.println(m.getCon());
					ObjectOutputStream oos = new ObjectOutputStream(s.getOutputStream());
					oos.writeObject(m);


				}
				else{
				//把验证账号的结果通过信息包再发送回去
				Message m = new Message();
				ObjectOutputStream oos = new ObjectOutputStream(s.getOutputStream());
				
				
				File f = new File("Register.txt");
				Reader r = new FileReader(f);
				BufferedReader br = new BufferedReader(r);
				String s1;
				boolean flag = false;
				while((s1 = br.readLine())!=null)
				{
		
					Scanner in = new Scanner(s1);
					if(in.next().equals(u.getId()))
					{
						if(in.next().equals(u.getPw()))
						{
							flag = true;
						}
					}
				}
				
				if(flag == true)//先随便写一个
				{
					//返回一个登陆成功的信息包
					m.setMesType("1");
					oos.writeObject(m);
					
					//单开一个线程，让该线程与客户端通信
					ConnectThread ct = new ConnectThread(s);//第二个客户端传入的是另一个socket
					ManageClientThread.addClientThread(u.getId(), ct);;
					//启动与该客户端通讯的进程
					ct.start();
					
					//并通知其他在线用户，用ConnectThread里实现
					ct.notifyThread(u.getId());
					
				}
				else{//登陆失败
					m.setMesType("2");
					oos.writeObject(m);
					//关闭连接
					s.close();
				}
			}
				}
		}	
		catch(Exception e){
			e.printStackTrace();
		}
		finally{
			
		}
	}

}
