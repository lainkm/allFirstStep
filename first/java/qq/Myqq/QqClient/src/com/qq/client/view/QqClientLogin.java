/*
 * qq客户端登录界面
 * */
package com.qq.client.view;
import javax.swing.*;
import java.io.*;
import com.qq.client.model.QqClientUser;
import com.qq.common.User;
import com.qq.client.tools.*;
import com.qq.common.*;
import java.awt.*;
import java.awt.event.*;

public class QqClientLogin extends JFrame implements ActionListener, MouseListener{

	//定义上面
	JLabel jbl1;
	
	//定义中部网格
	JPanel jp2;
	JLabel jp2_jbl1, jp2_jbl2, jp2_jbl3, jp2_jbl4;
	JTextField jp2_jtf;
	JPasswordField jp2_jpf;
	JCheckBox jp2_jcb1, jp2_jcb2;
	
	//定义下方流式按钮
	JPanel jp1;
	JButton jp1_jb1, jp1_jb2, jp1_jb3;
	
	int xOld = 0;
	int yOld = 0;
	//主调
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		QqClientLogin qqClientLogin = new QqClientLogin();
	}

	public QqClientLogin()
	{
		
		/*尝试修改窗口边框，但是出了点问题
        this.addMouseListener(new MouseAdapter() {  
            @Override  
            public void mousePressed(MouseEvent e) {  
                xOld = e.getX();  
                yOld = e.getY();  
            }  
        });  
        this.addMouseMotionListener(new MouseMotionAdapter() {  
            @Override  
            public void mouseDragged(MouseEvent e) {  
                int xOnScreen = e.getXOnScreen();  
                int yOnScreen = e.getYOnScreen();  
                int xx = xOnScreen - xOld;  
                int yy = yOnScreen - yOld;  
                QqClientLogin.this.setLocation(xx, yy);  
            }  
        });  
        */
		
		//北边
		jbl1 = new JLabel(new ImageIcon("image/morning.jpg"));
		
		//中部
		jp2 = new JPanel(new GridLayout(3, 3));
		jp2_jbl1 = new JLabel("qq账户", JLabel.CENTER);
		jp2_jbl2 = new JLabel("qq密码", JLabel.CENTER);
		jp2_jbl3 = new JLabel("找回密码", JLabel.CENTER);
		jp2_jbl4 = new JLabel("注册账号", JLabel.CENTER);
		jp2_jbl3.setForeground(Color.blue);
		jp2_jbl4.setForeground(Color.blue);
		
		jp2_jtf = new JTextField();
		jp2_jpf = new JPasswordField();
		jp2_jcb1 = new JCheckBox("隐身登陆");
		jp2_jcb2 = new JCheckBox("记住密码");
		
		//控件加入
		jp2.add(jp2_jbl1);
		jp2.add(jp2_jtf);
		jp2.add(jp2_jbl4);
		jp2.add(jp2_jbl2);
		jp2.add(jp2_jpf);
		jp2.add(jp2_jbl3);
		jp2.add(jp2_jcb1);
		jp2.add(jp2_jcb2);
	
		this.add(jp2);
		this.add(jp2,"Center");
	
		//南边
		jp1 = new JPanel();//默认流式布局
		jp1_jb1 = new JButton(new ImageIcon("image/login.png"));
		
		//相应登陆
		jp1_jb1.addActionListener(this);
		jp2_jbl4.addMouseListener(this);
		jp2_jbl3.addMouseListener(this);
		//按钮放入jp1
		jp1.add(jp1_jb1);
		
		//把jbl1放在北边
		this.add(jbl1,"North");
		//把jp1放在南边
		this.add(jp1,"South");
		
		this.setSize(400, 350);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setVisible(true);
		
	}

	
	public void actionPerformed(ActionEvent e) {
		// TODO Auto-generated method stub
		
		//用户点击登陆
		if(e.getSource()==jp1_jb1)
		{
			//创建qcu对象
			QqClientUser qqClientUser = new QqClientUser();
			
			//得到登陆的user信息
			User u = new User();
			u.setId(jp2_jtf.getText().trim());
			u.setPw(new String(jp2_jpf.getPassword()));
			
			if(qqClientUser.checkUser(u))
			{
				
				try{
					
				QqList qqList = new QqList(u.getId());
				ManageQqList.addQqList(u.getId(), qqList);
				
				
				//发送一个要求返回在线好友的请求包（这个时候CheckUser已经启动线程了
				ObjectOutputStream oos = new ObjectOutputStream
						(ManageNewUserConnectThread.getNewUserThread(u.getId()).getS().getOutputStream());
				
				//定义一个message包
				Message m = new Message();
				m.setMesType(MessageType.Message_get_online);//请求得到在线好友的包
				m.setSender(u.getId());//表示请求的是当前这个号的qq好友，表明是谁发送的请求
				oos.writeObject(m);
				
				}
				catch(Exception e0){
					e0.printStackTrace();
				}
				
				
				
				//打开好友列表，关闭登录界面
				this.dispose();
			}
			else
			{
				JOptionPane.showMessageDialog(this, "用户名和密码错误");
			}
		}
	}

	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() == jp2_jbl3&& e.getClickCount() == 1)
		{
			//找回密码
			
		}
		else if(e.getSource() == jp2_jbl4&& e.getClickCount() == 1)
		{
			//注册账号
			QqRegister qr = new QqRegister();
		}
	}

	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() == jp2_jbl4)
		jp2_jbl4.setForeground(Color.pink);
		else if(e.getSource() == jp2_jbl3)
			jp2_jbl3.setForeground(Color.pink);
	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() == jp2_jbl4)
		jp2_jbl4.setForeground(Color.blue);
		else if(e.getSource() == jp2_jbl3)
			jp2_jbl3.setForeground(Color.blue);
	}

}
