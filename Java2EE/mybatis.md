# Mybatis相关技术

## 传统JDBC写法
```java
public static void main(String[] args){
    Class.forName("com.mysql.jdbc.Driver");
    Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/demo","root","123456");
    conn.setAutoCommit(false);
    PreparedStatement pStatement = conn.prepareStatement("insert into dept value (?,?)");
    pStatement.setInt(1,1009);
    pStatement.setString(2,"asdasd");
    try {
        pStatement.executeUpdate();
        conn.commit();
    }catch(Exception ex) {
        conn.rollback();
        ex.printStackTrace();
    }finally{
        if(pStatement != null){
            pStatement.close();
        }
    }
}

```

## mybatis相关配置文件
### 核心配置文件
1. `configration`: 
2. 自定义类型转换器 : 需要实现`typeHandle`接口,主配置文件如下: <br>
```XML
<typeHandlers>
    <typeHandler handle="com.liuwei.util.MyHandler" javaType="Boolean" jdbcType="NUMERIC">
    </typeHandler>
</typeHandlers>
```
3. `objectFactor`对象工厂
4. `interceptor` 自定义拦截器