/*
 * ����ͻ����������ͨѶ���߳���
 * ����û����߳�
 * */

package com.qq.client.tools;

import java.util.*;

public class ManageNewUserConnectThread {

	//���Ծ�̬��һ��������ֻ��Ҫһ��hashmap
	static HashMap hm = new HashMap<String, NewUserThread>();
	
	//�Ѵ����õ����û��̺߳Ͷ�Ӧ��id�ŷŽ������õ��߳�
	public static void addNewUserThread(String userId, NewUserThread nut){
		hm.put(userId, nut);//���û�id���̷߳Ž�ȥ
	}
	
	//����һ���̣߳���ΪҪͨ������߳�ת��
	public static NewUserThread getNewUserThread(String userId)
	{
		return (NewUserThread)hm.get(userId);
	}
	
}
