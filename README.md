|done|||
|-|-|-|
|✅|运行opensandbox-server|了解沙盒；使用docker运行时|
|✅| 创建沙盒 |cli / code-interpreter两种方式；了解python线程/协程模型|
|✅| 自定义openclaw镜像|替换基础镜像中的node版本为24+；安装openclaw|
|✅|运行openclaw|脚本创建沙盒；首次创建成功后，在沙盒内执行openclaw onboard进行配置provider，挂载.openclaw目录，实现重复使用|
|✅|调用openclaw|脚本调用,写爬虫爬虎扑|
|✅|安装skill，文章去ai化|https://skillhub.cn/skills/user_ab5ae6ee/unclecheng-reduce-ai-perception-v2|
||镜像优化|固化环境变量，openclaw运行参数等到镜像或者脚本；挂载数据卷实现持久化；|
||接入微信|公众号接入流程；暴露公网ip；|
||系统调用隔离|使用k8s运行时；gVisor|
||脚本调用改为web入口|react；antDesign；python or go|

- 脚本创建沙盒
- docker exec -d < container_id > openclaw gateway
- 脚本与openclaw对话
