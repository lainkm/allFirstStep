/**
 *������ͬ�û�qq���ѣ���������İ���˽����� 
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