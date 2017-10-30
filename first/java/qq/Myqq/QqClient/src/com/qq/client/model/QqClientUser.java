/**
 *qq后台登陆验证 
 */

package com.qq.client.model;

import com.qq.common.*;

public class QqClientUser {
	
	//去数据库验证，但是数据库不在本地，所以委托一个类去验证
	public boolean checkUser(User u)
	{
		return new MyQqConnect(u).sendLoginInfoToserver();
	}
}
