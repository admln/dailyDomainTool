<h1>工具简介</h1>
用于下载每日新增域名，解析后进行敏感词匹配，找出可疑的新注册域名，用于预测攻击行为<br>
例如：公司产品所辖单位域名有abc-server.com，如果本日新增域名中有abc-server-updates-official.com，则是可疑域名的可能性很大，应该重点关注<br>
例如：常被恶意模仿的域名有microsoft-update.com，如果本日新增域名中有microsoft-update-official.com，则恶意域名的可能性非常大，应该重点关注<br>

<h1>TODO</h1>
1. 增加日志输出；<br>
2. 增加数据库存储，支持通过特征词和条件进行历史域名筛查（例如近一个月）；<br>
3. 增加可视化界面，以服务形式运行；<br>
4. 提供Whois信息关联查询（支持以注册人、注册邮箱等whois信息单条件或者多条件筛查）；<br>
5. 支持基于词素的机器学习算法进行域名相似度匹配（例如micr0s0ft-update.com）；<br>