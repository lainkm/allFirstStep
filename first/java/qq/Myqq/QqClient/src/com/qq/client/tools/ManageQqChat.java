/*
 * �����û�����������
 * ����qqchatʵ����hashmap
 * 
 * */

package com.qq.client.tools;

import java.util.*;

import com.qq.client.view.*;

public class ManageQqChat {

	private static HashMap hm = new HashMap<String, QqChat>();
	
	public static void addQqChat(String iAndFriendId, QqChat qc){
		hm.put(iAndFriendId, qc);
	}
	
	public static QqChat getQqChat(String iAndFriendId){
		return (QqChat)hm.get(iAndFriendId);
	}
}
