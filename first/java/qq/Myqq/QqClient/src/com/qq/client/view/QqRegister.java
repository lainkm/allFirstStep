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
		
		jl1 = new JLabel("请输入用户名:",JLabel.CENTER);
		jl2 = new JLabel("请输入密码:",JLabel.CENTER);
		jl3 = new JLabel("请确认密码:",JLabel.CENTER);
		jb1 = new JButton("注册");
		jb2 = new JButton("重置");
		
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
			//输入合法
			if(jtf_name.getText().toString().equals(""))
			{
				JOptionPane.showMessageDialog(null, "用户名不能为空", "",JOptionPane.WARNING_MESSAGE);
				

				jtf_name.setText("");
				jtf_pw.setText("");
				jtf_pw2.setText("");
			}
			else if(String.valueOf(jtf_pw.getPassword()).equals("")||
					String.valueOf(jtf_pw2.getPassword()).equals(""))
			{
				JOptionPane.showMessageDialog(null, "请重新输入密码", "",JOptionPane.WARNING_MESSAGE);

				jtf_name.setText("");
				jtf_pw.setText("");
				jtf_pw2.setText("");
			}
			else if(!String.valueOf(jtf_pw.getPassword()).equals(String.valueOf(jtf_pw2.getPassword())))		
			{
				System.out.println(jtf_pw.getPassword().toString().trim());
				String pw = jtf_pw2.getPassword().toString().trim();
				System.out.println(pw);
				
				Object[] options = { "确定", "取消" }; 
				JOptionPane.showOptionDialog(null, "您输入的密码两次不匹配，请重新输入", "", JOptionPane.DEFAULT_OPTION, 
				JOptionPane.WARNING_MESSAGE,null, options, options[0]);
				
				jtf_name.setText("");
				jtf_pw.setText("");
				jtf_pw2.setText("");
			}
			else{
			//去服务器验证注册
				
				//创建qcu对象
				QqRegisterCheck qr = new QqRegisterCheck();
				//得到登陆的user信息
				User u = new User();
				u.setId("");
				u.setName(new String(jtf_name.getText().trim()));
				u.setPw(new String(jtf_pw.getPassword()));
				
				String id = qr.backId(u);
				if(id != "")
				{
					JOptionPane.showMessageDialog(this, "注册成功，您的账号是" + id);
				}
				else
				{
					JOptionPane.showMessageDialog(this, "注册失败");
				}
			
			}
			
		}
		else if(e.getSource() == jb2)
		{
			//重置，所有的Jtf清空
			jtf_name.setText("");
			jtf_pw.setText("");
			jtf_pw2.setText("");
		}
	}
}
