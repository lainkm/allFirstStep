package com.qq.common;

public class Message implements java.io.Serializable{
	
	private String mesType;//��������1��2��3...
	private String sender;
	private String getter;
	private String con;//��Ϣ���ݱ���
	private String time;//��Ϣ���͵�ʱ��

	public String getSender() {
		return sender;
	}

	public void setSender(String sender) {
		this.sender = sender;
	}

	public String getGetter() {
		return getter;
	}

	public void setGetter(String getter) {
		this.getter = getter;
	}

	public String getCon() {
		return con;
	}

	public void setCon(String con) {
		this.con = con;
	}

	public String getTime() {
		return time;
	}

	public void setTime(String time) {
		this.time = time;
	}

	public String getMesType() {
		return mesType;
	}

	public void setMesType(String mesType) {
		this.mesType = mesType;
	}
}