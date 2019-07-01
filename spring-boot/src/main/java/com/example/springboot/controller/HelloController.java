package com.example.springboot.controller;

import com.example.springboot.entity.TotalEntity;
import com.example.springboot.service.TotalService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.ArrayList;
import java.util.List;

@Controller
public class HelloController {
   @Autowired
    TotalService totalService;


    @RequestMapping("/hello")
    public String hello(){
        return "index";

    }

    @RequestMapping("/qq")
    public String submits(String word, ModelMap map){
        System.out.println("qewrwtwwywwuwuwu");
        TotalEntity t1 = new TotalEntity();
        t1.setTag("金融理财");
        t1.setDownloadNum(570000000l);
        TotalEntity t2 = new TotalEntity();
        t2.setTag("金融理财");
        t2.setDownloadNum(130000000l);
        TotalEntity t3 = new TotalEntity();
        t3.setTag("金融理财");
        t3.setDownloadNum(91429000l);
        TotalEntity t4 = new TotalEntity();
        t4.setTag("通讯社交");
        t4.setDownloadNum(2150000000l);
        TotalEntity t5 = new TotalEntity();
        t5.setTag("通讯社交");
        t5.setDownloadNum(810000000l);
        TotalEntity t6 = new TotalEntity();
        t6.setTag("通讯社交");
        t6.setDownloadNum(2150000000l);
        TotalEntity t7 = new TotalEntity();
        t7.setTag("育儿亲子");
        t7.setDownloadNum(5887000l);
        TotalEntity t8 = new TotalEntity();
        t8.setTag("育儿亲子");
        t8.setDownloadNum(14548000l);
        TotalEntity t9 = new TotalEntity();
        t9.setTag("育儿亲子");
        t9.setDownloadNum(4343000l);
        TotalEntity t10 = new TotalEntity();
        t10.setTag("考试学习");
        t10.setDownloadNum(11929000l);
        TotalEntity t11 = new TotalEntity();
        t11.setTag("考试学习");
        t11.setDownloadNum(220000000l);
        TotalEntity t12 = new TotalEntity();
        t12.setTag("考试学习");
        t12.setDownloadNum(11929000l);
        TotalEntity t13 = new TotalEntity();
        t13.setTag("考试学习");
        t13.setDownloadNum(150000000l);
        TotalEntity t14 = new TotalEntity();
        t14.setTag("网上购物");
        t14.setDownloadNum(610000000l);
        TotalEntity t15 = new TotalEntity();
        t15.setTag("网上购物");
        t15.setDownloadNum(220000000l);
        TotalEntity t16 = new TotalEntity();
        t16.setTag("网上购物");
        t16.setDownloadNum(229999999l);
        TotalEntity t17 = new TotalEntity();
        t17.setTag("系统工具");
        t17.setDownloadNum(550000000l);
        TotalEntity t18 = new TotalEntity();
        t18.setTag("系统工具");
        t18.setDownloadNum(470000000l);
        TotalEntity t19 = new TotalEntity();
        t19.setTag("系统工具");
        t19.setDownloadNum(470000000l);
        TotalEntity t20 = new TotalEntity();
        t20.setTag("系统工具");
        t20.setDownloadNum(560000000l);
        TotalEntity t21 = new TotalEntity();
        t21.setTag("生活休闲");
        t21.setDownloadNum(120000000l);
        TotalEntity t22 = new TotalEntity();
        t22.setTag("生活休闲");
        t22.setDownloadNum(170000000l);
        TotalEntity t23 = new TotalEntity();
        t23.setTag("生活休闲");
        t23.setDownloadNum(120000000l);
        TotalEntity t24 = new TotalEntity();
        t24.setTag("生活休闲");
        t24.setDownloadNum(120000000l);
        TotalEntity t25 = new TotalEntity();
        t25.setTag("旅游出行");
        t25.setDownloadNum(110000000l);
        TotalEntity t26 = new TotalEntity();
        t26.setTag("旅游出行");
        t26.setDownloadNum(190000000l);
        TotalEntity t27 = new TotalEntity();
        t27.setTag("旅游出行");
        t27.setDownloadNum(110000000l);
        TotalEntity t28 = new TotalEntity();
        t28.setTag("新闻阅读");
        t28.setDownloadNum(170000000l);
        TotalEntity t29 = new TotalEntity();
        t29.setTag("新闻阅读");
        t29.setDownloadNum(160000000l);
        TotalEntity t30 = new TotalEntity();
        t30.setTag("新闻阅读");
        t30.setDownloadNum(320000000l);
        TotalEntity t31 = new TotalEntity();
        t31.setTag("摄影图像");
        t31.setDownloadNum(300000000l);
        TotalEntity t32 = new TotalEntity();
        t32.setTag("摄影图像");
        t32.setDownloadNum(560000000l);
        TotalEntity t33 = new TotalEntity();
        t33.setTag("摄影图像");
        t33.setDownloadNum(229999999l);
        TotalEntity t34 = new TotalEntity();
        t34.setTag("手机美化");
        t34.setDownloadNum(27667000l);
        TotalEntity t35 = new TotalEntity();
        t35.setTag("手机美化");
        t35.setDownloadNum(14559000l);
        TotalEntity t36 = new TotalEntity();
        t36.setTag("手机美化");
        t36.setDownloadNum(35035000l);
        TotalEntity t37 = new TotalEntity();
        t37.setTag("影音播放");
        t37.setDownloadNum(1050000000l);
        TotalEntity t38 = new TotalEntity();
        t38.setTag("影音播放");
        t38.setDownloadNum(860000000l);
        TotalEntity t39 = new TotalEntity();
        t39.setTag("影音播放");
        t39.setDownloadNum(900000000l);
        TotalEntity t40 = new TotalEntity();
        t40.setTag("办公商务");
        t40.setDownloadNum(69671000l);
        TotalEntity t41 = new TotalEntity();
        t41.setTag("办公商务");
        t41.setDownloadNum(330000000l);
        TotalEntity t42 = new TotalEntity();
        t42.setTag("办公商务");
        t42.setDownloadNum(85398000l);
        TotalEntity t43 = new TotalEntity();
        t43.setTag("健康运动");
        t43.setDownloadNum(1094000l);
        TotalEntity t44 = new TotalEntity();
        t44.setTag("健康运动");
        t44.setDownloadNum(1204000l);
        TotalEntity t45 = new TotalEntity();
        t45.setTag("健康运动");
        t45.setDownloadNum(805000l);

        List<TotalEntity> list = new ArrayList<>();
            list.add(t1);
        list.add(t2);
        list.add(t3);
        list.add(t4);
        list.add(t5);
        list.add(t6);
        list.add(t7);
        list.add(t8);
        list.add(t9);
        list.add(t10);
        list.add(t11);
        list.add(t12);
        list.add(t13);
        list.add(t14);
        list.add(t15);
        list.add(t16);
        list.add(t17);
        list.add(t18);
        list.add(t19);
        list.add(t20);
        list.add(t21);
        list.add(t22);
        list.add(t23);
        list.add(t24);
        list.add(t25);
        list.add(t26);
        list.add(t27);
        list.add(t28);
        list.add(t29);
        list.add(t30);
        list.add(t31);
        list.add(t32);
        list.add(t33);
        list.add(t34);
        list.add(t35);
        list.add(t36);
        list.add(t37);
        list.add(t38);
        list.add(t39);
        list.add(t40);
        list.add(t41);
        list.add(t42);
        list.add(t43);
        list.add(t44);
        list.add(t45);
List list1 = new ArrayList();
String ss="sd";
        for (int i=0;i<list.size();i++){
            if (word.equals(list.get(i).getTag())){
               Long num1=list.get(i).getDownloadNum();
                System.out.println(num1);
               list1.add(num1);
            }
        }
        map.put("list1",list1);
        return "show.ftl";

    }



}

