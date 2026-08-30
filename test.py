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
            ep = await sandbox.get_endpoint(18789)
            base = f"http://{ep.endpoint}"
            print("sandbox id:", info.id)  # ← 关键：确认是哪个沙盒
            print("base:", base)

            # 1. GET models —— 测路由是否通
            r1 = httpx.get(f"{base}/v1/models",
                           headers={"Authorization": "Bearer my-secret-token"},
                           trust_env=False)
            print("GET /v1/models ->", r1.status_code, repr(r1.text[:200]))

            # 2. POST chat —— 复现 404，打印完整响应体
            r2 = httpx.post(f"{base}/v1/chat/completions",
                            headers={"Authorization": "Bearer my-secret-token"},
                            json={"model": "openclaw/default",
                                  "messages": [{"role": "user", "content": "hi"}]},
                            trust_env=False)
            print("POST chat ->", r2.status_code)
            print("resp headers:", dict(r2.headers))
            print("resp body:", repr(r2.text[:300]))

            # 3. 对照组：探沙盒内 gateway 是否真的活着
            r3 = httpx.get(f"{base}/",
                           headers={"Authorization": "Bearer my-secret-token"},
                           trust_env=False)
            print("GET / ->", r3.status_code, repr(r3.text[:120]))
if __name__ == "__main__":
    asyncio.run(main())
