import asyncio
import httpx

from opensandbox.manager import SandboxManager
from opensandbox.models.sandboxes import SandboxFilter
from opensandbox import Sandbox

async def main() -> None:
    async with await SandboxManager.create() as manager:
        sandboxes = await manager.list_sandbox_infos(
            SandboxFilter(
                states=["RUNNING"],
                page_size=10,
            )
        )
        for info in sandboxes.sandbox_infos:
            # print(info.model_dump_json(indent=2))
            sandbox = await Sandbox.connect(info.id)
            endpoint = await sandbox.get_endpoint(18789)
            url = f"http://{endpoint.endpoint}/v1/chat/completions"
            print(url)
            r = httpx.post(
                url=url,
                headers={"Authorization": "Bearer my_token"},
                json={"model": "openclaw/default",
                      "messages": [{"role": "user", "content": "写一个python脚本，脚本计算2+2的结果，并执行结果告诉我"}]},
                trust_env=False,
                timeout=60
            )
            print("== 实际发出的请求 ==")
            print(r.request.method, r.request.url)
            for k, v in r.request.headers.items():
                print(f"{k}: {v}")
            print("== 响应 ==")
            print(r.status_code)
            print(r.headers.get("server"), r.headers.get("content-type"))
            print(r.text)
if __name__ == "__main__":
    asyncio.run(main())
