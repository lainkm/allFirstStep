/**
 *qq������ 
 *����ĳ��qq�ͻ������� 
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
			System.out.println("�������ڼ���");
			//��9999����
			ServerSocket ss = new ServerSocket(9999);//���ڱ�����������������������ip��
			//�������ȴ�����
			
			while(true)
			{
				Socket s = ss.accept();
				
				//ֱ���ö��������տͻ��˷�������Ϣ
				ObjectInputStream ois = new ObjectInputStream(s.getInputStream());
				
				User u = (User)ois.readObject();
				System.out.println("�������յ��û� id: " + u.getId() + " ���룺" + u.getPw());
				
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
					
					
					//�û��������ڣ�Ҫע��
					//m.setCon((random++) + "");
					System.out.println(u.getPw());

					System.out.println(m.getCon());
					ObjectOutputStream oos = new ObjectOutputStream(s.getOutputStream());
					oos.writeObject(m);


				}
				else{
				//����֤�˺ŵĽ��ͨ����Ϣ���ٷ��ͻ�ȥ
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
				
				if(flag == true)//�����дһ��
				{
					//����һ����½�ɹ�����Ϣ��
					m.setMesType("1");
					oos.writeObject(m);
					
					//����һ���̣߳��ø��߳���ͻ���ͨ��
					ConnectThread ct = new ConnectThread(s);//�ڶ����ͻ��˴��������һ��socket
					ManageClientThread.addClientThread(u.getId(), ct);;
					//������ÿͻ���ͨѶ�Ľ���
					ct.start();
					
					//��֪ͨ���������û�����ConnectThread��ʵ��
					ct.notifyThread(u.getId());
					
				}
				else{//��½ʧ��
					m.setMesType("2");
					oos.writeObject(m);
					//�ر�����
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