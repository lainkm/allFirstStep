/**
 * ���������ƽ��棬�������������رշ�����
 * �������û�
 */

package com.qq.server.view;

import javax.swing.*;

import com.qq.server.model.MyQqServer;

import java.awt.*;
import java.awt.event.*;
public class MyServerFrame extends JFrame implements ActionListener{

	JPanel jp1;
	JButton jb1, jb2;
	
	public MyServerFrame()
	{
		jp1 = new JPanel();
		jb1 = new JButton("����������");
		jb1.addActionListener(this);//����
		jb2 = new JButton("�رշ�����");
		jp1.add(jb1);
		jp1.add(jb2);
		
		this.add(jp1);
		this.setSize(600, 500);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setVisible(true);
	}
	
	
	
	public static void main(String[] args){
		MyServerFrame myServerFrame = new MyServerFrame();
	}



	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource()==jb1)
		{
			new MyQqServer();
		}
		
	}
}
