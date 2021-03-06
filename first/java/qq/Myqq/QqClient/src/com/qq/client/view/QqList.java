/*
 * qq好友列表
 * */

package com.qq.client.view;

import javax.swing.*;
import com.qq.client.tools.*;
import com.qq.common.Message;

import java.awt.*;
import java.awt.event.*;

public class QqList extends JFrame implements ActionListener, MouseListener{

	//第一张卡片(打开好友列表
	JPanel jpf1, jpf2, jpf3;//第一个里面放后面两个
	JButton jpf_jb1, jpf_jb2, jpf_jb3;//好友黑名单选择按钮
	JScrollPane jsp1;//好友列表滚动条
	
	//第一张卡片(打开陌生人列表
	JPanel jps1, jps2, jps3;//第一个里面放后面两个
	JButton jps_jb1, jps_jb2, jps_jb3;//好友黑名单选择按钮
	JScrollPane jsp2;//好友列表滚动条
	
	
	//第三张卡片（收起
	JPanel jp1, jp2;
	JButton jb1, jb2, jb3;
	
	String myId;
	JLabel jbls[];
	JLabel jbls2[];
	
	//把整个jframe写成cardlayout布局
	CardLayout c1;
	public QqList(String myId){
		this.myId = myId;
		//第一张卡片，显示好友列表
		jpf1 = new JPanel(new BorderLayout());
		
		//假如5个好友
		jpf2 = new JPanel(new GridLayout(25, 1, 4, 4));//4,4是行列间距
		jpf3 = new JPanel(new GridLayout(2, 1));//这个panel放两个按钮黑名单，陌生人
		
		//给jpf2初始化5个好友，
		//默认只有自己在线，其他好友都不在线
		jbls = new JLabel[25];
		for(int i = 0; i < jbls.length; i++)
		{
			jbls[i] =  new JLabel((i + 1) + "", new ImageIcon("image/tx3.png"), JLabel.LEFT);
			jbls[i].setEnabled(false);
			if(jbls[i].getText().equals(myId) )
			{
				jbls[i].setEnabled(true);
			}
			jbls[i].addMouseListener(this);
			jpf2.add(jbls[i]);
		}
		
		jpf_jb1 = new JButton("我的好友");
		jpf_jb1.addActionListener(this);
		jpf_jb2 = new JButton("陌生人");
		jpf_jb2.addActionListener(this);
		jpf_jb3 = new JButton("黑名单");
		
		jp1 = new JPanel(new GridLayout(3, 1));
		jp2 = new JPanel(new BorderLayout());
		jb1 = new JButton("我的好友");
		jb1.addActionListener(this);
		jb2 = new JButton("陌生人");
		jb2.addActionListener(this);
		jb3 = new JButton("黑名单");
		jp1.add(jb1);
		jp1.add(jb2);
		jp1.add(jb3);
		jp2.add(jp1, "North");
		
		//把按钮放进jpanel3
		jpf3.add(jpf_jb2);
		jpf3.add(jpf_jb3);
		
		jsp1 = new JScrollPane(jpf2);
		
		//对jps1初始化，就是整个大的
		jpf1.add(jpf_jb1, "North");
		jpf1.add(jsp1,"Center");
		jpf1.add(jpf3, "South");
		
		
		//处理第二张卡片
		jps1 = new JPanel(new BorderLayout());
		
		//假如25个好友
		jps2 = new JPanel(new GridLayout(20, 1, 4, 4));//4,4是行列间距
		jps3 = new JPanel(new GridLayout(2, 1));//这个panel放两个按钮好友，陌生人
		
		//给jpf2初始化5个好友
		jbls2 = new JLabel[20];
		for(int i = 0; i < jbls2.length; i++)
		{
			jbls2[i] =  new JLabel(""+(i + 1), new ImageIcon("image/tx3.png"), JLabel.LEFT);
			jps2.add(jbls2[i]);
		}
		
		jps_jb1 = new JButton("我的好友");
		jps_jb1.addActionListener(this);
		jps_jb2 = new JButton("陌生人");
		jps_jb2.addActionListener(this);
		jps_jb3 = new JButton("黑名单");
		
		//把按钮放进jpanel3
		jps3.add(jps_jb1);
		jps3.add(jps_jb2);
		
		jsp2 = new JScrollPane(jps2);
		
		//对jps1初始化，就是整个大的
		jps1.add(jps3, "North");
		jps1.add(jsp2,"Center");
		jps1.add(jps_jb3, "South");
		
		
		
		
		c1 = new CardLayout();
		this.setLayout(c1);
		this.add(jpf1, "1");
		this.add(jps1,"2"); 
		this.add(jp2,"3");
		
		//this.add(jpf1, "Center");
		this.setSize(300, 800);
		this.setTitle("好友列表");

		this.setIconImage(new ImageIcon("image/qq.gif").getImage());
		
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setVisible(true);
		this.setTitle(myId);
		
		
		 
	}
	
	
	//更新好友列表,灰色的变彩色，彩色变灰色
	public void updateQqList(Message m) {
		String con = m.getCon();
		String friList[] = con.split(" ");
		String getter = m.getGetter();//服务器发给谁的,当前账号请求要的
		
		for(int i = 0; i < friList.length; i++)
		{
			jbls[Integer.parseInt(friList[i]) - 1].setEnabled(true);
		}
	}
	
	
	
	

	//把整个jframe写成cardlayout布局
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//	QqList qqList = new QqList("1");
	}

	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource()==jpf_jb2 || e.getSource()==jb2 )
		{
			c1.show(this.getContentPane(), "2");//不能对第二张卡片进行控制，只能对卡片的panel进行控制
		}
		else if(e.getSource()==jps_jb1 ||e.getSource()==jb1 )
		{
			c1.show(this.getContentPane(), "1");
		}
		else if(e.getSource()==jpf_jb1 || e.getSource()==jps_jb2)
		{
			c1.show(this.getContentPane(), "3");
		}
	}

	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		//相应用户双击事件，得到好友编号
		if(e.getClickCount()==2)
		{
			//得到该好友的编号
			String friendId = ((JLabel)e.getSource()).getText();
			System.out.println("要和"+friendId+"聊天");
			
			QqChat qc = new QqChat(myId, friendId);
			
			ManageQqChat.addQqChat(myId + " " + friendId, qc);
			//QqChat里面去实现一个显示的方法
			
			
			//把界面的线程交给另外的线程类
			//Thread t = new Thread(qc);
			//t.start();//启动聊天界面线程，
			//System.out.println("一直读取。。。");
		}
	}

	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		JLabel j1 = (JLabel)e.getSource();
		j1.setForeground(Color.red);
	}

	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		JLabel j1 = (JLabel)e.getSource();
		j1.setForeground(Color.black);
	}

	
	
	

	

}
