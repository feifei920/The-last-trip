package com.example.springboot.mapper;

import com.example.springboot.entity.TotalEntity;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface TotalMapper {
    public List<TotalEntity> getTotal();

   // 根据id查询
    public TotalEntity getById(int id);

    public List<TotalEntity> GetAllTotalEntity();
}
