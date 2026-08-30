import asyncio

from opensandbox.manager import SandboxManager
from opensandbox.models.sandboxes import SandboxFilter

async def main() -> None:
    async with await SandboxManager.create() as manager:
        sandboxes = await manager.list_sandbox_infos(
            SandboxFilter(
                states=["RUNNING"],
                page_size=10,
            )
        )
        for info in sandboxes.sandbox_infos:
            print(info.model_dump_json(indent=2))
            print(info.expires_at.astimezone())
if __name__ == "__main__":
    asyncio.run(main())
