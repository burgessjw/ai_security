|done|||
|-|-|-|
|✅|运行opensandbox-server|了解沙盒；使用docker运行时|
|✅| 创建沙盒 |cli / code-interpreter两种方式；了解python线程/协程模型|
|✅| 自定义openclaw镜像|替换基础镜像中的node版本为24+；安装openclaw<br>目前通过容器内执行openclaw onboard进行配置provider，挂载.openclaw目录实现一次配置多次使用|
|✅|运行openclaw|通过api调用方式实现与openclaw的对话|
|✅|调用openclaw|脚本调用,写爬虫爬虎扑|
|✅|安装skill，文章去ai化|https://skillhub.cn/skills/user_ab5ae6ee/unclecheng-reduce-ai-perception-v2|
||镜像优化|固化环境变量，openclaw运行参数等到镜像或者脚本；挂载数据卷实现持久化；|
||接入微信|公众号接入流程；暴露公网ip；|
||系统调用合理|使用k8s运行时；gVisor|
