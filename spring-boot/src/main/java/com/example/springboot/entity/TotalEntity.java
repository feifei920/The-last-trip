package com.example.springboot.entity;

public class TotalEntity {
    private int appId;
    private String appName;
    private Integer downloadTime;
    private Long downloadNum;
    private String good;
    private Integer commentNumber;
    private String tag;
    private String classific;
    private String commentDetail;

    public TotalEntity(int appId, String appName, Integer downloadTime, Long downloadNum, String good, Integer commentNumber, String tag, String classific, String commentDetail) {
        this.appId = appId;
        this.appName = appName;
        this.downloadTime = downloadTime;
        this.downloadNum = downloadNum;
        this.good = good;
        this.commentNumber = commentNumber;
        this.tag = tag;
        this.classific = classific;
        this.commentDetail = commentDetail;
    }

    public TotalEntity() {
    }

    public int getAppId() {
        return appId;
    }

    public void setAppId(int appId) {
        this.appId = appId;
    }

    public String getAppName() {
        return appName;
    }

    public void setAppName(String appName) {
        this.appName = appName;
    }

    public Integer getDownloadTime() {
        return downloadTime;
    }

    public void setDownloadTime(Integer downloadTime) {
        this.downloadTime = downloadTime;
    }

    public Long getDownloadNum() {
        return downloadNum;
    }

    public void setDownloadNum(Long downloadNum) {
        this.downloadNum = downloadNum;
    }

    public String getGood() {
        return good;
    }

    public void setGood(String good) {
        this.good = good;
    }

    public Integer getCommentNumber() {
        return commentNumber;
    }

    public void setCommentNumber(Integer commentNumber) {
        this.commentNumber = commentNumber;
    }

    public String getTag() {
        return tag;
    }

    public void setTag(String tag) {
        this.tag = tag;
    }

    public String getClassific() {
        return classific;
    }

    public void setClassific(String classific) {
        this.classific = classific;
    }

    public String getCommentDetail() {
        return commentDetail;
    }

    public void setCommentDetail(String commentDetail) {
        this.commentDetail = commentDetail;
    }
}
