/*
 * qq�����б�
 * */

package com.qq.client.view;

import javax.swing.*;
import com.qq.client.tools.*;
import com.qq.common.Message;

import java.awt.*;
import java.awt.event.*;

public class QqList extends JFrame implements ActionListener, MouseListener{

	//��һ�ſ�Ƭ(�򿪺����б�
	JPanel jpf1, jpf2, jpf3;//��һ������ź�������
	JButton jpf_jb1, jpf_jb2, jpf_jb3;//���Ѻ�����ѡ��ť
	JScrollPane jsp1;//�����б�������
	
	//��һ�ſ�Ƭ(��İ�����б�
	JPanel jps1, jps2, jps3;//��һ������ź�������
	JButton jps_jb1, jps_jb2, jps_jb3;//���Ѻ�����ѡ��ť
	JScrollPane jsp2;//�����б�������
	
	
	//�����ſ�Ƭ������
	JPanel jp1, jp2;
	JButton jb1, jb2, jb3;
	
	String myId;
	JLabel jbls[];
	JLabel jbls2[];
	
	//������jframeд��cardlayout����
	CardLayout c1;
	public QqList(String myId){
		this.myId = myId;
		//��һ�ſ�Ƭ����ʾ�����б�
		jpf1 = new JPanel(new BorderLayout());
		
		//����5������
		jpf2 = new JPanel(new GridLayout(25, 1, 4, 4));//4,4�����м��
		jpf3 = new JPanel(new GridLayout(2, 1));//���panel��������ť��������İ����
		
		//��jpf2��ʼ��5�����ѣ�
		//Ĭ��ֻ���Լ����ߣ��������Ѷ�������
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
		
		jpf_jb1 = new JButton("�ҵĺ���");
		jpf_jb1.addActionListener(this);
		jpf_jb2 = new JButton("İ����");
		jpf_jb2.addActionListener(this);
		jpf_jb3 = new JButton("������");
		
		jp1 = new JPanel(new GridLayout(3, 1));
		jp2 = new JPanel(new BorderLayout());
		jb1 = new JButton("�ҵĺ���");
		jb1.addActionListener(this);
		jb2 = new JButton("İ����");
		jb2.addActionListener(this);
		jb3 = new JButton("������");
		jp1.add(jb1);
		jp1.add(jb2);
		jp1.add(jb3);
		jp2.add(jp1, "North");
		
		//�Ѱ�ť�Ž�jpanel3
		jpf3.add(jpf_jb2);
		jpf3.add(jpf_jb3);
		
		jsp1 = new JScrollPane(jpf2);
		
		//��jps1��ʼ���������������
		jpf1.add(jpf_jb1, "North");
		jpf1.add(jsp1,"Center");
		jpf1.add(jpf3, "South");
		
		
		//�����ڶ��ſ�Ƭ
		jps1 = new JPanel(new BorderLayout());
		
		//����25������
		jps2 = new JPanel(new GridLayout(20, 1, 4, 4));//4,4�����м��
		jps3 = new JPanel(new GridLayout(2, 1));//���panel��������ť���ѣ�İ����
		
		//��jpf2��ʼ��5������
		jbls2 = new JLabel[20];
		for(int i = 0; i < jbls2.length; i++)
		{
			jbls2[i] =  new JLabel(""+(i + 1), new ImageIcon("image/tx3.png"), JLabel.LEFT);
			jps2.add(jbls2[i]);
		}
		
		jps_jb1 = new JButton("�ҵĺ���");
		jps_jb1.addActionListener(this);
		jps_jb2 = new JButton("İ����");
		jps_jb2.addActionListener(this);
		jps_jb3 = new JButton("������");
		
		//�Ѱ�ť�Ž�jpanel3
		jps3.add(jps_jb1);
		jps3.add(jps_jb2);
		
		jsp2 = new JScrollPane(jps2);
		
		//��jps1��ʼ���������������
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
		this.setTitle("�����б�");

		this.setIconImage(new ImageIcon("image/qq.gif").getImage());
		
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setVisible(true);
		this.setTitle(myId);
		
		
		 
	}
	
	
	//���º����б�,��ɫ�ı��ɫ����ɫ���ɫ
	public void updateQqList(Message m) {
		String con = m.getCon();
		String friList[] = con.split(" ");
		String getter = m.getGetter();//����������˭��,��ǰ�˺�����Ҫ��
		
		for(int i = 0; i < friList.length; i++)
		{
			jbls[Integer.parseInt(friList[i]) - 1].setEnabled(true);
		}
	}
	
	
	
	

	//������jframeд��cardlayout����
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//	QqList qqList = new QqList("1");
	}

	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource()==jpf_jb2 || e.getSource()==jb2 )
		{
			c1.show(this.getContentPane(), "2");//���ܶԵڶ��ſ�Ƭ���п��ƣ�ֻ�ܶԿ�Ƭ��panel���п���
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
		//��Ӧ�û�˫���¼����õ����ѱ��
		if(e.getClickCount()==2)
		{
			//�õ��ú��ѵı��
			String friendId = ((JLabel)e.getSource()).getText();
			System.out.println("Ҫ��"+friendId+"����");
			
			QqChat qc = new QqChat(myId, friendId);
			
			ManageQqChat.addQqChat(myId + " " + friendId, qc);
			//QqChat����ȥʵ��һ����ʾ�ķ���
			
			
			//�ѽ�����߳̽���������߳���
			//Thread t = new Thread(qc);
			//t.start();//������������̣߳�
			//System.out.println("һֱ��ȡ������");
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