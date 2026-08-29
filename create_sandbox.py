import asyncio
from datetime import timedelta

from opensandbox import Sandbox

async def main() -> None:
    # Create a sandbox with code interpreter
    sandbox = await Sandbox.create(
        "opensandbox:openclaw",
        entrypoint=["/opt/code-interpreter/code-interpreter.sh"],
        env={"PYTHON_VERSION": "3.11"},
        timeout=timedelta(minutes=10),
    )

    # Print the created sandbox as JSON
    info = await sandbox.get_info()
    print(info.model_dump_json(indent=2))
    print(info.expires_at.astimezone())

if __name__ == "__main__":
    asyncio.run(main())
