package com.qq.client.model;

import com.qq.common.User;

public class QqRegisterCheck {

	public String backId(User u)
	{
		return new MyQqConnect(u).sendRegisterMessage();
	}
}
