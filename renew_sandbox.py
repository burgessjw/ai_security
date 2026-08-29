import asyncio

from opensandbox.manager import SandboxManager
from opensandbox.models.sandboxes import SandboxFilter
from datetime import timedelta

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
            await manager.renew_sandbox(info.id,timedelta(minutes=10))
            print("Sandbox renewed", info.expires_at.astimezone())
if __name__ == "__main__":
    asyncio.run(main())
