/**
 * �û���Ϣ�࣬��Ϊ��������һ������������
 */

package com.qq.common;

public class User implements java.io.Serializable{//���л�����һ�������������ϻ��ļ��д���

	private String id;
	private String pw;
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
	 
}
