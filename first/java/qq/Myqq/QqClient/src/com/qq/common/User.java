/**
 * �û���Ϣ�࣬��Ϊ��������һ������������
 */

package com.qq.common;

public class User implements java.io.Serializable{//���л�����һ�������������ϻ��ļ��д���

	private String id;
	private String pw;
	private String name;
	//private String name;
	//�û�ͷ��
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getPw() {
		return pw;
	}
	public void setPw(String pw) {
		this.pw = pw;
	}
	public String getName()
	{
		return this.name;
	}
	public void setName(String name)
	{
		this.name = name;
	}
	 
}
