/**
 * 用户信息类，作为对象流的一个对象来传递
 */

package com.qq.common;

public class User implements java.io.Serializable{//序列化，让一个对象在网络上或文件中传输

	private String id;
	private String pw;
	private String name;
	//private String name;
	//用户头像
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
