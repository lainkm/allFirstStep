/**
 *管理不同用户qq好友，黑名单，陌生人界面类 
 */

package com.qq.client.tools;

import java.io.*;
import java.util.*;
import com.qq.client.view.*;

public class ManageQqList {
	
	private static HashMap hm = new HashMap<String, QqList>();
	
	public static void addQqList(String qqId, QqList qqList){
		hm.put(qqId, qqList);
	}
	
	public static QqList getQqList(String qqId){
		return (QqList)hm.get(qqId);
	}
}
