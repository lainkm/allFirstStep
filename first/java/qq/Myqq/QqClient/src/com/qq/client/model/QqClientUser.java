/**
 *qq��̨��½��֤ 
 */

package com.qq.client.model;

import com.qq.common.*;

public class QqClientUser {
	
	//ȥ���ݿ���֤���������ݿⲻ�ڱ��أ�����ί��һ����ȥ��֤
	public boolean checkUser(User u)
	{
		return new MyQqConnect(u).sendLoginInfoToserver();
	}
}
