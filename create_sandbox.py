import asyncio
from datetime import timedelta

from opensandbox import Sandbox
from opensandbox.models import Volume, Host


async def main() -> None:
    # Create a sandbox with code interpreter
    sandbox = await Sandbox.create(
        "opensandbox:openclaw",
        entrypoint=["/opt/code-interpreter/code-interpreter.sh"],
        volumes=[Volume(name="openclaw",host=Host(path="/Users/jarvis/work/ai_security/.openclaw"),mountPath="/root/.openclaw")],
        env={"PYTHON_VERSION": "3.11","OPENCLAW_GATEWAY_TOKEN":"my_token"},
        timeout=timedelta(minutes=60),
    )

    # Print the created sandbox as JSON
    info = await sandbox.get_info()
    print(info.model_dump_json(indent=2))
    print(info.expires_at.astimezone())

if __name__ == "__main__":
    asyncio.run(main())
