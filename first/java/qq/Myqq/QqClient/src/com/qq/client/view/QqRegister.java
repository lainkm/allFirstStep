package com.qq.client.view;

import javax.imageio.spi.RegisterableService;
import javax.swing.*;

import com.qq.client.model.QqClientUser;
import com.qq.client.model.QqRegisterCheck;
import com.qq.client.tools.ManageNewUserConnectThread;
import com.qq.client.tools.ManageQqList;
import com.qq.client.tools.NewUserThread;
import com.qq.common.Message;
import com.qq.common.MessageType;
import com.qq.common.User;

import java.awt.*;
import java.awt.event.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.rmi.activation.ActivationInstantiator;

public class QqRegister extends JFrame implements ActionListener{

	JPanel jp;
	JTextField jtf_name;
	JPasswordField jtf_pw,jtf_pw2;
	JLabel jl1,jl2,jl3;
	JButton jb1,jb2;
	
	public Socket s; 
	
	public QqRegister()
	{
		jtf_name = new JTextField();
		jtf_pw = new JPasswordField();
		jtf_pw2 = new JPasswordField();
		
		jl1 = new JLabel("�������û���:",JLabel.CENTER);
		jl2 = new JLabel("����������:",JLabel.CENTER);
		jl3 = new JLabel("��ȷ������:",JLabel.CENTER);
		jb1 = new JButton("ע��");
		jb2 = new JButton("����");
		
		jp = new JPanel(new GridLayout(4, 2));
		
		jb1.addActionListener(this);
		jb2.addActionListener(this);
		
		jp.add(jl1);
		jp.add(jtf_name);
		jp.add(jl2);
		jp.add(jtf_pw);
		jp.add(jl3);
		jp.add(jtf_pw2);
		jp.add(jb1);
		jp.add(jb2);
		
		this.add(jp);
		this.setVisible(true);
		this.setBounds(500, 500, 400, 180);
	}
	public static void main(String[] args)
	{
		QqRegister qr = new QqRegister();
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() == jb1)
		{
			//����Ϸ�
			if(jtf_name.getText().toString().equals(""))
			{
				JOptionPane.showMessageDialog(null, "�û�������Ϊ��", "",JOptionPane.WARNING_MESSAGE);
				

				jtf_name.setText("");
				jtf_pw.setText("");
				jtf_pw2.setText("");
			}
			else if(String.valueOf(jtf_pw.getPassword()).equals("")||
					String.valueOf(jtf_pw2.getPassword()).equals(""))
			{
				JOptionPane.showMessageDialog(null, "��������������", "",JOptionPane.WARNING_MESSAGE);

				jtf_name.setText("");
				jtf_pw.setText("");
				jtf_pw2.setText("");
			}
			else if(!String.valueOf(jtf_pw.getPassword()).equals(String.valueOf(jtf_pw2.getPassword())))		
			{
				System.out.println(jtf_pw.getPassword().toString().trim());
				String pw = jtf_pw2.getPassword().toString().trim();
				System.out.println(pw);
				
				Object[] options = { "ȷ��", "ȡ��" }; 
				JOptionPane.showOptionDialog(null, "��������������β�ƥ�䣬����������", "", JOptionPane.DEFAULT_OPTION, 
				JOptionPane.WARNING_MESSAGE,null, options, options[0]);
				
				jtf_name.setText("");
				jtf_pw.setText("");
				jtf_pw2.setText("");
			}
			else{
			//ȥ��������֤ע��
				
				//����qcu����
				QqRegisterCheck qr = new QqRegisterCheck();
				//�õ���½��user��Ϣ
				User u = new User();
				u.setId("");
				u.setName(new String(jtf_name.getText().trim()));
				u.setPw(new String(jtf_pw.getPassword()));
				
				String id = qr.backId(u);
				if(id != "")
				{
					JOptionPane.showMessageDialog(this, "ע��ɹ��������˺���" + id);
				}
				else
				{
					JOptionPane.showMessageDialog(this, "ע��ʧ��");
				}
			
			}
			
		}
		else if(e.getSource() == jb2)
		{
			//���ã����е�Jtf���
			jtf_name.setText("");
			jtf_pw.setText("");
			jtf_pw2.setText("");
		}
	}
}
