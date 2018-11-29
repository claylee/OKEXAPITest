### OKEXAPITest

## 当前
  + 基于Flask
  + 网站数据 bithumb 和 OKEX。但是bithumb目前国内已经无法解析域名
  + Data通过网站的Python API,做了测试。控制台Python同步数据，存在sqlite里面。


## 下步

  1.  找到公式，excel
  2.  一个site的模拟登陆
  3. 确定行情Data的model, SQLAlchemy保存 (okxon)
  4. sqlalchemy生成Json，返回给chart  ..Done
  4. 同步行情Data的机制。实时、获取历史阶段
  5. 绘制Data的Chart                 ..Done
  6. 绘制对比Data。或者找到对比模式
